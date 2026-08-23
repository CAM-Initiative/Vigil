#!/usr/bin/env python3
"""Validate the canonical/public VIGIL record set.

Only records under ``vigil/records`` participate in public publication and public
record resolution. PROP, PATCH and LEARN material under ``vigil/drafts`` is
intentionally outside this boundary and is not loaded, validated, resolved, or
published here.

Published records may retain typed references to withdrawn PROP/PATCH/LEARN IDs
for historical chain provenance. Those identifiers are accepted as non-resolvable
cross-reference tokens; their draft artefacts are never loaded to satisfy public
validation.
"""

from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
VIGIL_DIR = ROOT / "vigil"
MODULE_PATH = VIGIL_DIR / "scripts" / "validate-vigil-records.py"
WITHDRAWN_REFERENCE_ID = re.compile(r"^VIGIL-\d{4}-(?:PROP|PATCH|LEARN)-\d{4}$")


def load_module() -> Any:
    spec = importlib.util.spec_from_file_location("vigil_record_validation", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load validator from {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def withdrawn_reference_ids(record: dict[str, Any]) -> set[str]:
    """Return well-formed withdrawn IDs referenced by a public record.

    This examines only public record metadata already loaded for validation. It
    does not inspect ``vigil/drafts`` and therefore does not make withdrawn
    records publicly resolvable.
    """
    linked = record.get("linked_records")
    if not isinstance(linked, dict):
        return set()

    references: set[str] = set()
    for field in ("related_proposals", "related_patch_notes", "related_learn_records"):
        values = linked.get(field, [])
        if not isinstance(values, list):
            continue
        for value in values:
            if isinstance(value, str) and WITHDRAWN_REFERENCE_ID.fullmatch(value):
                references.add(value)

    contextual = linked.get("contextual_relations", [])
    if isinstance(contextual, list):
        for relation in contextual:
            if not isinstance(relation, dict):
                continue
            record_id = relation.get("record_id")
            if isinstance(record_id, str) and WITHDRAWN_REFERENCE_ID.fullmatch(record_id):
                references.add(record_id)

    return references


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
        if record.get("record_type") in {"proposal", "patch", "patch_note", "learn"}:
            errors.append(f"{path}: withdrawn record type must not appear in vigil/records")
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

    acknowledged_withdrawn_ids: set[str] = set()
    for record in public_records_by_path.values():
        acknowledged_withdrawn_ids.update(withdrawn_reference_ids(record))
    for record in public_research_by_path.values():
        acknowledged_withdrawn_ids.update(withdrawn_reference_ids(record))

    # The base validator accepts a set of IDs considered valid for link checks.
    # Add only well-formed withdrawn IDs already referenced by public metadata.
    # This suppresses false "future record" warnings/errors without reading or
    # resolving anything from vigil/drafts.
    validation_link_ids = public_ids | acknowledged_withdrawn_ids

    for path, record in public_records_by_path.items():
        module.validate_record(
            path,
            record,
            validation_link_ids,
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
            validation_link_ids,
            errors,
            research_body_by_path.get(path, ""),
        )

    public_records_by_id = {
        record["id"]: record
        for record in public_records_by_path.values()
        if isinstance(record.get("id"), str)
    }

    for path, research in public_research_by_path.items():
        research_id = research.get("id")
        linked = research.get("linked_records", {})
        if not isinstance(research_id, str) or not isinstance(linked, dict):
            continue
        # Reciprocity is a public-record integrity rule. Withdrawn PROP/PATCH/LEARN
        # references are provenance tokens only and are deliberately excluded.
        for field in ("related_observations", "related_failure_modes"):
            for linked_id in linked.get(field, []):
                target = public_records_by_id.get(linked_id)
                if target is None:
                    continue
                target_research = target.get("linked_records", {}).get("research", [])
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
        f"{len(public_ids)} public records; "
        f"{len(acknowledged_withdrawn_ids)} withdrawn link IDs retained as non-resolvable provenance references."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
