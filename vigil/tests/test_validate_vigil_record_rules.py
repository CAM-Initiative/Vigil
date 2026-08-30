#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "vigil" / "scripts" / "validate-vigil-records.py"
SPEC = importlib.util.spec_from_file_location("validate_vigil_records", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load VIGIL validator")
VALIDATOR = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = VALIDATOR
SPEC.loader.exec_module(VALIDATOR)


class RuntimeConformanceValidationTests(unittest.TestCase):
    def validate_patch(self, block):
        errors = []
        VALIDATOR.validate_runtime_conformance(
            Path("VIGIL-TEST-PATCH.json"),
            {"record_type": "patch", "runtime_conformance": block},
            errors,
        )
        return errors

    def validate_failure(self, block):
        errors = []
        VALIDATOR.validate_runtime_non_conformance(
            Path("VIGIL-TEST-FM.json"),
            {"record_type": "failure_mode", "runtime_non_conformance": block},
            errors,
        )
        return errors

    def test_valid_compact_runtime_conformance(self):
        errors = self.validate_patch({
            "overall_status": "mixed",
            "confirming_count": 1,
            "non_confirming_count": 0,
            "unknown_count": 0,
            "confirming_runtimes": [{
                "vendor": "Example Vendor",
                "platform": "Example Platform",
                "runtime": "Example Runtime",
                "date_observed": "2026-07-13",
                "evidence_basis": "Maintainer behavioural testing"
            }],
            "notes": "Conformance remains runtime-bounded."
        })
        self.assertEqual(errors, [])

    def test_valid_compact_runtime_non_conformance(self):
        errors = self.validate_failure({
            "non_confirming_count": 1,
            "unknown_count": 0,
            "non_confirming_runtimes": [{
                "vendor": "Example Vendor",
                "platform": "Example Platform",
                "runtime": "Successor Runtime",
                "date_observed": "2026-07-13",
                "failure_expression": "Previously repaired behaviour recurred.",
                "evidence_urls": [],
                "related_patch_ids": ["VIGIL-2026-PATCH-0008"]
            }],
            "notes": "A non-confirming runtime does not invalidate the patch."
        })
        self.assertEqual(errors, [])

    def test_invalid_status_value(self):
        errors = self.validate_patch({
            "overall_status": "globally-confirmed",
            "confirming_count": 0,
            "non_confirming_count": 0,
            "unknown_count": 0,
            "notes": "Invalid test status."
        })
        self.assertTrue(any("overall_status" in error and "not allowed" in error for error in errors))

    def test_negative_count(self):
        errors = self.validate_patch({
            "overall_status": "unknown",
            "confirming_count": -1,
            "non_confirming_count": 0,
            "unknown_count": 0,
            "notes": "Negative count test."
        })
        self.assertTrue(any("non-negative integer" in error for error in errors))

    def test_count_detail_mismatch(self):
        errors = self.validate_failure({
            "non_confirming_count": 2,
            "unknown_count": 0,
            "non_confirming_runtimes": [{
                "vendor": "Example Vendor",
                "platform": "Example Platform",
                "runtime": "Runtime One",
                "date_observed": "2026-07-13",
                "failure_expression": "Observed regression.",
                "evidence_urls": [],
                "related_patch_ids": []
            }],
            "notes": "Mismatch test."
        })
        self.assertTrue(any("does not match" in error for error in errors))


class LinkedRecordIdentifierValidationTests(unittest.TestCase):
    def validate_record(self, linked_records):
        errors = []
        warnings = []
        VALIDATOR.validate_record(
            Path("VIGIL-2026-PROP-0999.json"),
            {
                "id": "VIGIL-2026-PROP-0999",
                "record_type": "proposal",
                "record_identity": {
                    "record_id": "VIGIL-2026-PROP-0999",
                    "record_type": "proposal",
                },
                "record_state": "active",
                "source_records": [],
                "linked_records": linked_records,
                "system_context": {
                    "platform_or_vendor": "Other",
                    "product_or_service": "Other",
                    "specific_model_or_runtime": "Not applicable",
                    "interface_surface": "test",
                },
            },
            {"VIGIL-2026-PROP-0999", "VIGIL-2026-FM-0001"},
            errors,
            warnings,
            VALIDATOR.FALLBACK_ALLOWED_PLATFORM_OR_VENDOR_VALUES,
            VALIDATOR.FALLBACK_ALLOWED_PRODUCT_OR_SERVICE_VALUES,
        )
        return errors, warnings

    def test_malformed_internal_link_is_an_error_not_a_future_record_warning(self):
        errors, warnings = self.validate_record({"related_failure_modes": ["VIGIL-1"]})

        self.assertTrue(any("malformed VIGIL record id 'VIGIL-1'" in error for error in errors))
        self.assertFalse(any("VIGIL-1" in warning for warning in warnings))

    def test_valid_future_internal_link_remains_a_warning(self):
        errors, warnings = self.validate_record({"related_failure_modes": ["VIGIL-2026-FM-0999"]})

        self.assertFalse(any("malformed" in error for error in errors))
        self.assertTrue(any("VIGIL-2026-FM-0999" in warning for warning in warnings))


class ResearchQualityValidationTests(unittest.TestCase):
    def valid_record(self):
        return {
            "id": "VIGIL-2026-RESEARCH-0999",
            "record_type": "research",
            "record_state": "active",
            "date_recorded": "2026-07-30",
            "title": "Research quality fixture",
            "summary": "A substantive fixture for the published research quality contract.",
            "status": "research record — non-binding",
            "publication_status": "published",
            "research_method": "Structured comparison of primary sources.",
            "research_scope": "A bounded test fixture.",
            "governance_purpose": "Validate the research quality contract.",
            "evidence_confidence": "corroborated",
            "corroboration_scope": "The fixture uses several primary artefacts from one institutional corpus.",
            "limitations": "Synthetic content used only for validator testing.",
            "source_corpus": [
                {
                    "title": f"Source {index}",
                    "publisher": "Example Research Institute",
                    "url": f"https://research.example/source-{index}",
                    "source_kind": "primary research",
                    "relevance": "Supports a distinct fixture claim.",
                }
                for index in range(1, 5)
            ],
            "domains": ["OPERATIONS"],
            "linked_records": {
                "related_observations": [],
                "related_failure_modes": [],
                "related_proposals": [],
                "related_patch_notes": [],
            },
        }

    def valid_body(self):
        sections = "\n\n".join(
            f"## {section}\n\n"
            + (
                "Claim "
                "[one](https://research.example/source-1), "
                "[two](https://research.example/source-2), and "
                "[three](https://research.example/source-3). "
                if section == "Findings"
                else ""
            )
            + ("evidence " * 240)
            for section in VALIDATOR.RESEARCH_REQUIRED_SECTIONS
        )
        return sections + "\n\n1. https://research.example/source-1\n2. https://research.example/source-2\n3. https://research.example/source-3\n4. https://research.example/source-4\n"

    def validate(self, record=None, body=None):
        errors = []
        VALIDATOR.validate_research_record(
            Path("VIGIL-2026-RESEARCH-0999.md"),
            record or self.valid_record(),
            {"VIGIL-2026-RESEARCH-0999"},
            errors,
            self.valid_body() if body is None else body,
        )
        return errors

    def test_substantive_published_research_passes(self):
        self.assertEqual(self.validate(), [])

    def test_thin_published_research_fails(self):
        errors = self.validate(body="## Research question\n\nToo short.")
        self.assertTrue(any("minimum is" in error for error in errors))
        self.assertTrue(any("missing required section" in error for error in errors))

    def test_published_research_requires_multiple_sources(self):
        record = self.valid_record()
        record["source_corpus"] = record["source_corpus"][:1]
        errors = self.validate(record=record)
        self.assertTrue(any("source_corpus entries" in error for error in errors))

    def test_single_publisher_corroboration_requires_qualification(self):
        record = self.valid_record()
        record.pop("corroboration_scope")
        errors = self.validate(record=record)
        self.assertTrue(any("corroboration_scope" in error for error in errors))


class RelationshipScopeValidationTests(unittest.TestCase):
    KNOWN_IDS = {
        "VIGIL-2026-FM-0001",
        "VIGIL-2026-FM-0002",
        "VIGIL-2026-PATCH-0001",
    }

    def validate(self, record):
        errors = []
        VALIDATOR.validate_relationship_scope(
            Path("VIGIL-TEST-RECORD.json"),
            record,
            self.KNOWN_IDS,
            errors,
        )
        return errors

    def test_contextual_relation_is_non_transitive(self):
        errors = self.validate({
            "record_type": "failure_mode",
            "linked_records": {
                "related_failure_modes": [],
                "contextual_relations": [{
                    "record_id": "VIGIL-2026-FM-0002",
                    "relationship": "contrast",
                    "chain_inclusion": False,
                    "rationale": "Comparison only; it is not part of this repair chain.",
                }],
            },
        })
        self.assertEqual(errors, [])

    def test_contextual_relation_cannot_also_be_authoritative(self):
        errors = self.validate({
            "record_type": "proposal",
            "linked_records": {
                "related_failure_modes": ["VIGIL-2026-FM-0001"],
                "contextual_relations": [{
                    "record_id": "VIGIL-2026-FM-0001",
                    "relationship": "adjacent",
                    "chain_inclusion": False,
                    "rationale": "Invalid dual classification.",
                }],
            },
        })
        self.assertTrue(any("both contextual and chain-included" in error for error in errors))

    def test_multiple_patch_failures_require_explicit_exception(self):
        errors = self.validate({
            "record_type": "patch",
            "linked_records": {
                "related_failure_modes": [
                    "VIGIL-2026-FM-0001",
                    "VIGIL-2026-FM-0002",
                ],
                "contextual_relations": [],
            },
        })
        self.assertTrue(any("multi-failure-mode exception" in error for error in errors))

    def test_multi_failure_patch_requires_per_failure_verification(self):
        errors = self.validate({
            "record_type": "patch",
            "linked_records": {
                "related_failure_modes": [
                    "VIGIL-2026-FM-0001",
                    "VIGIL-2026-FM-0002",
                ],
                "contextual_relations": [],
            },
            "repair_scope": {
                "primary_failure_mode": "VIGIL-2026-FM-0001",
                "additional_resolved_failure_modes": ["VIGIL-2026-FM-0002"],
                "multi_failure_mode_exception": True,
                "exception_rationale": "One indivisible amendment directly closes both failures.",
                "verification_by_failure_mode": {
                    "VIGIL-2026-FM-0001": "verified",
                },
            },
        })
        self.assertTrue(any("exactly one result" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
