#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RECORDS = ROOT / "vigil" / "records"
GENERIC_ACCESS = "not independently re-assessed during registry-wide metadata migration"
EXPECTED_REVIEWS = {
    "VIGIL-2026-FM-0034": "VIGIL-REVIEW-2026-07-15-GPT-5.6-THINKING",
    "VIGIL-2026-FM-0035": "VIGIL-REVIEW-2026-07-16-GPT-5.6-THINKING-FM-0035",
    "VIGIL-2026-PATCH-0022": "VIGIL-REVIEW-2026-07-16-GPT-5.6-THINKING-PATCH-0022",
}
MIGRATION_REVIEW = "VIGIL-REVIEW-2026-07-14-GPT-5.6-THINKING"


def load_migration_module():
    path = ROOT / "vigil" / "scripts" / "migrate-vigil-interpretive-provenance.py"
    spec = importlib.util.spec_from_file_location("vigil_interpretive_provenance_migration", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load migration module from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load(record_id: str) -> dict:
    folder = "patches" if "-PATCH-" in record_id else "failures"
    path = RECORDS / folder / "2026" / f"{record_id}.json"
    return json.loads(path.read_text(encoding="utf-8"))


class ProvenancePreservationTests(unittest.TestCase):
    def test_record_specific_current_reviews_are_preserved(self):
        for record_id, expected_review_id in EXPECTED_REVIEWS.items():
            with self.subTest(record_id=record_id):
                record = load(record_id)
                current = record["interpretive_provenance"]["current_ai_review"]
                self.assertEqual(current["review_id"], expected_review_id)

    def test_authored_source_modalities_are_text(self):
        for record_id in EXPECTED_REVIEWS:
            with self.subTest(record_id=record_id):
                record = load(record_id)
                for source in record["source_records"]:
                    self.assertEqual(source["evidence_modality"], ["text"])

    def test_source_access_is_not_replaced_by_generic_migration_metadata(self):
        for record_id in EXPECTED_REVIEWS:
            with self.subTest(record_id=record_id):
                record = load(record_id)
                for source in record["source_records"]:
                    access = source["primary_artefact_access"]
                    self.assertNotEqual(access["access_status"], GENERIC_ACCESS)
                    self.assertIsInstance(access["direct_primary_artefact_review"], bool)

    def test_dated_migration_review_is_not_backfilled_into_later_record(self):
        migration = load_migration_module()
        record = {
            "date_recorded": "2026-07-23",
            "record_identity": {"created": "2026-07-23"},
            "interpretive_provenance": {
                "review_history": [{"review_id": "VIGIL-REVIEW-2026-07-23-AUTHORED"}],
                "current_ai_review": {"review_id": "VIGIL-REVIEW-2026-07-23-AUTHORED"},
                "historical_reviewer_note": "No earlier record existed.",
            },
        }

        migration.add_provenance(record)

        provenance = record["interpretive_provenance"]
        self.assertNotIn(
            MIGRATION_REVIEW,
            [item.get("review_id") for item in provenance["review_history"]],
        )
        self.assertEqual(
            provenance["current_ai_review"]["review_id"],
            "VIGIL-REVIEW-2026-07-23-AUTHORED",
        )
        self.assertEqual(provenance["historical_reviewer_note"], "No earlier record existed.")

    def test_dated_migration_review_remains_available_to_preexisting_record(self):
        migration = load_migration_module()
        record = {
            "date_recorded": "2026-07-13",
            "record_identity": {"created": "2026-07-13"},
        }

        migration.add_provenance(record)

        provenance = record["interpretive_provenance"]
        self.assertIn(
            MIGRATION_REVIEW,
            [item.get("review_id") for item in provenance["review_history"]],
        )
        self.assertEqual(provenance["current_ai_review"]["review_id"], MIGRATION_REVIEW)


if __name__ == "__main__":
    unittest.main()
