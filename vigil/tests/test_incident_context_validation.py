"""Gate 1 approved opt-in Incident Context structural regression tests."""
from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

VIGIL = Path(__file__).resolve().parents[1]
HELPER = VIGIL / "scripts" / "incident_context_validation.py"
SPEC = importlib.util.spec_from_file_location("incident_context_validation_test", HELPER)
assert SPEC and SPEC.loader
context = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(context)
RULES = json.loads((VIGIL / "VIGIL.Schema.json").read_text(encoding="utf-8"))["incident_context_rules"]

def fixture():
    return {
        "source_records": [{"source_title": "Example publication"}, {"source_title": "Example independent report"}],
        "affected_party_context": {"entities": [{
            "party_id": "PARTY-001", "name": "Example public service",
            "kind": "service", "roles": ["affected-service"],
            "evidence_state": "attributed", "evidence_basis": "The publication identifies a service touched by the occurrence.",
            "source_record_refs": ["source_records[0]"],
        }]},
        "jurisdictional_context": {
            "primary_jurisdiction": "Australia",
            "normalized_geography": {
                "scope": "cross-border",
                "relations": [{
                    "relationship_id": "GEO-001", "role": "affected-service-jurisdiction",
                    "evidence_state": "attributed",
                    "evidence_basis": "The cited report names the government service jurisdiction; not event location.",
                    "source_record_refs": ["source_records[0]"],
                    "party_refs": ["PARTY-001"],
                    "locations": [{"country_code": "AU", "subdivision_code": "AU-NSW"}],
                }],
            },
        },
    }

class ContextValidationTests(unittest.TestCase):
    def errors(self, record):
        return context.validate(record, RULES)

    def test_valid_relationships_and_legacy_optional(self):
        self.assertEqual(self.errors(fixture()), [])
        self.assertEqual(self.errors({"source_records": [], "jurisdictional_context": {}}), [])
        self.assertEqual(self.errors({"source_records": []}), [])

    def test_affected_party_accepted_without_asserting_harm(self):
        record = fixture()
        self.assertEqual(self.errors(record), [])
        self.assertNotIn("harm_assessment", json.dumps(record))

    def test_invalid_iso_country_rejected(self):
        record = fixture()
        record["jurisdictional_context"]["normalized_geography"]["relations"][0]["locations"][0]["country_code"] = "ZZ"
        self.assertTrue(any("ISO 3166-1" in e for e in self.errors(record)))

    def test_country_subdivision_mismatch_rejected(self):
        record = fixture()
        record["jurisdictional_context"]["normalized_geography"]["relations"][0]["locations"][0]["subdivision_code"] = "US-NY"
        self.assertTrue(any("match country_code" in e for e in self.errors(record)))

    def test_no_unreferenced_affirmative_claims(self):
        record = fixture()
        record["affected_party_context"]["entities"][0]["source_record_refs"] = []
        record["jurisdictional_context"]["normalized_geography"]["relations"][0]["source_record_refs"] = []
        errors = self.errors(record)
        self.assertEqual(sum("requires evidence" in e for e in errors), 2, errors)

    def test_invalid_refs_and_unknown_party_link(self):
        record = fixture()
        record["affected_party_context"]["entities"][0]["source_record_refs"] = ["source_records[9999]"]
        record["jurisdictional_context"]["normalized_geography"]["relations"][0]["party_refs"] = ["PARTY-999"]
        errors = self.errors(record)
        self.assertTrue(any("invalid source_records[N]" in e for e in errors))
        self.assertTrue(any("party_refs" in e for e in errors))

    def test_unresolved_relation_has_no_pseudo_country(self):
        record = fixture()
        relation = record["jurisdictional_context"]["normalized_geography"]["relations"][0]
        relation.update(evidence_state="unresolved", source_record_refs=[], locations=[])
        self.assertEqual(self.errors(record), [])
        relation["locations"] = [{"country_code": "US"}]
        self.assertTrue(any("must be empty for unresolved" in e for e in self.errors(record)))

    def test_many_to_many_multiple_roles_and_locations(self):
        record = fixture()
        geo = record["jurisdictional_context"]["normalized_geography"]
        geo["relations"][0]["locations"].append({"country_code": "US"})
        geo["relations"].append({
            "relationship_id": "GEO-002", "role": "provider-location",
            "evidence_state": "supported", "evidence_basis": "Explicit source-backed location.",
            "source_record_refs": ["source_records[1]"],
            "locations": [{"country_code": "US"}],
        })
        self.assertEqual(self.errors(record), [])

    def test_no_silent_regulatory_applicability(self):
        record = fixture()
        relation = record["jurisdictional_context"]["normalized_geography"]["relations"][0]
        relation["role"] = "regulatory-context"
        self.assertEqual(self.errors(record), [])
        relation["law_applies"] = True
        self.assertTrue(any("unknown fields" in e for e in self.errors(record)))

    def test_duplicate_ids_and_locations(self):
        record = fixture()
        geo = record["jurisdictional_context"]["normalized_geography"]
        geo["relations"].append(copy.deepcopy(geo["relations"][0]))
        geo["relations"][0]["locations"].append(copy.deepcopy(geo["relations"][0]["locations"][0]))
        errors = self.errors(record)
        self.assertTrue(any("unique within" in e for e in errors))
        self.assertTrue(any("duplicates a jurisdiction" in e for e in errors))

    def test_integration_with_canonical_validator(self):
        validator_path = VIGIL / "scripts" / "validate-vigil-records.py"
        spec = importlib.util.spec_from_file_location("vigil_context_validator_integration", validator_path)
        assert spec and spec.loader
        validator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(validator)
        canonical = json.loads((VIGIL / "records" / "incidents" / "VIGIL-INC-000187.json").read_text(encoding="utf-8"))
        canonical["affected_party_context"] = fixture()["affected_party_context"]
        canonical["jurisdictional_context"]["normalized_geography"] = fixture()["jurisdictional_context"]["normalized_geography"]
        errors, _ = validator.validate_record(Path("VIGIL-INC-000187.json"), canonical)
        self.assertEqual(errors, [])
        canonical["affected_party_context"]["entities"][0]["source_record_refs"] = ["source_records[999]"]
        errors, _ = validator.validate_record(Path("VIGIL-INC-000187.json"), canonical)
        self.assertTrue(any("invalid source_records[N]" in e for e in errors), errors)

if __name__ == "__main__":
    unittest.main()
