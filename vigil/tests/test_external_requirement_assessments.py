import copy
import json
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from occurrence_requirement_validation import assessment_errors

REQ = 'EXTREQ-0123456789ABCDEF'
FC = 'VIGIL-FC-000001'


class OccurrenceRequirementAssessmentTests(unittest.TestCase):
    def setUp(self):
        self.record = {'source_records': [{}], 'vigil_assessment': {'source_clause_analysis': {'clauses': [
            {'taxonomy_relationships': [{'class_id': FC, 'canonical_taxonomy_mapping': True}]}]}}}
        self.assessment = {'requirement_id': REQ, 'alignment_result': 'aligned',
                           'assessment_basis': 'The observed action satisfies the independently reviewed proposition.',
                           'source_record_refs': ['source_records[0]'], 'assessed_on': '2026-10-03',
                           'identification_basis': 'The source clause describes this requirement directly.'}
        self.relationships = [{'class_id': FC, 'requirement_id': REQ, 'review_status': 'supported', 'strength': 'direct'}]

    def validate(self, changes=None, known=None):
        self.record['external_requirement_assessments'] = [self.assessment | (changes or {})]
        return assessment_errors(self.record, {REQ} if known is None else known, self.relationships)

    def test_independent_identification_does_not_require_fc(self):
        self.assertEqual(self.validate(), [])

    def test_derived_relationship_requires_clause_and_supported_link(self):
        changes = {'derived_from_class_ids': [FC], 'source_clause_indices': [0]}
        self.assertEqual(self.validate(changes), [])
        self.relationships[0]['review_status'] = 'unresolved'
        self.assertTrue(self.validate(changes))

    def test_common_alignment_results(self):
        for result in ('aligned', 'not-aligned', 'boundary'):
            self.assertEqual(self.validate({'alignment_result': result}), [])
        for result in ('met', 'not-met', 'insufficient-evidence', 'failure-occurrence', None):
            self.assertTrue(self.validate({'alignment_result': result}))

    def test_legacy_fields_are_rejected(self):
        for key in ('applicability_status', 'applicability_basis', 'finding', 'finding_basis'):
            self.assertTrue(self.validate({key: 'legacy'}))

    def test_taxonomy_polarity_does_not_select_external_result(self):
        changes = {'derived_from_class_ids': [FC], 'source_clause_indices': [0]}
        relationship = self.record['vigil_assessment']['source_clause_analysis']['clauses'][0]['taxonomy_relationships'][0]
        for role in ('failure-occurrence', 'successful-invariant', 'ambiguous-boundary'):
            relationship['relationship'] = role
            for result in ('aligned', 'not-aligned', 'boundary'):
                self.assertEqual(self.validate(changes | {'alignment_result': result}), [])

    def test_evidence_and_requirement_references_must_resolve(self):
        self.assertTrue(self.validate({'source_record_refs': ['source_records[1]']}))
        self.assertTrue(self.validate(known=set()))

    def test_alignment_requires_assessment_basis(self):
        self.assertTrue(self.validate({'assessment_basis': ''}))

    def validate_pair(self, left, right, **changes):
        second = 'EXTREQ-FEDCBA9876543210'
        record = copy.deepcopy(self.record)
        record['external_requirement_assessments'] = [
            self.assessment | {'assessment_basis': left},
            self.assessment | {'requirement_id': second, 'assessment_basis': right} | changes,
        ]
        return assessment_errors(record, {REQ, second}, self.relationships)

    def test_duplicate_complete_explanations_are_rejected_for_different_requirements(self):
        basis = 'The operator replaced the models. Its wider governance protocols are unpublished.'
        errors = self.validate_pair(basis, basis)
        self.assertEqual(len(errors), 1)
        self.assertIn('boilerplate: duplicate complete assessment_basis', errors[0])
        self.assertIn('external_requirement_assessments[0]', errors[0])
        self.assertIn('external_requirement_assessments[1]', errors[0])
        for result in ('aligned', 'not-aligned', 'boundary'):
            self.assertTrue(self.validate_pair(basis, basis, alignment_result=result))

    def test_case_whitespace_and_unicode_presentation_do_not_hide_duplicates(self):
        self.assertTrue(self.validate_pair('The office protocol is unpublished.',
                                           '  THE  oﬃce\nPROTOCOL is unpublished. '))

    def test_shared_facts_with_distinct_requirement_reasoning_are_allowed(self):
        self.assertEqual(self.validate_pair(
            'The operator replaced the models. A prior halt plan is not published.',
            'The operator replaced the models. Regular review of deactivation criteria is not published.'), [])

    def test_malformed_or_missing_bases_do_not_crash_duplicate_detection(self):
        for value in (None, [], {}, 42, ''):
            errors = self.validate_pair(value, value)
            self.assertTrue(errors)
            self.assertFalse(any('boilerplate:' in error for error in errors))
        errors = self.validate_pair('Identical basis.', 'Identical basis.', requirement_id=[])
        self.assertTrue(errors)
        self.assertFalse(any('boilerplate:' in error for error in errors))

    def test_source_and_history_repetition_are_outside_duplicate_scope(self):
        text = 'The operator replaced the models.'
        self.record['source_records'] = [{'source_anchor': text}, {'source_anchor': text}]
        self.record['interpretive_provenance'] = {'review_history': [{'review_outcome': text}]}
        self.assertEqual(self.validate({'assessment_basis': text}), [])

    def test_assessment_optional_in_incident_schema(self):
        schema = json.loads((Path(__file__).resolve().parents[1] / 'VIGIL.Schema.json').read_text())
        self.assertNotIn('external_requirement_assessments', schema['record_classes']['incident']['required_top_level_fields'])


if __name__ == '__main__':
    unittest.main()
