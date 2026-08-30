#!/usr/bin/env python3
"""Focused regression tests for the INCIDENT-01 pilot architecture."""

from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
VALIDATOR = VIGIL / "scripts" / "validate-vigil-records.py"
spec = importlib.util.spec_from_file_location("validate_vigil_records", VALIDATOR)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


class IncidentRegistryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.incidents = {
            path.stem: load(path)
            for path in sorted((VIGIL / "records" / "incidents").glob("*.json"))
        }
        cls.crosswalk = load(
            VIGIL / "migrations" / "incident-registry" / "VIGIL.FM-OBS-to-INC.Crosswalk.json"
        )
        cls.by_legacy = {entry["legacy_id"]: entry for entry in cls.crosswalk["entries"]}

    def test_incident_ids_are_year_independent_and_unique(self):
        self.assertEqual(len(self.incidents), 8)
        self.assertTrue(all(identifier.startswith("VIGIL-INC-") for identifier in self.incidents))

    def test_unclassified_incident_has_no_asserted_mapping(self):
        block = self.incidents["VIGIL-INC-000002"]["taxonomy_classification"]
        self.assertEqual(block["classification_status"], "unclassified")
        self.assertIsNone(block["primary_classification"])
        self.assertEqual(block["secondary_classifications"], [])

    def test_split_and_non_incident_dispositions_are_explicit(self):
        self.assertEqual(len(self.by_legacy["VIGIL-2026-FM-0038"]["successor_incidents"]), 4)
        self.assertEqual(
            self.by_legacy["VIGIL-2026-OBS-0011"]["migration_status"],
            "non-incident-not-migrated",
        )
        self.assertEqual(self.by_legacy["VIGIL-2026-OBS-0011"]["successor_incidents"], [])

    def test_incident_validator_rejects_secondary_without_primary(self):
        record = json.loads(json.dumps(self.incidents["VIGIL-INC-000002"]))
        record["taxonomy_classification"]["secondary_classifications"] = [
            {
                "family_id": "VIGIL-FF-0001",
                "class_id": "VIGIL-FC-000002",
                "classification_basis": "test",
                "classification_confidence": "low",
            }
        ]
        errors: list[str] = []
        validator.validate_incident(Path(record["id"] + ".json"), record, errors)
        self.assertTrue(any("secondary classifications require a primary" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
