"""Isolated contract fixtures: no dependence on a particular live Incident."""
import copy
import importlib.util
from pathlib import Path
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
spec = importlib.util.spec_from_file_location('wording_record_validator', SCRIPTS / 'validate-vigil-records.py')
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class WordingSpecificEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.record = {
            'record_type': 'incident',
            'source_records': [{'source_url': 'https://example.org/original'}],
            'vigil_assessment': {'source_clause_analysis': {'clauses': [{
                'episode_id': 'E001', 'source_record_refs': ['source_records[0]'],
                'taxonomy_relationships': [{'rationale': 'First meaning'}, {'rationale': 'Second meaning'}],
                'statement_analysis': [
                    {'statement_id': 'S1', 'source_anchor': 'First words', 'source_paraphrase': 'First context',
                     'recovered_invariant_interpretation': 'First interpretation', 'taxonomy_relationship_indices': [0]},
                    {'statement_id': 'S2', 'source_anchor': 'Second words', 'source_paraphrase': 'Second context',
                     'recovered_invariant_interpretation': 'Second interpretation', 'taxonomy_relationship_indices': [1]},
                ],
            }]}}
        }
        self.clause = self.record['vigil_assessment']['source_clause_analysis']['clauses'][0]
        self.statement = self.clause['statement_analysis'][0]

    def errors(self):
        before = copy.deepcopy(self.record)
        result = []
        validator.validate_statement_analysis(Path('fixture.json'), self.record, result)
        self.assertEqual(self.record, before, 'validation must never rewrite the input')
        return '\n'.join(result)

    def test_unmarked_legacy_and_valid_statements_pass(self):
        self.assertEqual(self.errors(), '')
        del self.clause['statement_analysis']
        self.assertEqual(self.errors(), '')
        del self.record['vigil_assessment']['source_clause_analysis']
        self.assertEqual(self.errors(), '')

    def test_exhaustive_bindings_and_context_without_relationships(self):
        self.clause['statement_analysis'].append({
            'statement_id': 'S3', 'recovered_invariant_interpretation': 'Context only',
            'taxonomy_relationship_indices': []})
        self.assertEqual(self.errors(), '')
        self.clause['statement_analysis'][1]['taxonomy_relationship_indices'] = []
        self.assertIn('omits parent relationship indices [1]', self.errors())

    def test_duplicate_indices_within_and_between_statements_fail(self):
        self.statement['taxonomy_relationship_indices'] = [0, 0]
        self.assertIn('duplicates parent relationship index 0', self.errors())
        self.statement['taxonomy_relationship_indices'] = [0, 1]
        self.assertIn('duplicates parent relationship index 1', self.errors())

    def test_indices_are_integers_in_range_not_booleans(self):
        for value in [-1, 2, 0.0, True, '0', None, {}, []]:
            with self.subTest(value=value):
                self.statement['taxonomy_relationship_indices'] = [value]
                self.assertIn('out-of-range or non-integer', self.errors())

    def test_ids_are_nonempty_and_unique_within_parent(self):
        for value in ['', ' ', None, 7]:
            self.statement['statement_id'] = value
            self.assertIn('statement_id must be non-empty', self.errors())
        self.statement['statement_id'] = ' S2 '
        self.assertIn('statement_id duplicates', self.errors())

    def test_each_statement_requires_its_own_interpretation(self):
        self.clause['recovered_invariant_interpretation'] = 'Parent explanation is insufficient'
        del self.statement['recovered_invariant_interpretation']
        self.assertIn('recovered_invariant_interpretation must explain', self.errors())

    def test_malformed_statement_shapes_fail_without_crashing(self):
        for value in [None, {}, 'invalid']:
            self.clause['statement_analysis'] = value
            self.assertIn('statement_analysis must be an array', self.errors())
        self.clause['statement_analysis'] = [None]
        self.assertIn('must be an object', self.errors())

    def test_original_quote_requires_local_quote_context_and_parent_refs(self):
        self.statement['wording_evidence'] = {'basis': 'original-quotation'}
        self.assertEqual(self.errors(), '')
        del self.statement['source_anchor']
        self.clause['source_anchor'] = 'A parent quote cannot supply the local quotation'
        self.assertIn('source_anchor must contain', self.errors())
        self.statement['source_anchor'] = 'Words'
        del self.statement['source_paraphrase']
        self.assertIn('source_paraphrase must give local context', self.errors())
        self.statement['source_paraphrase'] = 'Context'
        for refs in [None, [], ['source_records[8]'], ['source_records[0]', 'source_records[0]'], [{}]]:
            self.clause['source_record_refs'] = refs
            self.assertIn('source_record_refs', self.errors())

    def test_attributed_quote_requires_attribution_and_access_limits(self):
        self.statement['wording_evidence'] = {'basis': 'attributed-quotation'}
        self.assertIn('attribution must identify', self.errors())
        self.assertIn('access_limitations must explain', self.errors())
        self.statement['wording_evidence'].update(attribution='The author reports these words.',
                                                access_limitations='Native dialogue unavailable.')
        self.assertEqual(self.errors(), '')

    def test_unavailable_basis_preserves_paraphrase_without_inventing_quote(self):
        self.statement['wording_evidence'] = {'basis': 'unavailable', 'access_limitations': 'No transcript survives.'}
        self.assertIn('source_anchor must be absent or empty', self.errors())
        del self.statement['source_anchor']
        self.assertEqual(self.errors(), '')
        del self.statement['source_paraphrase']
        self.assertIn('source_paraphrase must give local context', self.errors())
        del self.statement['wording_evidence']['access_limitations']
        self.assertIn('access_limitations must explain', self.errors())

    def test_clause_level_marker_and_invalid_basis(self):
        self.clause.update(source_anchor='Parent quotation', source_paraphrase='Parent context',
                           wording_evidence={'basis': 'original-quotation'})
        self.assertEqual(self.errors(), '')
        for value in [None, [], 'original-quotation', {}, {'basis': []}, {'basis': 'paraphrase'}]:
            self.clause['wording_evidence'] = value
            self.assertIn('wording_evidence', self.errors())

    def test_record_validation_invokes_the_new_checks(self):
        errors, _ = validator.validate_record(Path('fixture.json'), self.record)
        # The intentionally minimal fixture has unrelated omissions, but no wording error.
        self.assertFalse(any('statement_analysis' in error for error in errors))
        self.statement['taxonomy_relationship_indices'] = []
        errors, _ = validator.validate_record(Path('fixture.json'), self.record)
        self.assertTrue(any('omits parent relationship indices [0]' in error for error in errors))


if __name__ == '__main__':
    unittest.main()
