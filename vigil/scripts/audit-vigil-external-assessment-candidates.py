#!/usr/bin/env python3
"""Flag unresolved sources that may warrant external-assessment review.

This is intentionally a review aid, not a validator or admission rule.  It never
promotes a source into ``external_assessments`` and deliberately excludes ordinary
news, social posts, status records and incident-database entries.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
INCIDENT_DIR = ROOT / "vigil" / "records" / "incidents"

CANDIDATE_TYPES = {
    "government report",
    "incident report",
    "investigation report",
    "legal filing or decision",
    "research paper",
    "technical analysis",
    "technical report",
}
EXCLUDED_TYPES = {
    "incident database entry",
    "news article",
    "platform status report",
    "social media post",
}
CANDIDATE_TERMS = re.compile(
    r"(evaluation|assessment|audit|investigation|finding|analysis|root cause|misalignment|alignment|"
    r"scheming|deception|capability|exploit|vulnerability|benchmark|score|rating|classification|"
    r"red.team|monitorability|control evaluation|postmortem|causal|remediation|clinical review|consent order)",
    re.I,
)

# These sources were explicitly adjudicated as occurrence/context evidence in the
# 2026-09-20 corpus review.  Keeping the decision keys here prevents a completed
# review from becoming permanent warning noise while leaving new sources visible.
REVIEWED_NON_ASSESSMENTS = {
    ("VIGIL-INC-000003", 0), ("VIGIL-INC-000003", 1),
    ("VIGIL-INC-000011", 0), ("VIGIL-INC-000028", 0),
    ("VIGIL-INC-000031", 0), ("VIGIL-INC-000032", 0),
    ("VIGIL-INC-000032", 1), ("VIGIL-INC-000035", 1),
    ("VIGIL-INC-000063", 1), ("VIGIL-INC-000081", 1),
    ("VIGIL-INC-000081", 2), ("VIGIL-INC-000089", 0),
    ("VIGIL-INC-000089", 1), ("VIGIL-INC-000090", 0),
    ("VIGIL-INC-000093", 1), ("VIGIL-INC-000104", 0),
    ("VIGIL-INC-000107", 0), ("VIGIL-INC-000109", 1),
    ("VIGIL-INC-000109", 2), ("VIGIL-INC-000110", 2),
    ("VIGIL-INC-000120", 1), ("VIGIL-INC-000127", 1),
    ("VIGIL-INC-000129", 2),
}


def source_is_candidate(source: dict) -> bool:
    source_type = source.get("source_type")
    if source_type in EXCLUDED_TYPES:
        return False
    text = " ".join(
        str(source.get(field, ""))
        for field in ("source_title", "source_context", "relevance_note", "interpretive_reliance")
    )
    return source_type in CANDIDATE_TYPES or bool(CANDIDATE_TERMS.search(text))


def unresolved_candidates() -> list[dict]:
    flags = []
    for path in sorted(INCIDENT_DIR.glob("VIGIL-INC-*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        resolved_refs = {
            ref
            for assessment in (record.get("external_assessments") or [])
            for ref in (assessment.get("source_record_refs") or [])
        }
        for index, source in enumerate(record.get("source_records") or []):
            if not source_is_candidate(source):
                continue
            if (record["id"], index) in REVIEWED_NON_ASSESSMENTS:
                continue
            ref = f"source_records[{index}]"
            if ref in resolved_refs:
                continue
            flags.append({
                "incident": record["id"],
                "source_ref": ref,
                "publisher": source.get("author_or_publisher"),
                "source_type": source.get("source_type"),
                "source_title": source.get("source_title"),
                "source_url": source.get("source_url"),
                "review_note": "Semantic review required; this flag is not an admission decision.",
            })
    return flags


def main() -> None:
    flags = unresolved_candidates()
    print(json.dumps({"review_flag_count": len(flags), "review_flags": flags}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

