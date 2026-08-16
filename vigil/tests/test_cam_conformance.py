#!/usr/bin/env python3
"""Regression tests for VIGIL Layer 2 CAM applicability/conformance separation."""
from __future__ import annotations

import copy
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate-cam-conformance.py"
SPEC = importlib.util.spec_from_file_location("cam_conformance", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)


class CamConformanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.effective = MODULE.load(MODULE.EFFECTIVE_REQUIREMENTS)
        cls.extreq = cls.effective["requirements"][0]

    def fixture(self) -> dict:
        extreq = self.extreq
        commit = "0" * 40
        return {
            "assessment_id": MODULE.assessment_id(extreq["requirement_id"], commit),
            "extreq_id": extreq["requirement_id"],
            "external_source_id": extreq["external_source_id"],
            "source_version": extreq["source_version"],
            "normative_force": extreq["normative_force"],
            "alignment_relationship": extreq["alignment_relationship"],
            "applicability_state": "unresolved",
            "applicability_rationale": "Applicability has not yet been established against this corpus commit.",
            "coverage_state": "indeterminate",
            "cam_corpus_commit": commit,
            "cam_instrument_refs": [],
            "coverage_evidence_refs": [],
            "assessment_provenance": copy.deepcopy(MODULE.DEFAULT_PROVENANCE),
            "assurance_provenance": [],
            "remediation_required": False,
            "remediation_refs": [],
            "vigil_routing_state": "none",
            "limitations": ["No substantive CAM applicability finding is asserted by this fixture."],
        }

    def document(self, item: dict) -> dict:
        doc = MODULE.load(MODULE.ASSESSMENTS)
        doc["assessments"] = [item]
        return doc

    def test_current_layer2_state_is_empty_and_valid(self) -> None:
        doc = MODULE.load(MODULE.ASSESSMENTS)
        self.assertEqual(doc["assessments"], [])
        self.assertEqual(MODULE.validate_repository(doc, self.effective), [])

    def test_valid_unresolved_assessment_passes(self) -> None:
        item = self.fixture()
        self.assertEqual(MODULE.validate_repository(self.document(item), self.effective), [])

    def test_layer1_normative_semantics_drift_is_rejected(self) -> None:
        item = self.fixture()
        item["normative_force"] = (
            "industry-framework"
            if self.extreq["normative_force"] != "industry-framework"
            else "binding-law"
        )
        errors = MODULE.validate_repository(self.document(item), self.effective)
        self.assertTrue(any("normative_force differs from effective Layer 1 EXTREQ" in e for e in errors), errors)

    def test_unresolved_applicability_cannot_claim_full_coverage(self) -> None:
        item = self.fixture()
        item["coverage_state"] = "full"
        item["cam_instrument_refs"] = ["Governance/example.md"]
        item["coverage_evidence_refs"] = ["Governance/example.md#evidence"]
        errors = MODULE.validate_repository(self.document(item), self.effective)
        self.assertTrue(any("unresolved applicability requires indeterminate coverage" in e for e in errors), errors)

    def test_full_coverage_requires_evidence_and_instrument_refs(self) -> None:
        item = self.fixture()
        item["applicability_state"] = "applicable"
        item["coverage_state"] = "full"
        errors = MODULE.validate_repository(self.document(item), self.effective)
        self.assertTrue(any("full coverage requires CAM instrument references and coverage evidence" in e for e in errors), errors)

    def test_contract_approval_cannot_claim_human_review(self) -> None:
        item = self.fixture()
        item["assessment_provenance"]["human_review_status"] = "substantively-reviewed"
        errors = MODULE.validate_repository(self.document(item), self.effective)
        self.assertTrue(any("contract approval cannot assert substantive human review" in e for e in errors), errors)

    def test_not_applicable_assessment_cannot_require_remediation(self) -> None:
        item = self.fixture()
        item["applicability_state"] = "not-applicable"
        item["coverage_state"] = "not-applicable"
        item["remediation_required"] = True
        item["vigil_routing_state"] = "needs-review"
        errors = MODULE.validate_repository(self.document(item), self.effective)
        self.assertTrue(any("not-applicable assessment cannot require remediation" in e for e in errors), errors)


if __name__ == "__main__":
    unittest.main()
