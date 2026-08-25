#!/usr/bin/env python3
"""Regression tests for the canonical external governance source registry."""

from __future__ import annotations

import importlib.util
import datetime as dt
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
            "public_summary": (
                "This example source describes a bounded governance subject for testing the public knowledge contract. "
                "It explains the instrument's subject matter, its relationship to AI governance, and the principal "
                "scope boundary an external reader needs to understand. The wording is substantive rather than a "
                "description of internal maintenance activity, and it is long enough to exercise meaningful-content "
                "validation without pretending to reproduce any normative clause or provide legal advice."
            ),
            "ai_governance_relevance": ["risk-management"],
            "applicable_lifecycle_stages": ["governance"],
            "relevance_scope": "A generally applicable governance source with bounded relevance to AI risk decisions.",
            "last_substantive_reviewed": "2026-08-19",
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
        self.assertEqual(merged["last_substantive_reviewed"], "2026-08-19")

    def test_changed_final_reopens_review(self):
        current = mod.canonicalise(self.item("published", title="Old"), "test", self.source)
        current["review_state"] = "reviewed"
        incoming = mod.canonicalise(self.item("published", title="New"), "test", self.source)
        merged = mod.merge_item(current, incoming)
        self.assertEqual(merged["change_state"], "changed")
        self.assertEqual(merged["review_state"], "review-required")
        self.assertEqual(merged["last_substantive_reviewed"], "2026-08-19")

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

    def test_review_due_is_distinct_from_source_freshness(self):
        item = mod.canonicalise(self.item("published"), "source-a", self.source)
        item["last_seen"] = "2026-12-01T00:00:00Z"
        item["last_substantive_reviewed"] = "2026-08-19"
        self.assertTrue(mod.review_is_due(item, as_of=dt.date(2026, 11, 18)))

    def test_recent_substantive_review_is_not_due(self):
        item = mod.canonicalise(self.item("published"), "source-a", self.source)
        self.assertFalse(mod.review_is_due(item, as_of=dt.date(2026, 11, 17)))

    def test_due_review_enters_queue_after_workflow_review(self):
        item = mod.canonicalise(self.item("published"), "source-a", self.source)
        item["review_state"] = "reviewed"
        registry = {"updated_at": "2026-08-19", "entries": [item]}
        queue = mod.build_queue(registry, as_of=dt.date(2026, 11, 18))
        self.assertEqual(queue["items"][0]["required_action"], "substantive-reassessment")

    def test_internal_language_pattern_is_targeted(self):
        self.assertTrue(mod.PUBLIC_NARRATIVE_PATTERNS["project or corpus context"].search("VIGIL included this source"))
        self.assertFalse(mod.PUBLIC_NARRATIVE_PATTERNS["maintainer tasking"].search("The standard requires periodic review"))


if __name__ == "__main__":
    unittest.main()
