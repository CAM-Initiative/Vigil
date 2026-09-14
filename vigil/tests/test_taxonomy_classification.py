import importlib.util
import json
import subprocess
import unittest
from pathlib import Path

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

    def test_generated_examples_preserve_primary_secondary_roles(self):
        subprocess.run(["python", str(VIGIL / "scripts" / "build-vigil-public-records.py")], cwd=ROOT, check=True)
        projection = json.loads(
            (VIGIL / "taxonomy" / "generated" / "VIGIL.FailureTaxonomy.CaseFileExamples.json").read_text(encoding="utf-8")
        )
        primary = next(item for item in projection["classes"]["VIGIL-FC-000069"] if item["incident_id"] == "VIGIL-INC-000003")
        capability_secondary = next(item for item in projection["classes"]["VIGIL-FC-000002"] if item["incident_id"] == "VIGIL-INC-000003")
        authority_secondary = next(item for item in projection["classes"]["VIGIL-FC-000009"] if item["incident_id"] == "VIGIL-INC-000003")
        self.assertEqual(primary["classification_role"], "primary")
        self.assertEqual(capability_secondary["classification_role"], "secondary")
        self.assertEqual(authority_secondary["classification_role"], "secondary")

    def test_reverse_mapping_matches_canonical_classified_incidents(self):
        projection = json.loads(
            (VIGIL / "taxonomy" / "generated" / "VIGIL.FailureTaxonomy.CaseFileExamples.json").read_text(encoding="utf-8")
        )
        projected = {
            item["incident_id"]
            for rows in projection["classes"].values()
            for item in rows if item["classification_role"] == "primary"
        }
        canonical = {
            record["id"] for record in self.incidents
            if record["taxonomy_classification"]["classification_status"] in {
                "classified", "provisionally-classified", "classification-disputed"
            }
            and isinstance(record["taxonomy_classification"].get("primary_classification"), dict)
        }
        self.assertEqual(projected, canonical)

    def test_exemplar_is_mapped_but_not_projected_as_failure_evidence(self):
        exemplar = next(record for record in self.incidents if record["id"] == "VIGIL-INC-000126")
        block = exemplar["taxonomy_classification"]
        self.assertEqual(block["classification_status"], "exemplar")
        self.assertEqual(block["primary_classification"]["class_id"], "VIGIL-FC-000073")
        projection = json.loads(
            (VIGIL / "taxonomy" / "generated" / "VIGIL.FailureTaxonomy.CaseFileExamples.json").read_text(encoding="utf-8")
        )
        self.assertFalse(any(
            item["incident_id"] == "VIGIL-INC-000126"
            for item in projection["classes"]["VIGIL-FC-000073"]
        ))


if __name__ == "__main__":
    unittest.main()
