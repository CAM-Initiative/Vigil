import copy
import importlib.util
import json
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
SCRIPT = VIGIL / "scripts" / "validate-vigil-records.py"
SPEC = importlib.util.spec_from_file_location("validate_vigil_records_extreq", SCRIPT)
VALIDATOR = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(VALIDATOR)

CLASS_ID = "VIGIL-FC-000001"
REQ_ID = "EXTREQ-0123456789ABCDEF"
UNMAPPED_CLASS_ID = "VIGIL-FC-000002"


class ExternalRequirementAssessmentTests(unittest.TestCase):
    def setUp(self):
        self.record = {
            "id": "VIGIL-INC-999999",
            "taxonomy_classification": {
                "primary_classification": {"class_id": CLASS_ID},
                "secondary_classifications": [
                    {"class_id": UNMAPPED_CLASS_ID},
                ],
            },
            "external_requirement_assessments": [],
        }
        self.classes = {
            CLASS_ID: {"external_references": [{"requirement_id": REQ_ID}]},
            UNMAPPED_CLASS_ID: {"external_references": []},
        }

    def assessment(self, **changes):
        result = {
            "requirement_id": REQ_ID,
            "derived_from_class_ids": [CLASS_ID],
            "applicability_status": "applicable",
            "applicability_basis": "The identified legal scope, time period and system context apply to this occurrence.",
            "finding": "successful-invariant",
            "finding_basis": "The preserved occurrence evidence establishes that the stated requirement held at the relevant boundary.",
            "assessed_on": "2026-09-29",
        }
        result.update(changes)
        return result

    def validate(self, assessments, known_ids=None):
        record = copy.deepcopy(self.record)
        record["external_requirement_assessments"] = assessments
        errors = []
        with patch.object(VALIDATOR, "taxonomy_catalogue", return_value=({}, self.classes)):
            VALIDATOR.validate_external_requirement_assessments(
                Path("synthetic-incident.json"),
                record,
                known_ids if known_ids is not None else {REQ_ID},
                errors,
            )
        return errors

    def test_empty_optional_array_is_valid(self):
        self.assertEqual(self.validate([]), [])

    def test_applicable_successful_invariant_is_valid(self):
        self.assertEqual(self.validate([self.assessment()]), [])

    def test_applicable_requires_finding_and_basis(self):
        errors = self.validate([self.assessment(finding="", finding_basis="")])
        self.assertTrue(any("finding is required" in error for error in errors), errors)
        self.assertTrue(any("finding_basis is required" in error for error in errors), errors)

    def test_insufficient_evidence_forbids_a_finding(self):
        item = self.assessment(applicability_status="insufficient-evidence")
        errors = self.validate([item])
        self.assertTrue(any("must not include finding" in error for error in errors), errors)

    def test_not_applicable_without_finding_is_valid(self):
        item = self.assessment(applicability_status="not-applicable")
        item.pop("finding")
        item.pop("finding_basis")
        self.assertEqual(self.validate([item]), [])

    def test_noncanonical_fields_and_duplicate_requirement_ids_are_rejected(self):
        item = self.assessment(evidence_refs=["source_records[0]"])
        errors = self.validate([item, self.assessment()])
        self.assertTrue(any("non-canonical fields: evidence_refs" in error for error in errors), errors)
        self.assertTrue(any("unique within the Incident" in error for error in errors), errors)

    def test_derived_classes_must_be_mapped_and_cite_the_requirement(self):
        item = self.assessment(derived_from_class_ids=[UNMAPPED_CLASS_ID])
        errors = self.validate([item])
        self.assertTrue(any("preserve every mapped source class" in error for error in errors), errors)

    def test_requirement_id_must_resolve_in_canonical_corpus(self):
        errors = self.validate([self.assessment()], known_ids=set())
        self.assertTrue(any("does not resolve in the canonical EXTREQ corpus" in error for error in errors), errors)

    def test_schema_keeps_the_top_level_array_optional(self):
        contract = json.loads((VIGIL / "VIGIL.Schema.json").read_text(encoding="utf-8"))
        incident = contract["record_classes"]["incident"]
        self.assertNotIn("external_requirement_assessments", incident["required_top_level_fields"])
        self.assertIn("external_requirement_assessment_rule", incident)
        self.assertFalse(contract["$defs"]["external_requirement_assessment"]["additionalProperties"])
        self.assertEqual(
            contract["$defs"]["vigil_record"]["properties"]["external_requirement_assessments"]["items"]["$ref"],
            "#/$defs/external_requirement_assessment",
        )


if __name__ == "__main__":
    unittest.main()
