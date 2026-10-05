import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from resolve_clause_external_requirements import resolve_clause


class ClauseResolverTests(unittest.TestCase):
    def setUp(self):
        self.clause = {'adjudication_status': 'mapped', 'taxonomy_relationships': [
            {'class_id': 'FC-A', 'canonical_taxonomy_mapping': True, 'relationship': 'successful-invariant'}]}
        self.relationship = {'relationship_id': 'link-a', 'requirement_id': 'req-a', 'class_id': 'FC-A',
                             'strength': 'direct', 'review_status': 'supported'}

    def test_scoped_deterministic_deduplication(self):
        result = resolve_clause(self.clause, [self.relationship] * 2, {'req-a'})
        self.assertEqual(len(result), 1)
        self.assertTrue(result[0]['requires_independent_relevance_and_alignment'])
        self.assertEqual(result[0]['derived_from_class_ids'], ['FC-A'])
        self.assertNotIn('finding', result[0])

    def test_contextual_unresolved_and_unresolvable_links_are_excluded(self):
        for changes in ({'strength': 'contextual'}, {'review_status': 'unresolved'}, {'class_id': 'FC-B'}):
            self.assertEqual(resolve_clause(self.clause, [self.relationship | changes], {'req-a'}), [])
        self.assertEqual(resolve_clause(self.clause, [self.relationship], set()), [])

    def test_noncanonical_candidate_and_unresolved_clause_are_excluded(self):
        self.clause['taxonomy_relationships'][0]['canonical_taxonomy_mapping'] = False
        self.assertEqual(resolve_clause(self.clause, [self.relationship], {'req-a'}), [])
        self.clause['taxonomy_relationships'][0]['canonical_taxonomy_mapping'] = True
        self.clause['adjudication_status'] = 'unresolved'
        self.assertEqual(resolve_clause(self.clause, [self.relationship], {'req-a'}), [])


if __name__ == '__main__':
    unittest.main()
