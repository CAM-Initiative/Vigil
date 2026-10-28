#!/usr/bin/env python3
"""Synthetic, isolated tests for approved opt-in review-archive integrity."""
from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "vigil" / "scripts" / "incident_provenance_archive.py"
spec = importlib.util.spec_from_file_location("vigil_provenance_archive_test", SOURCE)
archive = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(archive)

ID = "VIGIL-INC-000034"
RECORD = f"vigil/records/incidents/{ID}.json"


def review(key, day="2026-10-10", reviewer="AI analytical reviewer"):
    return {
        "review_id": key,
        "reviewer_type": reviewer,
        "reviewer_platform": "Synthetic fixture",
        "reviewer_model": "Original recorded model",
        "review_date": day,
        "review_scope": "Evidence and occurrence interpretation",
        "capability_profile": {"direct_source_access": False},
        "known_limitations": ["Synthetic fixture, no human assessment"],
        "review_outcome": "Source-grounded bounded assessment",
    }


def index_entry(value, batch=None):
    return {
        "review_id": value["review_id"],
        "review_date": value["review_date"],
        "reviewer_type": value["reviewer_type"],
        "reviewer_platform": value["reviewer_platform"],
        "reviewer_model": value["reviewer_model"],
        "review_sha256": archive.review_digest(value),
        "archive_batch_id": batch,
    }


