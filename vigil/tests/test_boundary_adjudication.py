"""Isolated tests of the approved canonical Boundary explanation control."""
import copy
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location('boundary_validator', ROOT / 'vigil/scripts/validate-vigil-records.py')
V = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(V)


class BoundaryAdjudicationTests(unittest.TestCase):
    def setUp(self):
        self.value = {
            'taxonomy_version': '0.7.0',
            'material_engagement': 'A protected tool was used without an established permission basis.',
            'unresolved_conditions': [{
                'polarity': 'failure-occurrence',
                'condition': 'Availability is used as a material basis for permission.',
                'assessment': 'The record establishes use, but not this permission premise. It also does not establish independently authorised execution.',
                'source_record_refs': ['source_records[0]'], 'episode_refs': ['E001']}],
            'diagnostic_reasons': ['insufficient-evidence'],
            'decisive_blocker': 'The operational permission premise remains unavailable.',
            'resolution_requirements': 'Retrieve the corresponding authority decision in the full source trajectory.'}
        self.mapping = {'classification_role': 'ambiguous-boundary', 'boundary_adjudication': self.value}
        self.record = {'source_records': [{}], 'vigil_assessment': {'source_clause_analysis': {'clauses': [{'episode_id': 'E001'}]}}}

    def errors(self, record=True):
        errors = []
        V.validate_boundary_adjudication(Path('synthetic.json'), self.mapping, 'mapping', errors, self.record if record else None)
        return errors

    def test_completed_boundary(self):
        self.assertEqual(self.errors(), [])

    def test_each_required_field(self):
        for key in list(self.value):
            with self.subTest(field=key):
                saved = self.value.pop(key)
                self.assertTrue(self.errors())
                self.value[key] = saved

    def test_empty_strings(self):
        for key in ['taxonomy_version', 'material_engagement', 'decisive_blocker', 'resolution_requirements']:
            with self.subTest(field=key):
                saved = self.value[key]; self.value[key] = '  '
                self.assertTrue(self.errors()); self.value[key] = saved

    def test_missing_and_non_object(self):
        for value in [None, '', [], 'pending']:
            self.mapping['boundary_adjudication'] = value
            self.assertTrue(self.errors())

    def test_only_completed_diagnostic_reasons(self):
        for value in [[], ['E'], ['D'], ['pending'], ['unsupported-class-engagement'], ['insufficient-evidence', 'insufficient-evidence'], [None], [['insufficient-evidence']]]:
            self.value['diagnostic_reasons'] = value
            self.assertTrue(self.errors())

    def test_multiple_reasons(self):
        self.value['diagnostic_reasons'] = ['conflicting-evidence', 'recognition-criteria-insufficiency']
        self.assertEqual(self.errors(), [])

    def test_unresolved_condition_shape(self):
        original = copy.deepcopy(self.value['unresolved_conditions'])
        for value in [[], None, ['pending'], [{}]]:
            self.value['unresolved_conditions'] = value
            self.assertTrue(self.errors())
        self.value['unresolved_conditions'] = original
        for field in list(original[0]):
            with self.subTest(field=field):
                saved = self.value['unresolved_conditions'][0].pop(field)
                self.assertTrue(self.errors()); self.value['unresolved_conditions'][0][field] = saved

    def test_source_reference_resolution(self):
        c = self.value['unresolved_conditions'][0]
        for refs in [[], ['source_records[1]'], ['external URL'], ['source_records[0]', 'source_records[0]']]:
            c['source_record_refs'] = refs
            self.assertTrue(self.errors())

    def test_episode_reference_resolution(self):
        c = self.value['unresolved_conditions'][0]
        for refs in [[], ['E999'], ['E001', 'E001'], [None]]:
            c['episode_refs'] = refs
            self.assertTrue(self.errors())

    def test_decisive_roles_do_not_require_boundary_object(self):
        for role in ['failure-occurrence', 'successful-invariant']:
            self.mapping = {'classification_role': role}
            self.assertEqual(self.errors(), [])

    def test_mapping_validator_enforces_both_positions(self):
        mapping = dict(self.mapping, family_id='F', class_id='C', classification_basis='Specific occurrence basis.', classification_confidence='medium')
        mapping.pop('boundary_adjudication')
        for label in ['primary_classification', 'secondary_classifications[0]']:
            errors = []
            V.validate_taxonomy_mapping(Path('synthetic.json'), mapping, label, {'F': {}}, {'C': {'family_id': 'F'}}, {}, errors, self.record)
            self.assertTrue(any(label + '.boundary_adjudication' in e for e in errors))

    def test_historical_confidence_unchanged(self):
        self.mapping['classification_confidence'] = 'medium'
        original = copy.deepcopy(self.mapping)
        self.errors()
        self.assertEqual(self.mapping, original)


if __name__ == '__main__':
    unittest.main()
