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

    def test_reclassified_immutable_ids_are_preserved_in_activation_family(self):
        documents = [json.loads(path.read_text(encoding="utf-8")) for path in self.paths()]
        activation = next(item for item in documents if item["family"]["family_id"] == "VIGIL-FF-0008")
        self.assertEqual(
            [item["class_id"] for item in activation["classes"]],
            ["VIGIL-FC-000037", "VIGIL-FC-000038", "VIGIL-FC-000039", "VIGIL-FC-000043"],
        )

    def test_unwarranted_activation_is_a_peer_class_with_bounded_exclusions(self):
        documents = [json.loads(path.read_text(encoding="utf-8")) for path in self.paths()]
        activation = next(item for item in documents if item["family"]["family_id"] == "VIGIL-FF-0008")
        unwarranted = next(item for item in activation["classes"] if item["class_id"] == "VIGIL-FC-000043")
        self.assertEqual(unwarranted["abstraction"], "class")
        self.assertEqual(len(unwarranted["recognition"]["required_conditions"]), 5)
        relationship = next(item for item in unwarranted["relationships"] if item["target_id"] == "VIGIL-FC-000038")
        self.assertEqual(relationship["type"], "distinguish_from")
        exclusions = " ".join(unwarranted["exclusions"]).lower()
        for boundary in ("classification", "scope", "stale", "authority", "reach"):
            self.assertIn(boundary, exclusions)

    def test_family_membership_alignment_is_mandatory_after_reclassification(self):
        path = next(path for path in self.paths() if "VIGIL-FF-0008" in path.name)
        data = json.loads(path.read_text(encoding="utf-8"))
        data["classes"][0]["family_id"] = "VIGIL-FF-0007"
        self.write(path, data)
        self.assertTrue(any("has family_id" in error and "expected" in error for error in self.errors()))

    def test_reclassified_variant_parent_remains_in_same_family(self):
        path = next(path for path in self.paths() if "VIGIL-FF-0008" in path.name)
        data = json.loads(path.read_text(encoding="utf-8"))
        variant = next(item for item in data["classes"] if item["class_id"] == "VIGIL-FC-000039")
        parent = next(rel for rel in variant["relationships"] if rel["type"] == "child_of")
        self.assertEqual(parent["target_id"], "VIGIL-FC-000038")
        self.assertEqual(self.errors(), [])

    def test_reclassification_relationships_resolve_across_family_boundary(self):
        self.assertEqual(self.errors(), [])
        documents = [json.loads(path.read_text(encoding="utf-8")) for path in self.paths()]
        class_ids = {item["class_id"] for document in documents for item in document["classes"]}
        activation = next(item for item in documents if item["family"]["family_id"] == "VIGIL-FF-0008")
        targets = {
            relationship["target_id"]
            for item in activation["classes"]
            for relationship in item.get("relationships", [])
        }
        self.assertTrue(targets <= class_ids)

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

    def test_evidence_accessibility_classes_are_distinct_peer_mechanisms(self):
        documents = [json.loads(path.read_text(encoding="utf-8")) for path in self.paths()]
        observability = next(item for item in documents if item["family"]["family_id"] == "VIGIL-FF-0004")
        classes = {item["class_id"]: item for item in observability["classes"]}
        primary = classes["VIGIL-FC-000044"]
        pathway = classes["VIGIL-FC-000045"]
        self.assertEqual(primary["abstraction"], "class")
        self.assertEqual(pathway["abstraction"], "class")
        self.assertTrue(any(r["type"] == "distinguish_from" and r["target_id"] == pathway["class_id"] for r in primary["relationships"]))
        self.assertTrue(any(r["type"] == "distinguish_from" and r["target_id"] == primary["class_id"] for r in pathway["relationships"]))
        primary_boundaries = " ".join(primary["exclusions"]).lower()
        self.assertIn("never captured", primary_boundaries)
        self.assertIn("reconstruct", primary_boundaries)
        pathway_boundaries = " ".join(pathway["exclusions"]).lower()
        self.assertIn("lacks valid authority", pathway_boundaries)
        self.assertIn("self-authorise", pathway_boundaries)

    def test_taxonomy_08_allocations_are_sequential_and_bounded(self):
        documents = [json.loads(path.read_text(encoding="utf-8")) for path in self.paths()]
        classes = {item["class_id"]: item for document in documents for item in document["classes"]}
        self.assertEqual(
            [class_id for class_id in sorted(classes) if class_id >= "VIGIL-FC-000046"],
            [f"VIGIL-FC-{number:06d}" for number in range(46, 54)],
        )
        authority = next(document for document in documents if document["family"]["family_id"] == "VIGIL-FF-0001")
        self.assertEqual(classes["VIGIL-FC-000046"]["family_id"], authority["family"]["family_id"])
        self.assertEqual(classes["VIGIL-FC-000047"]["family_id"], "VIGIL-FF-0002")
        self.assertEqual(classes["VIGIL-FC-000048"]["family_id"], "VIGIL-FF-0005")
        self.assertEqual(classes["VIGIL-FC-000053"]["family_id"], authority["family"]["family_id"])

    def test_identity_representation_authority_class_is_portable_and_bounded(self):
        documents = [json.loads(path.read_text(encoding="utf-8")) for path in self.paths()]
        classes = {item["class_id"]: item for document in documents for item in document["classes"]}
        identity = classes["VIGIL-FC-000053"]
        recognition = " ".join(identity["recognition"]["required_conditions"]).lower()
        self.assertIn("identifiable real person", recognition)
        self.assertIn("consent", recognition)
        self.assertIn("possession", recognition)
        self.assertNotIn("sexual", identity["definition"].lower())
        boundaries = " ".join(identity["exclusions"]).lower()
        self.assertIn("progressively resembles", boundaries)
        self.assertIn("valid consent", boundaries)
        neighbours = {item["target_id"] for item in identity["relationships"] if item["type"] == "distinguish_from"}
        self.assertEqual(neighbours, {"VIGIL-FC-000002", "VIGIL-FC-000003", "VIGIL-FC-000005"})

    def test_agency_preserving_influence_family_has_one_bounded_invariant(self):
        documents = [json.loads(path.read_text(encoding="utf-8")) for path in self.paths()]
        influence = next(document for document in documents if document["family"]["family_id"] == "VIGIL-FF-0009")
        self.assertEqual(len(influence["classes"]), 4)
        self.assertEqual(
            [item["class_id"] for item in influence["classes"]],
            ["VIGIL-FC-000049", "VIGIL-FC-000050", "VIGIL-FC-000051", "VIGIL-FC-000052"],
        )
        invariant = influence["family"]["invariant"].lower()
        for boundary in ("independent deliberation", "choice", "disengagement", "protected"):
            self.assertIn(boundary, invariant)
        exclusions = influence["family"]["exclusion_rule"].lower()
        for non_failure in ("warm", "personalised", "effective"):
            self.assertIn(non_failure, exclusions)


if __name__ == "__main__":
    unittest.main()
