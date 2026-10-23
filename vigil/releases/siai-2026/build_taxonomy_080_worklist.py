#!/usr/bin/env python3
"""Construct a deterministic current-taxonomy reconciliation queue; NO adjudication."""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
INCIDENTS = ROOT / "vigil" / "records" / "incidents"
DEST = Path(__file__).resolve().parent / "TAXONOMY-080-WORKLIST.json"
FOCAL = {"VIGIL-INC-000003", "VIGIL-INC-000117", "VIGIL-INC-000129"}
NONFINAL = {"provisionally-classified", "requires-human-review", "classification-disputed"}

def priority(rec: dict) -> tuple[int, str]:
    rid, status, version = rec["incident_id"], rec["classification_status"], rec["recorded_taxonomy_version"]
    if rid in FOCAL:
        return 0, "SIAI case-study crosscheck"
    if status in NONFINAL:
        return 1, "unresolved or provisional status"
    if status == "unclassified":
        return 2, "evidence-bounded no-mapping review"
    if version != "0.8.0":
        return 3, "legacy-classification current-ruleset screen"
    return 4, "current-version integrity screen"

def build() -> dict:
    commit = subprocess.check_output(["git","rev-parse","HEAD^{commit}"], cwd=ROOT, text=True).strip()
    rows = []
    for path in sorted(INCIDENTS.glob("VIGIL-INC-*.json")):
        raw = path.read_bytes()
        data = json.loads(raw)
        identity = data.get("record_identity") or {}
        cl = data.get("taxonomy_classification") or {}
        record_id = data.get("id") or identity.get("record_id") or path.stem
        record = {
            "incident_id": record_id,
            "canonical_path": str(path.relative_to(ROOT)).replace("\\", "/"),
            "canonical_sha256": hashlib.sha256(raw).hexdigest(),
            "record_version": identity.get("version"),
            "title": identity.get("title") or (data.get("summary") or {}).get("title"),
            "classification_status": cl.get("classification_status") or "unspecified",
            "recorded_taxonomy_version": cl.get("taxonomy_version") or "unspecified",
            "primary_fidelity_class": (cl.get("primary_classification") or {}).get("class_id"),
            "secondary_class_ids": [x.get("class_id") for x in (cl.get("secondary_classifications") or [])],
            "source_record_count": len(data.get("source_records") or []),
            "current_080_screen_result": "NOT-REVIEWED",
            "human_assurance_not_inferred": True,
        }
        rank, reason = priority(record)
        record["priority"] = rank
        record["priority_reason"] = reason
        rows.append(record)
    if len(rows) != 200:
        raise SystemExit(f"Unexpected corpus size {len(rows)}; update count only through governed intake")
    if len({r["incident_id"] for r in rows}) != len(rows):
        raise SystemExit("Duplicate canonical incident IDs")
    rows.sort(key=lambda x: (x["priority"], x["incident_id"]))
    return {
        "worklist_schema": "vigil-taxonomy-080-reconciliation/1",
        "project": "VIGIL Observatory",
        "branch_scientific_commit": commit,
        "current_published_taxonomy": "0.8.0",
        "state": "QUEUE-ONLY--NO-REVIEW-COMPLETED",
        "roles": "No automated interpretation, version rewrite, or status changes",
        "counts": {
            "incidents": len(rows),
            "priority": dict(sorted(Counter(str(x["priority"]) for x in rows).items())),
            "status": dict(sorted(Counter(x["classification_status"] for x in rows).items())),
            "recorded_taxonomy": dict(sorted(Counter(x["recorded_taxonomy_version"] for x in rows).items())),
        },
        "incident_worklist": rows,
    }

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = (json.dumps(build(), indent=2, ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8")
    if args.write:
        DEST.write_bytes(payload)
        summary = json.loads(payload)["counts"]
        print("TAXONOMY_080_RECONCILIATION_QUEUE " + json.dumps(summary, sort_keys=True))
        print("No statuses or evidence were adjudicated or altered.")
        return 0
    if DEST.read_bytes() != payload:
        print("ERROR: reconciliation roster differs from exact checkout", file=sys.stderr)
        return 1
    print("PASS: reconciliation roster reproduces current checkout")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
