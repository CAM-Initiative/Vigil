#!/usr/bin/env python3
"""Validate the Observatory Reference Registry and build its CSV projection."""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "vigil"
SOURCE = ROOT / "references" / "VIGIL.ObservatoryReferenceRegistry.json"
TARGET = ROOT / "references" / "VIGIL.ObservatoryReferenceRegistry.csv"
MATRIX = ROOT / "methodologies" / "VIGIL.HarmImpactMatrix.v1.0.0.json"
ID = re.compile(r"^VIGIL-REF-\d{6}$")
FIELDS = ["reference_id", "title", "publisher", "reference_type", "url", "accessed_on", "use_note"]


def main() -> None:
    registry = json.loads(SOURCE.read_text(encoding="utf-8"))
    rows = registry.get("references", [])
    ids = [row.get("reference_id") for row in rows]
    if not rows or any(not isinstance(value, str) or not ID.fullmatch(value) for value in ids):
        raise SystemExit("Reference registry contains a missing or invalid stable ID")
    if len(ids) != len(set(ids)):
        raise SystemExit("Reference registry IDs must be unique")
    urls = [row.get("url") for row in rows]
    if len(urls) != len(set(urls)):
        raise SystemExit("Reference registry URLs must be unique")
    for row in rows:
        missing = [field for field in FIELDS if not isinstance(row.get(field), str) or not row[field].strip()]
        if missing:
            raise SystemExit(f"{row.get('reference_id')}: missing {', '.join(missing)}")
    matrix = json.loads(MATRIX.read_text(encoding="utf-8"))
    unresolved = sorted(set(matrix.get("reference_ids", [])) - set(ids))
    if unresolved:
        raise SystemExit(f"Harm Impact Matrix has unresolved reference IDs: {', '.join(unresolved)}")
    threshold_ids = [
        threshold.get("threshold_id")
        for dimension in matrix.get("dimensions", [])
        for threshold in dimension.get("thresholds", {}).values()
    ]
    if len(threshold_ids) != 40 or len(threshold_ids) != len(set(threshold_ids)):
        raise SystemExit("Harm Impact Matrix must contain 40 unique S1-S5 threshold IDs")
    with TARGET.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows({field: row[field] for field in FIELDS} for row in rows)
    print(f"Reference registry valid; wrote {len(rows)} rows to {TARGET.relative_to(ROOT.parent)}")


if __name__ == "__main__":
    main()
