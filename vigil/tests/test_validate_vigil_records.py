import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "vigil" / "scripts" / "validate-vigil-records.py"
spec = importlib.util.spec_from_file_location("validate_vigil_records", VALIDATOR)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


class ValidateVigilRecordsTest(unittest.TestCase):
    def test_canonical_repository_validation_closes_withdrawn_provenance_links(self):
        self.assertEqual(validator.validate(), 0)

    def test_only_typed_withdrawn_relationships_are_acknowledged(self):
        record = {
            "linked_records": {
                "related_proposals": ["VIGIL-2026-PROP-0001"],
                "related_patch_notes": ["VIGIL-2026-PATCH-0023"],
                "related_observations": ["VIGIL-2026-OBS-9999"],
            }
        }
        self.assertEqual(
            validator.withdrawn_reference_ids(record),
            {"VIGIL-2026-PROP-0001", "VIGIL-2026-PATCH-0023"},
        )

    def test_valid_fixtures_pass(self):
        self.assertEqual(validator.validate(ROOT / "vigil" / "tests" / "fixtures" / "valid"), 0)

    def test_invalid_fixtures_fail(self):
        invalid_dir = ROOT / "vigil" / "tests" / "fixtures" / "invalid"
        for fixture in sorted(invalid_dir.glob("*.json")):
            with self.subTest(fixture=fixture.name):
                self.assertNotEqual(validator.validate(fixture), 0)

    def test_source_data_is_forbidden(self):
        fixture = ROOT / "vigil" / "tests" / "fixtures" / "invalid" / "invalid-obs-source-data.json"
        self.assertNotEqual(validator.validate(fixture), 0)

    def validate_mutated_fixture(self, fixture_name, mutate, schema_path=None):
        fixture = ROOT / "vigil" / "tests" / "fixtures" / "valid" / fixture_name
        with fixture.open(encoding="utf-8") as handle:
            record = json.load(handle)
        mutate(record)
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / f"{record['id']}.json"
            path.write_text(json.dumps(record), encoding="utf-8")
            return validator.validate(path, schema_path=schema_path)

    def validate_mutated_incident(self, mutate):
        fixture = ROOT / "vigil" / "records" / "incidents" / "VIGIL-INC-000001.json"
        with fixture.open(encoding="utf-8") as handle:
            record = json.load(handle)
        mutate(record)
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / f"{record['id']}.json"
            path.write_text(json.dumps(record), encoding="utf-8")
            return validator.validate(path)

    def test_incident_source_evidence_status_contract(self):
        self.assertEqual(self.validate_mutated_incident(lambda record: None), 0)

        def remove_status(record):
            record["source_records"][0].pop("evidence_status")

        def remove_basis(record):
            record["source_records"][0].pop("evidence_status_basis")

        def narrative_status(record):
            record["source_records"][0]["evidence_status"] = "credible reporting with caveats"

        def revive_incident_confidence(record):
            record["evidence_confidence"] = "medium"

        self.assertNotEqual(self.validate_mutated_incident(remove_status), 0)
        self.assertNotEqual(self.validate_mutated_incident(remove_basis), 0)
        self.assertNotEqual(self.validate_mutated_incident(narrative_status), 0)
        self.assertNotEqual(self.validate_mutated_incident(revive_incident_confidence), 0)

    def test_incident_evidence_status_vocabulary_matches_schema(self):
        with (ROOT / "vigil" / "VIGIL.Schema.json").open(encoding="utf-8") as handle:
            schema = json.load(handle)
        self.assertEqual(
            validator.INCIDENT_EVIDENCE_STATUSES,
            set(schema["record_classes"]["incident"]["evidence_status_values"]),
        )

    def test_incident_severity_rejects_generic_circular_and_incoherent_assessments(self):
        self.assertEqual(self.validate_mutated_incident(lambda record: None), 0)

        def generic(record):
            record["severity_assessment"]["assessment_basis"] = "S2 reflects high impact or risk in this occurrence."

        def missing_adjacent_boundary(record):
            record["severity_assessment"].update({
                "severity": "S2",
                "assessment_status": "incident-assessed",
                "assessment_basis": "S2 records the reported consequence without a boundary explanation.",
            })

        def invalid_incident_s0(record):
            record["severity_assessment"]["severity"] = "S0"

        def su_without_review(record):
            record["severity_assessment"].update({
                "severity": "SU",
                "assessment_status": "incident-assessed",
                "assessment_basis": "SU: occurrence-level harm and affected scope remain unknown pending primary evidence review.",
            })

        self.assertNotEqual(self.validate_mutated_incident(generic), 0)
        self.assertNotEqual(self.validate_mutated_incident(missing_adjacent_boundary), 0)
        self.assertNotEqual(self.validate_mutated_incident(invalid_incident_s0), 0)
        self.assertNotEqual(self.validate_mutated_incident(su_without_review), 0)

    def adopt_triage_v2(self, record, priority="P2", status="action-required", severity="S2"):
        record["failure_classification"]["severity"] = severity
        record["failure_classification"]["severity_assessment_basis"] = (
            "Credible foreseeable harm within the evidenced deployment scope."
        )
        record["failure_classification"].pop("severity_assessment_gap", None)
        record["triage"].update(
            {
                "model_version": "2.0",
                "triage_priority": priority,
                "triage_status": status,
                "triage_owner": "AI analytical reviewer",
                "triage_action_basis": "A defined governance action remains.",
                "triage_review_date": "2026-08-12",
                "escalation_required": "not required for this priority",
                "recommended_next_step": "Complete the defined governance action.",
            }
        )
        record["triage"].pop("triage_assessment_gap", None)
        record["triage"].pop("active_escalation_trigger", None)
        record["triage"].pop("intervention_pathway", None)
        record["triage"].pop("urgent_condition", None)
        record["triage_history"] = []

    def test_canonical_path_validation_by_record_type_and_year(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_records = Path(temp_dir) / "records"
            fixture = ROOT / "vigil" / "tests" / "fixtures" / "valid" / "VIGIL-2026-OBS-0001.json"
            wrong_path = temp_records / "proposals" / "2026" / "VIGIL-2026-OBS-0001.json"
            wrong_path.parent.mkdir(parents=True)
            shutil.copy2(fixture, wrong_path)

            originals = (validator.RECORDS_ROOT, validator.RECORD_TYPE_DIRS)
            try:
                validator.RECORDS_ROOT = temp_records
                validator.RECORD_TYPE_DIRS = [
                    temp_records / "observations",
                    temp_records / "failures",
                    temp_records / "proposals",
                    temp_records / "patches",
                ]
                self.assertNotEqual(validator.validate(), 0)
            finally:
                validator.RECORDS_ROOT, validator.RECORD_TYPE_DIRS = originals

    def test_clean_observation_records_pass(self):
        for record_id in ("VIGIL-2026-OBS-0002", "VIGIL-2026-OBS-0003"):
            with self.subTest(record=record_id):
                path = ROOT / "vigil" / "records" / "observations" / "2026" / f"{record_id}.json"
                self.assertEqual(validator.validate(path), 0)

    def test_withdrawn_record_classes_are_absent_from_public_tree(self):
        for folder in ("proposals", "patches", "learn"):
            with self.subTest(folder=folder):
                self.assertFalse(
                    (ROOT / "vigil" / "records" / folder).exists(),
                    f"{folder} must remain outside the public record tree",
                )

    def test_patch_fixture_validates_without_publication(self):
        fixture = ROOT / "vigil" / "tests" / "fixtures" / "valid" / "VIGIL-2026-PATCH-0001.json"
        self.assertEqual(validator.validate(fixture), 0)

    def test_patch_note_record_type_uses_patch_prefix_and_patches_path(self):
        fixture = ROOT / "vigil" / "tests" / "fixtures" / "valid" / "VIGIL-2026-PATCH-0001.json"
        with fixture.open(encoding="utf-8") as handle:
            record = json.load(handle)
        record["record_type"] = "patch_note"
        record["record_identity"]["record_type"] = "patch_note"
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_records = Path(temp_dir) / "records"
            path = temp_records / "patches" / "2026" / "VIGIL-2026-PATCH-0001.json"
            path.parent.mkdir(parents=True)
            path.write_text(json.dumps(record), encoding="utf-8")
            originals = (validator.RECORDS_ROOT, validator.RECORD_TYPE_DIRS)
            try:
                validator.RECORDS_ROOT = temp_records
                validator.RECORD_TYPE_DIRS = [temp_records / "patches"]
                self.assertEqual(validator.validate(), 0)
            finally:
                validator.RECORDS_ROOT, validator.RECORD_TYPE_DIRS = originals

    def test_taxonomy_classified_fm_fixture_is_valid(self):
        self.assertEqual(
            self.validate_mutated_fixture("VIGIL-2026-FM-0001.json", lambda record: None),
            0,
        )

    def test_fm_rejects_retired_canonical_failure_group(self):
        def mutate(record):
            record["failure_classification"]["canonical_failure_group"] = "governance"

        self.assertNotEqual(self.validate_mutated_fixture("VIGIL-2026-FM-0001.json", mutate), 0)

    def test_fm_rejects_retired_failure_family(self):
        def mutate(record):
            record["failure_classification"]["failure_family"] = "legacy-runtime"

        self.assertNotEqual(self.validate_mutated_fixture("VIGIL-2026-FM-0001.json", mutate), 0)

    def test_fm_rejects_peer_failure_links(self):
        def mutate(record):
            record["linked_records"]["related_failure_modes"] = ["VIGIL-2026-FM-0002"]

        self.assertNotEqual(self.validate_mutated_fixture("VIGIL-2026-FM-0001.json", mutate), 0)

    def test_fm_requires_diagnostic_provenance(self):
        def mutate(record):
            record.pop("diagnostic_provenance")

        self.assertNotEqual(self.validate_mutated_fixture("VIGIL-2026-FM-0001.json", mutate), 0)

    def test_fm_diagnostic_model_must_match_creation_date(self):
        def mutate(record):
            record["diagnostic_provenance"]["ai_model"] = "GPT-5.6 Sol"

        self.assertNotEqual(self.validate_mutated_fixture("VIGIL-2026-FM-0001.json", mutate), 0)

    def test_fm_diagnostic_date_must_match_canonical_creation_date(self):
        def mutate(record):
            record["diagnostic_provenance"]["diagnostic_date"] = "2026-06-01"

        self.assertNotEqual(self.validate_mutated_fixture("VIGIL-2026-FM-0001.json", mutate), 0)

    def test_fm_conflicting_creation_dates_require_explicit_anomaly(self):
        def mutate(record):
            record["date_recorded"] = "2026-06-01"

        self.assertNotEqual(self.validate_mutated_fixture("VIGIL-2026-FM-0001.json", mutate), 0)

    def test_canonical_fm_diagnostic_provenance_inventory_is_non_brittle(self):
        paths = sorted((ROOT / "vigil" / "records" / "failures").rglob("*.json"))
        self.assertTrue(paths)
        for path in paths:
            with self.subTest(path=path):
                with path.open(encoding="utf-8") as handle:
                    record = json.load(handle)
                diagnostic = record.get("diagnostic_provenance")
                self.assertIsInstance(diagnostic, dict)
                self.assertIn(diagnostic.get("ai_model"), {"GPT-5.5", "GPT-5.6 Sol"})
                self.assertIn(
                    diagnostic.get("date_attribution_status"),
                    {"canonical-creation-date-aligned", "creation-date-conflict-recorded"},
                )

    def test_legacy_source_record_keys_are_rejected(self):
        def mutate(record):
            record["source_records"][0]["title"] = record["source_records"][0].pop("source_title")
            record["source_records"][0]["url"] = record["source_records"][0].pop("source_url")
            record["source_records"][0]["platform"] = record["source_records"][0].pop("source_platform")

        self.assertNotEqual(self.validate_mutated_fixture("VIGIL-2026-OBS-0001.json", mutate), 0)

    def test_record_identity_status_is_rejected(self):
        def mutate(record):
            record["record_identity"]["status"] = "open"

        self.assertNotEqual(self.validate_mutated_fixture("VIGIL-2026-OBS-0001.json", mutate), 0)

    def test_system_context_allowed_values_are_loaded_from_schema(self):
        schema_path = ROOT / "vigil" / "VIGIL.Schema.json"
        with schema_path.open(encoding="utf-8") as handle:
            schema = json.load(handle)
        schema["system_context_rules"]["allowed_platform_or_vendor_values"].append("SchemaOnlyVendor")
        schema["system_context_rules"]["allowed_product_or_service_values"].append("SchemaOnlyProduct")

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_schema = Path(temp_dir) / "VIGIL.Schema.json"
            temp_schema.write_text(json.dumps(schema), encoding="utf-8")

            def mutate(record):
                record["system_context"]["platform_or_vendor"] = "SchemaOnlyVendor"
                record["system_context"]["product_or_service"] = "SchemaOnlyProduct"

            self.assertEqual(
                self.validate_mutated_fixture("VIGIL-2026-OBS-0001.json", mutate, schema_path=temp_schema),
                0,
            )

    def test_system_context_allowed_lists_come_from_canonical_schema_contract(self):
        schema_path = ROOT / "vigil" / "VIGIL.Schema.json"
        with schema_path.open(encoding="utf-8") as handle:
            schema = json.load(handle)

        schema_platforms = schema["system_context_rules"]["allowed_platform_or_vendor_values"]
        schema_products = schema["system_context_rules"]["allowed_product_or_service_values"]

        self.assertEqual(validator.load_allowed_platform_or_vendor_values(), set(schema_platforms))
        self.assertEqual(validator.load_allowed_product_or_service_values(), set(schema_products))

    def test_xai_is_accepted_as_canonical_platform_or_vendor(self):
        def mutate(record):
            record["system_context"]["platform_or_vendor"] = "xAI"
            record["system_context"]["product_or_service"] = "Grok"

        self.assertEqual(self.validate_mutated_fixture("VIGIL-2026-OBS-0001.json", mutate), 0)

    def test_x_is_rejected_as_platform_or_vendor(self):
        def mutate(record):
            record["system_context"]["platform_or_vendor"] = "X"
            record["system_context"]["product_or_service"] = "X"

        self.assertNotEqual(self.validate_mutated_fixture("VIGIL-2026-OBS-0001.json", mutate), 0)

    def test_x_and_grok_are_accepted_as_products(self):
        for product_or_service in ("X", "Grok"):
            with self.subTest(product_or_service=product_or_service):
                def mutate(record, product_or_service=product_or_service):
                    record["system_context"]["platform_or_vendor"] = "xAI"
                    record["system_context"]["product_or_service"] = product_or_service

                self.assertEqual(self.validate_mutated_fixture("VIGIL-2026-OBS-0001.json", mutate), 0)

    def test_xai_is_rejected_as_product_or_service(self):
        def mutate(record):
            record["system_context"]["platform_or_vendor"] = "xAI"
            record["system_context"]["product_or_service"] = "xAI"

        self.assertNotEqual(self.validate_mutated_fixture("VIGIL-2026-OBS-0001.json", mutate), 0)

    def test_system_context_rejects_noncanonical_platform_or_vendor(s