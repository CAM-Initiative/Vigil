#!/usr/bin/env python3
from __future__ import annotations

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


if __name__ == "__main__":
    unittest.main()
