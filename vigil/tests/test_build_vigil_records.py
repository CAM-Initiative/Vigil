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
        self.assertEqual(len(paths), 81)
        self.assertTrue(all(BUILDER.load(path)["record_type"] == "incident" for path in paths))

    def test_structured_severity_and_compatibility_projection_are_both_published(self):
        record = BUILDER.load(BUILDER.INCIDENTS / "VIGIL-INC-000081.json")
        entry = BUILDER.incident_entry(BUILDER.INCIDENTS / "VIGIL-INC-000081.json", record)
        self.assertEqual(entry["severity_assessment"], record["severity_assessment"])
        self.assertIn("Materialised consequence:", entry["severity_assessment_basis"])
        self.assertNotIn("assessment_basis", record["severity_assessment"])

    def test_master_registry_is_incident_only(self):
        BUILDER.build()
        master = json.loads(BUILDER.MASTER_INDEX.read_text(encoding="utf-8"))
        self.assertEqual(master["registry_count"], 1)
        self.assertEqual(set(master["registries"]), {"incidents"})
        self.assertEqual(master["record_count"], {"incidents": 81, "total": 81})
        self.assertTrue(all(item["record_type"] == "incident" for item in master["records"]))

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
