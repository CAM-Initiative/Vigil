#!/usr/bin/env python3
"""Verify the 81 PR #166 Incident transfers against their pinned source branch.

A source review may be supplemented by later release-branch adjudication, but
its decisions, source evidence and provenance must not silently disappear.
This is a structural preservation audit, not a fresh semantic certification.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

PACKETS = "vigil/docs/reviews/2026-10-25-siai-paper-v081-100-plus"
RECORDS = "vigil/records/incidents"
EXPECTED = 81


def load(path: Path) -> dict:
    result = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(result, dict):
        raise ValueError(f"{path}: expected an object")
    return result


def roles(record: dict) -> list:
    tax = record.get("taxonomy_classification") or {}
    entries = [tax.get("primary_classification"), *(tax.get("secondary_classifications") or [])]
    return [
        (m.get("class_id"), m.get("family_id"), m.get("classification_role"),
         m.get("classification_confidence"))
        for m in entries if isinstance(m, dict) and m.get("class_id")
    ]


def episodes(record: dict) -> list:
    clauses = (record.get("vigil_assessment") or {}).get("source_clause_analysis") or {}
    result = []
    for c in clauses.get("clauses") or []:
        accepted = [
            (m.get("class_id"), m.get("relationship"))
            for m in c.get("taxonomy_relationships") or []
            if m.get("canonical_taxonomy_mapping") is True
        ]
        result.append((c.get("episode_id"), c.get("adjudication_status"), accepted))
    return result


def review_entries(record: dict) -> dict:
    reviews = (record.get("interpretive_provenance") or {}).get("review_history") or []
    seen = {}
    for item in reviews:
        key = item.get("review_id")
        if not isinstance(key, str) or not key or key in seen:
            raise ValueError(f"{record.get('id')}: duplicate/invalid review ID: {key}")
        seen[key] = item
    return seen


def version(value: str) -> tuple:
    return tuple(int(p) for p in value.split("."))


def validate(source_root: Path, current_root: Path) -> tuple[list, list]:
    errors, summary = [], []
    packets = sorted((source_root / PACKETS).glob("INC-*-081-REVIEW.json"))
    current_packets = sorted((current_root / PACKETS).glob("INC-*-081-REVIEW.json"))
    if len(packets) != EXPECTED or len(current_packets) != EXPECTED:
        errors.append(f"expected exactly {EXPECTED} review packets on both sides, "
                      f"found {len(packets)} source / {len(current_packets)} current")
    src_ids = {p.name for p in packets}
    target_ids = {p.name for p in current_packets}
    if src_ids != target_ids:
        errors.append(f"review packet set differs: source-only={sorted(src_ids-target_ids)}, "
                      f"current-only={sorted(target_ids-src_ids)}")
    for packet in packets:
        incident_id = packet.name.split("-081-REVIEW.json")[0].replace("INC-", "")
        canonical_name = f"VIGIL-INC-{incident_id}.json"
        source_path = source_root / RECORDS / canonical_name
        current_path = current_root / RECORDS / canonical_name
        current_packet = current_root / PACKETS / packet.name
        if not source_path.is_file() or not current_path.is_file() or not current_packet.is_file():
            errors.append(f"{incident_id}: missing source/current canonical file or packet")
            continue
        a, b = load(source_path), load(current_path)
        pa, pb = load(packet), load(current_packet)
        prefix = f"INC-{incident_id}"
        if pa != pb:
            errors.append(f"{prefix}: transferred review packet differs from PR #166")
        if a.get("id") != b.get("id") or a.get("id") != f"VIGIL-INC-{incident_id}":
            errors.append(f"{prefix}: canonical identity changed")
        ca, cb = a.get("taxonomy_classification") or {}, b.get("taxonomy_classification") or {}
        for key in ("taxonomy_version", "classification_status", "adjudication_coverage"):
            if ca.get(key) != cb.get(key):
                errors.append(f"{prefix}: changed taxonomy {key} from transferred adjudication")
        if roles(a) != roles(b):
            errors.append(f"{prefix}: class, role, order, or confidence differs from PR #166")
        if episodes(a) != episodes(b):
            errors.append(f"{prefix}: source-episode disposition or accepted relationships changed")
        for key in ("source_records", "preferred_evidence", "harm_impact_assessment",
                    "external_requirement_assessments", "external_assessments"):
            if a.get(key) != b.get(key):
                errors.append(f"{prefix}: {key} differs (must independently reconcile)")
        try:
            sa, sb = review_entries(a), review_entries(b)
            missing = sorted(set(sa) - set(sb))
            changed = sorted(k for k in set(sa) & set(sb) if sa[k] != sb[k])
            if missing or changed:
                errors.append(f"{prefix}: missing/changed transferred review history "
                              f"{missing=}, {changed=}")
        except ValueError as ex:
            errors.append(str(ex))
            sa, sb = {}, {}
        v_a = (a.get("record_identity") or {}).get("version") or ""
        v_b = (b.get("record_identity") or {}).get("version") or ""
        try:
            if version(v_b) < version(v_a):
                errors.append(f"{prefix}: release version {v_b} regressed from {v_a}")
        except ValueError:
            errors.append(f"{prefix}: unparsable version {v_a!r}/{v_b!r}")
        if pa.get("incident_id") != a.get("id"):
            errors.append(f"{prefix}: source case packet identity differs")
        summary.append({
            "incident": prefix, "source_version": v_a, "release_version": v_b,
            "source_review_count": len(sa), "release_review_count": len(sb),
            "equal_canonical_record": a == b,
        })
    return errors, summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", type=Path, required=True,
                        help="Pinned checkout of PR #166 at SHA 99347d4")
    parser.add_argument("--current-root", type=Path, default=Path("."))
    args = parser.parse_args()
    errors, summary = validate(args.source_root, args.current_root)
    for issue in errors:
        print("ERROR:", issue)
    if errors:
        print(f"Transfer preservation audit FAILED: {len(errors)} error(s) "
              f"across {len(summary)} inspected incidents.")
        return 1
    differing = [row["incident"] for row in summary if not row["equal_canonical_record"]]
    print(f"Transfer preservation audit PASS: {len(summary)}/{EXPECTED} canonical records, "
          f"{EXPECTED} exact review packets, all class roles/confidences, "
          f"accepted source episodes, source/evidence/harm/external records "
          f"and transferred review histories preserved.")
    print(f"{len(differing)} records contain additional approved-branch context, "
          f"prose or review-history differences; preservation comparisons passed.")
    if differing:
        print("Different canonical bytes:", ", ".join(differing))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
