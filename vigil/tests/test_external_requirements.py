#!/usr/bin/env python3
import copy
import importlib.util
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "manage-external-requirements.py"
spec = importlib.util.spec_from_file_location("external_requirements", SCRIPT)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)


class ExternalRequirementsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger_entries = mod.load_json(mod.LEDGER_PATH)["entries"]
        cls.scope_entries = mod.load_json(mod.SCOPE_PATH)["entries"]
        cls.requirements = mod.load_json(mod.REQUIREMENTS_PATH)["requirements"]

    def validate_requirements(self, requirements=None, scope_entries=None):
        requirements = copy.deepcopy(self.requirements if requirements is None else requirements)
        scopes = copy.deepcopy(self.scope_entries if scope_entries is None else scope_entries)
        ledger = {mod.source_key(item): item for item in self.ledger_entries}
        errors = []
        scope = mod.validate_scope(ledger, scopes, errors)
        mod.validate_requirements(requirements, ledger, scope, errors)
        return errors

    def test_current_corpus_and_generated_outputs_validate(self):
        outputs, errors = mod.load_and_validate()
        self.assertEqual(errors, [])
        for path, expected in outputs.items():
            self.assertTrue(path.exists(), path)
            self.assertEqual(path.read_text(encoding="utf-8"), expected, path)

    def test_requirement_identity_survives_editorial_summary_change(self):
        item = self.requirements[0]
        before = mod.requirement_id(
            item["vigil_source_id"], item["source_version"], item["clause_or_control"], item["identity_key"]
        )
        edited = copy.deepcopy(item)
        edited["requirement_summary"] = "Editorially improved analytical summary."
        after = mod.requirement_id(
            edited["vigil_source_id"], edited["source_version"], edited["clause_or_control"], edited["identity_key"]
        )
        self.assertEqual(before, after)

    def test_same_clause_atomic_requirements_have_distinct_identities(self):
        item = next(req for req in self.requirements if req["clause_or_control"] == "Article 50(4)")
        peer = next(req for req in self.requirements if req["clause_or_control"] == "Article 50(4)" and req["identity_key"] != item["identity_key"])
        self.assertNotEqual(item["requirement_id"], peer["requirement_id"])

    def test_source_version_change_changes_requirement_identity(self):
        item = self.requirements[0]
        changed = mod.requirement_id(item["vigil_source_id"], item["source_version"] + "-revised", item["clause_or_control"], item["identity_key"])
        self.assertNotEqual(item["requirement_id"], changed)

    def test_clause_renumbering_changes_requirement_identity(self):
        item = self.requirements[0]
        changed = mod.requirement_id(item["vigil_source_id"], item["source_version"], item["clause_or_control"] + "A", item["identity_key"])
        self.assertNotEqual(item["requirement_id"], changed)

    def test_duplicate_requirement_id_fails(self):
        requirements = copy.deepcopy(self.requirements)
        requirements.append(copy.deepcopy(requirements[0]))
        errors = self.validate_requirements(requirements)
        self.assertTrue(any("duplicate requirement_id" in error for error in errors), errors)

    def test_unknown_source_version_fails(self):
        requirements = copy.deepcopy(self.requirements)
        requirements[0]["source_version"] = "unknown-version"
        errors = self.validate_requirements(requirements)
        self.assertTrue(any("references unknown source/version" in error for error in errors), errors)

    def test_missing_clause_provenance_fails(self):
        requirements = copy.deepcopy(self.requirements)
        requirements[0]["clause_or_control"] = ""
        errors = self.validate_requirements(requirements)
        self.assertTrue(any("clause_or_control is required" in error for error in errors), errors)

    def test_metadata_only_source_cannot_claim_direct_review(self):
        requirements = copy.deepcopy(self.requirements)
        scopes = copy.deepcopy(self.scope_entries)
        target = requirements[0]
        for entry in scopes:
            if mod.source_key(entry) == mod.source_key(target):
                entry["source_access_status"] = "official-metadata-only"
                entry["extraction_status"] = "blocked-access"
                entry["inaccessible_sections"] = ["Normative text"]
                entry["maintainer_action_required"] = True
                entry["maintainer_action"] = "Obtain lawful source access."
        target["source_access_status"] = "official-metadata-only"
        target["interpretation_provenance"]["basis"] = "official-metadata-only"
        errors = self.validate_requirements(requirements, scopes)
        self.assertTrue(any("direct review claim conflicts" in error for error in errors), errors)
        self.assertTrue(any("requirement cannot be established" in error for error in errors), errors)

    def test_complete_primary_source_cannot_be_omitted(self):
        complete = next(
            entry for entry in self.scope_entries
            if entry["source_role"] == "primary-ai-governance" and entry["extraction_status"] == "complete"
        )
        requirements = [item for item in self.requirements if mod.source_key(item) != mod.source_key(complete)]
        errors = self.validate_requirements(requirements)
        self.assertTrue(any("claims complete extraction but has no requirements" in error for error in errors), errors)

    def test_official_extract_cannot_claim_reviewed_interpretation(self):
        requirements = copy.deepcopy(self.requirements)
        scopes = copy.deepcopy(self.scope_entries)
        imda = next(item for item in requirements if item["external_source_id"] == "IMDA-AGENTIC-AI-MGF")
        for entry in scopes:
            if mod.source_key(entry) == mod.source_key(imda):
                entry["source_access_status"] = "official-public-extract"
                entry["extraction_status"] = "partial"
                entry["known_unreviewed_sections"] = ["Full framework"]
                entry["maintainer_action_required"] = True
                entry["maintainer_action"] = "Review the complete authoritative framework."
                entry["next_action"] = entry["maintainer_action"]
        imda["source_access_status"] = "official-public-extract"
        imda["interpretation_provenance"]["basis"] = "official-public-extract"
        imda["interpretation_status"] = "reviewed-analytical-summary"
        errors = self.validate_requirements(requirements, scopes)
        self.assertTrue(any("public-extract access requires" in error for error in errors), errors)

    def test_complete_source_cannot_retain_known_unreviewed_sections(self):
        scopes = copy.deepcopy(self.scope_entries)
        complete = next(entry for entry in scopes if entry["extraction_status"] == "complete")
        complete["known_unreviewed_sections"] = ["Unreviewed annex"]
        errors = self.validate_requirements(scope_entries=scopes)
        self.assertTrue(any("complete extraction cannot retain known unreviewed sections" in error for error in errors), errors)

    def test_nonmandatory_prohibition_fails(self):
        requirements = copy.deepcopy(self.requirements)
        target = next(item for item in requirements if item["expectation_type"] == "prohibition")
        target["requirement_posture"] = "recommended-practice"
        errors = self.validate_requirements(requirements)
        self.assertTrue(any("prohibition must have mandatory-normative posture" in error for error in errors), errors)

    def test_duplicate_source_defined_tag_scheme_fails(self):
        requirements = copy.deepcopy(self.requirements)
        target = next(item for item in requirements if item["source_defined_tags"])
        target["source_defined_tags"].append(copy.deepcopy(target["source_defined_tags"][0]))
        errors = self.validate_requirements(requirements)
        self.assertTrue(any("source_defined_tag schemes must be unique" in error for error in errors), errors)

    def test_requirement_on_superseded_source_version_fails(self):
        requirements = copy.deepcopy(self.requirements)
        eu = next(item for item in requirements if item["external_source_id"] == "EU-AI-ACT-2024-1689")
        old = next(
            item for item in self.ledger_entries
            if item["external_source_id"] == "EU-AI-ACT-2024-1689" and item["source_version"] == "2024-07-12"
        )
        eu["source_version"] = old["source_version"]
        eu["canonical_source_identifier"] = old["canonical_identifier"]
        eu["source_lifecycle_state"] = old["source_lifecycle_state"]
        eu["authoritative_locator"] = old["official_locator"]
        eu["interpretation_provenance"]["source_fingerprint"] = old["fingerprint"]
        eu["requirement_id"] = mod.requirement_id(
            eu["vigil_source_id"], eu["source_version"], eu["clause_or_control"], eu["identity_key"]
        )
        errors = self.validate_requirements(requirements)
        self.assertTrue(any("silently points at a superseded source version" in error for error in errors), errors)

    def test_forbidden_internal_mapping_field_fails(self):
        requirements = copy.deepcopy(self.requirements)
        requirements[0]["caelestis_coverage"] = "not-assessed"
        errors = self.validate_requirements(requirements)
        self.assertTrue(any("forbidden Caelestis-alignment fields" in error for error in errors), errors)

    def test_scope_role_and_extraction_conflict_fails(self):
        scopes = copy.deepcopy(self.scope_entries)
        scopes[0]["source_role"] = "supporting-external-authority"
        errors = self.validate_requirements(scope_entries=scopes)
        self.assertTrue(any("requires extraction_status supporting-only" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
