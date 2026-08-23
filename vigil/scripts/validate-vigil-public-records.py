#!/usr/bin/env python3
"""Validate the public VIGIL record set while resolving withdrawn draft references.

PROP, PATCH and LEARN records under ``vigil/drafts`` are retained working material.
They may satisfy referential-integrity checks from public records, but they are not
validated as canonical/public records and are not publication inputs.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
VIGIL_DIR = ROOT / "vigil"
MODULE_PATH = VIGIL_DIR / "scripts" / "validate-vigil-records.py"
DRAFTS_ROOT = VIGIL_DIR / "drafts"


def load_module() -> Any:
    spec = importlib.util.spec_from_file_location("vigil_record_validation", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load validator from {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_draft_reference_records() -> dict[str, dict[str, Any]]:
    records: dict[str, dict[str, Any]] = {}
    for folder in ("proposals", "patches", "learn"):
        root = DRAFTS_ROOT / folder
        if not root.exists():
            continue
        for path in sorted(root.rglob("*.json")):
            try:
                value = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                continue
            record_id = value.get("id") if isinstance(value, dict) else None
            if isinstance(record_id, str) and record_id:
                records[record_id] = value
    return records


def main() -> int:
    module = load_module()
    errors: list[str] = []
    warnings: list[str] = []

    for deprecated_path in module.DEPRECATED_OUTPUT_PATHS:
        if deprecated_path.exists():
            errors.append(f"{deprecated_path}: deprecated generated file must not exist")

    allowed_groups = module.load_allowed_canonical_failure_groups()
    allowed_vendors = module.load_allowed_platform_or_vendor_values()
    allowed_products = module.load_allowed_product_or_service_values()

    public_records_by_path: dict[Path, dict[str, Any]] = {}
    public_research_by_path: dict[Path, dict[str, Any]] = {}
    research_body_by_path: dict[Path, str] = {}
    public_ids: set[str] = set()

    for path in module.record_files():
        try:
            record = module.load_json(path)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{path}: unable to read JSON: {exc}")
            continue
        if not isinstance(record, dict):
            errors.append(f"{path}: individual record file must contain one JSON object")
            continue
        if "records" in record or "generated_notice" in record:
            errors.append(f"{path}: individual record file must not contain a generated aggregate wrapper")
        public_records_by_path[path] = record
        record_id = record.get("id")
        if isinstance(record_id, str):
            if record_id in public_ids:
                errors.append(f"{path}: duplicate id {record_id!r}")
            public_ids.add(record_id)

    if module.RESEARCH_ROOT.exists():
        for path in sorted(module.RESEARCH_ROOT.rglob("*.md"), key=lambda item: item.as_posix()):
            try:
                record, body = module.load_research_document(path)
            except Exception as exc:  # noqa: BLE001
                errors.append(f"{path}: unable to read research metadata: {exc}")
                continue
            public_research_by_path[path] = record
            research_body_by_path[path] = body
            record_id = record.get("id")
            if isinstance(record_id, str):
                if record_id in public_ids:
                    errors.append(f"{path}: duplicate id {record_id!r}")
                public_ids.add(record_id)

    draft_reference_records = load_draft_reference_records()
    duplicate_draft_ids = sorted(public_ids.intersection(draft_reference_records))
    if duplicate_draft_ids:
        errors.append(
            "Draft/public record ID collision(s): " + ", ".join(duplicate_draft_ids)
        )
    known_ids = public_ids | set(draft_reference_records)

    for path, record in public_records_by_path.items():
        module.validate_record(
            path,
            record,
            known_ids,
            errors,
            warnings,
            allowed_groups,
            allowed_vendors,
            allowed_products,
        )

    for path, record in public_research_by_path.items():
        module.validate_research_record(
            path,
            record,
            known_ids,
            errors,
            research_body_by_path.get(path, ""),
        )

    reference_records_by_id = {
        record["id"]: record
        for record in public_records_by_path.values()
        if isinstance(record.get("id"), str)
    }
    reference_records_by_id.update(draft_reference_records)

    for path, research in public_research_by_path.items():
        research_id = research.get("id")
        linked = research.get("linked_records", {})
        if not isinstance(research_id, str) or not isinstance(linked, dict):
            continue
        for field in (
            "related_observations",
            "related_failure_modes",
            "related_proposals",
            "related_patch_notes",
        ):
            for linked_id in linked.get(field, []):
                target = reference_records_by_id.get(linked_id)
                target_research = target.get("linked_records", {}).get("research", []) if target else []
                if research_id not in target_research:
                    errors.append(
                        f"{path}: {linked_id} must reciprocally include {research_id} in linked_records.research"
                    )

    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)

    if errors:
        print("VIGIL public record validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "VIGIL public record validation passed: "
        f"{len(public_records_by_path)} JSON files, {len(public_research_by_path)} research files, "
        f"{len(public_ids)} public records; {len(draft_reference_records)} withdrawn draft references available for resolution."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
