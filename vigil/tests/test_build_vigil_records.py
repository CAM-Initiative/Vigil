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
        self.assertEqual(entry["severity"], record["harm_impact_assessment"]["overall_severity"])
        self.assertEqual(entry["classification_status"], record["taxonomy_classification"]["classification_status"])
        self.assertEqual(entry.get("classification_role"), record["taxonomy_classification"].get("classification_role"))
        self.assertEqual(
            entry["primary_classification"]["classification_role"],
            record["taxonomy_classification"]["primary_classification"]["classification_role"],
        )
        self.assertEqual(
            entry["secondary_classifications"],
            [BUILDER.projected_mapping(item) for item in record["taxonomy_classification"]["secondary_classifications"]],
        )
        self.assertEqual(entry["record_version"], record["record_identity"]["version"])
        self.assertEqual(entry["record_last_updated"], record["record_identity"]["updated"])
        self.assertEqual(entry["source_roles"], BUILDER.source_roles(record))
        self.assertIn("search_terms", entry)
        self.assertTrue(entry["search_terms"])
        for canonical_detail in (
            "harm_impact_assessment",
            "source_records",
            "diagnostic_provenance_summary",
            "interpretive_provenance_summary",
            "evidence_access_summary",
            "external_incident_references",
            "related_incidents",
            "research_references",
            "standards_and_regulatory_references",
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
        self.assertFalse(any(item["incident_id"] == "VIGIL-INC-000126" for item in examples))
        successful = [item for rows in projection["successful_invariants"].values() for item in rows]
        self.assertTrue(any(item["incident_id"] == "VIGIL-INC-000126" for item in successful))

    def test_failure_examples_and_repair_are_derived_per_mapping(self):
        def mapping(class_id, role):
            return {
                "family_id": "VIGIL-FF-0001",
                "class_id": class_id,
                "classification_role": role,
                "classification_basis": "Bounded test basis.",
                "classification_confidence": "high",
            }

        structures = {
            "A": (mapping("VIGIL-FC-000001", "failure-occurrence"), [], ["VIGIL-FC-000001"]),
            "B": (mapping("VIGIL-FC-000001", "failure-occurrence"), [mapping("VIGIL-FC-000002", "failure-occurrence")], ["VIGIL-FC-000001", "VIGIL-FC-000002"]),
            "C": (mapping("VIGIL-FC-000001", "successful-invariant"), [], []),
            "D": (mapping("VIGIL-FC-000001", "failure-occurrence"), [mapping("VIGIL-FC-000002", "successful-invariant")], ["VIGIL-FC-000001"]),
            "E": (mapping("VIGIL-FC-000001", "successful-invariant"), [mapping("VIGIL-FC-000002", "failure-occurrence")], ["VIGIL-FC-000002"]),
        }
        records = []
        for label, (primary, secondary, expected_repairs) in structures.items():
            record = {
                "id": f"VIGIL-INC-TEST-{label}",
                "record_identity": {"title": f"Structure {label}"},
                "taxonomy_classification": {
                    "primary_classification": primary,
                    "secondary_classifications": secondary,
                },
            }
            records.append(record)
            self.assertEqual(
                [item["class_id"] for item in BUILDER.repair_classifications(record)],
                expected_repairs,
                label,
            )

        projection = BUILDER.taxonomy_examples(records)
        failure_pairs = {
            (item["incident_id"], class_id)
            for class_id, rows in projection["classes"].items()
            for item in rows
        }
        exemplar_pairs = {
            (item["incident_id"], class_id)
            for class_id, rows in projection["successful_invariants"].items()
            for item in rows
        }
        self.assertIn(("VIGIL-INC-TEST-D", "VIGIL-FC-000001"), failure_pairs)
        self.assertIn(("VIGIL-INC-TEST-D", "VIGIL-FC-000002"), exemplar_pairs)
        self.assertIn(("VIGIL-INC-TEST-E", "VIGIL-FC-000001"), exemplar_pairs)
        self.assertIn(("VIGIL-INC-TEST-E", "VIGIL-FC-000002"), failure_pairs)
        self.assertNotIn(("VIGIL-INC-TEST-C", "VIGIL-FC-000001"), failure_pairs)

    def test_generation_is_byte_stable(self):
        targets = (BUILDER.INCIDENT_INDEX, BUILDER.MASTER_INDEX, BUILDER.TAXONOMY_EXAMPLES)
        subprocess.run(["python", str(SCRIPT)], cwd=ROOT, check=True, capture_output=True, text=True)
        first = {path: path.read_bytes() for path in targets}
        subprocess.run(["python", str(SCRIPT)], cwd=ROOT, check=True, capture_output=True, text=True)
        self.assertEqual(first, {path: path.read_bytes() for path in targets})


if __name__ == "__main__":
    unittest.main()
