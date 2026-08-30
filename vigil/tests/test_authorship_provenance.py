#!/usr/bin/env python3
"""Regression tests for VIGIL authorship and human-review provenance."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "scripts"))
SCRIPT = ROOT / "scripts" / "validate-authorship-provenance.py"
SPEC = importlib.util.spec_from_file_location("authorship_provenance", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)


class AuthorshipProvenanceTests(unittest.TestCase):
    def test_repository_provenance_is_valid(self) -> None:
        self.assertEqual(MODULE.validate_repository(), [])

    def test_contract_approval_cannot_inflate_human_involvement(self) -> None:
        for field, value, expected in (
            ("human_authorship", True, "cannot assert human authorship"),
            ("human_review_status", "spot-checked", "cannot assert human review"),
            ("human_verification_status", "sample-verified", "cannot assert human verification"),
        ):
            with self.subTest(field=field):
                provenance = dict(MODULE.DEFAULT)
                provenance[field] = value
                errors = MODULE.validate_provenance(provenance, "test")
                self.assertTrue(any(expected in error for error in errors), errors)

    def test_publication_does_not_upgrade_review(self) -> None:
        rules = MODULE.INHERITANCE_RULES
        self.assertFalse(rules["repository_publication_means_human_review"])
        self.assertFalse(rules["repository_acceptance_means_human_review"])
        self.assertFalse(rules["repository_acceptance_means_human_verification"])

    def test_generated_artefact_requires_upstream_provenance(self) -> None:
        errors = MODULE.validate_provenance(
            dict(MODULE.GENERATED),
            "generated",
            require_upstream=True,
        )
        self.assertTrue(any("upstream_provenance" in error for error in errors), errors)

    def test_explicit_override_precedes_inherited_default(self) -> None:
        rules = MODULE.INHERITANCE_RULES
        self.assertTrue(rules["explicit_artefact_override_precedence"])
        self.assertTrue(rules["default_applies_when_override_absent"])
        self.assertFalse(rules["absence_of_override_means_human_review"])
        self.assertEqual(rules["explicit_artefact_override_field"], "authorship_provenance")
        self.assertFalse(rules["legacy_interpretive_provenance_is_authorship_override"])


if __name__ == "__main__":
    unittest.main()
