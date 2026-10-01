"""Generic invariant/failure polarity contracts; no Incident adjudication snapshots."""
from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / 'taxonomy'
def module(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / filename)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result

VALIDATOR = module('invariant_contract_validator', 'validate_taxonomy.py')
RENDERER = module('invariant_contract_renderer', 'render_taxonomy.py')
SCHEMA = json.loads((ROOT / 'VIGIL.FailureTaxonomy.Schema.json').read_text())


def fixture():
    item = {
        'class_id': 'VIGIL-FC-999999', 'class_code': 'EVIDENCE_RECONSTRUCTABILITY',
        'family_id': 'VIGIL-FF-9999', 'name': 'Evidence Reconstructability',
        'status': 'beta', 'abstraction': 'class',
        'plain_english': 'Evidence supports reconstruction of material events.',
        'definition': 'The property by which evidence preserves material event relationships.',
        'invariant': 'Material event relationships must remain reconstructable.',
        'success_condition': 'An actual review reconstructs the material event pathway from preserved relationships.',
        'success_recognition': {'applies_to': 'successful-invariant', 'required_conditions': [
            'Material events require reconstruction.', 'The review reconstructs those events using preserved relationships.']},
        'failure_condition': 'A failure in which evidence lacks necessary material relationships.',
        'failure_plain_english': 'Records exist but cannot establish what happened.',
        'failure_recognition': {'applies_to': 'failure-occurrence', 'required_conditions': [
            'Evidence exists.', 'Necessary event relationships cannot be established.']},
        'exclusions': ['Event relationships can be reconstructed adequately.'],
        'examples': ['Records omit the link between a decision and its action.'], 'aliases': [],
    }
    family = {
        'family_id': 'VIGIL-FF-9999', 'family_code': 'EVIDENCE_INTEGRITY',
        'name': 'Evidence Integrity', 'status': 'beta', 'abstraction': 'family',
        'version': '1.0.0', 'plain_english': 'Material evidence remains usable for review.',
        'definition': 'The integrity domain preserving material evidence for review.',
        'invariant': 'Material evidence must remain available and usable.',
        'failure_condition': 'Failures in which material evidence is absent or unusable.',
        'failure_plain_english': 'Material evidence is missing or unusable.',
        'boundary_role': 'failure-occurrence', 'inclusion_rule': 'Evidence integrity fails.',
        'exclusion_rule': 'Evidence remains adequate for the review.', 'scope': ['Evidence.'],
        'allowed_class_ids': [item['class_id']], 'allowed_class_codes': [item['class_code']], 'aliases': [],
    }
    return {'schema_version': SCHEMA['properties']['schema_version']['const'],
            'semantic_model': 'invariant-with-occurrence-polarity',
            'standard': {'name': 'Synthetic taxonomy', 'version': '1.0.0',
                         'publication_date': '2026-01-01', 'status': 'beta'},
            'family': family, 'classes': [item]}


