"""Regression tests for the portable VIGIL Failure Taxonomy contract."""

from __future__ import annotations

import copy
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
        return MODULE.validate_catalogue(self.paths(), enforce_current_release=False)[0]

    def published_errors(self):
        return MODULE.validate_catalogue(self.paths(), enforce_current_release=True)[0]

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

    def test_subtype_historical_id_must_map_to_containing_class(self):
        path, data = self.document()
        parent = next(item for item in data["classes"] if item.get("subtypes"))
        parent["subtypes"][0]["historical_class_id"] = "VIGIL-FC-000007"
        self.write(path, data)
        self.assertTrue(any("retirement successor must be containing class" in error for error in self.errors()))

    def test_reclassified_immutable_ids_are_preserved_in_activation_family(self):
        documents = [json.loads(path.read_text(encoding="utf-8")) for path in self.paths()]
        activation = next(item for item in documents if item["family"]["family_id"] == "VIGIL-FF-0008")
        self.assertEqual(
            [item["class_id"] for item in activation["classes"]],
            ["VIGIL-FC-000037", "VIGIL-FC-000038", "VIGIL-FC-000043"],
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

    def test_retired_control_suppression_is_preserved_as_non_selectable_subtype(self):
        path = next(path for path in self.paths() if "VIGIL-FF-0008" in path.name)
        data = json.loads(path.read_text(encoding="utf-8"))
        parent = next(item for item in data["classes"] if item["class_id"] == "VIGIL-FC-000038")
        subtype = next(item for item in parent["subtypes"] if item["historical_class_id"] == "VIGIL-FC-000039")
        self.assertEqual(subtype["name"], "Control Authority Suppression")
        self.assertNotIn("VIGIL-FC-000039", data["family"]["allowed_class_ids"])
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

    def test_family_prose_semantic_roles_are_explicit(self):
        schema = json.loads(MODULE.SCHEMA_PATH.read_text(encoding="utf-8"))
        properties = schema["$defs"]["family"]["properties"]
        self.assertIn("failure condition", properties["plain_english"]["description"])
        self.assertIn("bounded failure set", properties["definition"]["description"])
        self.assertIn("Positive bounded structural property", properties["invariant"]["description"])
        guidance = (self.root / "README.md").read_text(encoding="utf-8")
        self.assertIn("### Semantic roles of family prose", guidance)
        self.assertIn("Parent prose must be re-tested whenever a class is added", guidance)

    def test_observability_parent_encompasses_authorised_evidence_access(self):
        documents = [json.loads(path.read_text(encoding="utf-8")) for path in self.paths()]
        family = next(item["family"] for item in documents if item["family"]["family_id"] == "VIGIL-FF-0004")
        parent_prose = " ".join(
            family[field] for field in ("plain_english", "definition", "invariant", "inclusion_rule", "exclusion_rule")
        ).lower()
        for boundary in ("authorised", "accessible", "evidence-production", "access pathway"):
            self.assertIn(boundary, parent_prose)
        self.assertIn("does not create or enlarge investigative authority", parent_prose)

    def test_access_session_parent_encompasses_verification_dependency(self):
        documents = [json.loads(path.read_text(encoding="utf-8")) for path in self.paths()]
        access = next(item for item in documents if item["family"]["family_id"] == "VIGIL-FF-0005")
        self.assertEqual(
            [item["class_id"] for item in access["classes"]],
            ["VIGIL-FC-000031", "VIGIL-FC-000032", "VIGIL-FC-000048"],
        )
        parent_prose = " ".join(
            access["family"][field]
            for field in ("plain_english", "definition", "invariant", "inclusion_rule", "exclusion_rule")
        ).lower()
        for boundary in ("verification", "practically", "fallback", "valid or unresolved access"):
            self.assertIn(boundary, parent_prose)

    def test_governance_reach_parent_covers_route_bypass_and_operative_signal_reach(self):
        documents = [json.loads(path.read_text(encoding="utf-8")) for path in self.paths()]
        reach = next(item for item in documents if item["family"]["family_id"] == "VIGIL-FF-0007")
        family = reach["family"]
        self.assertIn("VIGIL-FC-000041", family["allowed_class_ids"])
        self.assertNotIn("only after", family["inclusion_rule"].lower())
        parent_prose = " ".join(
            family[field] for field in ("plain_english", "definition", "invariant", "inclusion_rule")
        ).lower()
        for boundary in ("bypasses", "required governance route", "operative control state", "reach"):
            self.assertIn(boundary, parent_prose)

    def test_control_activation_parent_describes_failure_conditions(self):
        documents = [json.loads(path.read_text(encoding="utf-8")) for path in self.paths()]
        activation = next(item for item in documents if item["family"]["family_id"] == "VIGIL-FF-0008")
        family = activation["family"]
        plain = family["plain_english"].lower()
        self.assertIn("fails to activate", plain)
        self.assertIn("activates without valid conditions", plain)
        definition = family["definition"].lower()
        for boundary in (
            "cannot be determined in time",
            "does not become operative",
            "becomes operative when its valid activation conditions are not satisfied",
            "authority required to activate",
        ):
            self.assertIn(boundary, definition)

    def test_working_branch_preserves_last_published_metadata_in_families(self):
        index = json.loads(MODULE.INDEX_PATH.read_text(encoding="utf-8"))
        self.assertEqual(index["standard"]["version"], "0.3.0-draft")
        self.assertEqual(index["standard"]["publication_date"], "2026-09-02")
        self.assertEqual(index["release_history"][-1]["change_level"], "minor")
        for path in self.paths():
            document = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(document["standard"]["version"], "0.3.0-draft")
            self.assertEqual(document["standard"]["publication_date"], "2026-09-02")

    def test_family_or_class_change_requires_new_dataset_release_metadata(self):
        path, data = self.document()
        data["family"]["plain_english"] += " Material amendment for release-linter testing."
        self.write(path, data)
        self.assertTrue(
            any(
                "changed without a new dataset version, date and release digest" in error
                for error in self.published_errors()
            )
        )

    def test_existing_record_change_requires_patch_not_minor_increment(self):
        index = json.loads(MODULE.INDEX_PATH.read_text(encoding="utf-8"))
        previous = index["release_history"][-1]
        release = copy.deepcopy(previous)
        release["version"] = "0.4.0-draft"
        release["change_level"] = "minor"
        release["content_digest"] = "sha256:" + "f" * 64
        index["release_history"].append(release)
        index["standard"]["version"] = "0.4.0-draft"
        self.write(MODULE.INDEX_PATH, index)
        for path in self.paths():
            document = json.loads(path.read_text(encoding="utf-8"))
            document["standard"]["version"] = "0.4.0-draft"
            self.write(path, document)
        self.assertTrue(any("must advance to 0.3.1" in error for error in self.published_errors()))

    def test_new_family_requires_minor_dataset_increment(self):
        index = json.loads(MODULE.INDEX_PATH.read_text(encoding="utf-8"))
        previous = index["release_history"][-1]
        release = copy.deepcopy(previous)
        release["version"] = "0.3.1-draft"
        release["change_level"] = "patch"
        release["content_digest"] = "sha256:" + "e" * 64
        release["family_ids"].append("VIGIL-FF-0011")
        index["release_history"].append(release)
        index["standard"]["version"] = "0.3.1-draft"
        self.write(MODULE.INDEX_PATH, index)
        self.assertTrue(any("must advance to 0.4.0" in error for error in self.published_errors()))

    def test_dataset_release_requires_fixed_edition_date(self):
        index = json.loads(MODULE.INDEX_PATH.read_text(encoding="utf-8"))
        del index["standard"]["publication_date"]
        self.write(MODULE.INDEX_PATH, index)
        self.assertTrue(any("standard.publication_date must be a valid" in error for error in self.errors()))

    def test_allocations_through_current_branch_head_are_sequential_and_bounded(self):
        documents = [json.loads(path.read_text(encoding="utf-8")) for path in self.paths()]
        classes = {item["class_id"]: item for document in documents for item in document["classes"]}
        self.assertEqual(
            [class_id for class_id in sorted(classes) if class_id >= "VIGIL-FC-000046"],
            [f"VIGIL-FC-{number:06d}" for number in range(46, 62)],
        )
        authority = next(document for document in documents if document["family"]["family_id"] == "VIGIL-FF-0001")
        self.assertEqual(classes["VIGIL-FC-000046"]["family_id"], authority["family"]["family_id"])
        self.assertEqual(classes["VIGIL-FC-000047"]["family_id"], "VIGIL-FF-0002")
        self.assertEqual(classes["VIGIL-FC-000048"]["family_id"], "VIGIL-FF-0005")
        self.assertEqual(classes["VIGIL-FC-000053"]["family_id"], authority["family"]["family_id"])

    def test_selectable_classes_and_non_selectable_subtypes_are_disjoint(self):
        index = json.loads(MODULE.INDEX_PATH.read_text(encoding="utf-8"))
        documents = [json.loads(path.read_text(encoding="utf-8")) for path in self.paths()]
        selectable = {item["class_id"] for document in documents for item in document["classes"]}
        self.assertEqual(len(selectable), 54)
        self.assertTrue(all(item["abstraction"] == "class" for document in documents for item in document["classes"]))
        subtypes = {
            subtype["historical_class_id"]: item["class_id"]
            for document in documents
            for item in document["classes"]
            for subtype in item.get("subtypes", [])
        }
        mappings = {row["retired_id"]: row["successor_id"] for row in index["retired_class_mappings"]}
        self.assertEqual(subtypes, mappings)
        self.assertEqual(set(index["removed_ids"]), set(mappings))
        self.assertTrue(selectable.isdisjoint(mappings))

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
