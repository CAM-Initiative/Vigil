"""Deterministic jurisdiction-normalization tests; no canonical Incident writes."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "build-vigil-jurisdiction-index.py"
spec = importlib.util.spec_from_file_location("jurisdiction_projection", SCRIPT)
geo = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(geo)


def record(primary="", secondary=None, incident_id="VIGIL-INC-000001"):
    return {
        "id": incident_id,
        "record_identity": {"version": "1.2.3"},
        "jurisdictional_context": {
            "primary_jurisdiction": primary,
            "secondary_jurisdictions": secondary or [],
        },
    }


class JurisdictionProjectionTest(unittest.TestCase):
    def reviewed(self):
        r = record("United States")
        r["source_records"] = [{"source_title": "Controlled source fixture"}]
        def relation(i, role, code, state="attributed"):
            return {"relationship_id": f"GEO-{i:03}", "role": role,
                    "evidence_state": state, "evidence_basis": "Fixture-specific source basis.",
                    "source_record_refs": ["source_records[0]"],
                    "locations": [{"country_code": code}] if code else []}
        r["jurisdictional_context"]["normalized_geography"] = {
            "scope": "cross-border", "relations": [
                relation(1, "provider-location", "US"),
                relation(2, "affected-service-jurisdiction", "AU", "disputed"),
                relation(3, "affected-organization-jurisdiction", "AU"),
                relation(4, "occurrence-location", None, "unresolved")]}
        return r

    def test_reviewed_relationships_keep_roles_states_and_no_legacy_anchor(self):
        r = self.reviewed()
        p = geo.project(r)
        self.assertEqual(p["projection_status"], "reviewed-canonical")
        self.assertEqual(p["scope"], "cross-border")
        self.assertEqual(p["relations"], r["jurisdictional_context"]["normalized_geography"]["relations"])
        self.assertEqual(p["reviewed_country_codes"], ["AU", "US"])
        self.assertIsNone(p["anchor_country_code"])
        self.assertEqual(p["legacy_text_projection"]["anchor_country_code"], "US")
        self.assertEqual(p["record_version"], "1.2.3")
        p["relations"][0]["locations"].clear()
        self.assertTrue(r["jurisdictional_context"]["normalized_geography"]["relations"][0]["locations"])

    def test_country_counts_deduplicate_incident_and_country(self):
        p = geo.build_projection([self.reviewed()])
        self.assertEqual(p["reviewed_country_incident_counts"], {"AU": 1, "US": 1})
        self.assertEqual(p["reviewed_mapped_record_count"], 1)

    def test_explicit_unknown_never_falls_back_to_legacy_country(self):
        r = self.reviewed()
        r["jurisdictional_context"]["normalized_geography"] = {
            "scope": "not-established", "relations": [r["jurisdictional_context"]["normalized_geography"]["relations"][-1]]}
        p = geo.project(r)
        self.assertFalse(p["map_eligible"])
        self.assertEqual(p["reviewed_country_codes"], [])
        self.assertEqual(p["scope"], "not-established")

    def test_invalid_canonical_source_reference_and_duplicate_ids_rejected(self):
        r = self.reviewed()
        r["jurisdictional_context"]["normalized_geography"]["relations"][0]["source_record_refs"] = ["source_records[5]"]
        with self.assertRaises(ValueError):
            geo.project(r)
        with self.assertRaises(ValueError):
            geo.build_projection([record(), record()])

    def test_single_country_anchor_is_explicit_and_not_a_point_location(self):
        p = geo.project(record("Perth, Western Australia, Australia"))
        self.assertEqual(p["scope"], "single-country")
        self.assertEqual(p["country_codes_mentioned"], ["AU"])
        self.assertEqual(p["anchor_country_code"], "AU")
        self.assertEqual(p["subdivision_codes_mentioned"], ["AU-WA"])
        self.assertTrue(p["map_eligible"])
        self.assertEqual(p["anchor_semantics"], "recorded-primary-jurisdiction-not-incident-location")
        self.assertEqual(p["evidence_review_status"], "source-field-derived-not-independently-verified")

    def test_recorded_secondary_subdivision_remains_traceable(self):
        p = geo.project(record("Australia", ["New South Wales"]))
        self.assertEqual(p["anchor_country_code"], "AU")
        self.assertEqual(p["subdivision_codes_mentioned"], ["AU-NSW"])
        self.assertEqual(p["secondary_jurisdictions_text"], ["New South Wales"])
        self.assertIn("jurisdictional_context.secondary_jurisdictions", p["source_fields"])

    def test_mixed_countries_not_forced_onto_one_pin(self):
        for raw in [
            "United States / Canada", "Singapore / Norway",
            "United States / Singapore / China-linked entities",
            "Ukraine / Russian-occupied Ukrainian territory / United States commercial provider",
            "Thailand / Hong Kong-hosted attacker infrastructure",
        ]:
            with self.subTest(raw=raw):
                p = geo.project(record(raw))
                self.assertEqual(p["scope"], "multi-jurisdiction")
                self.assertFalse(p["map_eligible"])
                self.assertIsNone(p["anchor_country_code"])
                self.assertGreaterEqual(len(p["country_codes_mentioned"]), 2)

    def test_unknown_global_and_cross_border_not_geocoded(self):
        samples = [
            ("global consumer service", "global"),
            ("cross-border / United States and China", "cross-border"),
            ("not established", "not-established"),
            ("Not applicable — controlled training", "non-geographic"),
            ("", "not-established"),
            ("United States / global", "mixed-global"),
        ]
        for name, scope in samples:
            with self.subTest(name=name):
                p = geo.project(record(name))
                self.assertEqual(p["scope"], scope)
                self.assertFalse(p["map_eligible"])

    def test_secondary_country_blocks_single_country_pin(self):
        p = geo.project(record("United States", ["Canada"]))
        self.assertEqual(p["scope"], "multi-jurisdiction")
        self.assertEqual(p["country_codes_mentioned"], ["CA", "US"])
        self.assertIsNone(p["anchor_country_code"])

    def test_no_source_evidence_or_legal_conclusion_fabricated(self):
        p = geo.project(record("United States / Washington"))
        self.assertNotIn("latitude", json.dumps(p))
        self.assertNotIn("longitude", json.dumps(p))
        self.assertNotIn("source_record_refs", p)
        self.assertNotIn("law_applies", json.dumps(p))
        self.assertEqual(p["subdivision_codes_mentioned"], ["US-WA"])

    def test_deterministic_record_order_and_counts(self):
        a = record("not established", incident_id="VIGIL-INC-000002")
        b = record("France")
        first = geo.build_projection([a, b])
        second = geo.build_projection([b, a])
        self.assertEqual(first, second)
        self.assertEqual(first["record_count"], 2)
        self.assertEqual(first["map_eligible_count"], 1)
        self.assertEqual(first["scope_counts"], {"not-established": 1, "single-country": 1})
        self.assertEqual(first["authorship_provenance"]["human_review_status"], "not-reviewed")


if __name__ == "__main__":
    unittest.main()
