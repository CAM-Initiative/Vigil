"""Release-mode regression tests for taxonomy working-branch/publication semantics."""

from __future__ import annotations

import importlib.util
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

SOURCE_ROOT = Path(__file__).resolve().parents[1] / "taxonomy"

VALIDATOR_SPEC = importlib.util.spec_from_file_location("validate_taxonomy", SOURCE_ROOT / "validate_taxonomy.py")
VALIDATOR = importlib.util.module_from_spec(VALIDATOR_SPEC)
assert VALIDATOR_SPEC and VALIDATOR_SPEC.loader
VALIDATOR_SPEC.loader.exec_module(VALIDATOR)
sys.modules["validate_taxonomy"] = VALIDATOR

PREP_SPEC = importlib.util.spec_from_file_location("taxonomy_release_preparer", SOURCE_ROOT / "prepare_taxonomy_release.py")
PREP = importlib.util.module_from_spec(PREP_SPEC)
assert PREP_SPEC and PREP_SPEC.loader
PREP_SPEC.loader.exec_module(PREP)


class TaxonomyReleaseModeTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name) / "taxonomy"
        shutil.copytree(SOURCE_ROOT, self.root)

        self.validator_originals = (
            VALIDATOR.ROOT,
            VALIDATOR.SCHEMA_PATH,
            VALIDATOR.INDEX_PATH,
            VALIDATOR.FAMILIES_DIR,
            VALIDATOR.MIGRATION_LEDGER,
        )
        VALIDATOR.ROOT = self.root
        VALIDATOR.SCHEMA_PATH = self.root / "VIGIL.FailureTaxonomy.Schema.json"
        VALIDATOR.INDEX_PATH = self.root / "VIGIL.FailureTaxonomy.Index.json"
        VALIDATOR.FAMILIES_DIR = self.root / "families"
        VALIDATOR.MIGRATION_LEDGER = self.root / "migration" / "Caelestis.LegacyFailure.MigrationLedger.json"

        self.prep_originals = (PREP.ROOT, PREP.INDEX_PATH, PREP.FAMILIES_DIR, PREP.validator)
        PREP.ROOT = self.root
        PREP.INDEX_PATH = self.root / "VIGIL.FailureTaxonomy.Index.json"
        PREP.FAMILIES_DIR = self.root / "families"
        PREP.validator = VALIDATOR

    def tearDown(self):
        (
            VALIDATOR.ROOT,
            VALIDATOR.SCHEMA_PATH,
            VALIDATOR.INDEX_PATH,
            VALIDATOR.FAMILIES_DIR,
            VALIDATOR.MIGRATION_LEDGER,
        ) = self.validator_originals
        PREP.ROOT, PREP.INDEX_PATH, PREP.FAMILIES_DIR, PREP.validator = self.prep_originals
        self.tempdir.cleanup()

    def paths(self):
        return sorted(VALIDATOR.FAMILIES_DIR.glob("*.json"))

    def mutate_family_content(self):
        path = self.paths()[0]
        data = json.loads(path.read_text(encoding="utf-8"))
        data["family"]["plain_english"] += " Working-branch release-mode test amendment."
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    def test_working_mode_allows_unreleased_taxonomy_content(self):
        self.mutate_family_content()
        errors, _ = VALIDATOR.validate_catalogue(self.paths(), enforce_current_release=False)
        self.assertFalse(any("published dataset release" in error for error in errors))
        strict_errors, _ = VALIDATOR.validate_catalogue(self.paths(), enforce_current_release=True)
        self.assertTrue(any("published dataset release" in error for error in strict_errors))

    def test_main_release_preparation_bumps_once_for_whole_tranche(self):
        index_before = json.loads(PREP.INDEX_PATH.read_text(encoding="utf-8"))
        previous = index_before["release_history"][-1]["version"]
        parsed = VALIDATOR.parse_version(previous)
        self.assertIsNotNone(parsed)
        major, minor, patch, draft = parsed
        expected = f"{major}.{minor}.{patch + 1}{'-draft' if draft else ''}"

        self.mutate_family_content()
        self.assertTrue(PREP.prepare_release("2026-08-31"))
        index_after = json.loads(PREP.INDEX_PATH.read_text(encoding="utf-8"))
        self.assertEqual(index_after["standard"]["version"], expected)
        self.assertEqual(len(index_after["release_history"]), len(index_before["release_history"]) + 1)

        self.assertFalse(PREP.prepare_release("2026-08-31"))
        index_second = json.loads(PREP.INDEX_PATH.read_text(encoding="utf-8"))
        self.assertEqual(index_second["standard"]["version"], expected)
        self.assertEqual(len(index_second["release_history"]), len(index_after["release_history"]))

        errors, _ = VALIDATOR.validate_catalogue(self.paths(), enforce_current_release=True)
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
