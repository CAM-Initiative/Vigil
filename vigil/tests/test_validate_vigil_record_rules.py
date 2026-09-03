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

    def test_structured_severity_components_are_required(self):
        self.assertTrue(self.errors(lambda record: record["severity_assessment"].pop("affected_scope")))

    def test_canonical_assessment_basis_is_rejected(self):
        self.assertTrue(self.errors(lambda record: record["severity_assessment"].update(assessment_basis="S2 because S2")))

    def test_generic_and_circular_band_reasoning_is_rejected(self):
        def mutate(record):
            record["severity_assessment"]["affected_scope"] = (
                "The assessment is confined to the people, systems, organisations, service cohort."
            )
            record["severity_assessment"]["band_rationale"] = (
                "S2 because this is an S2 incident; S1 and S3 are different."
            )
        errors = self.errors(mutate)
        self.assertTrue(any("generic/template" in error for error in errors), errors)
        self.assertTrue(any("circular" in error for error in errors), errors)

    def test_su_requires_review_gap_and_no_assessed_fields(self):
        def mutate(record):
            record["severity_assessment"] = {
                "severity": "SU", "assessment_status": "incident-assessed",
                "assessed_on": "2026-09-02", "legacy_sources": [],
                "materialised_consequence": "Invented consequence",
            }
        errors = self.errors(mutate)
        self.assertTrue(any("requires-incident-review" in error for error in errors), errors)
        self.assertTrue(any("assessment_gap" in error for error in errors), errors)
        self.assertTrue(any("must not fabricate" in error for error in errors), errors)

    def test_historical_provenance_tokens_do_not_resolve(self):
        def mutate(record):
            record["legacy_provenance"] = [{
                "legacy_id": "VIGIL-2026-FM-9999",
                "legacy_type": "failure_mode",
                "relationship": "governance-analysis-source",
                "preservation_note": "Historical derivation token; no live target is required.",
            }]
        self.assertEqual(self.errors(mutate), [])

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
