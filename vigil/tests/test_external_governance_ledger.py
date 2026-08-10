#!/usr/bin/env python3
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "manage-external-governance-ledger.py"
spec = importlib.util.spec_from_file_location("external_ledger", SCRIPT)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)


class ExternalGovernanceLedgerTests(unittest.TestCase):
    def setUp(self):
        self.source = {
            "alignment_eligible_states": ["published", "effective"],
        }

    def item(self, lifecycle="draft", version="1", title="Example"):
        return {
            "external_source_id": "TEST-001",
            "source_version": version,
            "canonical_identifier": {"scheme": "TEST", "value": "001"},
            "title": title,
            "issuer": "Test Authority",
            "jurisdiction": "Test",
            "source_class": "standard",
            "source_lifecycle_state": lifecycle,
            "official_locator": "https://example.invalid/001",
            "observed_at": "2026-08-10T00:00:00Z"
        }

    def test_draft_does_not_queue(self):
        item = mod.canonicalise(self.item("draft"), "test", self.source)
        self.assertFalse(item["alignment_eligible"])
        self.assertEqual(item["alignment_state"], "unassigned")

    def test_published_enters_review_queue(self):
        item = mod.canonicalise(self.item("published"), "test", self.source)
        self.assertTrue(item["alignment_eligible"])
        self.assertEqual(item["alignment_state"], "review-required")

    def test_unchanged_preserves_human_disposition(self):
        current = mod.canonicalise(self.item("published"), "test", self.source)
        current["alignment_state"] = "verified"
        incoming = mod.canonicalise(self.item("published"), "test", self.source)
        merged = mod.merge_item(current, incoming)
        self.assertEqual(merged["change_state"], "unchanged")
        self.assertEqual(merged["alignment_state"], "verified")

    def test_changed_final_reopens_review(self):
        current = mod.canonicalise(self.item("published", title="Old"), "test", self.source)
        current["alignment_state"] = "verified"
        incoming = mod.canonicalise(self.item("published", title="New"), "test", self.source)
        merged = mod.merge_item(current, incoming)
        self.assertEqual(merged["change_state"], "changed")
        self.assertEqual(merged["alignment_state"], "review-required")

    def test_changed_draft_does_not_erase_disposition(self):
        current = mod.canonicalise(self.item("draft", title="Old"), "test", self.source)
        current["alignment_state"] = "not-applicable"
        incoming = mod.canonicalise(self.item("draft", title="New"), "test", self.source)
        merged = mod.merge_item(current, incoming)
        self.assertEqual(merged["change_state"], "changed")
        self.assertEqual(merged["alignment_state"], "not-applicable")

    def test_stable_id_independent_of_upstream_provider(self):
        a = mod.canonicalise(self.item("published"), "source-a", self.source)
        b = mod.canonicalise(self.item("published"), "source-b", self.source)
        self.assertEqual(a["vigil_source_id"], b["vigil_source_id"])


if __name__ == "__main__":
    unittest.main()
