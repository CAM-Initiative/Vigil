import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
INCIDENTS = ROOT / "vigil" / "records" / "incidents"
SCHEMA = ROOT / "vigil" / "VIGIL.Schema.json"


def load(incident_id: str) -> dict:
    return json.loads((INCIDENTS / f"{incident_id}.json").read_text(encoding="utf-8"))


class RegistrySourceRoleTests(unittest.TestCase):
    def test_schema_admits_explicit_harm_evidence_role(self):
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        self.assertIn("harm-evidence", schema["$defs"]["source_role"]["enum"])

    def test_inc_129_media_sources_are_explicit_harm_evidence(self):
        record = load("VIGIL-INC-000129")
        media_sources = record["source_records"][3:9]
        self.assertEqual(len(media_sources), 6)
        self.assertTrue(all(item["source_type"] == "news article" for item in media_sources))
        self.assertTrue(all(item["source_role"] == "harm-evidence" for item in media_sources))
        reputation = next(
            item for item in record["harm_impact_assessment"]["dimensions"]
            if item["dimension_id"] == "reputation-dignity"
        )
        self.assertEqual(
            reputation["evidence_refs"],
            [f"source_records[{index}]" for index in range(3, 9)],
        )

    def test_inc_127_evidence_hierarchy_is_structural(self):
        record = load("VIGIL-INC-000127")
        by_publisher = {item["author_or_publisher"]: item for item in record["source_records"]}

        self.assertEqual(by_publisher["GreyNoise"]["source_role"], "incident-evidence")
        self.assertEqual(by_publisher["PaperCut"]["source_role"], "affected-party-evidence")
        self.assertEqual(by_publisher["OECD.AI"]["source_role"], "record-cross-reference")
        self.assertEqual(by_publisher["OECD.AI"]["source_residence"], "external")
        self.assertEqual(by_publisher["OECD.AI"]["evidence_status"], "registry-reported")
        self.assertEqual(record["preferred_evidence"]["source_url"], by_publisher["GreyNoise"]["source_url"])
        self.assertTrue(any(
            item.get("source_url") == by_publisher["OECD.AI"]["source_url"]
            and item.get("relationship") == "same-incident"
            for item in record["external_incident_references"]
        ))
        harm_refs = {
            ref
            for row in record["harm_impact_assessment"]["dimensions"]
            for ref in row.get("evidence_refs", [])
        }
        self.assertNotIn("source_records[2]", harm_refs)
        self.assertEqual(harm_refs, {"source_records[0]", "source_records[1]", "source_records[3]"})

    def test_registry_reported_does_not_imply_cross_reference(self):
        record = load("VIGIL-INC-000104")
        registry = next(
            item for item in record["source_records"]
            if item["source_type"] == "incident database entry"
        )
        self.assertEqual(registry["evidence_status"], "registry-reported")
        self.assertEqual(registry["source_role"], "incident-evidence")
        self.assertEqual(record["preferred_evidence"]["source_url"], registry["source_url"])

    def test_recovered_consequences_are_banded_per_him_evidence(self):
        expected = {
            "VIGIL-INC-000061": ("S3", "service-operational-infrastructure"),
            "VIGIL-INC-000065": ("S4", "reputation-dignity"),
            "VIGIL-INC-000131": ("S3", "privacy-confidentiality"),
            "VIGIL-INC-000135": ("S3", "privacy-confidentiality"),
            "VIGIL-INC-000148": ("S3", "service-operational-infrastructure"),
        }
        for incident_id, (severity, controller) in expected.items():
            with self.subTest(incident_id=incident_id):
                record = load(incident_id)
                assessment = record["harm_impact_assessment"]
                self.assertEqual(assessment["overall_severity"], severity)
                self.assertIn(controller, assessment["controlling_dimensions"])
                row = next(item for item in assessment["dimensions"] if item["dimension_id"] == controller)
                self.assertEqual(row["assessment_status"], "assessed")
                self.assertEqual(row["severity"], severity)
                self.assertTrue(row["evidence_refs"])

    def test_non_usd_legal_consequence_is_banded_with_documented_conversion(self):
        record = load("VIGIL-INC-000140")
        assessment = record["harm_impact_assessment"]
        financial = next(
            item for item in assessment["dimensions"]
            if item["dimension_id"] == "financial-economic"
        )
        self.assertEqual(assessment["overall_severity"], "S1")
        self.assertEqual(financial["assessment_status"], "assessed")
        self.assertEqual(financial["severity"], "S1")
        self.assertEqual(financial["threshold_id"], "VIGIL-HIM-1.0.1-FIN-S1")
        self.assertIn("US$599.27", financial["assessment_basis"])
        self.assertEqual(financial["evidence_refs"], [
            "source_records[1]", "source_records[2]", "source_records[3]",
        ])


if __name__ == "__main__":
    unittest.main()
