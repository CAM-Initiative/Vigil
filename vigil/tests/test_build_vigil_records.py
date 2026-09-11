import importlib.util
import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
SCRIPT = VIGIL / "scripts" / "build-vigil-public-records.py"
SPEC = importlib.util.spec_from_file_location("build_vigil_public_records", SCRIPT)
BUILDER = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(BUILDER)


class IncidentBuilderTests(unittest.TestCase):
    def test_builder_loads_only_canonical_incidents(self):
        paths = sorted(BUILDER.INCIDENTS.glob("VIGIL-INC-*.json"))
        self.assertTrue(paths)
        self.assertTrue(all(BUILDER.load(path)["record_type"] == "incident" for path in paths))

    def test_incident_index_is_a_lightweight_catalogue_projection(self):
        record = BUILDER.load(BUILDER.INCIDENTS / "VIGIL-INC-000081.json")
        entry = BUILDER.incident_entry(BUILDER.INCIDENTS / "VIGIL-INC-000081.json", record)
        self.assertEqual(entry["severity"], record["severity_assessment"]["severity"])
        self.assertEqual(entry["classification_status"], record["taxonomy_classification"]["classification_status"])
        self.assertEqual(entry["record_version"], record["record_identity"]["version"])
        self.assertEqual(entry["record_last_updated"], record["record_identity"]["updated"])
        self.assertIn("search_terms", entry)
        self.assertTrue(entry["search_terms"])
        for canonical_detail in (
            "severity_assessment",
            "primary_classification",
            "secondary_classifications",
            "source_records",
            "diagnostic_provenance_summary",
            "interpretive_provenance_summary",
            "evidence_access_summary",
            "external_incident_references",
            "legacy_provenance",
        ):
            self.assertNotIn(canonical_detail, entry)

    def test_master_registry_is_incident_only(self):
        BUILDER.build()
        master = json.loads(BUILDER.MASTER_INDEX.read_text(encoding="utf-8"))
        incident_count = len(list(BUILDER.INCIDENTS.glob("VIGIL-INC-*.json")))
        self.assertEqual(master["registry_count"], 1)
        self.assertEqual(set(master["registries"]), {"incidents"})
        self.assertEqual(master["record_count"], {"incidents": incident_count, "total": incident_count})
        self.assertNotIn("records", master)
        self.assertEqual(master["registries"]["incidents"]["path"], "vigil/VIGIL.Incidents.Index.json")
        self.assertEqual(master["registries"]["incidents"]["record_count"], incident_count)

    def test_taxonomy_examples_are_incident_derived(self):
        BUILDER.build()
        projection = json.loads(BUILDER.TAXONOMY_EXAMPLES.read_text(encoding="utf-8"))
        examples = [item for rows in projection["classes"].values() for item in rows]
        self.assertTrue(examples)
        self.assertTrue(all(item["incident_id"].startswith("VIGIL-INC-") for item in examples))

    def test_generation_is_byte_stable(self):
        targets = (BUILDER.INCIDENT_INDEX, BUILDER.MASTER_INDEX, BUILDER.TAXONOMY_EXAMPLES)
        subprocess.run(["python", str(SCRIPT)], cwd=ROOT, check=True, capture_output=True, text=True)
        first = {path: path.read_bytes() for path in targets}
        subprocess.run(["python", str(SCRIPT)], cwd=ROOT, check=True, capture_output=True, text=True)
        self.assertEqual(first, {path: path.read_bytes() for path in targets})


if __name__ == "__main__":
    unittest.main()
