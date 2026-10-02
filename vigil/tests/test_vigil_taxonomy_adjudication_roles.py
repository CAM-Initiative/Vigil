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
    def test_unresolved_reason_rejects_matrix_state_placeholder(self):
        self.assertFalse(
            VALIDATOR["unresolved_reason_identifies_evidence_gap"](
                "The preserved record does not establish the recognition facts "
                "needed to resolve VIGIL-FC-000040; this candidate remains "
                "unresolved at the class boundary."
            )
        )

    def test_unresolved_reason_accepts_occurrence_specific_gap(self):
        self.assertTrue(
            VALIDATOR["unresolved_reason_identifies_evidence_gap"](
                "The agents attacked excluded countries, but the record does not "
                "establish whether an operative target restriction reached each agent."
            )
        )

    def test_unresolved_reason_accepts_equivalent_gap_constructions(self):
        reasons = (
            "No receiving-agent trace establishes whether the inherited restriction was revalidated.",
            "The record does not identify a protective gate or show whether it blocked the probe.",
            "The consent records and identity-use authority facts are unavailable.",
            "The diagnostic artefacts needed to establish decision authority are unavailable.",
        )
        for reason in reasons:
            with self.subTest(reason=reason):
                self.assertTrue(VALIDATOR["unresolved_reason_identifies_evidence_gap"](reason))

    def test_unresolved_reason_still_rejects_generic_or_affirmative_reasons(self):
        for reason in (
            "",
            "The candidate remains unresolved at the class boundary.",
            "The recognition fact needed to resolve VIGIL-FC-000001 is unavailable.",
            "The gate rejected the unauthorised request.",
        ):
            with self.subTest(reason=reason):
                self.assertFalse(VALIDATOR["unresolved_reason_identifies_evidence_gap"](reason))

    def test_section02_accepts_only_documented_role_values(self):
        record = {
            "vigil_assessment": {
                "source_clause_analysis": {
                    "clauses": [
                        {
                            "taxonomy_relationships": [
                                {
                                    "class_id": "VIGIL-FC-000005",
                                    "relationship": "ambiguous-boundary",
                                    "canonical_taxonomy_mapping": True,
                                },
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
        self.assertEqual(roles["ambiguous-boundary"], {"VIGIL-FC-000003", "VIGIL-FC-000005"})
        self.assertEqual(invalid, [("VIGIL-FC-000004", "canonical failure mapping")])

    def test_incident_filter_rejects_an_unenrolled_incident(self):
        errors, actions = VALIDATOR["validate"](["VIGIL-INC-999999"])
        self.assertEqual(
            errors,
            ["VIGIL-INC-999999: Incident is not enrolled in the matrix"],
        )
        self.assertEqual(actions, [])


class ExemplarReciprocityTests(unittest.TestCase):
    def roles(self, role, class_id="VIGIL-FC-000001"):
        roles = {name: set() for name in VALIDATOR["ROLE_DECISIONS"]}
        roles[role].add(class_id)
        return roles

    def test_occurrence_roles_do_not_require_exemplar_admission(self):
        for role in ("successful-invariant", "ambiguous-boundary"):
            with self.subTest(role=role):
                self.assertEqual(
                    VALIDATOR["reciprocal_actions"]("VIGIL-INC-999998", self.roles(role), {}),
                    [],
                )

    def test_matching_admitted_exemplar_passes(self):
        for role in ("successful-invariant", "ambiguous-boundary"):
            with self.subTest(role=role):
                exemplars = {("VIGIL-FC-000001", role): {"VIGIL-INC-999998"}}
                self.assertEqual(
                    VALIDATOR["reciprocal_actions"]("VIGIL-INC-999998", self.roles(role), exemplars),
                    [],
                )

    def test_admitted_exemplar_with_missing_or_wrong_role_fails(self):
        for role in ("successful-invariant", "ambiguous-boundary"):
            exemplars = {("VIGIL-FC-000001", role): {"VIGIL-INC-999998"}}
            for roles in (self.roles("failure-occurrence"), self.roles(role, "VIGIL-FC-000002")):
                with self.subTest(role=role, roles=roles):
                    self.assertEqual(len(VALIDATOR["reciprocal_actions"](
                        "VIGIL-INC-999998", roles, exemplars
                    )), 1)

    def test_other_incident_admission_does_not_require_this_incident_mapping(self):
        exemplars = {("VIGIL-FC-000001", "successful-invariant"): {"VIGIL-INC-999997"}}
        self.assertEqual(VALIDATOR["reciprocal_actions"](
            "VIGIL-INC-999998", self.roles("failure-occurrence"), exemplars
        ), [])

    def test_role_surface_comparison_accepts_non_exemplar_occurrence(self):
        for role in ("successful-invariant", "ambiguous-boundary"):
            record = {
                "taxonomy_classification": {
                    "primary_classification": {"class_id": "VIGIL-FC-000001", "classification_role": role},
                },
                "vigil_assessment": {"source_clause_analysis": {"clauses": [{
                    "taxonomy_relationships": [{
                        "class_id": "VIGIL-FC-000001", "relationship": role,
                        "canonical_taxonomy_mapping": True,
                    }],
                }]}},
            }
            with self.subTest(role=role):
                self.assertEqual(VALIDATOR["compare_role_surfaces"](
                    "VIGIL-INC-999998", self.roles(role), record, {}
                ), [])
                actions = VALIDATOR["compare_role_surfaces"](
                    "VIGIL-INC-999998", self.roles("failure-occurrence"), record, {}
                )
                self.assertTrue(actions)


if __name__ == "__main__":
    unittest.main()
