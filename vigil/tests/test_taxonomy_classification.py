#!/usr/bin/env python3
"""Regression tests for VIGIL-native Failure Mode taxonomy classification."""

from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
VALIDATOR_PATH = VIGIL / "scripts" / "validate-vigil-records.py"
spec = importlib.util.spec_from_file_location("validate_vigil_records_taxonomy", VALIDATOR_PATH)
validator = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(validator)


class TaxonomyClassificationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = []
        for path in sorted((VIGIL / "records" / "failures" / "2026").glob("*.json")):
            cls.records.append(json.loads(path.read_text(encoding="utf-8")))
        cls.failures_index = json.loads((VIGIL / "VIGIL.Failures.Index.json").read_text(encoding="utf-8"))
        cls.registry_index = json.loads((VIGIL / "VIGIL.Registry.Index.json").read_text(encoding="utf-8"))

    def test_every_canonical_failure_has_explicit_outcome(self):
        self.assertEqual(len(self.records), 71)
        allowed = {"classified", "family-only", "candidate-new-class", "unmapped", "deferred"}
        self.assertTrue(all(r["taxonomy_classification"]["classification_status"] in allowed for r in self.records))

    def test_classified_ids_and_labels_resolve_canonically(self):
        families, classes = validator.taxonomy_catalogue()
        for record in self.records:
            block = record["taxonomy_classification"]
            errors = []
            validator.validate_taxonomy_classification(Path(record["id"]), record, errors)
            self.assertEqual(errors, [], record["id"])
            if block["classification_status"] == "classified":
                family = block["primary_family"]
                klass = block["primary_class"]
                self.assertEqual(classes[klass["class_id"]]["family_id"], family["family_id"])
                self.assertEqual(families[family["family_id"]]["name"], family["family_name"])

    def test_non_exact_outcomes_do_not_invent_class_ids(self):
        for record in self.records:
            block = record["taxonomy_classification"]
            if block["classification_status"] != "classified":
                self.assertNotIn("primary_class", block, record["id"])
        for record in self.records:
            candidate = record["taxonomy_classification"].get("candidate_class")
            if candidate:
                self.assertNotIn("class_id", candidate)

    def test_native_unwarranted_activation_evidence_is_reconciled(self):
        expected = {
            "VIGIL-2026-FM-0019": "high",
            "VIGIL-2026-FM-0020": "medium",
            "VIGIL-2026-FM-0048": "high",
        }
        for record_id, confidence in expected.items():
            record = next(r for r in self.records if r["id"] == record_id)
            block = record["taxonomy_classification"]
            self.assertEqual(block["classification_status"], "classified")
            self.assertEqual(block["primary_family"]["family_id"], "VIGIL-FF-0008")
            self.assertEqual(block["primary_class"]["class_id"], "VIGIL-FC-000043")
            self.assertEqual(block["primary_class"]["abstraction"], "class")
            self.assertEqual(block["classification_confidence"], confidence)
            self.assertNotIn("candidate_class", block)

    def test_classification_ledger_class_ids_resolve(self):
        _, classes = validator.taxonomy_catalogue()
        ledger = json.loads((VIGIL / "taxonomy" / "migration" / "VIGIL.FailureMode.TaxonomyClassificationLedger.json").read_text(encoding="utf-8"))
        for entry in ledger["entries"]:
            if entry["class_id"]:
                self.assertIn(entry["class_id"], classes, entry["failure_mode_id"])

    def test_positive_control_fm_0068(self):
        record = next(r for r in self.records if r["id"] == "VIGIL-2026-FM-0068")
        block = record["taxonomy_classification"]
        self.assertEqual(block["primary_family"]["family_id"], "VIGIL-FF-0001")
        self.assertEqual(block["primary_class"]["class_id"], "VIGIL-FC-000005")

    def test_retired_taxonomy_fields_remain_rejected_and_absent(self):
        retired = validator.RETIRED_FM_TAXONOMY_FIELDS
        for record in self.records:
            self.assertFalse(retired.intersection(record["failure_classification"]), record["id"])
            self.assertNotIn("related_failure_modes", record["linked_records"])

    def test_invalid_family_class_pair_is_rejected(self):
        record = copy.deepcopy(next(r for r in self.records if r["id"] == "VIGIL-2026-FM-0068"))
        record["taxonomy_classification"]["primary_family"] = {
            "family_id": "VIGIL-FF-0002", "family_code": "PROVENANCE_LINEAGE",
            "family_name": "Provenance & Lineage Integrity Failures",
        }
        errors = []
        validator.validate_taxonomy_classification(Path("test.json"), record, errors)
        self.assertTrue(any("does not belong" in error for error in errors), errors)

    def test_generated_summaries_match_canonical_records(self):
        canonical = {r["id"]: r["taxonomy_classification"] for r in self.records}
        for index in (self.failures_index, self.registry_index):
            for entry in index["records"]:
                if entry.get("record_type") != "failure_mode":
                    continue
                block = canonical[entry["id"]]
                family = block.get("primary_family", {})
                klass = block.get("primary_class", {})
                expected = {
                    "taxonomy_version": block["taxonomy_version"],
                    "classification_status": block["classification_status"],
                    "family_id": family.get("family_id", ""), "family_name": family.get("family_name", ""),
                    "class_id": klass.get("class_id", ""), "class_name": klass.get("class_name", ""),
                    "abstraction": klass.get("abstraction", ""),
                }
                self.assertEqual(entry["taxonomy_classification_summary"], {k: v for k, v in expected.items() if v})

    def test_reverse_mapping_contains_only_canonical_classifications(self):
        projection = json.loads((VIGIL / "taxonomy" / "generated" / "VIGIL.FailureTaxonomy.CaseFileExamples.json").read_text(encoding="utf-8"))
        projected = {item["failure_mode_id"] for rows in projection["classes"].values() for item in rows}
        exact = {r["id"] for r in self.records if r["taxonomy_classification"]["classification_status"] == "classified"}
        self.assertEqual(projected, exact)


if __name__ == "__main__":
    unittest.main()
