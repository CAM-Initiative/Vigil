import importlib.util
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
            "alignment_result": "not-aligned",
            "assessment_basis": "The occurrence failed the independently assessed proposition.",
            "assessed_on": "2026-09-29",
        }
        entry = BUILDER.incident_entry(Path("vigil/records/incidents/VIGIL-INC-000001.json"), self.record(assessment))
        self.assertEqual(entry["external_requirement_assessment_count"], 1)
        self.assertNotIn("external_requirement_assessments", entry)
        self.assertIn(assessment["requirement_id"], entry["search_terms"])
        self.assertIn("not-aligned", entry["search_terms"])


if __name__ == "__main__":
    unittest.main()
