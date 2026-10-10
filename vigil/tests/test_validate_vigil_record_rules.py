import copy
import importlib.util
import json
import unittest
from pathlib import Path
from unittest.mock import patch

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
            # Version-specific tests need the historical eleven-row assessment,
            # regardless of later substantive changes to the live Incident.
            (VIGIL / "tests" / "fixtures" / "VIGIL-INC-000001-HIM-1.0.1.json").read_text(encoding="utf-8")
        )

    def errors(self, mutate=lambda record: None):
        record = copy.deepcopy(self.record)
        mutate(record)
        errors, _ = VALIDATOR.validate_record(Path(f"{record['id']}.json"), record)
        return errors

    def test_valid_incident_passes(self):
        self.assertEqual(self.errors(), [])
        live = json.loads(
            (VIGIL / "records" / "incidents" / "VIGIL-INC-000001.json").read_text(encoding="utf-8")
        )
        errors, _ = VALIDATOR.validate_record(Path(live["id"] + ".json"), live)
        self.assertEqual(errors, [])

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

    def test_insufficient_evidence_is_not_s1(self):
        record = json.loads(
            (VIGIL / "records" / "incidents" / "VIGIL-INC-000028.json").read_text(encoding="utf-8")
        )
        assessment = record["harm_impact_assessment"]
        assessment["overall_severity"] = "S1"
        assessment["no_materialised_harm_basis"] = "Unsupported synthetic test basis."
        assessment.pop("assessment_gap")
        errors, _ = VALIDATOR.validate_record(Path(record["id"] + ".json"), record)
        self.assertTrue(any("cannot contain insufficient-evidence" in error for error in errors), errors)

    def test_bounded_no_materialised_harm_s1_requires_basis_and_no_controller(self):
        record = json.loads(
            (VIGIL / "records" / "incidents" / "VIGIL-INC-000123.json").read_text(encoding="utf-8")
        )
        errors, _ = VALIDATOR.validate_record(Path(record["id"] + ".json"), record)
        self.assertEqual(errors, [])
        record["harm_impact_assessment"].pop("no_materialised_harm_basis")
        errors, _ = VALIDATOR.validate_record(Path(record["id"] + ".json"), record)
        self.assertTrue(any("requires a concrete no_materialised_harm_basis" in error for error in errors), errors)

    def him_110_record(self, generic=False):
        record = copy.deepcopy(self.record)
        assessment = record["harm_impact_assessment"]
        matrix = VALIDATOR.harm_matrix("1.1.0")
        by_id = {d["dimension_id"]: d for d in matrix["dimensions"]}
        assessment["methodology_version"] = "1.1.0"
        assessment["derivation_rule"] = matrix["derivation_rule"]
        assessment["assessment_pathway"] = "generic_deployed_evaluation" if generic else "specific_consequence"
        assessment["dimensions"].append({
            "dimension_id": "relational-integrity-autonomy",
            "assessment_status": "unreported",
            "assessment_basis": "No source-supported relational-autonomy consequence was established.",
            "evidence_confidence": "not-assessed",
        })
        for row in assessment["dimensions"]:
            if row["assessment_status"] == "assessed":
                row["threshold_id"] = by_id[row["dimension_id"]]["thresholds"][row["severity"]]["threshold_id"]
        return record

    def test_him_110_inline_quantification_and_twelve_dimensions(self):
        matrix = VALIDATOR.harm_matrix("1.1.0")
        self.assertEqual(len(matrix["dimensions"]), 12)
        self.assertEqual(len({d["dimension_id"] for d in matrix["dimensions"]}), 12)
        for dimension in matrix["dimensions"]:
            self.assertEqual(set(dimension["thresholds"]), {"S1", "S2", "S3", "S4", "S5"})
            for band in dimension["thresholds"].values():
                self.assertTrue(band["criterion"].strip())
                self.assertNotIn("threshold_quantitative_guidance", band)
        psych = next(d for d in matrix["dimensions"] if d["dimension_id"] == "psychological-wellbeing")
        self.assertIn("baseline", psych["thresholds"]["S4"]["criterion"])
        self.assertIn("support", psych["thresholds"]["S1"]["criterion"])
        self.assertIn("referral", psych["thresholds"]["S2"]["criterion"])
        self.assertIn("reinforcement", psych["thresholds"]["S3"]["criterion"])
        self.assertIn("contribution", psych["thresholds"]["S5"]["criterion"])
        self.assertIn("pre-interaction psychological baseline is not required", matrix["adjudication_guidance"]["psychological_attribution"])
        self.assertNotIn("baseline_course_and_competing_contributors", psych["quantitative_indicators"])
        self.assertIn("governance", matrix["adjudication_guidance"]["psychological_attribution"])

    def test_him_110_specific_harm_preserves_historical_record(self):
        record = self.him_110_record()
        errors = []
        VALIDATOR.validate_harm_impact(Path(record["id"] + ".json"), record, errors)
        self.assertEqual(errors, [])
        # The original eleven-row 1.0.1 record remains unchanged and valid.
        self.assertEqual(self.errors(), [])

    def test_him_110_pathway_and_dimension_required(self):
        record = self.him_110_record()
        assessment = record["harm_impact_assessment"]
        assessment.pop("assessment_pathway")
        errors = []
        VALIDATOR.validate_harm_impact(Path("synthetic.json"), record, errors)
        self.assertTrue(any("requires assessment_pathway" in error for error in errors), errors)
        assessment["assessment_pathway"] = "specific_consequence"
        assessment["dimensions"] = assessment["dimensions"][:-1]
        errors = []
        VALIDATOR.validate_harm_impact(Path("synthetic.json"), record, errors)
        self.assertTrue(any("every canonical dimension exactly once" in error for error in errors), errors)

    def test_him_110_generic_population_gate_and_provenance(self):
        record = self.him_110_record(generic=True)
        assessment = record["harm_impact_assessment"]
        for row in assessment["dimensions"]:
            row["assessment_status"] = "unreported"
            row["assessment_basis"] = "Generic cohort case does not establish a separate domain outcome."
            row["evidence_confidence"] = "not-assessed"
            for field in ("severity", "threshold_id", "observed_values", "evidence_refs"):
                row.pop(field, None)
        psych = next(row for row in assessment["dimensions"] if row["dimension_id"] == "psychological-wellbeing")
        psych.update({
            "assessment_status": "assessed",
            "severity": "S2",
            "threshold_id": "VIGIL-HIM-1.1.0-PSY-S2",
            "assessment_basis": "Synthetic positive test: reproduced live safety-relevant failure with bounded modelled minor consequence.",
            "evidence_confidence": "medium",
            "observed_values": [],
            "evidence_refs": ["source_records[0]"],
            "aggregate_harm_evidence": {
                "tested_deployed_model_and_version": "Synthetic deployed model v1",
                "tested_product_surface": "Synthetic production chat feature",
                "evaluation_and_deployment_window": "2026-10-10",
                "demonstrated_failure_and_consequence_pathway": "Synthetic reproducible unsafe response and grounded minor harm model",
                "eligible_denominator_count": 100000,
                "eligible_denominator_unit": "relevant active users",
                "denominator_time_window": "2026-10-01 to 2026-10-10",
                "denominator_source_refs": ["source_records[0]"],
                "limitations_and_uncertainty": "Synthetic fixture, not a real published impact estimate",
            },
        })
        assessment["overall_severity"] = "S2"
        assessment["controlling_dimensions"] = ["psychological-wellbeing"]
        assessment.pop("assessment_gap", None)
        assessment.pop("no_materialised_harm_basis", None)
        errors = []
        VALIDATOR.validate_harm_impact(Path("synthetic.json"), record, errors)
        self.assertEqual(errors, [])
        psych["aggregate_harm_evidence"]["eligible_denominator_count"] = 200
        errors = []
        VALIDATOR.validate_harm_impact(Path("synthetic.json"), record, errors)
        self.assertTrue(any("outside S2 gate" in error for error in errors), errors)
        psych["aggregate_harm_evidence"]["eligible_denominator_count"] = 100000
        psych["aggregate_harm_evidence"]["denominator_source_refs"] = ["source_records[999999]"]
        errors = []
        VALIDATOR.validate_harm_impact(Path("synthetic.json"), record, errors)
        self.assertTrue(any("invalid source_records[N]" in error for error in errors), errors)
        psych["aggregate_harm_evidence"]["denominator_source_refs"] = ["source_records[0]"]
        assessment["assessment_pathway"] = "specific_consequence"
        errors = []
        VALIDATOR.validate_harm_impact(Path("synthetic.json"), record, errors)
        self.assertTrue(any("permitted only for assessed 1.1.0 Aggregate Harm" in error for error in errors), errors)

    def test_financial_usd_boundaries(self):
        cases = {
            0: "S1", 9_999: "S1", 10_000: "S2", 999_999: "S2",
            1_000_000: "S3", 99_999_999: "S3", 100_000_000: "S4",
            99_999_999_999: "S4", 100_000_000_000: "S5",
        }
        for value, expected in cases.items():
            with self.subTest(value=value):
                self.assertEqual(VALIDATOR.financial_band_for_usd(value), expected)

    def test_multi_harm_and_tied_controlling_dimensions_are_valid(self):
        assessment = self.record["harm_impact_assessment"]
        assessed = [row for row in assessment["dimensions"] if row["assessment_status"] == "assessed"]
        self.assertGreaterEqual(len(assessed), 2)
        self.assertEqual(
            assessment["controlling_dimensions"],
            ["property-asset-damage", "service-operational-infrastructure"],
        )
        self.assertEqual(self.errors(), [])

    def test_small_financial_loss_does_not_control_more_severe_privacy_harm(self):
        record = json.loads(
            (VIGIL / "records" / "incidents" / "VIGIL-INC-000082.json").read_text(encoding="utf-8")
        )
        assessment = record["harm_impact_assessment"]
        self.assertEqual(assessment["overall_severity"], "S3")
        self.assertIn("privacy-confidentiality", assessment["controlling_dimensions"])
        self.assertNotIn("financial-economic", assessment["controlling_dimensions"])
        financial = next(row for row in assessment["dimensions"] if row["dimension_id"] == "financial-economic")
        self.assertEqual(financial["severity"], "S1")
        errors, _ = VALIDATOR.validate_record(Path(record["id"] + ".json"), record)
        self.assertEqual(errors, [])

    def test_cross_reference_source_cannot_support_harm_band(self):
        record = json.loads(
            (VIGIL / "records" / "incidents" / "VIGIL-INC-000127.json").read_text(encoding="utf-8")
        )
        row = next(item for item in record["harm_impact_assessment"]["dimensions"] if item["assessment_status"] == "assessed")
        row["evidence_refs"] = ["source_records[2]"]
        errors, _ = VALIDATOR.validate_record(Path(record["id"] + ".json"), record)
        self.assertTrue(any("must not cite a record-cross-reference" in error for error in errors), errors)

    def test_legacy_operational_priority_is_rejected_recursively(self):
        def mutate(record):
            record["legacy_governance_state"] = [{"preserved_analysis": {"triage": {"triage_priority": "P1"}}}]
        errors = self.errors(mutate)
        self.assertTrue(any("legacy operational priority field" in error for error in errors), errors)

    def taxonomy_fixture(self):
        return {
            "taxonomy_classification": {
                "taxonomy_version": "0.0.0",
                "classification_status": "classified",
                "classification_basis": "The protective gate rejected the test request.",
                "classification_review_provenance": {
                    "review_date": "2026-01-01", "reviewer": "Fixture reviewer",
                    "review_status": "Fixture review",
                },
                "primary_classification": {
                    "family_id": "VIGIL-FF-000001", "class_id": "VIGIL-FC-000001",
                    "classification_role": "successful-invariant",
                    "classification_basis": "The protective gate rejected the test request.",
                    "classification_confidence": "high",
                },
                "secondary_classifications": [],
            },
        }

    def taxonomy_errors(self, record):
        errors = []
        catalogue = ({"VIGIL-FF-000001": {}}, {
            "VIGIL-FC-000001": {"family_id": "VIGIL-FF-000001", "invariant_exemplars": []},
        })
        with patch.object(VALIDATOR, "taxonomy_catalogue", return_value=catalogue), \
                patch.object(VALIDATOR, "retired_taxonomy_class_successors", return_value={}):
            VALIDATOR.validate_incident_taxonomy(Path("fixture.json"), record, errors)
        return errors

    def mapped_clause_fixture(self):
        record = self.taxonomy_fixture()
        record["taxonomy_classification"]["adjudication_coverage"] = {"status": "complete"}
        record["vigil_assessment"] = {"source_clause_analysis": {"clauses": [{
            "adjudication_status": "mapped",
            "taxonomy_relationships": [{
                "class_id": "VIGIL-FC-000001",
                "relationship": "successful-invariant",
                "canonical_taxonomy_mapping": True,
                "rationale": "The protective gate rejected the test request.",
            }],
        }]}}
        self.assertEqual(self.taxonomy_errors(record), [])
        return record

    def test_successful_occurrence_role_does_not_require_exemplar_admission(self):
        record = self.taxonomy_fixture()
        self.assertEqual(self.taxonomy_errors(record), [])
        record["taxonomy_classification"]["primary_classification"]["classification_role"] = "unsupported"
        self.assertTrue(any("classification_role" in error for error in self.taxonomy_errors(record)))

    def test_adjudication_coverage_is_recomputed_from_clause_dispositions(self):
        record = self.mapped_clause_fixture()
        record["taxonomy_classification"]["adjudication_coverage"]["status"] = "partial"
        errors = self.taxonomy_errors(record)
        self.assertTrue(any("clause dispositions require 'complete'" in error for error in errors), errors)

    def test_mapped_clause_requires_canonical_relationship(self):
        record = self.mapped_clause_fixture()
        relationship = record["vigil_assessment"]["source_clause_analysis"]["clauses"][0]["taxonomy_relationships"][0]
        relationship["canonical_taxonomy_mapping"] = False
        errors = self.taxonomy_errors(record)
        self.assertTrue(any("mapped requires a canonical taxonomy relationship" in error for error in errors), errors)

    def test_unresolved_clause_requires_candidate_relationship(self):
        record = self.taxonomy_fixture()
        clause = {"adjudication_status": "unresolved", "taxonomy_relationships": []}
        record["vigil_assessment"] = {"source_clause_analysis": {"clauses": [clause]}}
        record["taxonomy_classification"]["adjudication_coverage"] = {"status": "partial"}
        errors = self.taxonomy_errors(record)
        self.assertTrue(any("unresolved requires an unresolved candidate relationship" in error for error in errors), errors)
        clause["taxonomy_relationships"] = [{
            "class_id": "VIGIL-FC-000001", "relationship": "candidate boundary",
            "canonical_taxonomy_mapping": False,
        }]
        self.assertEqual(self.taxonomy_errors(record), [])

    def test_resolved_without_mapping_rejects_canonical_relationship(self):
        record = self.mapped_clause_fixture()
        clause = record["vigil_assessment"]["source_clause_analysis"]["clauses"][0]
        clause["adjudication_status"] = "resolved-no-mapping"
        errors = self.taxonomy_errors(record)
        self.assertTrue(any("resolved-no-mapping must not contain a canonical mapping" in error for error in errors), errors)

    def test_taxonomy_gap_rejects_canonical_relationship(self):
        record = self.mapped_clause_fixture()
        clause = record["vigil_assessment"]["source_clause_analysis"]["clauses"][0]
        clause["adjudication_status"] = "taxonomy-gap"
        record["taxonomy_classification"]["adjudication_coverage"]["status"] = "partial"
        errors = self.taxonomy_errors(record)
        self.assertTrue(any("taxonomy-gap must not contain a canonical mapping" in error for error in errors), errors)

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

    def test_empty_external_assessments_is_valid(self):
        self.assertEqual(self.errors(lambda record: record.update(external_assessments=[])), [])

    def test_invalid_external_assessment_type_is_rejected(self):
        def mutate(record):
            record["external_assessments"] = [{
                "assessment_id": "VIGIL-EXTASSESS-999991",
                "assessor": "Example evaluator",
                "assessment_title": "Example analysis",
                "assessment_date": "2026-09-19",
                "assessment_url": "https://example.invalid/assessment",
                "assessment_type": "news-opinion",
                "relationship_to_incident": "same-occurrence",
                "assessment_summary": "The evaluator reaches a bounded analytical conclusion.",
                "reviewed_on": "2026-09-19",
            }]
        errors = self.errors(mutate)
        self.assertTrue(any("assessment_type is not canonical" in error for error in errors), errors)

    def test_bad_external_assessment_source_ref_is_rejected(self):
        def mutate(record):
            record["external_assessments"] = [{
                "assessment_id": "VIGIL-EXTASSESS-999992",
                "assessor": "Example evaluator",
                "assessment_title": "Example analysis",
                "assessment_date": "2026-09-19",
                "assessment_url": "https://example.invalid/assessment",
                "assessment_type": "technical-analysis",
                "relationship_to_incident": "same-occurrence",
                "assessment_summary": "The evaluator reaches a bounded analytical conclusion.",
                "source_record_refs": ["source_records[999]"],
                "reviewed_on": "2026-09-19",
            }]
        errors = self.errors(mutate)
        self.assertTrue(any("points outside source_records" in error for error in errors), errors)

    def test_duplicate_external_assessment_id_is_rejected(self):
        assessment = {
            "assessment_id": "VIGIL-EXTASSESS-999993",
            "assessor": "Example evaluator",
            "assessment_title": "Example analysis",
            "assessment_date": "2026-09-19",
            "assessment_url": "https://example.invalid/assessment",
            "assessment_type": "independent-evaluation",
            "relationship_to_incident": "same-occurrence",
            "assessment_summary": "The evaluator reaches a bounded analytical conclusion.",
            "reviewed_on": "2026-09-19",
        }
        errors = self.errors(lambda record: record.update(external_assessments=[assessment, assessment.copy()]))
        self.assertTrue(any("unique within the Incident" in error for error in errors), errors)

    def test_external_assessment_does_not_become_harm_evidence(self):
        record = copy.deepcopy(self.record)
        record["external_assessments"] = [{
            "assessment_id": "VIGIL-EXTASSESS-999994",
            "assessor": "Example evaluator",
            "assessment_title": "Example analysis",
            "assessment_date": "2026-09-19",
            "assessment_url": "https://example.invalid/assessment",
            "assessment_type": "technical-analysis",
            "relationship_to_incident": "same-occurrence",
            "assessment_summary": "The evaluator reaches a bounded analytical conclusion.",
            "reviewed_on": "2026-09-19",
        }]
        harm_before = copy.deepcopy(record["harm_impact_assessment"])
        taxonomy_before = copy.deepcopy(record["taxonomy_classification"])
        errors, _ = VALIDATOR.validate_record(Path(record["id"] + ".json"), record)
        self.assertEqual(errors, [])
        self.assertEqual(record["harm_impact_assessment"], harm_before)
        self.assertEqual(record["taxonomy_classification"], taxonomy_before)
    def test_harm_matrix_preserves_digital_asset_effective_destruction_note(self):
        matrix = json.loads(
            (VIGIL / "methodologies" / "VIGIL.HarmImpactMatrix.v1.0.1.json").read_text(encoding="utf-8")
        )
        property_dimension = next(
            item for item in matrix["dimensions"]
            if item["dimension_id"] == "property-asset-damage"
        )
        note = property_dimension.get("adaptation_note", "")
        self.assertIn("must be wiped and rebuilt", note)
        self.assertIn("known-clean state", note)
        self.assertIn("does not establish S5", note)

    def test_inc003_s5_asset_rebuild_regression(self):
        record = json.loads(
            (VIGIL / "records" / "incidents" / "VIGIL-INC-000003.json").read_text(encoding="utf-8")
        )
        assessment = record["harm_impact_assessment"]
        self.assertEqual(assessment["overall_severity"], "S5")
        self.assertEqual(assessment["controlling_dimensions"], ["property-asset-damage"])
        property_row = next(
            item for item in assessment["dimensions"]
            if item["dimension_id"] == "property-asset-damage"
        )
        self.assertEqual(property_row["assessment_status"], "assessed")
        self.assertEqual(property_row["severity"], "S5")
        self.assertEqual(property_row["threshold_id"], "VIGIL-HIM-1.0.1-PAD-S5")
        self.assertTrue(property_row["evidence_refs"])
        self.assertIn("wiped and rebuilt", property_row["assessment_basis"].lower())

    def test_taxonomy_mapping_must_resolve_and_match_family(self):
        record = json.loads(
            (VIGIL / "records" / "incidents" / "VIGIL-INC-000003.json").read_text(encoding="utf-8")
        )
        record["taxonomy_classification"]["primary_classification"]["family_id"] = "VIGIL-FF-0002"
        errors, _ = VALIDATOR.validate_record(Path(record["id"] + ".json"), record)
        self.assertTrue(any("does not belong" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
