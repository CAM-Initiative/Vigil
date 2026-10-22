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
