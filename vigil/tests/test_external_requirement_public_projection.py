import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "vigil" / "scripts" / "build-vigil-public-records.py"
SPEC = importlib.util.spec_from_file_location("build_vigil_public_extreq", SCRIPT)
BUILDER = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(BUILDER)


class ExternalRequirementProjectionTests(unittest.TestCase):
    def record(self, assessment=None):
        return {
            "id": "VIGIL-INC-000001",
            "record_type": "incident",
            "record_state": "active",
            "record_identity": {"title": "Example occurrence", "version": "0.1.0"},
            "taxonomy_classification": {"secondary_classifications": []},
            "external_requirement_assessments": [] if assessment is None else [assessment],
        }

    def test_optional_assessment_has_navigation_count(self):
        entry = BUILDER.incident_entry(Path("vigil/records/incidents/VIGIL-INC-000001.json"), self.record())
        self.assertEqual(entry["external_requirement_assessment_count"], 0)
        self.assertNotIn("external_requirement_assessments", entry)

    def test_requirement_is_searchable_without_duplicating_assessment(self):
        assessment = {
            "requirement_id": "EXTREQ-0123456789ABCDEF",
            "derived_from_class_ids": ["VIGIL-FC-000001"],
            "applicability_status": "applicable",
            "applicability_basis": "Territorial and system scope are established.",
            "finding": "not-met",
            "finding_basis": "The occurrence failed the stated requirement.",
            "assessed_on": "2026-09-29",
        }
        entry = BUILDER.incident_entry(Path("vigil/records/incidents/VIGIL-INC-000001.json"), self.record(assessment))
        self.assertEqual(entry["external_requirement_assessment_count"], 1)
        self.assertNotIn("external_requirement_assessments", entry)
        self.assertIn(assessment["requirement_id"], entry["search_terms"])
        self.assertIn("not-met", entry["search_terms"])


    def test_inc001_public_assessments_do_not_expand_to_stage4_candidate_inventory(self):
        record_path = ROOT / "vigil" / "records" / "incidents" / "VIGIL-INC-000001.json"
        record = json.loads(record_path.read_text(encoding="utf-8"))
        assessments = record.get("external_requirement_assessments", [])
        self.assertEqual(
            {item["requirement_id"] for item in assessments},
            {"EXTREQ-2E1D2C63187C14E8", "EXTREQ-C25CB2D997BC6FE8"},
        )
        self.assertTrue(all(item["applicability_status"] == "insufficient-evidence" for item in assessments))



if __name__ == "__main__":
    unittest.main()
