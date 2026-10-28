import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

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
        self.assertEqual(entry["alignment_exemplar_eligible"], BUILDER.alignment_exemplar_eligible(record))
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
        self.assertEqual(entry["external_assessment_count"], len(record.get("external_assessments", [])))
        self.assertEqual(
            entry["agent_context"],
            {
                key: record["system_context"]["agent_context"][key]
                for key in ("agentic_status", "agent_count", "agent_count_min", "agent_count_max", "count_basis")
            },
        )
        self.assertEqual(
            entry["occurrence_environment"],
            {
                key: record["system_context"]["occurrence_environment"][key]
                for key in ("deployment_state", "activity_contexts", "external_reach", "activity_actor")
            },
        )
        self.assertNotIn("evidence_basis", entry["agent_context"])
        self.assertNotIn("source_record_refs", entry["occurrence_environment"])
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

    def test_external_assessment_navigation_count_does_not_affect_taxonomy_or_repair(self):
        record = BUILDER.load(BUILDER.INCIDENTS / "VIGIL-INC-000129.json")
        entry = BUILDER.incident_entry(BUILDER.INCIDENTS / "VIGIL-INC-000129.json", record)
        self.assertEqual(entry["external_assessment_count"], len(record["external_assessments"]))
        self.assertEqual(entry["primary_classification"]["class_id"], "VIGIL-FC-000075")
        # Repair remains failure-only. The approved reassessment now leaves
        # INC-000129 with ambiguous-boundary mappings, not a failure mapping.
        mappings = [
            record["taxonomy_classification"]["primary_classification"],
            *record["taxonomy_classification"]["secondary_classifications"],
        ]
        expected_failure_ids = [
            item["class_id"] for item in mappings
            if item["classification_role"] == "failure-occurrence"
        ]
        self.assertEqual(
            [item["class_id"] for item in entry.get("repair_classifications", [])],
            expected_failure_ids,
        )
        self.assertEqual(
            entry["primary_classification"]["classification_role"],
            "ambiguous-boundary",
        )

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

        failure_id = "VIGIL-FC-TEST-FAILURE"
        success_id = "VIGIL-FC-TEST-SUCCESS"
        boundary_id = "VIGIL-FC-TEST-BOUNDARY"

        def mapping(class_id, role):
            return {
                "family_id": "VIGIL-FF-TEST",
                "class_id": class_id,
                "classification_role": role,
                "classification_basis": "Fixture mapping basis.",
                **({"classification_confidence": "high"} if role != "ambiguous-boundary" else {}),
            }

        mixed = {
            "id": "VIGIL-INC-TEST-MIXED",
            "record_identity": {"title": "Mixed mapping-role fixture"},
            "taxonomy_classification": {
                "classification_status": "classified",
                "adjudication_coverage": {"status": "complete"},
                "primary_classification": mapping(success_id, "successful-invariant"),
                "secondary_classifications": [
                    mapping(failure_id, "failure-occurrence"),
                    mapping(boundary_id, "ambiguous-boundary"),
                ],
            },
        }
        with tempfile.TemporaryDirectory() as directory:
            taxonomy_dir = Path(directory)
            index_path = taxonomy_dir / "index.json"
            family_path = taxonomy_dir / "family.json"
            index_path.write_text(json.dumps({"families": [{"file": "family.json"}]}), encoding="utf-8")
            family_path.write_text(
                json.dumps({"classes": [{"class_id": class_id} for class_id in
                                        (failure_id, success_id, boundary_id)]}),
                encoding="utf-8",
            )
            with patch.object(BUILDER, "TAXONOMY_INDEX", index_path):
                fixture_projection = BUILDER.taxonomy_examples([mixed])

        def projected_pairs(bucket):
            return {
                (item["incident_id"], class_id, item["mapping_position"], item["classification_role"])
                for class_id, rows in fixture_projection[bucket].items()
                for item in rows
            }

        incident_id = mixed["id"]
        self.assertEqual(
            projected_pairs("classes"),
            {(incident_id, failure_id, "secondary", "failure-occurrence")},
        )
        self.assertEqual(
            projected_pairs("successful_invariants"),
            {(incident_id, success_id, "primary", "successful-invariant")},
        )
        self.assertEqual(
            projected_pairs("ambiguous_boundaries"),
            {(incident_id, boundary_id, "secondary", "ambiguous-boundary")},
        )

        mixed_entry = BUILDER.incident_entry(
            BUILDER.INCIDENTS / "VIGIL-INC-TEST-MIXED.json", mixed
        )
        self.assertEqual(mixed_entry["classification_status"], "classified")
        self.assertNotIn("classification_role", mixed_entry)
        self.assertEqual(mixed_entry["adjudication_coverage"], {"status": "complete"})
        self.assertFalse(BUILDER.alignment_exemplar_eligible(mixed))

        success_only = {
            "id": "VIGIL-INC-TEST-SUCCESS-ONLY",
            "record_identity": {"title": "Complete success-only fixture"},
            "taxonomy_classification": {
                "classification_status": "classified",
                "classification_role": "successful-invariant",
                "adjudication_coverage": {"status": "complete"},
                "primary_classification": mapping(success_id, "successful-invariant"),
                "secondary_classifications": [],
            },
        }
        success_entry = BUILDER.incident_entry(
            BUILDER.INCIDENTS / "VIGIL-INC-TEST-SUCCESS-ONLY.json", success_only
        )
        self.assertEqual(success_entry["classification_status"], "classified")
        self.assertEqual(success_entry["classification_role"], "successful-invariant")
        self.assertEqual(success_entry["adjudication_coverage"], {"status": "complete"})
        self.assertTrue(BUILDER.alignment_exemplar_eligible(success_only))

        for role in ("failure-occurrence", "ambiguous-boundary"):
            mixed_roles = {
                **success_only,
                "id": f"VIGIL-INC-TEST-SUCCESS-PLUS-{role}",
                "taxonomy_classification": {
                    **success_only["taxonomy_classification"],
                    "secondary_classifications": [mapping(f"VIGIL-FC-TEST-{role.upper()}", role)],
                },
            }
            self.assertFalse(BUILDER.alignment_exemplar_eligible(mixed_roles), role)

        partial_success = {
            **success_only,
            "taxonomy_classification": {
                **success_only["taxonomy_classification"],
                "adjudication_coverage": {"status": "partial"},
            },
        }
        self.assertFalse(BUILDER.alignment_exemplar_eligible(partial_success))

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
            "F": (mapping("VIGIL-FC-000001", "failure-occurrence"), [mapping("VIGIL-FC-000002", "ambiguous-boundary")], ["VIGIL-FC-000001"]),
        }
        records = []
        for label, (primary, secondary, expected_repairs) in structures.items():
            record = {
                "id": f"VIGIL-INC-TEST-{label}",
                "record_identity": {"title": f"Structure {label}"},
                "taxonomy_classification": {
                    "primary_classification": primary,
                    "secondary_classifications": secondary,
                    "adjudication_coverage": {"status": "complete"},
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
        ambiguous_pairs = {
            (item["incident_id"], class_id)
            for class_id, rows in projection["ambiguous_boundaries"].items()
            for item in rows
        }
        self.assertIn(("VIGIL-INC-TEST-D", "VIGIL-FC-000001"), failure_pairs)
        self.assertIn(("VIGIL-INC-TEST-D", "VIGIL-FC-000002"), exemplar_pairs)
        self.assertIn(("VIGIL-INC-TEST-E", "VIGIL-FC-000001"), exemplar_pairs)
        self.assertIn(("VIGIL-INC-TEST-C", "VIGIL-FC-000001"), exemplar_pairs)
        self.assertIn(("VIGIL-INC-TEST-E", "VIGIL-FC-000002"), failure_pairs)
        self.assertNotIn(("VIGIL-INC-TEST-C", "VIGIL-FC-000001"), failure_pairs)
        self.assertIn(("VIGIL-INC-TEST-F", "VIGIL-FC-000002"), ambiguous_pairs)
        self.assertNotIn(("VIGIL-INC-TEST-F", "VIGIL-FC-000002"), failure_pairs)
        self.assertNotIn(("VIGIL-INC-TEST-F", "VIGIL-FC-000002"), exemplar_pairs)

    def test_generation_is_byte_stable(self):
        targets = (BUILDER.INCIDENT_INDEX, BUILDER.MASTER_INDEX, BUILDER.TAXONOMY_EXAMPLES)
        subprocess.run(["python", str(SCRIPT)], cwd=ROOT, check=True, capture_output=True, text=True)
        first = {path: path.read_bytes() for path in targets}
        subprocess.run(["python", str(SCRIPT)], cwd=ROOT, check=True, capture_output=True, text=True)
        self.assertEqual(first, {path: path.read_bytes() for path in targets})


if __name__ == "__main__":
    unittest.main()
