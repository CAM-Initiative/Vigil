#!/usr/bin/env python3
"""Regression tests for the canonical external governance requirements corpus."""

from __future__ import annotations

import copy
import importlib.util
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "scripts"))
import external_requirements_io as REQUIREMENTS_IO  # noqa: E402

SCRIPT = ROOT / "scripts" / "manage-external-requirements.py"
SPEC = importlib.util.spec_from_file_location("external_requirements", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)


class ExternalRequirementsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.registry_entries = MODULE.load_json(MODULE.REGISTRY_PATH)["entries"]
        cls.scope_entries = MODULE.load_json(MODULE.SCOPE_PATH)["entries"]
        cls.requirements = MODULE.load_requirements_document()["requirements"]
        cls.coverage = MODULE.load_json(MODULE.COVERAGE_PATH)["manifests"]

    def validate_requirements(self, requirements=None, scope_entries=None):
        requirements = copy.deepcopy(self.requirements if requirements is None else requirements)
        scopes = copy.deepcopy(self.scope_entries if scope_entries is None else scope_entries)
        registry = {MODULE.source_key(item): item for item in self.registry_entries}
        errors = []
        scope = MODULE.validate_scope(registry, scopes, errors)
        reviews = MODULE.load_assurance(registry, requirements, errors)
        MODULE.validate_requirements(requirements, registry, scope, reviews, errors)
        return errors

    def test_current_corpus_and_generated_outputs_validate(self):
        outputs, errors = MODULE.load_and_validate()
        self.assertEqual(errors, [])
        for path, expected in outputs.items():
            self.assertTrue(path.exists(), path)
            self.assertEqual(path.read_text(encoding="utf-8"), expected, path)

    def test_source_version_shards_are_canonical_and_deterministic(self):
        paths = REQUIREMENTS_IO.iter_shard_paths()
        self.assertEqual(len(paths), 18)
        self.assertEqual(
            [record["requirement_id"] for record in self.requirements],
            sorted(record["requirement_id"] for record in self.requirements),
        )
        for path in paths:
            records = REQUIREMENTS_IO.load_json(path)
            self.assertTrue(records, path)
            self.assertEqual(
                [record["requirement_id"] for record in records],
                sorted(record["requirement_id"] for record in records),
                path,
            )
            self.assertTrue(all(
                record["external_source_id"] == path.parent.name
                and record["source_version"] == path.stem
                for record in records
            ), path)

    def test_generated_aggregate_is_exact_projection_of_shards(self):
        self.assertTrue(REQUIREMENTS_IO.aggregate_is_current())
        aggregate = REQUIREMENTS_IO.load_json(REQUIREMENTS_IO.REQUIREMENTS_AGGREGATE_PATH)
        self.assertEqual(aggregate, REQUIREMENTS_IO.load_requirements_document())
        self.assertEqual(aggregate["requirement_count"], len(self.requirements))

    def test_shard_loader_rejects_corpus_wide_duplicate_ids(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "requirements"
            manifest = root / "manifest.json"
            manifest.parent.mkdir(parents=True)
            manifest.write_text(REQUIREMENTS_IO.json_text({
                "schema_version": "1.2",
                "updated_at": "2026-08-28",
                "authorship_provenance": {},
            }), encoding="utf-8")
            requirement_id = "EXTREQ-0000000000000000"
            for source_id in ("SOURCE-A", "SOURCE-B"):
                path = root / source_id / "1.0.json"
                path.parent.mkdir(parents=True)
                path.write_text(REQUIREMENTS_IO.json_text([{
                    "requirement_id": requirement_id,
                    "external_source_id": source_id,
                    "source_version": "1.0",
                }]), encoding="utf-8")
            with (
                mock.patch.object(REQUIREMENTS_IO, "REQUIREMENTS_ROOT", root),
                mock.patch.object(REQUIREMENTS_IO, "REQUIREMENTS_MANIFEST_PATH", manifest),
            ):
                with self.assertRaisesRegex(ValueError, "duplicate requirement_id"):
                    REQUIREMENTS_IO.load_requirements()

    def test_requirement_identity_survives_editorial_summary_change(self):
        item = self.requirements[0]
        before = MODULE.requirement_id(item["vigil_source_id"], item["source_version"], item["clause_or_control"], item["identity_key"])
        edited = copy.deepcopy(item)
        edited["requirement_summary"] = "Editorially improved analytical summary."
        after = MODULE.requirement_id(edited["vigil_source_id"], edited["source_version"], edited["clause_or_control"], edited["identity_key"])
        self.assertEqual(before, after)

    def test_priority_ieee_sources_retain_substantive_direct_extractions(self):
        counts = Counter(r["external_source_id"] for r in self.requirements)
        minimums = {
            "IEEE-7000": 50,
            "IEEE-7001": 30,
            "IEEE-7007": 10,
            "IEEE-7009": 50,
            "IEEE-7010": 18,
            "IEEE-7014": 40,
            "IEEE-7014.1": 60,
        }
        for source_id, minimum in minimums.items():
            self.assertGreaterEqual(counts[source_id], minimum, source_id)

    def test_recommended_practices_are_not_inflated_to_mandatory(self):
        for record in self.requirements:
            if record["external_source_id"] in {"IEEE-7010", "IEEE-7014.1"}:
                self.assertEqual(record["requirement_posture"], "recommended-practice")

    def test_ontology_is_not_converted_into_operational_duties(self):
        records = [r for r in self.requirements if r["external_source_id"] == "IEEE-7007"]
        self.assertTrue(records)
        self.assertTrue(all(r["requirement_posture"] == "definitional" for r in records))
        self.assertTrue(all(r["expectation_type"] == "definition" for r in records))

    def test_access_blocked_source_has_no_reconstructed_requirements(self):
        self.assertFalse(any(r["external_source_id"] == "IEEE-2863" for r in self.requirements))

    def test_supporting_sources_remain_outside_exhaustive_decomposition(self):
        supporting = {"IEEE-2089", "IEEE-7002", "IEEE-7005", "IEEE-7012"}
        self.assertFalse(any(r["external_source_id"] in supporting for r in self.requirements))

    def test_annex_a3_stable_records_are_not_duplicated(self):
        records = [
            r for r in self.requirements
            if r["external_source_id"] == "IEEE-7009"
            and r["clause_or_control"].startswith("Annex A.3 / 7009-ASR-")
        ]
        self.assertEqual(len(records), 16)
        self.assertEqual(len({r["requirement_id"] for r in records}), 16)

    def test_interpretation_provenance_does_not_inflate_human_review(self):
        for record in self.requirements:
            provenance = record["interpretation_provenance"]
            self.assertEqual(provenance["content_origin"], "ai-authored")
            self.assertEqual(provenance["generated_by"], "ai")
            self.assertEqual(provenance["generation_mode"], "semi-autonomous")
            self.assertEqual(provenance["human_role"], "contract-approver")
            self.assertFalse(provenance["human_authorship"])
            self.assertEqual(provenance["human_review_status"], "not-reviewed")
            self.assertEqual(provenance["human_verification_status"], "not-verified")

    def test_source_metadata_and_reviewed_source_digest_are_separate(self):
        sources = {(x["vigil_source_id"], x["source_version"]): x for x in self.registry_entries}
        for record in self.requirements:
            provenance = record["interpretation_provenance"]
            source = sources[(record["vigil_source_id"], record["source_version"])]
            self.assertEqual(provenance["source_metadata_fingerprint"], source["source_metadata_fingerprint"])
            self.assertIn(provenance["reviewed_source_digest_status"], {"recorded", "not-recorded", "not-applicable"})
            if provenance["reviewed_source_digest_status"] == "recorded":
                self.assertEqual(provenance["reviewed_source_digest_algorithm"], "sha256")
                self.assertRegex(provenance["reviewed_source_digest"], r"^[a-f0-9]{64}$")
            else:
                self.assertIsNone(provenance["reviewed_source_digest"])
                self.assertIsNone(provenance["reviewed_source_digest_algorithm"])

    def test_external_semantics_do_not_create_cam_findings(self):
        allowed_force = MODULE.NORMATIVE_FORCE
        allowed_relationship = MODULE.ALIGNMENT_RELATIONSHIP
        forbidden = MODULE.FORBIDDEN_INTERNAL_FIELDS
        for record in self.requirements:
            self.assertIn(record["normative_force"], allowed_force)
            self.assertIn(record["alignment_relationship"], allowed_relationship)
            self.assertFalse(forbidden.intersection(record))

    def test_coverage_manifest_uses_bounded_complete_and_separates_retrieval(self):
        complete = [item for item in self.coverage if item["analysis_state"] == "complete"]
        self.assertTrue(complete)
        self.assertTrue(all(item["coverage_state"] == "bounded-complete" for item in complete))
        ieee7003 = next(item for item in self.coverage if item["external_source_id"] == "IEEE-7003")
        self.assertEqual(ieee7003["represented_requirement_count"], 0)
        self.assertNotEqual(ieee7003["source_retrieval_state"], "retrieved")

    def test_generated_coverage_preserves_current_review_model_and_clock(self):
        for item in self.coverage:
            provenance = item["substantive_review_provenance"]
            self.assertEqual(provenance["canonical_source"], "vigil/external_sources/source-registry.json")
            self.assertEqual(provenance["review_system"], {
                "provider": "OpenAI", "platform": "ChatGPT", "model": "GPT-5.6 Sol"
            })
            self.assertEqual(provenance["review_date"], "2026-08-24")
            self.assertEqual(provenance["next_substantive_review"], "2026-11-22")

    def test_recorded_source_digest_does_not_invent_human_assurance(self):
        overlay = MODULE.load_json(MODULE.REVIEW_ASSURANCE_PATH)
        nist_gai = next(
            review for review in overlay["source_reviews"]
            if review["external_source_id"] == "NIST-AI-600-1"
        )
        self.assertEqual(nist_gai["reviewed_source_digest"]["algorithm"], "sha256")
        self.assertEqual(nist_gai["assurance_provenance"], [])
        self.assertTrue(all(record["assurance_provenance"] == [] for record in self.requirements))
        self.assertTrue(all(
            item["substantive_review_provenance"]["human_review_status"] == "not-reviewed"
            and item["substantive_review_provenance"]["human_verification_status"] == "not-verified"
            for item in self.coverage
        ))

    def test_metadata_only_source_cannot_claim_direct_review(self):
        requirements = copy.deepcopy(self.requirements)
        scopes = copy.deepcopy(self.scope_entries)
        target = requirements[0]
        for entry in scopes:
            if MODULE.source_key(entry) == MODULE.source_key(target):
                entry["source_access_status"] = "official-metadata-only"
                entry["extraction_status"] = "blocked-access"
                entry["inaccessible_sections"] = ["Normative text"]
                entry["maintainer_action_required"] = True
                entry["maintainer_action"] = "Obtain primary-source access."
        target["source_access_status"] = "official-metadata-only"
        target["interpretation_provenance"]["basis"] = "official-metadata-only"
        errors = self.validate_requirements(requirements, scopes)
        self.assertTrue(any("direct review claim conflicts" in error for error in errors), errors)
        self.assertTrue(any("requirement cannot be established" in error for error in errors), errors)

    def test_complete_primary_source_cannot_be_omitted(self):
        complete = next(entry for entry in self.scope_entries if entry["source_role"] == "primary-ai-governance" and entry["extraction_status"] == "complete")
        requirements = [item for item in self.requirements if MODULE.source_key(item) != MODULE.source_key(complete)]
        errors = self.validate_requirements(requirements)
        self.assertTrue(any("claims complete extraction but has no requirements" in error for error in errors), errors)

    def test_transitional_architecture_is_not_operational(self):
        obsolete = [
            ROOT / "external_sources" / "effective-ledger.json",
            ROOT / "external_sources" / "ledger.json",
            ROOT / "external_sources" / "EFFECTIVE-GOVERNANCE-SOURCES.md",
            ROOT / "external_sources" / "EXTERNAL-GOVERNANCE-SOURCES.md",
            ROOT / "external_requirements" / "effective-requirements.json",
            ROOT / "external_requirements" / "effective-external-requirement.schema.json",
            ROOT / "external_requirements" / "extension-transitions.json",
            ROOT / "external_requirements" / "extensions",
            ROOT / "scripts" / "manage-external-requirements-effective.py",
            ROOT / "scripts" / "manage-external-requirements-extended.py",
        ]
        for path in obsolete:
            self.assertFalse(path.exists(), path)


if __name__ == "__main__":
    unittest.main()
