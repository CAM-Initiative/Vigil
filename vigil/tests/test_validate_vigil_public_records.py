import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "vigil" / "scripts" / "validate-vigil-public-records.py"
spec = importlib.util.spec_from_file_location("validate_vigil_public_records", VALIDATOR)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


class ValidateVigilPublicRecordsTest(unittest.TestCase):
    def test_generated_incident_projection_rejects_embedded_detail_fields(self):
        record = {
            "id": "VIGIL-INC-000001",
            "record_type": "incident",
            "record_state": "active",
            "date_recorded": "2026-09-11",
            "record_identity": {
                "title": "Canonical Incident",
                "version": "1.0.0",
                "updated": "2026-09-11",
            },
            "incident_identity": {"occurred_from": "2026-09-10"},
            "summary": "A bounded Incident summary.",
            "system_context": {
                "platform_or_vendor": "Example Provider",
                "agent_context": {
                    "agentic_status": "non-agentic",
                    "agent_count": None,
                    "agent_count_min": None,
                    "agent_count_max": None,
                    "count_basis": "not-applicable",
                },
                "occurrence_environment": {
                    "operational_setting": "live",
                    "testing_actor": "not-applicable",
                },
            },
            "source_records": [{"source_role": "incident-evidence"}],
            "harm_impact_assessment": {"overall_severity": "S3"},
            "external_assessments": [],
            "taxonomy_classification": {
                "classification_status": "classified",
                "classification_role": "successful-invariant",
                "primary_classification": {
                    "class_id": "VIGIL-FC-000001",
                    "family_id": "VIGIL-FF-0001",
                    "classification_role": "successful-invariant",
                },
                "secondary_classifications": [],
            },
        }

        expected = validator.expected_projection(record)
        self.assertEqual(expected["classification_role"], "successful-invariant")
        self.assertEqual(expected["primary_classification"]["classification_role"], "successful-invariant")
        self.assertEqual(expected["repair_classifications"], [])
        entry = {
            key: value
            for key, value in expected.items()
            if value not in (None, "", [], {}) or key in {"secondary_classifications", "external_assessments"}
        }
        entry["search_terms"] = ["Example Provider", "VIGIL-FC-000001"]

        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "VIGIL.Incidents.Index.json"
            validator.INCIDENT_INDEX = path

            path.write_text(json.dumps({"records": [entry]}), encoding="utf-8")
            errors = []
            validator.validate_generated_incident_projection({record["id"]: record}, errors)
            self.assertEqual(errors, [])

            entry["harm_impact_assessment"] = record["harm_impact_assessment"]
            path.write_text(json.dumps({"records": [entry]}), encoding="utf-8")
            errors = []
            validator.validate_generated_incident_projection({record["id"]: record}, errors)
            self.assertTrue(any("non-index fields" in error for error in errors))
            self.assertTrue(any("embeds canonical detail field harm_impact_assessment" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
