#!/usr/bin/env python3
"""Regression tests for VIGIL-native Failure Mode taxonomy classification."""

from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
VALIDATOR_PATH = VIGIL / "scripts" / "validate-vigil-records.py"
OPENAI_REPORT_URL = "https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf"
OPENAI_SUMMARY_URL = "https://openai.com/index/hugging-face-incident-and-the-road-ahead/"
METR_REPORT_URL = "https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/"
spec = importlib.util.spec_from_file_location("validate_vigil_records_taxonomy", VALIDATOR_PATH)
validator = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(validator)


class TaxonomyClassificationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = []
        for path in sorted((VIGIL / "records" / "failures" / "2026").glob("*.json")):
            cls.records.append(json.loads(path.read_text(encoding="utf-8")))
        cls.incidents = [
            json.loads(path.read_text(encoding="utf-8"))
            for path in sorted((VIGIL / "records" / "incidents").glob("*.json"))
        ]
        cls.failures_index = json.loads((VIGIL / "VIGIL.Failures.Index.json").read_text(encoding="utf-8"))
        cls.registry_index = json.loads((VIGIL / "VIGIL.Registry.Index.json").read_text(encoding="utf-8"))

    def test_every_canonical_failure_has_explicit_outcome(self):
        self.assertEqual(len(self.records), 74)
        allowed = {"classified", "family-only", "candidate-new-class", "unmapped", "deferred"}
        self.assertTrue(all(r["taxonomy_classification"]["classification_status"] in allowed for r in self.records))

    def test_classified_ids_and_labels_resolve_canonically(self):
        families, classes = validator.taxonomy_catalogue()
        for record in self.records:
            block = record["taxonomy_classification"]
            errors = []
            validator.validate_taxonomy_classification(Path(record["id"]), record, errors)
            self.assertEqual(errors, [], record["id"])
            if block["classification_status"] == "classified":
                self.assertIn("primary_family", block, record["id"])
                self.assertIn("primary_class", block, record["id"])
                family = block["primary_family"]
                klass = block["primary_class"]
                self.assertEqual(classes[klass["class_id"]]["family_id"], family["family_id"])
                self.assertEqual(families[family["family_id"]]["name"], family["family_name"])

    def test_secondary_classifications_are_optional_and_zero_is_valid(self):
        legacy = copy.deepcopy(next(r for r in self.records if r["id"] == "VIGIL-2026-FM-0068"))
        self.assertNotIn("secondary_classifications", legacy["taxonomy_classification"])
        errors = []
        validator.validate_taxonomy_classification(Path("legacy.json"), legacy, errors)
        self.assertEqual(errors, [])
        legacy["taxonomy_classification"]["secondary_classifications"] = []
        errors = []
        validator.validate_taxonomy_classification(Path("zero.json"), legacy, errors)
        self.assertEqual(errors, [])

    def test_secondary_ids_must_resolve_and_match_family(self):
        record = copy.deepcopy(next(r for r in self.records if r["id"] == "VIGIL-2026-FM-0062"))
        secondary = record["taxonomy_classification"]["secondary_classifications"][0]
        secondary["class"]["class_id"] = "VIGIL-FC-999999"
        errors = []
        validator.validate_taxonomy_classification(Path("unknown.json"), record, errors)
        self.assertTrue(any("class ID does not resolve" in error for error in errors), errors)

        record = copy.deepcopy(next(r for r in self.records if r["id"] == "VIGIL-2026-FM-0062"))
        record["taxonomy_classification"]["secondary_classifications"][0]["family"] = {
            "family_id": "VIGIL-FF-0002",
            "family_code": "PROVENANCE_LINEAGE",
            "family_name": "Provenance & Lineage Integrity Failures",
        }
        errors = []
        validator.validate_taxonomy_classification(Path("mismatch.json"), record, errors)
        self.assertTrue(any("does not belong" in error for error in errors), errors)

    def test_primary_class_cannot_be_repeated_as_secondary(self):
        record = copy.deepcopy(next(r for r in self.records if r["id"] == "VIGIL-2026-FM-0062"))
        block = record["taxonomy_classification"]
        secondary = block["secondary_classifications"][0]
        secondary["family"] = copy.deepcopy(block["primary_family"])
        secondary["class"] = copy.deepcopy(block["primary_class"])
        errors = []
        validator.validate_taxonomy_classification(Path("duplicate-primary.json"), record, errors)
        self.assertTrue(any("duplicates the primary class" in error for error in errors), errors)

    def test_duplicate_secondary_class_is_rejected(self):
        record = copy.deepcopy(next(r for r in self.records if r["id"] == "VIGIL-2026-FM-0062"))
        block = record["taxonomy_classification"]
        block["secondary_classifications"].append(copy.deepcopy(block["secondary_classifications"][0]))
        errors = []
        validator.validate_taxonomy_classification(Path("duplicate-secondary.json"), record, errors)
        self.assertTrue(any("duplicates a secondary class" in error for error in errors), errors)

    def test_retired_subtype_cannot_duplicate_canonical_parent(self):
        record = copy.deepcopy(next(r for r in self.records if r["id"] == "VIGIL-2026-FM-0036"))
        block = record["taxonomy_classification"]
        block["secondary_classifications"] = [{
            "family": copy.deepcopy(block["primary_family"]),
            "class": {
                "class_id": "VIGIL-FC-000008",
                "class_code": "DELEGATION_SCOPE_EXPANSION",
                "class_name": "Delegation Scope Expansion",
                "abstraction": "variant",
            },
            "classification_basis": "Invalid duplicate-subtype regression fixture.",
            "classification_confidence": block["classification_confidence"],
        }]
        errors = []
        validator.validate_taxonomy_classification(Path("retired-subtype.json"), record, errors)
        self.assertTrue(any("uses retired subtype VIGIL-FC-000008" in error for error in errors), errors)
        self.assertTrue(any("duplicates one mechanism" in error for error in errors), errors)

    def test_secondary_cannot_replace_primary(self):
        record = copy.deepcopy(next(r for r in self.records if r["id"] == "VIGIL-2026-FM-0062"))
        block = record["taxonomy_classification"]
        block["classification_status"] = "unmapped"
        del block["primary_family"]
        del block["primary_class"]
        errors = []
        validator.validate_taxonomy_classification(Path("replacement.json"), record, errors)
        self.assertTrue(any("cannot replace a missing primary" in error for error in errors), errors)

    def test_non_exact_outcomes_do_not_invent_class_ids(self):
        for record in self.records:
            block = record["taxonomy_classification"]
            if block["classification_status"] != "classified":
                self.assertNotIn("primary_class", block, record["id"])
        for record in self.records:
            candidate = record["taxonomy_classification"].get("candidate_class")
            if candidate:
                self.assertNotIn("class_id", candidate)

    def test_native_unwarranted_activation_evidence_is_reconciled(self):
        expected = {
            "VIGIL-2026-FM-0019": "high",
            "VIGIL-2026-FM-0020": "medium",
            "VIGIL-2026-FM-0048": "high",
        }
        for record_id, confidence in expected.items():
            record = next(r for r in self.records if r["id"] == record_id)
            block = record["taxonomy_classification"]
            self.assertEqual(block["classification_status"], "classified")
            self.assertEqual(block["primary_family"]["family_id"], "VIGIL-FF-0008")
            self.assertEqual(block["primary_class"]["class_id"], "VIGIL-FC-000043")
            self.assertEqual(block["primary_class"]["abstraction"], "class")
            self.assertEqual(block["classification_confidence"], confidence)
            self.assertNotIn("candidate_class", block)

    def test_classification_ledger_class_ids_resolve(self):
        _, classes = validator.taxonomy_catalogue()
        retired = validator.retired_taxonomy_class_successors()
        ledger = json.loads(
            (
                VIGIL
                / "docs"
                / "audits"
                / "taxonomy"
                / "migration"
                / "VIGIL.FailureMode.TaxonomyClassificationLedger.json"
            ).read_text(encoding="utf-8")
        )
        for entry in ledger["entries"]:
            if entry["class_id"]:
                self.assertTrue(
                    entry["class_id"] in classes or entry["class_id"] in retired,
                    entry["failure_mode_id"],
                )

    def test_evidence_accessibility_family_only_records_are_reconciled(self):
        expected = {
            "VIGIL-2026-FM-0033": "VIGIL-FC-000044",
            "VIGIL-2026-FM-0055": "VIGIL-FC-000045",
        }
        for record_id, class_id in expected.items():
            record = next(r for r in self.records if r["id"] == record_id)
            block = record["taxonomy_classification"]
            self.assertEqual(block["classification_status"], "classified")
            self.assertEqual(block["primary_family"]["family_id"], "VIGIL-FF-0004")
            self.assertEqual(block["primary_class"]["class_id"], class_id)
            self.assertEqual(block["classification_confidence"], "medium")

    def test_positive_control_fm_0068(self):
        record = next(r for r in self.records if r["id"] == "VIGIL-2026-FM-0068")
        block = record["taxonomy_classification"]
        self.assertEqual(block["primary_family"]["family_id"], "VIGIL-FF-0001")
        self.assertEqual(block["primary_class"]["class_id"], "VIGIL-FC-000005")

    def test_retired_taxonomy_fields_remain_rejected_and_absent(self):
        retired = validator.RETIRED_FM_TAXONOMY_FIELDS
        for record in self.records:
            self.assertFalse(retired.intersection(record["failure_classification"]), record["id"])
            self.assertNotIn("related_failure_modes", record["linked_records"])

    def test_invalid_family_class_pair_is_rejected(self):
        record = copy.deepcopy(next(r for r in self.records if r["id"] == "VIGIL-2026-FM-0068"))
        record["taxonomy_classification"]["primary_family"] = {
            "family_id": "VIGIL-FF-0002", "family_code": "PROVENANCE_LINEAGE",
            "family_name": "Provenance & Lineage Integrity Failures",
        }
        errors = []
        validator.validate_taxonomy_classification(Path("test.json"), record, errors)
        self.assertTrue(any("does not belong" in error for error in errors), errors)

    def test_generated_summaries_match_canonical_records(self):
        canonical = {r["id"]: r["taxonomy_classification"] for r in self.records}
        for index in (self.failures_index, self.registry_index):
            for entry in index["records"]:
                if entry.get("record_type") != "failure_mode":
                    continue
                block = canonical[entry["id"]]
                family = block.get("primary_family", {})
                klass = block.get("primary_class", {})
                expected = {
                    "taxonomy_version": block["taxonomy_version"],
                    "classification_status": block["classification_status"],
                    "family_id": family.get("family_id", ""), "family_name": family.get("family_name", ""),
                    "class_id": klass.get("class_id", ""), "class_name": klass.get("class_name", ""),
                    "abstraction": klass.get("abstraction", ""),
                }
                secondary_summaries = []
                for secondary in block.get("secondary_classifications", []):
                    secondary_summaries.append({
                        "family_id": secondary["family"]["family_id"],
                        "family_name": secondary["family"]["family_name"],
                        "class_id": secondary["class"]["class_id"],
                        "class_name": secondary["class"]["class_name"],
                        "abstraction": secondary["class"]["abstraction"],
                    })
                if secondary_summaries:
                    expected["secondary_classifications"] = secondary_summaries
                self.assertEqual(entry["taxonomy_classification_summary"], {k: v for k, v in expected.items() if v})

    def test_reverse_mapping_contains_only_canonical_classifications(self):
        projection = json.loads((VIGIL / "taxonomy" / "generated" / "VIGIL.FailureTaxonomy.CaseFileExamples.json").read_text(encoding="utf-8"))
        projected = {
            item["incident_id"]
            for rows in projection["classes"].values()
            for item in rows
            if item["classification_role"] == "primary"
        }
        exact = {
            record["id"]
            for record in self.incidents
            if record["taxonomy_classification"]["classification_status"]
            in {"classified", "provisionally-classified"}
            and record["taxonomy_classification"].get("primary_classification")
        }
        self.assertEqual(projected, exact)

    def test_generated_examples_preserve_primary_secondary_distinction(self):
        projection = json.loads((VIGIL / "taxonomy" / "generated" / "VIGIL.FailureTaxonomy.CaseFileExamples.json").read_text(encoding="utf-8"))
        primary = next(item for item in projection["classes"]["VIGIL-FC-000002"] if item["incident_id"] == "VIGIL-INC-000003")
        secondary = next(item for item in projection["classes"]["VIGIL-FC-000009"] if item["incident_id"] == "VIGIL-INC-000003")
        self.assertEqual(primary["classification_role"], "primary")
        self.assertEqual(secondary["classification_role"], "secondary")
        self.assertNotEqual(primary["classification_basis"], secondary["classification_basis"])

    def test_taxonomy_08_identity_authority_outcome_has_no_speculative_secondary(self):
        record = next(r for r in self.records if r["id"] == "VIGIL-2026-FM-0064")
        block = record["taxonomy_classification"]
        self.assertEqual(block["classification_status"], "classified")
        self.assertEqual(block["primary_family"]["family_id"], "VIGIL-FF-0001")
        self.assertEqual(block["primary_class"]["class_id"], "VIGIL-FC-000053")
        self.assertNotIn("secondary_classifications", block)
        review = record["interpretive_provenance"]["current_ai_review"]
        self.assertIn("does not independently establish", review["review_outcome"])

    def test_taxonomy_08_epistemic_warrant_candidate_remains_unmapped(self):
        record = next(r for r in self.records if r["id"] == "VIGIL-2026-FM-0065")
        block = record["taxonomy_classification"]
        self.assertEqual(record["record_identity"]["title"], "Untrustworthy retrieved evidence converted into authoritative synthetic fact")
        self.assertEqual(block["classification_status"], "unmapped")
        self.assertNotIn("primary_family", block)
        self.assertNotIn("primary_class", block)
        self.assertIn("candidate-epistemic-warrant-family", block["structural_review_flags"])
        self.assertIn("not a required structural condition", record["failure_mode_definition"])
        self.assertIn("Synthetic origin alone", record["failure_threshold"])

    def test_taxonomy_08_searchleak_source_fidelity_and_compound_outcome(self):
        record = next(r for r in self.records if r["id"] == "VIGIL-2026-FM-0070")
        analysis = record["source_fidelity_analysis"]
        self.assertEqual([stage["stage"] for stage in analysis["exploit_chain"]], [1, 2, 3])
        self.assertEqual(len(analysis["what_the_source_does_not_establish"]), 6)
        limitations = " ".join(analysis["what_the_source_does_not_establish"]).lower()
        self.assertIn("complete internal assurance", limitations)
        self.assertIn("live malicious exploitation", limitations)
        block = record["taxonomy_classification"]
        self.assertEqual(block["primary_class"]["class_id"], "VIGIL-FC-000001")
        self.assertEqual(
            [item["class"]["class_id"] for item in block["secondary_classifications"]],
            ["VIGIL-FC-000038", "VIGIL-FC-000009"],
        )

    def test_hf_02_transitive_authority_outcome_uses_existing_classes(self):
        record = next(r for r in self.records if r["id"] == "VIGIL-2026-FM-0072")
        block = record["taxonomy_classification"]
        self.assertEqual(block["classification_status"], "classified")
        self.assertEqual(block["primary_class"]["class_id"], "VIGIL-FC-000009")
        self.assertEqual(
            [item["class"]["class_id"] for item in block["secondary_classifications"]],
            ["VIGIL-FC-000001"],
        )
        self.assertIn("every hop", record["summary"])
        self.assertIn("material uncertainty signal", record["failure_threshold"])
        self.assertIn("genuinely authorised arbiter", record["failure_threshold"])

    def test_hf_02_preserves_neighbouring_failure_boundaries(self):
        floor = next(r for r in self.records if r["id"] == "VIGIL-2026-FM-0002")
        adversarial = next(r for r in self.records if r["id"] == "VIGIL-2026-FM-0047")
        defensive_refusal = next(r for r in self.records if r["id"] == "VIGIL-2026-FM-0048")
        human_assurance = next(r for r in self.records if r["id"] == "VIGIL-2026-FM-0059")
        self.assertEqual(floor["taxonomy_classification"]["classification_status"], "unmapped")
        self.assertEqual(adversarial["taxonomy_classification"]["primary_class"]["class_id"], "VIGIL-FC-000009")
        self.assertIn("without being overstated", adversarial["interpretive_provenance"]["current_ai_review"]["review_outcome"].lower())
        new_urls = {OPENAI_REPORT_URL, OPENAI_SUMMARY_URL, METR_REPORT_URL}
        self.assertTrue(new_urls.isdisjoint({s["source_url"] for s in defensive_refusal["source_records"]}))
        self.assertTrue(new_urls.isdisjoint({s["source_url"] for s in human_assurance["source_records"]}))

    def test_hf_02_primary_sources_and_trajectory_compound_are_preserved(self):
        authority = next(r for r in self.records if r["id"] == "VIGIL-2026-FM-0072")
        trajectory = next(r for r in self.records if r["id"] == "VIGIL-2026-FM-0071")
        required = {OPENAI_REPORT_URL, OPENAI_SUMMARY_URL, METR_REPORT_URL}
        self.assertTrue(required.issubset({s["source_url"] for s in authority["source_records"]}))
        self.assertIn(OPENAI_SUMMARY_URL, {s["source_url"] for s in trajectory["source_records"]})
        relation = next(
            item for item in trajectory["linked_records"]["contextual_relations"]
            if item["record_id"] == "VIGIL-2026-FM-0072"
        )
        self.assertEqual(relation["relationship"], "compound-authority-and-trajectory-failure")

    def test_deterministic_regeneration_is_byte_stable(self):
        targets = [
            VIGIL / "VIGIL.Failures.Index.json",
            VIGIL / "VIGIL.Registry.Index.json",
            VIGIL / "taxonomy" / "generated" / "VIGIL.FailureTaxonomy.CaseFileExamples.json",
        ]
        subprocess.run(["python", str(VIGIL / "scripts" / "build-vigil-records.py")], cwd=ROOT, check=True, capture_output=True, text=True)
        first = {path: path.read_bytes() for path in targets}
        subprocess.run(["python", str(VIGIL / "scripts" / "build-vigil-records.py")], cwd=ROOT, check=True, capture_output=True, text=True)
        self.assertEqual(first, {path: path.read_bytes() for path in targets})


if __name__ == "__main__":
    unittest.main()
