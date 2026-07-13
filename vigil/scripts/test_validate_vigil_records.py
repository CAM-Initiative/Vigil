#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("validate-vigil-records.py")
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


if __name__ == "__main__":
    unittest.main()
