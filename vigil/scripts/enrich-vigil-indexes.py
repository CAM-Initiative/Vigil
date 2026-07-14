#!/usr/bin/env python3
"""Enrich generated VIGIL indexes with lifecycle and corpus-coverage summaries."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
RECORDS = VIGIL / "records"

INDEXES = {
    "failures": VIGIL / "VIGIL.Failures.Index.json",
    "proposals": VIGIL / "VIGIL.Proposals.Index.json",
    "patches": VIGIL / "VIGIL.PatchNotes.Index.json",
}


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def records_by_id(directory: str) -> dict[str, dict[str, Any]]:
    output: dict[str, dict[str, Any]] = {}
    for path in sorted((RECORDS / directory).rglob("*.json")):
        record = load(path)
        if isinstance(record, dict) and isinstance(record.get("id"), str):
            output[record["id"]] = record
    return output


def enrich_index(
    path: Path,
    source_records: dict[str, dict[str, Any]],
    fields: dict[str, str],
) -> None:
    index = load(path)
    if not isinstance(index, dict) or not isinstance(index.get("records"), list):
        raise ValueError(f"{path} is not a generated VIGIL index")
    for item in index["records"]:
        if not isinstance(item, dict):
            continue
        source = source_records.get(str(item.get("id", "")))
        if source is None:
            continue
        for output_field, source_field in fields.items():
            value = source.get(source_field)
            if value not in (None, "", [], {}):
                item[output_field] = value
    write(path, index)


def main() -> None:
    enrich_index(
        INDEXES["failures"],
        records_by_id("failures"),
        {
            "ecosystem_status_summary": "ecosystem_status",
            "repair_status_summary": "repair_status",
            "corpus_coverage_summary": "corpus_coverage",
        },
    )
    enrich_index(
        INDEXES["proposals"],
        records_by_id("proposals"),
        {
            "resolution_status_summary": "resolution_status",
            "coverage_reconciliation_summary": "coverage_reconciliation",
        },
    )
    enrich_index(
        INDEXES["patches"],
        records_by_id("patches"),
        {
            "patch_classifications": "patch_classifications",
            "repair_provenance_summary": "repair_provenance",
        },
    )
    print("Enriched VIGIL indexes with lifecycle and corpus-coverage summaries.")


if __name__ == "__main__":
    main()
