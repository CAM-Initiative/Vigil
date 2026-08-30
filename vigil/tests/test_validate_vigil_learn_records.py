#!/usr/bin/env python3
"""Regression checks for withdrawn VIGIL record-class publication boundaries."""

from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
RECORDS = VIGIL / "records"
DRAFTS = VIGIL / "drafts"
TEMPLATES = VIGIL / "templates"


class WithdrawnRecordBoundaryTests(unittest.TestCase):
    def test_withdrawn_record_classes_are_not_public(self) -> None:
        for folder in ("proposals", "patches", "learn"):
            with self.subTest(folder=folder):
                self.assertFalse((RECORDS / folder).exists())
                self.assertTrue((DRAFTS / folder).exists())

    def test_withdrawn_class_indexes_are_absent(self) -> None:
        for filename in (
            "VIGIL.Proposals.Index.json",
            "VIGIL.PatchNotes.Index.json",
            "VIGIL.Learn.Index.json",
        ):
            with self.subTest(filename=filename):
                self.assertFalse((VIGIL / filename).exists())

    def test_withdrawn_class_templates_are_absent(self) -> None:
        for filename in (
            "learn-record-template.json",
            "patch-note-record-template.json",
            "patch-note-record-template.md",
            "proposal-record-tempate.json",
            "proposal-record-tempate.md",
            "proposal-record-template.md",
        ):
            with self.subTest(filename=filename):
                self.assertFalse((TEMPLATES / filename).exists())

    def test_withdrawn_learn_schema_is_not_a_live_root_contract(self) -> None:
        self.assertFalse((VIGIL / "VIGIL.Learn.Schema.json").exists())

    def test_parallel_legacy_record_schema_tree_is_absent(self) -> None:
        self.assertFalse((VIGIL / "schemas").exists())


if __name__ == "__main__":
    unittest.main()
