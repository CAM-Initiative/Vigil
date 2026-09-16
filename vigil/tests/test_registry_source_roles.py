import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
INCIDENTS = ROOT / "vigil" / "records" / "incidents"


def load(incident_id: str) -> dict:
    return json.loads((INCIDENTS / f"{incident_id}.json").read_text(encoding="utf-8"))


class RegistrySourceRoleTests(unittest.TestCase):
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
        self.assertEqual(harm_refs, {"source_records[0]", "source_records[1]"})

    def test_registry_reported_does_not_imply_cross_reference(self):
        record = load("VIGIL-INC-000104")
        registry = next(
            item for item in record["source_records"]
            if item["source_type"] == "incident database entry"
        )
        self.assertEqual(registry["evidence_status"], "registry-reported")
        self.assertEqual(registry["source_role"], "incident-evidence")
        self.assertEqual(record["preferred_evidence"]["source_url"], registry["source_url"])


if __name__ == "__main__":
    unittest.main()