class InvariantSemanticContractTests(unittest.TestCase):
    def test_valid_polarity_separation_passes(self):
        data = fixture()
        self.assertEqual(VALIDATOR.schema_errors(data, SCHEMA, SCHEMA), [])
        for item in [data['family'], *data['classes']]:
            self.assertEqual(VALIDATOR.invariant_description_errors(item, 'fixture'), [])

    def test_explicit_failure_fields_are_required_for_both_kinds(self):
        for kind in ('family', 'class'):
            for field in ('failure_condition', 'failure_plain_english'):
                with self.subTest(kind=kind, field=field):
                    data = fixture()
                    item = data['family'] if kind == 'family' else data['classes'][0]
                    del item[field]
                    errors = VALIDATOR.schema_errors(data, SCHEMA, SCHEMA)
                    self.assertTrue(any(f"missing required property '{field}'" in e for e in errors))

    def test_failure_recognition_scope_cannot_be_missing_or_success(self):
        for value in (None, 'successful-invariant', 'ambiguous-boundary'):
            data = fixture()
            recognition = data['classes'][0]['failure_recognition']
            if value is None:
                del recognition['applies_to']
            else:
                recognition['applies_to'] = value
            self.assertTrue(VALIDATOR.schema_errors(data, SCHEMA, SCHEMA))

    def test_family_failure_boundary_scope_is_required(self):
        for value in (None, 'successful-invariant'):
            data = fixture()
            if value is None:
                del data['family']['boundary_role']
            else:
                data['family']['boundary_role'] = value
            self.assertTrue(VALIDATOR.schema_errors(data, SCHEMA, SCHEMA))

    def test_failure_definitions_cannot_be_primary_descriptions(self):
        for value in ('A failure in which evidence is missing.',
                      'Failures where evidence is unusable.',
                      'The system fails to retain evidence.',
                      'A lineage failure in which source binding is lost.',
                      'A success in which evidence is available.'):
            for field in ('definition', 'plain_english'):
                item = fixture()['classes'][0]
                item[field] = value
                self.assertTrue(VALIDATOR.invariant_description_errors(item, 'fixture'))

    def test_copied_failure_or_recognition_text_is_rejected(self):
        data = fixture()
        for kind in ('family', 'class'):
            for source in ('failure_condition', 'failure_plain_english'):
                for target in ('definition', 'plain_english'):
                    item = copy.deepcopy(data['family'] if kind == 'family' else data['classes'][0])
                    item[target] = '  ' + item[source].upper() + '  '
                    self.assertTrue(VALIDATOR.invariant_description_errors(item, 'fixture'))
        item = data['classes'][0]
        item['definition'] = item['failure_recognition']['required_conditions'][0]
        self.assertTrue(VALIDATOR.invariant_description_errors(item, 'fixture'))

    def test_negative_normative_boundary_is_valid_invariant_language(self):
        item = fixture()['classes'][0]
        item['definition'] = 'Capability is not permission; valid authority remains independently established.'
        self.assertEqual(VALIDATOR.invariant_description_errors(item, 'fixture'), [])

    def test_all_publication_modes_keep_invariant_and_failure_separate(self):
        data = fixture()
        outputs = [RENDERER.markdown_family(data), RENDERER.html_family(data),
                   RENDERER.publication_family_html(data, 1)]
        for output in outputs:
            with self.subTest(output=output[:40]):
                for item in [data['family'], data['classes'][0]]:
                    self.assertIn(item['plain_english'], output)
                    self.assertIn(item['definition'], output)
                    self.assertIn(item['failure_condition'], output)
                    self.assertIn(item['failure_plain_english'], output)
                    self.assertLess(output.index(item['definition']), output.index(item['failure_condition']))
                self.assertIn('Success recognition criteria', output)
                self.assertIn(data['classes'][0]['success_condition'], output)
                self.assertIn('Failure recognition criteria', output)
                self.assertIn('Exclusions from failure recognition', output)
                self.assertIn('Failure examples and boundary illustrations', output)
                for role in ('failure-occurrence', 'successful-invariant', 'ambiguous-boundary'):
                    self.assertIn(role, output)
                self.assertIn('Absence of failure evidence alone does not establish successful holding', output)


class PositiveEvidenceAdmissionTests(unittest.TestCase):
    def admission(self, success, failure, excluded=False):
        import sys
        sys.path.insert(0, str(ROOT.parent / 'scripts'))
        from taxonomy_polarity import established_polarities
        return established_polarities(fixture()['classes'][0], success_evidence=success,
                                      failure_evidence=failure, failure_excluded=excluded)

    def test_absence_of_either_polarity_does_not_prove_the_other(self):
        self.assertEqual(self.admission([], []), set())
        self.assertEqual(self.admission([['source_records[0]'], []], []), set())
        self.assertEqual(self.admission([], [['source_records[0]'], []]), set())

    def test_exclusion_from_failure_does_not_prove_success(self):
        self.assertEqual(self.admission([], [['source_records[0]']] * 2, True), set())

    def test_independent_complete_affirmative_evidence_is_required(self):
        self.assertEqual(self.admission([['source_records[0]']] * 2, []), {'successful-invariant'})
        self.assertEqual(self.admission([], [['source_records[0]']] * 2), {'failure-occurrence'})

    def test_success_cannot_restate_invariant_or_primary_definition(self):
        for field in ('invariant', 'definition', 'failure_condition'):
            item = fixture()['classes'][0]
            item['success_condition'] = item[field]
            self.assertTrue(VALIDATOR.invariant_description_errors(item, 'fixture'))

    def test_success_scope_is_explicit_and_cannot_be_failure(self):
        data = fixture()
        data['classes'][0]['success_recognition']['applies_to'] = 'failure-occurrence'
        self.assertTrue(VALIDATOR.schema_errors(data, SCHEMA, SCHEMA))


if __name__ == '__main__':
    unittest.main()
