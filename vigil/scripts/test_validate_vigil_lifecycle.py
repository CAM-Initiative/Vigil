#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("validate-vigil-lifecycle.py")
SPEC = importlib.util.spec_from_file_location("validate_vigil_lifecycle", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load VIGIL lifecycle validator")
VALIDATOR = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = VALIDATOR
SPEC.loader.exec_module(VALIDATOR)


class RepairBasisLifecycleTests(unittest.TestCase):
    def failure(
        self,
        status: str,
        basis: str,
        repaired_by=None,
        coverage_classification: str = "partial-coverage",
        verification_status: str | None = None,
    ):
        repaired_by = [] if repaired_by is None else repaired_by
        verification_status = verification_status or ("corpus-verified" if repaired_by else "unverified")
        return {
            "id": "VIGIL-TEST-FM-0001",
            "record_type": "failure_mode",
            "ecosystem_status": {
                "status": "active",
                "basis": "Test ecosystem remains active.",
                "last_assessed": "2026-07-17",
                "monitoring_required": True,
            },
            "repair_status": {
                "status": status,
                "repaired_by": repaired_by,
                "date_repaired": "2026-07-17" if repaired_by else "",
                "verification_status": verification_status,
                "monitoring_status": "test",
                "verification_note": "test",
                "repair_basis": basis,
                "remaining_gaps": ["Test gap."],
            },
            "linked_records": {"related_patch_notes": repaired_by},
            "corpus_coverage": {
                "classification": coverage_classification,
                "corpus_repository": "CAM-Initiative/Caelestis",
                "corpus_ref": "main",
                "corpus_commit": "test-commit",
                "assessed_date": "2026-07-17",
                "coverage_summary": "Corpus coverage remains distinct from repair provenance.",
                "covered_by": [],
                "remaining_gaps": ["Test gap."],
            },
        }

    def validate(self, record, records=None):
        errors = []
        VALIDATOR.validate_failure(
            record["id"],
            record,
            Path("VIGIL-TEST-FM.json"),
            records or {record["id"]: record},
            errors,
        )
        return errors

    def test_unrepaired_uses_not_yet_established_despite_partial_coverage(self):
        record = self.failure("unrepaired", "not-yet-established")
        self.assertEqual(self.validate(record), [])

    def test_unrepaired_rejects_corpus_coverage_term_as_repair_basis(self):
        record = self.failure("unrepaired", "partial-coverage")
        errors = self.validate(record)
        self.assertTrue(any("repair_basis" in error for error in errors))

    def test_no_confirmed_coverage_is_canonical(self):
        record = self.failure(
            "unrepaired",
            "not-yet-established",
            coverage_classification="no-confirmed-coverage",
        )
        self.assertEqual(self.validate(record), [])

    def test_uncovered_is_rejected_as_deprecated_coverage_vocabulary(self):
        record = self.failure(
            "unrepaired",
            "not-yet-established",
            coverage_classification="uncovered",
        )
        errors = self.validate(record)
        self.assertTrue(any("corpus_coverage.classification" in error for error in errors))

    def test_partially_repaired_requires_patch(self):
        record = self.failure("partially-repaired", "patch-implemented")
        errors = self.validate(record)
        self.assertTrue(any("requires at least one repairing patch" in error for error in errors))

    def test_partially_repaired_accepts_linked_patch(self):
        patch_id = "VIGIL-TEST-PATCH-0001"
        record = self.failure("partially-repaired", "patch-implemented", [patch_id])
        patch = {
            "id": patch_id,
            "record_type": "patch",
            "linked_records": {"related_failure_modes": [record["id"]]},
            "corpus_implementation": {"canonical_state": "canonical-main"},
        }
        errors = self.validate(record, {record["id"]: record, patch_id: patch})
        self.assertEqual(errors, [])

    def test_repaired_rejects_branch_only_patch(self):
        patch_id = "VIGIL-TEST-PATCH-0001"
        record = self.failure("repaired", "patch-implemented", [patch_id])
        patch = {
            "id": patch_id,
            "record_type": "patch",
            "linked_records": {"related_failure_modes": [record["id"]]},
            "corpus_implementation": {"canonical_state": "branch-only"},
        }
        errors = self.validate(record, {record["id"]: record, patch_id: patch})
        self.assertTrue(any("branch-only" in error for error in errors))

    def test_implemented_repair_accepts_regression_detected(self):
        patch_id = "VIGIL-TEST-PATCH-0001"
        record = self.failure(
            "repaired",
            "patch-implemented",
            [patch_id],
            coverage_classification="implemented-repair",
            verification_status="regression-detected",
        )
        record["corpus_coverage"]["covered_by"] = [
            {
                "instrument_id": "CAM-EQ2026-RELATION-007-PLATINUM",
                "path": "Governance/Charters/CAM-EQ2026-RELATION-007-PLATINUM.md",
                "sections": ["§5.6.2"],
                "coverage_type": "implemented-doctrine",
            }
        ]
        patch = {
            "id": patch_id,
            "record_type": "patch",
            "linked_records": {"related_failure_modes": [record["id"]]},
            "corpus_implementation": {"canonical_state": "canonical-main"},
        }
        errors = self.validate(record, {record["id"]: record, patch_id: patch})
        self.assertEqual(errors, [])


class ProposalLifecycleTests(unittest.TestCase):
    def validate(self, record, records):
        errors = []
        VALIDATOR.validate_proposal(
            record,
            Path("VIGIL-TEST-PROP.json"),
            records,
            errors,
        )
        return errors

    def test_resolved_proposal_rejects_branch_only_patch(self):
        patch_id = "VIGIL-TEST-PATCH-0001"
        proposal = {
            "resolution_status": {
                "status": "resolved-by-patch",
                "resolved_by": [patch_id],
            }
        }
        patch = {
            "id": patch_id,
            "record_type": "patch",
            "corpus_implementation": {"canonical_state": "branch-only"},
        }
        errors = self.validate(proposal, {patch_id: patch})
        self.assertTrue(any("branch-only" in error for error in errors))

    def test_resolved_proposal_accepts_canonical_patch(self):
        patch_id = "VIGIL-TEST-PATCH-0001"
        proposal = {
            "resolution_status": {
                "status": "resolved-by-patch",
                "resolved_by": [patch_id],
            }
        }
        patch = {
            "id": patch_id,
            "record_type": "patch",
            "corpus_implementation": {"canonical_state": "canonical-main"},
        }
        self.assertEqual(self.validate(proposal, {patch_id: patch}), [])


if __name__ == "__main__":
    unittest.main()
