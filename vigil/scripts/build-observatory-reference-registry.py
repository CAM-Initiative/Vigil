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
MATRIX = ROOT / "methodologies" / "VIGIL.HarmImpactMatrix.v1.1.0.json"
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
    matrix_reference_ids = matrix.get("reference_ids", [])
    if len(matrix_reference_ids) != len(set(matrix_reference_ids)):
        raise SystemExit("Harm Impact Matrix has duplicate reference IDs")
    unresolved = sorted(set(matrix_reference_ids) - set(ids))
    if unresolved:
        raise SystemExit(f"Harm Impact Matrix has unresolved reference IDs: {', '.join(unresolved)}")
    # HIM 1.1.0 introduces domain-local applicability mappings. Ensure that
    # references attached to a particular harm dimension exist in the registry
    # and are included in the top-level methodology reference inventory.
    for dimension in matrix.get("dimensions", []):
        dimension_refs = dimension.get("reference_ids", [])
        if matrix.get("version") == "1.1.0" and not dimension_refs:
            raise SystemExit(f"{dimension.get('dimension_id')}: missing domain reference IDs")
        if len(dimension_refs) != len(set(dimension_refs)):
            raise SystemExit(f"{dimension.get('dimension_id')}: duplicate domain reference IDs")
        unknown = sorted(set(dimension_refs) - set(matrix_reference_ids))
        if unknown:
            raise SystemExit(f"{dimension.get('dimension_id')}: reference IDs not in methodology inventory: {', '.join(unknown)}")
    threshold_ids = [
        threshold.get("threshold_id")
        for dimension in matrix.get("dimensions", [])
        for threshold in dimension.get("thresholds", {}).values()
    ]
    dimensions = matrix.get("dimensions", [])
    expected_threshold_count = len(dimensions) * 5
    if any(set(dimension.get("thresholds", {})) != {"S1", "S2", "S3", "S4", "S5"} for dimension in dimensions):
        raise SystemExit("Every Harm Impact Matrix dimension must define exactly S1-S5")
    if len(threshold_ids) != expected_threshold_count or len(threshold_ids) != len(set(threshold_ids)):
        raise SystemExit(
            f"Harm Impact Matrix must contain {expected_threshold_count} unique S1-S5 threshold IDs"
        )
    with TARGET.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: row[field] for field in FIELDS} for row in rows)
    print(f"Reference registry valid; wrote {len(rows)} rows to {TARGET.relative_to(ROOT.parent)}")


if __name__ == "__main__":
    main()
