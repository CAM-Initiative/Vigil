"""Regression tests for optional source-episode provenance and EXTREQ pointers."""
from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from source_episode_validation import episode_errors
from occurrence_requirement_validation import assessment_errors

FC = "VIGIL-FC-000001"
REQ = "EXTREQ-0123456789ABCDEF"


def sample_record():
    return {
        "source_records": [{}, {}],
        "vigil_assessment": {"source_clause_analysis": {"clauses": [
            {"episode_id": "E001", "source_record_refs": ["source_records[0]"],
             "taxonomy_relationships": [{"class_id": FC, "canonical_taxonomy_mapping": True,
                                          "relationship": "successful-invariant"}]},
            {"episode_id": "E002", "source_record_refs": ["source_records[1]"],
             "taxonomy_relationships": []},
        ]}},
        "external_requirement_assessments": [{
            "requirement_id": REQ, "alignment_result": "boundary",
            "assessment_basis": "Independent bounded requirement conclusion.",
            "assessed_on": "2026-10-08", "source_record_refs": ["source_records[0]"],
            "derived_from_class_ids": [FC],
            "source_clause_indices": [0], "source_episode_refs": ["E001"],
        }],
    }


class SourceEpisodeIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.record = sample_record()
        self.relationships = [{"class_id": FC, "requirement_id": REQ,
                               "review_status": "supported", "strength": "direct"}]

    def requirement_errors(self):
        return assessment_errors(self.record, {REQ}, self.relationships)

    def test_valid_opted_in_episode_contract(self):
        self.assertEqual(episode_errors(self.record), [])
        self.assertEqual(self.requirement_errors(), [])

    def test_non_migrated_records_remain_valid(self):
        for clause in self.record["vigil_assessment"]["source_clause_analysis"]["clauses"]:
            clause.pop("episode_id")
            clause.pop("source_record_refs")
        self.record["external_requirement_assessments"][0].pop("source_episode_refs")
        self.assertEqual(episode_errors(self.record), [])
        self.assertEqual(self.requirement_errors(), [])

    def test_duplicate_episode_rejected(self):
        clauses = self.record["vigil_assessment"]["source_clause_analysis"]["clauses"]
        clauses[1]["episode_id"] = "E001"
        self.assertTrue(any("duplicates" in error for error in episode_errors(self.record)))

    def test_missing_episode_and_invalid_source_rejected(self):
        clauses = self.record["vigil_assessment"]["source_clause_analysis"]["clauses"]
        clauses[1].pop("episode_id")
        clauses[1]["source_record_refs"] = ["source_records[5]"]
        errors = episode_errors(self.record)
        self.assertTrue(any("episode_id" in error for error in errors))
        self.assertTrue(any("does not resolve" in error for error in errors))

    def test_migrated_derived_assessment_requires_episode_pointer(self):
        self.record["external_requirement_assessments"][0].pop("source_episode_refs")
        self.assertTrue(any("source_episode_refs required" in e for e in self.requirement_errors()))

    def test_same_in_range_index_different_episode_rejected(self):
        self.record["external_requirement_assessments"][0]["source_clause_indices"] = [1]
        self.assertTrue(any("disagree" in e for e in self.requirement_errors()))

    def test_dangling_episode_reference_rejected(self):
        self.record["external_requirement_assessments"][0]["source_episode_refs"] = ["E999"]
        self.assertTrue(any("unresolved episode" in e for e in self.requirement_errors()))

    def test_valid_episode_reference_without_numeric_index(self):
        self.record["external_requirement_assessments"][0].pop("source_clause_indices")
        self.assertEqual(self.requirement_errors(), [])

    def test_polarity_independent_external_result(self):
        relationship = self.record["vigil_assessment"]["source_clause_analysis"]["clauses"][0]["taxonomy_relationships"][0]
        for role in ("failure-occurrence", "successful-invariant", "ambiguous-boundary"):
            relationship["relationship"] = role
            for result in ("aligned", "not-aligned", "boundary"):
                self.record["external_requirement_assessments"][0]["alignment_result"] = result
                self.assertEqual(self.requirement_errors(), [])

    def test_multiple_class_explanations_do_not_require_multiple_events(self):
        clause = self.record["vigil_assessment"]["source_clause_analysis"]["clauses"][0]
        clause["taxonomy_relationships"].append({
            "class_id": "VIGIL-FC-000075", "canonical_taxonomy_mapping": True,
            "relationship": "failure-occurrence contribution"})
        self.assertEqual(episode_errors(self.record), [])
        self.assertEqual(self.requirement_errors(), [])


if __name__ == "__main__":
    unittest.main()
