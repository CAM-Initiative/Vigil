#!/usr/bin/env python3
"""Focused regression tests for the INCIDENT-01 migration architecture."""

from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
VALIDATOR = VIGIL / "scripts" / "validate-vigil-records.py"
spec = importlib.util.spec_from_file_location("validate_vigil_records", VALIDATOR)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


class IncidentRegistryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.incidents = {
            path.stem: load(path)
            for path in sorted((VIGIL / "records" / "incidents").glob("*.json"))
        }
        cls.crosswalk = load(
            VIGIL / "migrations" / "incident-registry" / "VIGIL.FM-OBS-to-INC.Crosswalk.json"
        )
        cls.by_legacy = {entry["legacy_id"]: entry for entry in cls.crosswalk["entries"]}

    def test_incident_ids_are_year_independent_and_unique(self):
        self.assertEqual(len(self.incidents), 79)
        self.assertTrue(all(identifier.startswith("VIGIL-INC-") for identifier in self.incidents))

    def test_external_registry_array_may_be_empty_but_must_exist(self):
        record = json.loads(json.dumps(self.incidents["VIGIL-INC-000009"]))
        self.assertEqual(record["external_incident_references"], [])
        errors: list[str] = []
        validator.validate_incident(Path(record["id"] + ".json"), record, errors)
        self.assertFalse(any("external_incident_references" in error for error in errors))

        del record["external_incident_references"]
        errors = []
        validator.validate_incident(Path(record["id"] + ".json"), record, errors)
        self.assertTrue(any("external_incident_references" in error for error in errors))

    def test_unclassified_incident_has_no_asserted_mapping(self):
        block = self.incidents["VIGIL-INC-000002"]["taxonomy_classification"]
        self.assertEqual(block["classification_status"], "unclassified")
        self.assertIsNone(block["primary_classification"])
        self.assertEqual(block["secondary_classifications"], [])

    def test_split_and_non_incident_dispositions_are_explicit(self):
        self.assertEqual(len(self.by_legacy["VIGIL-2026-FM-0038"]["successor_incidents"]), 4)
        self.assertEqual(
            self.by_legacy["VIGIL-2026-OBS-0011"]["migration_status"],
            "requires-human-review",
        )
        self.assertEqual(self.by_legacy["VIGIL-2026-OBS-0011"]["successor_incidents"], [])

    def test_majority_pass_limits_human_review(self):
        pending = [
            entry for entry in self.crosswalk["entries"]
            if entry["migration_status"] == "requires-human-review"
        ]
        self.assertEqual(len(pending), 11)
        self.assertEqual(self.crosswalk["migration_state"], "majority-migration-stabilisation")

    def test_current_incident_interpretation_is_not_legacy_pattern_text(self):
        for incident in self.incidents.values():
            current = incident["vigil_assessment"]["governance_interpretation"]
            self.assertFalse(current.casefold().startswith("a failure mode in which"))
            preserved = incident.get("legacy_governance_state", [])
            definitions = {
                item.get("preserved_analysis", {}).get("failure_mode_definition")
                for item in preserved
            }
            self.assertNotIn(current, definitions)

    def test_current_incidents_exclude_cam_repair_state_without_erasing_legacy_provenance(self):
        forbidden = {
            "corpus_coverage",
            "repair_status",
            "remaining_gaps",
            "proposal_needed",
            "patch_note_needed",
        }
        for incident in self.incidents.values():
            self.assertFalse(forbidden.intersection(incident))
            self.assertTrue(set(incident.get("cam_internal", {})).issubset(validator.INCIDENT_CAM_INTERNAL_ALLOWED))
            self.assertIn("legacy_governance_state", incident)
            self.assertIn("legacy_provenance", incident)

    def test_incident_validator_rejects_reintroduced_current_repair_state(self):
        record = json.loads(json.dumps(self.incidents["VIGIL-INC-000001"]))
        record["cam_internal"]["proposal_needed"] = "yes"
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / f"{record['id']}.json"
            path.write_text(json.dumps(record), encoding="utf-8")
            self.assertNotEqual(validator.validate(path), 0)

    def test_incident_validator_rejects_secondary_without_primary(self):
        record = json.loads(json.dumps(self.incidents["VIGIL-INC-000002"]))
        record["taxonomy_classification"]["secondary_classifications"] = [
            {
                "family_id": "VIGIL-FF-0001",
                "class_id": "VIGIL-FC-000002",
                "classification_basis": "test",
                "classification_confidence": "low",
            }
        ]
        errors: list[str] = []
        validator.validate_incident(Path(record["id"] + ".json"), record, errors)
        self.assertTrue(any("secondary classifications require a primary" in error for error in errors))

    def test_taxonomy_case_projection_is_incident_native(self):
        projection = load(
            VIGIL / "taxonomy" / "generated" / "VIGIL.FailureTaxonomy.CaseFileExamples.json"
        )
        examples = [item for rows in projection["classes"].values() for item in rows]
        self.assertTrue(examples)
        self.assertTrue(all(item["incident_id"] in self.incidents for item in examples))
        self.assertTrue(all("failure_mode_id" not in item for item in examples))
        self.assertEqual(projection["generated_from"], ["vigil/records/incidents/"])

    def test_taxonomy_publication_workflow_keeps_pdf_main_owned(self):
        workflow = (ROOT / ".github" / "workflows" / "taxonomy-publications.yml").read_text(
            encoding="utf-8"
        )
        self.assertNotIn("Verify generated publications are current", workflow)
        self.assertNotIn("generated/*.html", workflow)
        self.assertNotIn("Generate HTML publication for pull-request validation", workflow)
        self.assertIn("--taxonomy-examples-only", workflow)
        self.assertIn("Install PDF renderer on main publication build", workflow)
        self.assertIn("weasyprint==69.0", workflow)
        self.assertIn("Generate maintained PDF publication on main", workflow)
        self.assertIn("Verify maintained PDF publication on main", workflow)
        self.assertIn("--pdf", workflow)
        self.assertIn("VIGIL.Observatory.FailureTaxonomy.FullReference.pdf", workflow)
        self.assertIn("if: github.event_name != 'pull_request'", workflow)

    def test_incidents_publish_severity_and_canonical_source_genres(self):
        allowed_source_types = validator.CANONICAL_INCIDENT_SOURCE_TYPES
        for incident in self.incidents.values():
            severity = incident.get("severity_assessment", {})
            self.assertIn(severity.get("severity"), validator.ALLOWED_SEVERITIES)
            self.assertIn(severity.get("assessment_status"), validator.INCIDENT_SEVERITY_STATUSES)
            self.assertTrue(severity.get("assessment_basis"))
            self.assertTrue(all(source.get("source_type") in allowed_source_types for source in incident["source_records"]))

    def test_public_incident_narrative_is_not_taxonomy_process_text(self):
        for incident in self.incidents.values():
            self.assertTrue(incident.get("summary"))
            self.assertTrue(incident.get("vigil_assessment", {}).get("factual_basis"))
            self.assertNotEqual(incident["summary"], incident["taxonomy_classification"]["classification_basis"])


if __name__ == "__main__":
    unittest.main()
