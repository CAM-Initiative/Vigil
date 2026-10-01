"""Occurrence polarity does not require textbook exemplar admission."""
import importlib.util
import unittest
from pathlib import Path
from unittest.mock import patch
p = Path(__file__).resolve().parents[1] / 'scripts/validate-vigil-records.py'
spec = importlib.util.spec_from_file_location('role_independence_validator', p)
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class OccurrenceRoleIndependenceTests(unittest.TestCase):
    def test_partial_incident_can_have_local_success_or_ambiguity(self):
        for role in ('successful-invariant', 'ambiguous-boundary'):
            mapping = {'family_id': 'VIGIL-FF-9999', 'class_id': 'VIGIL-FC-999999',
                       'classification_role': role, 'classification_confidence': 'high',
                       'classification_basis': 'The cited occurrence establishes this bounded local relationship.'}
            record = {'id': 'VIGIL-INC-999999', 'taxonomy_classification': {
                'classification_status': 'provisionally-classified', 'taxonomy_version': 'fixture',
                'classification_basis': 'One local boundary is assessed; another remains unresolved.',
                'primary_classification': mapping, 'secondary_classifications': [],
                'classification_review_provenance': {'review_date': '2026-10-01', 'reviewer': 'fixture',
                                                     'review_status': 'provisional'},
                'adjudication_coverage': {'status': 'partial'}},
                'vigil_assessment': {'source_clause_analysis': {'clauses': [
                    {'adjudication_status': 'mapped', 'taxonomy_relationships': [
                        {'class_id': mapping['class_id'], 'canonical_taxonomy_mapping': True, 'relationship': role}]},
                    {'adjudication_status': 'unresolved', 'taxonomy_relationships': [
                        {'class_id': mapping['class_id'], 'canonical_taxonomy_mapping': False,
                         'relationship': 'unresolved candidate'}]}]}}}
            errors = []
            with patch.object(validator, 'taxonomy_catalogue', return_value=(
                {'VIGIL-FF-9999': {}}, {'VIGIL-FC-999999': {'family_id': 'VIGIL-FF-9999'}})), \
                    patch.object(validator, 'retired_taxonomy_class_successors', return_value={}):
                validator.validate_incident_taxonomy(Path('fixture.json'), record, errors)
            self.assertEqual(errors, [], role)


if __name__ == '__main__':
    unittest.main()
