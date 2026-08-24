"""Regression tests for the portable VIGIL Failure Taxonomy contract."""

from __future__ import annotations

import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

SOURCE_ROOT = Path(__file__).resolve().parents[1] / "taxonomy"
SPEC = importlib.util.spec_from_file_location("failure_taxonomy_validator", SOURCE_ROOT / "validate_taxonomy.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)


class FailureTaxonomyValidationTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name) / "taxonomy"
        shutil.copytree(SOURCE_ROOT, self.root)
        self.originals = (MODULE.ROOT, MODULE.SCHEMA_PATH, MODULE.INDEX_PATH, MODULE.FAMILIES_DIR, MODULE.MIGRATION_LEDGER)
        MODULE.ROOT = self.root
        MODULE.SCHEMA_PATH = self.root / "VIGIL.FailureTaxonomy.Schema.json"
        MODULE.INDEX_PATH = self.root / "VIGIL.FailureTaxonomy.Index.json"
        MODULE.FAMILIES_DIR = self.root / "families"
        MODULE.MIGRATION_LEDGER = self.root / "migration" / "Caelestis.LegacyFailure.MigrationLedger.json"

    def tearDown(self):
        MODULE.ROOT, MODULE.SCHEMA_PATH, MODULE.INDEX_PATH, MODULE.FAMILIES_DIR, MODULE.MIGRATION_LEDGER = self.originals
        self.tempdir.cleanup()

    def paths(self):
        return sorted(MODULE.FAMILIES_DIR.glob("*.json"))

    def document(self, number=0):
        path = self.paths()[number]
        return path, json.loads(path.read_text(encoding="utf-8"))

    def write(self, path, value):
        path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")

    def errors(self):
        return MODULE.validate_catalogue(self.paths())[0]

    def test_current_catalogue_validates(self):
        self.assertEqual(self.errors(), [])

    def test_duplicate_immutable_class_id_is_rejected(self):
        path, data = self.document()
        duplicate = data["classes"][0]["class_id"]
        data["classes"][1]["class_id"] = duplicate
        data["family"]["allowed_class_ids"][1] = duplicate
        self.write(path, data)
        self.assertTrue(any("duplicate class ID" in error or "must be unique" in error for error in self.errors()))

    def test_broken_relationship_target_is_rejected(self):
        path, data = self.document()
        data["classes"][0].setdefault("relationships", []).append(
            {"type": "distinguish_from", "target_id": "VIGIL-FC-999999"}
        )
        self.write(path, data)
        self.assertTrue(any("references missing class" in error for error in self.errors()))

    def test_variant_parent_must_be_one_in_family_class(self):
        path, data = self.document()
        variant = next(item for item in data["classes"] if item["abstraction"] == "variant")
        variant["relationships"] = [
            {"type": "child_of", "target_id": "VIGIL-FC-000010"}
        ]
        self.write(path, data)
        self.assertTrue(any("cannot have a parent in another family" in error for error in self.errors()))

    def test_index_count_drift_is_rejected(self):
        index = json.loads(MODULE.INDEX_PATH.read_text(encoding="utf-8"))
        index["families"][0]["class_count"] += 1
        self.write(MODULE.INDEX_PATH, index)
        self.assertTrue(any("class_count" in error for error in self.errors()))

    def test_missing_plain_english_definition_fails_schema(self):
        path, data = self.document()
        del data["classes"][0]["plain_english"]
        self.write(path, data)
        self.assertTrue(any("missing required property 'plain_english'" in error for error in self.errors()))

    def test_removed_id_cannot_be_referenced(self):
        index = json.loads(MODULE.INDEX_PATH.read_text(encoding="utf-8"))
        index["removed_ids"] = ["VIGIL-FC-999999"]
        self.write(MODULE.INDEX_PATH, index)
        path, data = self.document()
        data["classes"][0].setdefault("relationships", []).append(
            {"type": "distinguish_from", "target_id": "VIGIL-FC-999999"}
        )
        self.write(path, data)
        self.assertTrue(any("references removed ID" in error for error in self.errors()))

    def test_family_cannot_be_superseded_by_class(self):
        path, data = self.document()
        data["family"]["status"] = "deprecated"
        data["family"]["supersession"] = {
            "deprecated_on": "2026-08-24",
            "superseded_by_id": data["classes"][0]["class_id"],
            "reason": "Invalid cross-kind test fixture."
        }
        self.write(path, data)
        index = json.loads(MODULE.INDEX_PATH.read_text(encoding="utf-8"))
        index["families"][0]["status"] = "deprecated"
        self.write(MODULE.INDEX_PATH, index)
        self.assertTrue(any("must be the same taxonomy kind" in error for error in self.errors()))

    def test_class_cannot_be_superseded_by_family(self):
        path, data = self.document()
        item = data["classes"][0]
        item["status"] = "deprecated"
        item["supersession"] = {
            "deprecated_on": "2026-08-24",
            "superseded_by_id": data["family"]["family_id"],
            "reason": "Invalid cross-kind test fixture."
        }
        self.write(path, data)
        self.assertTrue(any("must be the same taxonomy kind" in error for error in self.errors()))

    def test_split_migration_entry_requires_split_notes(self):
        ledger = json.loads(MODULE.MIGRATION_LEDGER.read_text(encoding="utf-8"))
        entry = next(item for item in ledger["entries"] if item["disposition"] == "SPLIT_REQUIRED")
        entry["split_notes"] = []
        self.write(MODULE.MIGRATION_LEDGER, ledger)
        self.assertTrue(any("SPLIT_REQUIRED requires split_notes" in error for error in self.errors()))


if __name__ == "__main__":
    unittest.main()
