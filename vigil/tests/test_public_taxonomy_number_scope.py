import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('number_prose_validator', Path(__file__).resolve().parents[1] / 'scripts/validate-vigil-records.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


class PublicTaxonomyNumberScopeTests(unittest.TestCase):
    def errors(self, record):
        errors = []
        v.validate_taxonomy_number_prose(Path('fixture.json'), record, errors)
        return errors

    def test_aggregate_and_mapping_bases_are_checked(self):
        for field in ['classification_basis', 'primary_classification', 'secondary_classifications']:
            value = 'This demonstrates FC-038.'
            block = {field: value if field == 'classification_basis' else {'classification_basis': value}}
            if field == 'secondary_classifications': block[field] = [block[field]]
            self.assertEqual(len(self.errors({'taxonomy_classification': block})), 1)

    def test_clause_notes_context_and_rationales_are_checked(self):
        for field in ['source_paraphrase', 'recovered_invariant_interpretation', 'adjudication_note', 'taxonomy_relationships']:
            value = 'VIGIL-FC-000038 applies.'
            clause = {field: value if field != 'taxonomy_relationships' else [{'rationale': value}]}
            self.assertEqual(len(self.errors({'vigil_assessment': {'source_clause_analysis': {'clauses': [clause]}}})), 1)

    def test_statement_explanations_and_external_comparisons_are_checked(self):
        record = {'vigil_assessment': {'source_clause_analysis': {'clauses': [{'statement_analysis': [
            {'source_paraphrase': 'FC-038', 'recovered_invariant_interpretation': 'FC-083'}]}]}},
            'external_assessments': [{'vigil_comparison_note': 'VIGIL-FF-0001'}]}
        self.assertEqual(len(self.errors(record)), 3)

    def test_structured_ids_and_original_quotations_are_preserved(self):
        record = {'taxonomy_classification': {'primary_classification': {'class_id': 'VIGIL-FC-000038', 'family_id': 'VIGIL-FF-0001', 'classification_basis': 'The available control did not activate.'}},
                  'vigil_assessment': {'source_clause_analysis': {'clauses': [{'source_anchor': 'The source literally says FC-038.', 'taxonomy_relationships': [{'class_id': 'VIGIL-FC-000038', 'rationale': 'The evidence does not show control activation.'}], 'statement_analysis': [{'source_anchor': 'FC-083'}]}]}},
                  'interpretive_provenance': {'historical_note': 'Previously assessed under FC-038.'}}
        self.assertEqual(self.errors(record), [])

    def test_no_new_maintenance_word_prohibition_is_added(self):
        self.assertEqual(self.errors({'taxonomy_classification': {'classification_basis': 'The boundary was mapped after review.'}}), [])

    def test_canonical_validation_calls_the_check(self):
        errors, _ = v.validate_record(Path('fixture.json'), {'record_type': 'incident', 'taxonomy_classification': {'classification_basis': 'FC-038'}})
        self.assertTrue(any('contains taxonomy identifier' in e for e in errors))


if __name__ == '__main__': unittest.main()
