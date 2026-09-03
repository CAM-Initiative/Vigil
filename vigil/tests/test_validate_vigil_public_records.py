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
    def test_generated_incident_evidence_facets_must_match_canonical_sources(self):
        record = {
            "id": "VIGIL-INC-000001",
            "record_type": "incident",
            "preferred_evidence": {"source_url": "https://example.invalid/preferred"},
            "source_records": [
                {
                    "source_url": "https://example.invalid/preferred",
                    "evidence_status": "registry-reported",
                },
                {
                    "source_url": "https://example.invalid/reporting",
                    "evidence_status": "independent-reporting",
                },
            ],
        }
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "VIGIL.Incidents.Index.json"
            validator.INCIDENT_INDEX = path

            path.write_text(json.dumps({"records": [{
                "id": record["id"],
                "record_type": "incident",
                "evidence_statuses": ["independent-reporting", "registry-reported"],
                "preferred_evidence_status": "registry-reported",
            }]}), encoding="utf-8")
            errors = []
            validator.validate_generated_incident_evidence_facets({record["id"]: record}, errors)
            self.assertEqual(errors, [])

            path.write_text(json.dumps({"records": [{
                "id": record["id"],
                "record_type": "incident",
                "evidence_statuses": ["registry-reported"],
                "preferred_evidence_status": "verified",
                "evidence_confidence": "high",
            }]}), encoding="utf-8")
            errors = []
            validator.validate_generated_incident_evidence_facets({record["id"]: record}, errors)
            self.assertEqual(len(errors), 3)


if __name__ == "__main__":
    unittest.main()
