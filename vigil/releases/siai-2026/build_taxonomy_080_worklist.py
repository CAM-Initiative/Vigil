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
    # Overlay only a dated, explicitly reviewed decision packet, not AI-inferred
    # completion from a matching taxonomy version or changed status label.
    review_path = ROOT / "vigil/docs/reviews/2026-10-23-taxonomy-080-reconciliation/TRANCHE-01-DECISIONS.json"
    if review_path.exists():
        review = json.loads(review_path.read_text(encoding="utf-8"))
        if review.get("screening_taxonomy") not in (None, "0.8.0") or review.get("state") != "SOURCE_AND_CRITERION_SCREEN_COMPLETE_CANONICAL_FINDINGS_UNCHANGED":
            raise SystemExit("Malformed campaign review packet authority or current taxonomy scope")
        index = {r["incident_id"]: r for r in rows}
        seen = set()
        for decision in review.get("checked_records", []):
            rid = decision.get("incident_id")
            if rid in seen or rid not in index:
                raise SystemExit(f"Unknown or duplicate screened Incident: {rid}")
            seen.add(rid)
            row = index[rid]
            if row["record_version"] != decision.get("baseline_record_revision"):
                raise SystemExit(f"Review stale for {rid}: record version changed; update substantive disposition")
            if row["recorded_taxonomy_version"] != decision.get("baseline_taxonomy_edition"):
                raise SystemExit(f"Review stale for {rid}: adjudication taxonomy edition changed")
            if row["classification_status"] != decision.get("current_status"):
                raise SystemExit(f"Review stale for {rid}: classification state changed")
            if decision.get("has_canonical_record_been_modified") is not False:
                raise SystemExit(f"Review packet improperly claims no canonical change for {rid}")
            row["current_080_screen_result"] = decision["screening_outcome"]
            row["current_080_screen_date"] = decision["screening_date"]
            row["screening_decision_packet"] = str(review_path.relative_to(ROOT))
            row["screening_assurance"] = "AI-assessed; no independent human verification implied"
    # Separate genuinely restamped current-edition adjudications from screening
    # only. Never accept a packet merely because a version string happens to match.
    by_id = {r["incident_id"]: r for r in rows}
    packet_dir = ROOT / "vigil/docs/reviews/2026-10-23-taxonomy-080-reconciliation"
    for packet_path in sorted(packet_dir.glob("INC-*-CURRENT-080-DECISION.json")):
        packet = json.loads(packet_path.read_text(encoding="utf-8"))
        rid = packet.get("incident_id")
        if rid not in by_id:
            raise SystemExit(f"Unknown Incident in reviewed packet {packet_path}")
        row = by_id[rid]
        canonical = json.loads((ROOT / row["canonical_path"]).read_text(encoding="utf-8"))
        rev = canonical.get("taxonomy_classification") or {}
        source_mappings = [rev.get("primary_classification"), *(rev.get("secondary_classifications") or [])]
        source_mappings = [x for x in source_mappings if isinstance(x, dict)]
        decisions = (packet.get("baseline_mapping_dispositions")
                     or packet.get("previous_mapping_dispositions") or [])
        recorded_pairs = [(x.get("class_id"), x.get("classification_role")) for x in source_mappings]
        audited_pairs = [(x.get("class_id"), x.get("previous_role") or x.get("role"))
                         for x in decisions]
        criteria = packet.get("adjudicated_taxonomy") or packet.get("current_criteria") or {}
        candidate_version = criteria.get("published_version") or criteria.get("version")
        outcome = packet.get("current_decision") or packet.get("adjudicated_outcome") or {}
        previous_version = packet["baseline"]["record_version"]
        current_version = row["record_version"]
        oldparts, newparts = previous_version.split("."), current_version.split(".")
        expected_revision = (oldparts[:-1] == newparts[:-1]
                             and int(newparts[-1]) == int(oldparts[-1]) + 1)
        if (candidate_version != "0.8.0"
            or row["recorded_taxonomy_version"] != "0.8.0"
            or packet.get("status") != "completed-evidence-limited"
               and packet.get("adjudicated_taxonomy") is None
            or packet.get("incident_id") != rid
            or not expected_revision
            or packet["baseline"].get("taxonomy_version") not in (None, "0.6.11")
            or outcome.get("classification_status") != row["classification_status"]
            or audited_pairs != recorded_pairs
            or rev.get("classification_review_provenance", {}).get("review_reference")
               != str(packet_path.relative_to(ROOT))):
            raise SystemExit(f"Substantive current-taxonomy decision stale or invalid for {rid}")
        if row["current_080_screen_result"] != "NOT-REVIEWED":
            raise SystemExit(f"Duplicate case review overlay for {rid}")
        row["current_080_screen_result"] = "CANONICAL-080-RECONCILED-PROVISIONAL-RETAINED"
        row["current_080_screen_date"] = packet["review_date"]
        row["screening_decision_packet"] = str(packet_path.relative_to(ROOT))
        row["screening_assurance"] = "AI source/criterion review; original evidence limits preserved"
    rows.sort(key=lambda x: (x["priority"], x["incident_id"]))
    return {
        "worklist_schema": "vigil-taxonomy-080-reconciliation/1",
        "project": "VIGIL Observatory",
        "branch_scientific_commit": commit,
        "current_published_taxonomy": "0.8.0",
        "state": "RECONCILIATION-IN-PROGRESS--NO-INDEPENDENT-HUMAN-ASSURANCE-CERTIFIED",
        "roles": "Dated decision packet overlays only; approved canonical edits must independently pass rebuild and derived-output validation",
        "counts": {
            "incidents": len(rows),
            "priority": dict(sorted(Counter(str(x["priority"]) for x in rows).items())),
            "status": dict(sorted(Counter(x["classification_status"] for x in rows).items())),
            "recorded_taxonomy": dict(sorted(Counter(x["recorded_taxonomy_version"] for x in rows).items())),
            "screened_with_dated_packet": sum(r["current_080_screen_result"] != "NOT-REVIEWED" for r in rows),
            "not_screened": sum(r["current_080_screen_result"] == "NOT-REVIEWED" for r in rows),
            "screen_outcomes": dict(sorted(Counter(r["current_080_screen_result"] for r in rows).items())),
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
