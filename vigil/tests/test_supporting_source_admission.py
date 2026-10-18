"""Isolated supporting-authority admission and traceability regressions."""
import copy
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
import supporting_source_admission as admission

spec = importlib.util.spec_from_file_location("supporting_manager", SCRIPTS / "manage-external-requirements.py")
manager = importlib.util.module_from_spec(spec)
spec.loader.exec_module(manager)


class SupportingAdmissionTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.req = {
            "requirement_id": "EXTREQ-0000000000000001", "vigil_source_id": "EXT-000000000001",
            "external_source_id": "FIXTURE", "source_version": "1",
            "source_role": "supporting-external-authority", "clause_or_control": "1.1",
            "source_access_status": "direct-public-primary", "requirement_posture": "recommended-practice",
            "alignment_relationship": "alignment", "normative_force": "government-voluntary-framework",
            "applicable_actor": ["Operator"], "governed_object": ["Control system"],
            "applicability_conditions": ["Within the selected operational scope"],
            "exceptions_or_qualifications": ["A voluntary recommendation, not a legal duty"],
        }
        self.key = admission.source_key(self.req)
        self.scopes = {self.key: {"extraction_status": "partial"}}
        self.fidelity = [{**dict(zip(("vigil_source_id", "source_version"), self.key)),
                          "fidelity_status": "provisional", "audited_requirement_ids": [self.req["requirement_id"]]}]
        self.metadata = [{"requirement_id": self.req["requirement_id"], "reviewed_at": "2026-01-01",
                          "review_basis": "direct-primary-text", "field_status": {
            field: "populated-reviewed" if self.req.get(field) else "not-specified-by-source"
            for field in admission.METADATA_FIELDS}}]
        self.cls = {"class_id": "VIGIL-FC-000002", "invariant": "Actions remain within authorised scope."}
        self.relation = {
            **{field: self.req[field] for field in ("requirement_id", "vigil_source_id", "external_source_id", "source_version", "clause_or_control")},
            "class_id": self.cls["class_id"], "relationship_id": "FIXTURE-RELATIONSHIP",
            "review_status": "supported", "strength": "strong-supporting",
            "requirement_sha256": admission.digest(self.req), "class_semantic_sha256": admission.class_digest(self.cls),
            "invariant": self.cls["invariant"], "supported_component": "Authorised scope",
            "scope_correspondence": {"actors": ["Operator"], "objects": ["Control system"]},
            "limitation": "This supports a component, not the complete invariant.", "review_artifact": "review.json",
        }
        self.save_review()

    def save_review(self):
        (self.root / "review.json").write_text(json.dumps({
            "source_identity": {"external_source_id": "FIXTURE", "source_version": "1"},
            "reviewed_on": "2026-01-01", "review_basis": "Primary provision compared independently with invariant",
            "entries": [{"requirement_id": self.req["requirement_id"],
                         "requirement_sha256": admission.digest(self.req), "relationships": [self.relation]}],
        }))

    def errors(self):
        return admission.admission_errors([self.req], self.scopes, self.fidelity, self.metadata,
                                           [self.relation], {self.cls["class_id"]: self.cls}, self.root)

    def test_reviewed_bounded_supporting_recommendation_is_eligible(self):
        self.assertEqual(self.errors(), [])
        self.assertEqual(self.req["normative_force"], "government-voluntary-framework")

    def test_supporting_only_is_zero_requirement_state(self):
        self.scopes[self.key]["extraction_status"] = "supporting-only"
        self.assertTrue(any("bounded extraction state" in e for e in self.errors()))
        self.assertEqual(admission.admission_errors([], self.scopes, [], [], [], {}, self.root), [])

    def test_insufficient_access_and_commentary_cannot_be_promoted(self):
        for access in ("official-metadata-only", "secondary-source-only", "source-unavailable"):
            with self.subTest(access=access):
                self.req["source_access_status"] = access
                self.assertTrue(any("actual provision" in e for e in self.errors()))
        self.req["source_access_status"] = "direct-public-primary"
        for posture in ("informative-guidance", "implementation-example", "definitional"):
            with self.subTest(posture=posture):
                self.req["requirement_posture"] = posture
                self.assertTrue(any("reference-only" in e for e in self.errors()))

    def test_review_required_metadata_and_not_applicable_fidelity_block_admission(self):
        self.metadata[0]["field_status"]["applicable_actor"] = "review-required"
        self.assertTrue(any("applicable_actor" in e for e in self.errors()))
        self.fidelity[0]["fidelity_status"] = "not-applicable"
        self.assertTrue(any("substantive fidelity" in e for e in self.errors()))
        self.fidelity[0]["audited_requirement_ids"] = []
        self.assertTrue(any("include this requirement" in e for e in self.errors()))

    def test_complete_scope_requires_assured_fidelity(self):
        self.scopes[self.key]["extraction_status"] = "complete"
        self.assertTrue(any("assured bounded fidelity" in e for e in self.errors()))
        self.fidelity[0]["fidelity_status"] = "assured"
        self.assertEqual(self.errors(), [])

    def test_contextual_pending_and_unresolved_review_cannot_admit(self):
        for field, value in (("strength", "contextual"), ("review_status", "pending"),
                             ("review_artifact", "missing.json"), ("review_artifact", "../outside.json"),
                             ("requirement_sha256", "stale"), ("class_semantic_sha256", "stale")):
            with self.subTest(field=field, value=value):
                original = self.relation[field]
                self.relation[field] = value
                self.assertTrue(any("resolving reviewed" in e for e in self.errors()))
                self.relation[field] = original

    def test_changed_qualification_or_class_requires_new_review(self):
        self.req["exceptions_or_qualifications"].append("Additional material condition")
        self.assertTrue(any("resolving reviewed" in e for e in self.errors()))
        self.relation["requirement_sha256"] = admission.digest(self.req)
        self.save_review()
        self.assertEqual(self.errors(), [])
        self.cls["exclusions"] = ["Ordinary maintenance"]
        self.assertTrue(any("resolving reviewed" in e for e in self.errors()))

    def test_primary_requirement_is_outside_additive_gate(self):
        self.req["source_role"] = "primary-ai-governance"
        self.assertEqual(admission.admission_errors([self.req], {}, [], [], [], {}, self.root), [])

    def test_valid_relationship_cannot_mask_an_unreviewed_second_relationship(self):
        other = copy.deepcopy(self.relation)
        other["relationship_id"] = "UNREVIEWED-SECOND-RELATIONSHIP"
        errors = admission.admission_errors([self.req], self.scopes, self.fidelity, self.metadata,
                                           [self.relation, other], {self.cls["class_id"]: self.cls}, self.root)
        self.assertTrue(any("UNREVIEWED-SECOND-RELATIONSHIP" in error for error in errors))

    def test_malformed_review_json_is_rejected(self):
        (self.root / "review.json").write_text("[]")
        self.assertTrue(any("resolving reviewed" in error for error in self.errors()))

    def test_role_and_status_compatibility_keeps_existing_guards(self):
        source = {"external_source_id": "FIXTURE", "canonical_identifier": {"scheme": "test", "value": "1"}}
        entry = {field: "fixture" for field in manager.REQUIRED_SCOPE_FIELDS}
        entry.update(vigil_source_id="EXT-000000000001", source_version="1", external_source_id="FIXTURE",
                     canonical_source_identifier=source["canonical_identifier"], source_role="supporting-external-authority",
                     source_access_status="direct-public-primary", access_checked_at="2026-01-01",
                     review_priority="supporting-specialist-source", inaccessible_sections=[],
                     known_unreviewed_sections=[], maintainer_action_required=True)
        for status in ("in-progress", "partial", "complete", "supporting-only"):
            with self.subTest(status=status):
                entry["extraction_status"] = status
                errors = []
                manager.validate_scope({self.key: source}, [entry], errors)
                self.assertEqual(errors, [])
        for role in ("context-or-discovery", "excluded-from-current-scope"):
            entry.update(source_role=role, extraction_status="partial")
            errors = []
            manager.validate_scope({self.key: source}, [entry], errors)
            self.assertTrue(any("requires extraction_status" in e for e in errors))
        entry.update(source_role="supporting-external-authority", extraction_status="complete",
                     known_unreviewed_sections=["Material section"], source_access_status="official-metadata-only")
        errors = []
        manager.validate_scope({self.key: source}, [entry], errors)
        self.assertTrue(any("cannot be complete" in e for e in errors))
        self.assertTrue(any("known unreviewed" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
