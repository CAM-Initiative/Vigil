#!/usr/bin/env python3
"""Tests for role-aware Failure Taxonomy adjudication infrastructure."""
import runpy
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SYNC = runpy.run_path(
    str(ROOT / "vigil" / "scripts" / "sync-vigil-taxonomy-adjudications.py")
)
VALIDATOR = runpy.run_path(
    str(ROOT / "vigil" / "scripts" / "validate-vigil-taxonomy-adjudications.py")
)


class MigrationTests(unittest.TestCase):
    def test_yes_migrates_to_failure_occurrence(self):
        self.assertEqual(
            SYNC["migrate_row"]({"decision": "YES", "reason": "Specific cause."}),
            {"decision": "failure-occurrence", "reason": "Specific cause."},
        )

    def test_no_is_preserved_without_inventing_no_mapping(self):
        self.assertEqual(
            SYNC["migrate_row"]({"decision": "NO", "reason": "Condition absent."}),
            {
                "decision": "MISSING",
                "reason": "",
                "prior_failure_adjudication": {
                    "decision": "NO",
                    "reason": "Condition absent.",
                },
            },
        )

    def test_unresolved_remains_evidence_uncertainty(self):
        self.assertEqual(
            SYNC["migrate_row"](
                {"decision": "UNRESOLVED", "reason": "Required state is not public."}
            ),
            {"decision": "unresolved", "reason": "Required state is not public."},
        )


class RoleParsingTests(unittest.TestCase):
    def test_section02_accepts_only_documented_role_values(self):
        record = {
            "vigil_assessment": {
                "source_clause_analysis": {
                    "clauses": [
                        {
                            "taxonomy_relationships": [
                                {
                                    "class_id": "VIGIL-FC-000001",
                                    "relationship": "failure-occurrence contribution",
                                    "canonical_taxonomy_mapping": True,
                                },
                                {
                                    "class_id": "VIGIL-FC-000002",
                                    "relationship": "successful-invariant",
                                    "canonical_taxonomy_mapping": True,
                                },
                                {
                                    "class_id": "VIGIL-FC-000003",
                                    "relationship": "ambiguous-boundary exemplar",
                                    "canonical_taxonomy_mapping": True,
                                },
                                {
                                    "class_id": "VIGIL-FC-000004",
                                    "relationship": "canonical failure mapping",
                                    "canonical_taxonomy_mapping": True,
                                },
                            ]
                        }
                    ]
                }
            }
        }
        roles, invalid = VALIDATOR["section02_mappings_by_role"](record)
        self.assertEqual(roles["failure-occurrence"], {"VIGIL-FC-000001"})
        self.assertEqual(roles["successful-invariant"], {"VIGIL-FC-000002"})
        self.assertEqual(roles["ambiguous-boundary"], {"VIGIL-FC-000003"})
        self.assertEqual(invalid, [("VIGIL-FC-000004", "canonical failure mapping")])

    def test_incident_filter_rejects_an_unenrolled_incident(self):
        errors, actions = VALIDATOR["validate"](["VIGIL-INC-999999"])
        self.assertEqual(
            errors,
            ["VIGIL-INC-999999: Incident is not enrolled in the matrix"],
        )
        self.assertEqual(actions, [])


if __name__ == "__main__":
    unittest.main()