class CompactReviewArchiveFixture(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.file = self.root / RECORD
        self.file.parent.mkdir(parents=True)
        self.git("init", "-b", "archive")
        self.git("config", "user.email", "tests@example.invalid")
        self.git("config", "user.name", "Provenance Test Fixture")
        self.old = review("review-original", "2026-10-10")
        self.current = review("review-next", "2026-10-11")
        original = {
            "id": ID, "date_recorded": "2026-10-09", "record_identity": {"created": "2026-10-09"},
            "interpretive_provenance": {"review_history": [self.old],
                                        "current_ai_review": self.old}
        }
        self.put(original)
        self.git("add", RECORD)
        self.git("commit", "-m", "Full historical review")
        self.source_commit = self.git("rev-parse", "HEAD")
        self.source_blob = self.git("rev-parse", "HEAD:"+RECORD)
        self.git("checkout", "-b", "working")
        self.record = copy.deepcopy(original)
        self.record["interpretive_provenance"] = {
            "current_ai_review": self.current,
            "review_history_index": [index_entry(self.old, "initial"), index_entry(self.current)],
            "review_archive_batches": [{
                "batch_id": "initial",
                "source_commit": self.source_commit,
                "source_path": RECORD,
                "source_blob_sha": self.source_blob,
                "retention_ref": "refs/heads/archive",
                "review_ids": ["review-original"],
            }],
        }

    def git(self, *args):
        return subprocess.check_output(
            ["git", "-C", str(self.root), *args], text=True, stderr=subprocess.STDOUT
        ).strip()

    def put(self, value):
        self.file.write_text(json.dumps(value, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")

    def errors(self, doc=None):
        return archive.compact_provenance_errors(doc or self.record, root=self.root)

    def assert_bad(self, doc, fragment):
        errs = self.errors(doc)
        self.assertTrue(any(fragment in x for x in errs), errs)

    def test_full_reconstruction(self):
        self.assertEqual(self.errors(), [])

    def test_content_digest_ignores_dictionary_key_order(self):
        reordered = dict(reversed(list(self.old.items())))
        self.assertEqual(archive.review_digest(reordered), archive.review_digest(self.old))

    def test_legacy_remains_unmodified(self):
        legacy = {"interpretive_provenance": {"review_history": [self.old],
                                               "current_ai_review": self.old}}
        self.assertFalse("review_history_index" in legacy["interpretive_provenance"])

    def test_reject_changed_historical_digest(self):
        d = copy.deepcopy(self.record)
        d["interpretive_provenance"]["review_history_index"][0]["review_sha256"] = "0"*64
        self.assert_bad(d, "full review digest differs")

    def test_reject_changed_current_full_review(self):
        d = copy.deepcopy(self.record)
        d["interpretive_provenance"]["current_ai_review"]["review_outcome"] = "Changed without index"
        self.assert_bad(d, "current review digest mismatch")

    def test_unknown_original_model_stays_null(self):
        # Do not invent a vendor/model for an older reviewer with incomplete
        # contemporaneous attribution. The original Git object is authority.
        self.git("checkout", "archive")
        self.old["reviewer_model"] = None
        historical = {
            "id": ID, "date_recorded": "2026-10-09",
            "record_identity": {"created": "2026-10-09"},
            "interpretive_provenance": {
                "review_history": [self.old], "current_ai_review": self.old
            },
        }
        self.put(historical)
        self.git("add", RECORD)
        self.git("commit", "-m", "Source recorded unknown model")
        commit = self.git("rev-parse", "HEAD")
        blob = self.git("rev-parse", "HEAD:"+RECORD)
        self.git("checkout", "working")
        doc = copy.deepcopy(self.record)
        entry = doc["interpretive_provenance"]["review_history_index"][0]
        entry["reviewer_model"] = None
        entry["review_sha256"] = archive.review_digest(self.old)
        batch = doc["interpretive_provenance"]["review_archive_batches"][0]
        batch["source_commit"] = commit
        batch["source_blob_sha"] = blob
        self.assertEqual(self.errors(doc), [])

    def test_reject_forged_reviewer(self):
        d = copy.deepcopy(self.record)
        d["interpretive_provenance"]["review_history_index"][0]["reviewer_type"] = "human"
        self.assert_bad(d, "original reviewer_type differs")

    def test_reject_wrong_blob_sha(self):
        d = copy.deepcopy(self.record)
        d["interpretive_provenance"]["review_archive_batches"][0]["source_blob_sha"] = "a"*40
        self.assert_bad(d, "pinned source blob")

    def test_reject_missing_git_commit(self):
        d = copy.deepcopy(self.record)
        d["interpretive_provenance"]["review_archive_batches"][0]["source_commit"] = "a"*40
        self.assert_bad(d, "failed immutable archive verification")

    def test_reject_unreachable_source(self):
        self.git("checkout", "archive")
        self.git("commit", "--allow-empty", "-m", "Additional archived review")
        # Point retention at a separate orphan Git lineage.
        self.git("checkout", "--orphan", "unrelated")
        self.git("rm", "-rf", ".")
        (self.root / "other.txt").write_text("orphan", encoding="utf-8")
        self.git("add", "other.txt")
        self.git("commit", "-m", "Unrelated")
        d = copy.deepcopy(self.record)
        d["interpretive_provenance"]["review_archive_batches"][0]["retention_ref"] = "refs/heads/unrelated"
        self.assert_bad(d, "not reachable")

    def test_reject_absent_ref(self):
        d = copy.deepcopy(self.record)
        d["interpretive_provenance"]["review_archive_batches"][0]["retention_ref"] = "refs/heads/does-not-exist"
        self.assert_bad(d, "not reachable")

    def test_reject_mixed_history_modes(self):
        d = copy.deepcopy(self.record)
        d["interpretive_provenance"]["review_history"] = [self.old]
        self.assert_bad(d, "conflicts")

    def test_reject_missing_historical_entry(self):
        d = copy.deepcopy(self.record)
        d["interpretive_provenance"]["review_history_index"] = [index_entry(self.current)]
        self.assert_bad(d, "archive coverage")

    def test_reject_duplicate_review_id(self):
        d = copy.deepcopy(self.record)
        d["interpretive_provenance"]["review_history_index"].insert(1, index_entry(self.old, "initial"))
        self.assert_bad(d, "duplicate review_id")

    def test_reject_wrong_batch_coverage(self):
        d = copy.deepcopy(self.record)
        d["interpretive_provenance"]["review_archive_batches"][0]["review_ids"] = ["other"]
        self.assert_bad(d, "absent from pinned Git object")

    def test_reject_reversed_review_dates(self):
        d = copy.deepcopy(self.record)
        d["interpretive_provenance"]["review_history_index"].reverse()
        self.assert_bad(d, "chronology")

    def test_reject_review_before_creation(self):
        d = copy.deepcopy(self.record)
        d["interpretive_provenance"]["review_history_index"][0]["review_date"] = "2026-09-01"
        self.assert_bad(d, "predates creation")

    def test_reject_missing_current_review(self):
        d = copy.deepcopy(self.record)
        d["interpretive_provenance"]["current_ai_review"] = None
        self.assert_bad(d, "current_ai_review")

    def test_reject_current_archive_instead_of_full_current(self):
        d = copy.deepcopy(self.record)
        d["interpretive_provenance"]["review_history_index"][1]["archive_batch_id"] = "initial"
        self.assert_bad(d, "current review must resolve")

    def test_reject_invalid_date(self):
        d = copy.deepcopy(self.record)
        d["interpretive_provenance"]["review_history_index"][0]["review_date"] = "2026-99-99"
        self.assert_bad(d, "invalid review_date")

    def test_reject_untrusted_archive_path(self):
        d = copy.deepcopy(self.record)
        d["interpretive_provenance"]["review_archive_batches"][0]["source_path"] = "../../outside.json"
        self.assert_bad(d, "invalid Git source")

    def test_reject_missing_archive_index_fields(self):
        d = copy.deepcopy(self.record)
        d["interpretive_provenance"]["review_history_index"][0].pop("reviewer_model")
        self.assert_bad(d, "exact identity")

    def test_two_successive_compact_reviews(self):
        # Previous compact source is committed before superseding full current review.
        self.put(self.record)
        self.git("add", RECORD)
        self.git("commit", "-m", "Compact review snapshot")
        commit = self.git("rev-parse", "HEAD")
        blob = self.git("rev-parse", "HEAD:"+RECORD)
        self.git("branch", "archived-compact", commit)
        nextdoc = copy.deepcopy(self.record)
        newer = review("review-newest", "2026-10-12")
        prov = nextdoc["interpretive_provenance"]
        prov["current_ai_review"] = newer
        prov["review_history_index"][1]["archive_batch_id"] = "successor"
        prov["review_history_index"].append(index_entry(newer))
        prov["review_archive_batches"].append({
            "batch_id": "successor", "source_commit": commit,
            "source_path": RECORD, "source_blob_sha": blob,
            "retention_ref": "refs/heads/archived-compact",
            "review_ids": ["review-next"]
        })
        self.assertEqual(self.errors(nextdoc), [])


if __name__ == "__main__":
    unittest.main()
