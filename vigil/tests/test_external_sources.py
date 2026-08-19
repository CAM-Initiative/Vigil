#!/usr/bin/env python3
"""Regression tests for the canonical external governance source registry."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "manage-external-sources.py"
spec = importlib.util.spec_from_file_location("external_sources", SCRIPT)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)


class ExternalSourceRegistryTests(unittest.TestCase):
    def setUp(self):
        self.source = {"review_eligible_states": ["published", "effective"]}

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
            "observed_at": "2026-08-19T00:00:00Z",
        }

    def test_repository_registry_and_generated_outputs_validate(self):
        mod.validate(check_generated=True)

    def test_draft_does_not_enter_review_queue(self):
        item = mod.canonicalise(self.item("draft"), "test", self.source)
        self.assertFalse(item["review_eligible"])
        self.assertEqual(item["review_state"], "unassigned")

    def test_published_enters_review_queue(self):
        item = mod.canonicalise(self.item("published"), "test", self.source)
        self.assertTrue(item["review_eligible"])
        self.assertEqual(item["review_state"], "review-required")

    def test_unchanged_preserves_review_disposition(self):
        current = mod.canonicalise(self.item("published"), "test", self.source)
        current["review_state"] = "reviewed"
        incoming = mod.canonicalise(self.item("published"), "test", self.source)
        merged = mod.merge_item(current, incoming)
        self.assertEqual(merged["change_state"], "unchanged")
        self.assertEqual(merged["review_state"], "reviewed")

    def test_changed_final_reopens_review(self):
        current = mod.canonicalise(self.item("published", title="Old"), "test", self.source)
        current["review_state"] = "reviewed"
        incoming = mod.canonicalise(self.item("published", title="New"), "test", self.source)
        merged = mod.merge_item(current, incoming)
        self.assertEqual(merged["change_state"], "changed")
        self.assertEqual(merged["review_state"], "review-required")

    def test_changed_draft_preserves_existing_disposition(self):
        current = mod.canonicalise(self.item("draft", title="Old"), "test", self.source)
        current["review_state"] = "reviewed"
        incoming = mod.canonicalise(self.item("draft", title="New"), "test", self.source)
        merged = mod.merge_item(current, incoming)
        self.assertEqual(merged["change_state"], "changed")
        self.assertEqual(merged["review_state"], "reviewed")

    def test_stable_id_is_independent_of_discovery_provider(self):
        a = mod.canonicalise(self.item("published"), "source-a", self.source)
        b = mod.canonicalise(self.item("published"), "source-b", self.source)
        self.assertEqual(a["vigil_source_id"], b["vigil_source_id"])

    def test_metadata_fingerprint_is_not_a_reviewed_document_digest(self):
        item = mod.canonicalise(self.item("published"), "source-a", self.source)
        self.assertEqual(item["source_metadata_fingerprint"], mod.metadata_fingerprint(item))
        self.assertNotIn("reviewed_source_digest", item)


if __name__ == "__main__":
    unittest.main()
