#!/usr/bin/env python3
"""One-off, read-only, source-first preservation simulation for issue #168.

This does NOT validate future Git-ref durability and does NOT mutate canonical
Incident files. Its five fixed IDs are a dated experiment, never a permanent
corpus test. It must not become a retained CI dependency.
"""
from __future__ import annotations

import copy
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
BASE_COMMIT = "a63e3582f82b58954997cf69d5af9d29acb31c35"
BLOBS = {
    "000034": "ea1b4c179ca9e0d7111e0831f495e420efd18130",
    "000062": "acc8420187e1c3d1cd8588558b2cf04db5e1ef2b",
    "000101": "22446d77c70f34a5b57a6d1e17f18d6ac4e81b7b",
    "000145": "12b524bd6cb1aca23bac028e16e3f0c855405839",
    "000195": "0ae3818650c8e090ef138dc96bcb22e6aa4d5997",
}
REVIEW_REQUIRED = {
    "review_id", "reviewer_type", "reviewer_platform", "reviewer_model",
    "review_date", "review_scope", "capability_profile", "known_limitations",
    "review_outcome",
}


def git(*parts: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(ROOT), *parts])


def digest(review: dict) -> str:
    return hashlib.sha256(json.dumps(
        review, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")).hexdigest()


def main() -> int:
    summaries = []
    total_before = total_after = review_count = 0
    for ident, expected_blob in BLOBS.items():
        source_path = f"vigil/records/incidents/VIGIL-INC-{ident}.json"
        blob = git("rev-parse", f"{BASE_COMMIT}:{source_path}").decode().strip()
        assert blob == expected_blob, f"{ident}: immutable baseline blob mismatch"
        original_bytes = git("show", f"{BASE_COMMIT}:{source_path}")
        original = json.loads(original_bytes)
        current_bytes = (ROOT / source_path).read_bytes()
        assert git("hash-object", source_path).decode().strip() == blob, f"{ident}: current canonical changed"
        assert json.loads(current_bytes) == original, f"{ident}: current source diverged"
        p = original["interpretive_provenance"]
        history = p["review_history"]
        current = p["current_ai_review"]
        ids = [r["review_id"] for r in history]
        assert len(ids) == len(set(ids)), f"{ident}: duplicate historical review"
        assert history[-1] == current, f"{ident}: current review differs from final historical review"
        assert all(REVIEW_REQUIRED <= set(r) for r in history), f"{ident}: missing historical review field"
        in_memory = copy.deepcopy(original)
        cp = in_memory["interpretive_provenance"]
        index = []
        for review in history:
            rid = review["review_id"]
            index.append({
                "review_id": rid,
                "review_date": review["review_date"],
                "reviewer_type": review["reviewer_type"],
                "reviewer_platform": review["reviewer_platform"],
                "reviewer_model": review["reviewer_model"],
                "review_sha256": digest(review),
                "archive_batch_id": None if rid == current["review_id"] else "initial",
            })
        cp.pop("review_history")
        cp["review_history_index"] = index
        cp["review_archive_batches"] = [{
            "batch_id": "initial", "source_commit": BASE_COMMIT,
            "source_path": source_path, "source_blob_sha": blob,
            "retention_ref": "refs/heads/agent/incident-ecosystem-ingestion",
            "review_ids": ids[:-1]
        }]
        assert cp["current_ai_review"] == current, "active full current review must remain"
        before = copy.deepcopy(original)
        after = copy.deepcopy(in_memory)
        bp, ap = before.pop("interpretive_provenance"), after.pop("interpretive_provenance")
        assert before == after, f"{ident}: unrelated canonical fields modified in simulation"
        assert {k: v for k, v in bp.items() if k != "review_history"} == {
            k: v for k, v in ap.items() if k not in ("review_history_index", "review_archive_batches")
        }, f"{ident}: other current provenance changed"
        recovered = {r["review_id"]: r for r in json.loads(
            git("show", f"{BASE_COMMIT}:{source_path}")
        )["interpretive_provenance"]["review_history"]}
        assert set(recovered) == set(ids), f"{ident}: archive identity mismatch"
        for entry in index:
            full = current if entry["archive_batch_id"] is None else recovered[entry["review_id"]]
            assert entry["review_sha256"] == digest(full), f"{ident}: full review integrity mismatch"
            assert all(entry[k] == full[k] for k in
                       ("review_id", "review_date", "reviewer_type", "reviewer_platform", "reviewer_model"))
        compact_bytes = (json.dumps(in_memory, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        before_size = len(original_bytes)
        after_size = len(compact_bytes)
        summaries.append({"incident_id": original["id"],
                          "full_original_reviews_reconstructed": len(history),
                          "original_bytes": before_size, "compact_simulated_bytes": after_size,
                          "delta_bytes": after_size - before_size,
                          "full_original_blob": blob})
        total_before += before_size
        total_after += after_size
        review_count += len(history)
    result = {"status": "in-memory-only-Gate1",
              "baseline_commit": BASE_COMMIT, "incidents": len(summaries),
              "full_original_reviews_verified": review_count,
              "original_bytes": total_before,
              "simulated_compact_bytes": total_after,
              "reduction_percent": round(100*(total_before-total_after)/total_before, 2),
              "archive_permanence_proven": False,
              "canonical_files_modified": 0,
              "records": summaries}
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, OSError, subprocess.CalledProcessError, KeyError, ValueError) as exc:
        print(f"Read-only provenance pilot failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
