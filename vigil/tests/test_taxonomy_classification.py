import importlib.util
import json
import subprocess
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
SCRIPT = VIGIL / "scripts" / "validate-vigil-records.py"
SPEC = importlib.util.spec_from_file_location("validate_incident_taxonomy", SCRIPT)
VALIDATOR = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(VALIDATOR)


class IncidentTaxonomyClassificationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.incidents = [
            json.loads(path.read_text(encoding="utf-8"))
            for path in sorted((VIGIL / "records" / "incidents").glob("VIGIL-INC-*.json"))
        ]

    def test_every_incident_has_an_explicit_classification_outcome(self):
        allowed = set(VALIDATOR.incident_contract()["classification_status_values"])
        self.assertTrue(self.incidents)
        self.assertTrue(all(item["taxonomy_classification"]["classification_status"] in allowed for item in self.incidents))

    def test_all_asserted_classes_resolve_to_selectable_taxonomy_classes(self):
        _, classes = VALIDATOR.taxonomy_catalogue()
        retired = VALIDATOR.retired_taxonomy_class_successors()
        for record in self.incidents:
            block = record["taxonomy_classification"]
            mappings = [block.get("primary_classification"), *block.get("secondary_classifications", [])]
            for mapping in (item for item in mappings if isinstance(item, dict)):
                self.assertIn(mapping["class_id"], classes, record["id"])
                self.assertNotIn(mapping["class_id"], retired, record["id"])
                self.assertEqual(classes[mapping["class_id"]]["family_id"], mapping["family_id"], record["id"])

    def test_unclassified_records_assert_no_mapping(self):
        for record in self.incidents:
            block = record["taxonomy_classification"]
            if block["classification_status"] in {"unclassified", "requires-human-review"}:
                self.assertIsNone(block["primary_classification"], record["id"])
                self.assertEqual(block["secondary_classifications"], [], record["id"])

    def test_successful_invariant_is_classified_but_not_failure_evidence(self):
        record = next(item for item in self.incidents if item["id"] == "VIGIL-INC-000126")
        block = record["taxonomy_classification"]
        self.assertEqual(block["classification_status"], "classified")
        self.assertEqual(block["classification_role"], "successful-invariant")
        self.assertEqual(block["primary_classification"]["class_id"], "VIGIL-FC-000073")
        self.assertEqual(block["primary_classification"]["classification_role"], "successful-invariant")
        self.assertEqual(block["secondary_classifications"], [])

    def test_inc129_preserves_ambiguous_boundary_mappings(self):
        record = next(item for item in self.incidents if item["id"] == "VIGIL-INC-000129")
        block = record["taxonomy_classification"]
        mappings = {
            item["class_id"]: item["classification_role"]
            for item in [block["primary_classification"], *block["secondary_classifications"]]
        }
        self.assertEqual(mappings["VIGIL-FC-000075"], "failure-occurrence")
        self.assertEqual(mappings["VIGIL-FC-000074"], "successful-invariant")
        self.assertEqual(mappings["VIGIL-FC-000001"], "successful-invariant")
        self.assertEqual(mappings["VIGIL-FC-000005"], "successful-invariant")
        self.assertEqual(mappings["VIGIL-FC-000076"], "ambiguous-boundary")
        self.assertEqual(mappings["VIGIL-FC-000077"], "ambiguous-boundary")

    def test_generated_examples_preserve_primary_secondary_roles(self):
        subprocess.run(["python", str(VIGIL / "scripts" / "build-vigil-public-records.py")], cwd=ROOT, check=True)
        projection = json.loads(
            (VIGIL / "taxonomy" / "generated" / "VIGIL.FailureTaxonomy.CaseFileExamples.json").read_text(encoding="utf-8")
        )
        primary = next(item for item in projection["classes"]["VIGIL-FC-000069"] if item["incident_id"] == "VIGIL-INC-000003")
        capability_secondary = next(item for item in projection["classes"]["VIGIL-FC-000002"] if item["incident_id"] == "VIGIL-INC-000003")
        authority_secondary = next(item for item in projection["classes"]["VIGIL-FC-000009"] if item["incident_id"] == "VIGIL-INC-000003")
        self.assertEqual(primary["mapping_position"], "primary")
        self.assertEqual(capability_secondary["mapping_position"], "secondary")
        self.assertEqual(authority_secondary["mapping_position"], "secondary")
        self.assertEqual(primary["classification_role"], "failure-occurrence")
        self.assertEqual(capability_secondary["classification_role"], "failure-occurrence")
        self.assertEqual(authority_secondary["classification_role"], "failure-occurrence")

    def test_reverse_mapping_matches_canonical_classified_incidents(self):
        projection = json.loads(
            (VIGIL / "taxonomy" / "generated" / "VIGIL.FailureTaxonomy.CaseFileExamples.json").read_text(encoding="utf-8")
        )
        projected = {
            item["incident_id"]
            for rows in projection["classes"].values()
            for item in rows if item["mapping_position"] == "primary"
        }
        canonical = {
            record["id"] for record in self.incidents
            if isinstance(record["taxonomy_classification"].get("primary_classification"), dict)
            and record["taxonomy_classification"]["primary_classification"].get("classification_role") == "failure-occurrence"
        }
        self.assertEqual(projected, canonical)

    def test_primary_secondary_position_and_failure_exemplar_role_are_independent(self):
        families = {"VIGIL-FF-TEST": {"family_id": "VIGIL-FF-TEST"}}

        def mapping(class_id, role):
            return {
                "family_id": "VIGIL-FF-TEST",
                "class_id": class_id,
                "classification_role": role,
                "classification_basis": "Bounded test basis.",
                "classification_confidence": "high",
            }

        structures = {
            "A": (mapping("VIGIL-FC-A", "failure-occurrence"), []),
            "B": (mapping("VIGIL-FC-A", "failure-occurrence"), [mapping("VIGIL-FC-B", "failure-occurrence")]),
            "C": (mapping("VIGIL-FC-A", "successful-invariant"), []),
            "D": (mapping("VIGIL-FC-A", "failure-occurrence"), [mapping("VIGIL-FC-B", "successful-invariant")]),
            "E": (mapping("VIGIL-FC-A", "successful-invariant"), [mapping("VIGIL-FC-B", "failure-occurrence")]),
        }

        for label, (primary, secondary) in structures.items():
            record_id = f"VIGIL-INC-TEST-{label}"
            classes = {
                class_id: {
                    "family_id": "VIGIL-FF-TEST",
                    "invariant_exemplars": [{
                        "linked_incident_id": record_id,
                        "exemplar_type": "successful-invariant",
                        "exemplar_status": "admitted",
                    }],
                }
                for class_id in {"VIGIL-FC-A", "VIGIL-FC-B"}
            }
            block = {
                "taxonomy_version": "test",
                "classification_status": "classified",
                "classification_basis": "Test structure.",
                "primary_classification": primary,
                "secondary_classifications": secondary,
                "classification_review_provenance": {},
            }
            record = {"id": record_id, "taxonomy_classification": block}
            errors = []
            with patch.object(VALIDATOR, "taxonomy_catalogue", return_value=(families, classes)):
                patcher = patch.object(VALIDATOR, "retired_taxonomy_class_successors", return_value={})
                with patcher:
                    VALIDATOR.validate_incident_taxonomy(Path(f"{label}.json"), record, errors)
            self.assertEqual(errors, [], label)

        contradictory = {
            "id": "VIGIL-INC-TEST-CONTRADICTORY",
            "taxonomy_classification": {
                "taxonomy_version": "test",
                "classification_status": "classified",
                "classification_role": "successful-invariant",
                "classification_basis": "Test structure.",
                "primary_classification": mapping("VIGIL-FC-A", "failure-occurrence"),
                "secondary_classifications": [],
                "classification_review_provenance": {},
            },
        }
        errors = []
        classes = {"VIGIL-FC-A": {"family_id": "VIGIL-FF-TEST", "invariant_exemplars": []}}
        with patch.object(VALIDATOR, "taxonomy_catalogue", return_value=(families, classes)):
            with patch.object(VALIDATOR, "retired_taxonomy_class_successors", return_value={}):
                VALIDATOR.validate_incident_taxonomy(Path("contradictory.json"), contradictory, errors)
        self.assertTrue(any("legacy block-level" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
