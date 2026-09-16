import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
SCRIPT = VIGIL / "scripts" / "validate-vigil-records.py"
SPEC = importlib.util.spec_from_file_location("validate_vigil_records_rules", SCRIPT)
VALIDATOR = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(VALIDATOR)


class IncidentRuleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = json.loads(
            (VIGIL / "records" / "incidents" / "VIGIL-INC-000001.json").read_text(encoding="utf-8")
        )

    def errors(self, mutate=lambda record: None):
        record = copy.deepcopy(self.record)
        mutate(record)
        errors, _ = VALIDATOR.validate_record(Path(f"{record['id']}.json"), record)
        return errors

    def test_valid_incident_passes(self):
        self.assertEqual(self.errors(), [])

    def test_retired_record_type_is_rejected(self):
        self.assertTrue(self.errors(lambda record: record.update(record_type="failure_mode")))

    def test_harm_matrix_components_are_required(self):
        self.assertTrue(self.errors(lambda record: record["harm_impact_assessment"].pop("derivation_rule")))

    def test_overall_must_equal_highest_assessed_band(self):
        def mutate(record):
            record["harm_impact_assessment"]["overall_severity"] = "S1"
        errors = self.errors(mutate)
        self.assertTrue(any("highest supported" in error for error in errors), errors)

    def test_unreported_is_not_s1(self):
        def mutate(record):
            row = next(item for item in record["harm_impact_assessment"]["dimensions"] if item["assessment_status"] == "unreported")
            row["severity"] = "S1"
        errors = self.errors(mutate)
        self.assertTrue(any("forbidden when status is unreported" in error for error in errors), errors)

    def test_threshold_must_match_dimension_and_band(self):
        def mutate(record):
            row = next(item for item in record["harm_impact_assessment"]["dimensions"] if item["assessment_status"] == "assessed")
            row["threshold_id"] = "VIGIL-HIM-1.0.0-FIN-S1"
        errors = self.errors(mutate)
        self.assertTrue(any("does not match" in error for error in errors), errors)

    def test_su_requires_gap_and_no_assessed_dimensions(self):
        record = json.loads(
            (VIGIL / "records" / "incidents" / "VIGIL-INC-000028.json").read_text(encoding="utf-8")
        )
        record["harm_impact_assessment"].pop("assessment_gap")
        errors, _ = VALIDATOR.validate_record(Path(record["id"] + ".json"), record)
        self.assertTrue(any("SU requires" in error for error in errors), errors)

    def test_s1_requires_positive_assessed_evidence(self):
        record = json.loads(
            (VIGIL / "records" / "incidents" / "VIGIL-INC-000123.json").read_text(encoding="utf-8")
        )
        errors, _ = VALIDATOR.validate_record(Path(record["id"] + ".json"), record)
        self.assertEqual(errors, [])
        row = next(item for item in record["harm_impact_assessment"]["dimensions"] if item["assessment_status"] == "assessed")
        row["assessment_status"] = "unreported"
        for field in ("severity", "threshold_id", "observed_values", "evidence_refs"):
            row.pop(field, None)
        row["evidence_confidence"] = "not-assessed"
        errors, _ = VALIDATOR.validate_record(Path(record["id"] + ".json"), record)
        self.assertTrue(any("no assessed dimension" in error for error in errors), errors)

    def test_legacy_operational_priority_is_rejected_recursively(self):
        def mutate(record):
            record["legacy_governance_state"] = [{"preserved_analysis": {"triage": {"triage_priority": "P1"}}}]
        errors = self.errors(mutate)
        self.assertTrue(any("legacy operational priority field" in error for error in errors), errors)

    def test_successful_invariant_role_requires_matching_taxonomy_exemplar(self):
        record = json.loads(
            (VIGIL / "records" / "incidents" / "VIGIL-INC-000126.json").read_text(encoding="utf-8")
        )
        errors, _ = VALIDATOR.validate_record(Path(record["id"] + ".json"), record)
        self.assertEqual(errors, [])
        record["taxonomy_classification"]["primary_classification"]["class_id"] = "VIGIL-FC-000072"
        errors, _ = VALIDATOR.validate_record(Path(record["id"] + ".json"), record)
        self.assertTrue(any("invariant_exemplar" in error for error in errors), errors)

    def test_retired_legacy_structures_are_rejected(self):
        def mutate(record):
            record["legacy_provenance"] = [{
                "legacy_id": "VIGIL-2026-FM-9999",
                "legacy_type": "failure_mode",
                "relationship": "governance-analysis-source",
                "preservation_note": "Historical derivation token; no live target is required.",
            }]
        errors = self.errors(mutate)
        self.assertTrue(any("forbidden Incident fields" in error for error in errors), errors)

    def test_nested_migration_source_metadata_is_rejected(self):
        def mutate(record):
            record["source_records"][0]["migration_source_provenance"] = {
                "legacy_id": "VIGIL-2026-FM-9999"
            }
        errors = self.errors(mutate)
        self.assertTrue(any("forbidden retired Incident fields" in error for error in errors), errors)

    def test_retired_research_record_link_is_rejected(self):
        def mutate(record):
            record["research_references"] = ["VIGIL-2026-RESEARCH-0001"]
        errors = self.errors(mutate)
        self.assertTrue(any("retired VIGIL record ID" in error for error in errors), errors)

    def test_source_status_and_preferred_source_are_enforced(self):
        self.assertTrue(self.errors(lambda record: record["source_records"][0].pop("evidence_status")))
        self.assertTrue(self.errors(lambda record: record["preferred_evidence"].update(source_url="https://invalid.example")))

    def test_taxonomy_mapping_must_resolve_and_match_family(self):
        record = json.loads(
            (VIGIL / "records" / "incidents" / "VIGIL-INC-000003.json").read_text(encoding="utf-8")
        )
        record["taxonomy_classification"]["primary_classification"]["family_id"] = "VIGIL-FF-0002"
        errors, _ = VALIDATOR.validate_record(Path(record["id"] + ".json"), record)
        self.assertTrue(any("does not belong" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
