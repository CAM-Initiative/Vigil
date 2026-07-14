#!/usr/bin/env python3
"""Validate that VIGIL observes ecosystem failures and records CAM/Caelestis patches only."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
RECORDS = ROOT / "vigil" / "records"
INVALID_PATCH_IDS = {"VIGIL-2026-PATCH-0016", "VIGIL-2026-PATCH-0020"}


def load(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain one JSON object")
    return value


def cam_targets(record: dict[str, Any]) -> list[str]:
    cam = record.get("cam_internal")
    provenance = record.get("repair_provenance")
    targets: list[str] = []
    if isinstance(cam, dict):
        for field in ("changed_instruments", "target_instruments", "affected_instruments"):
            values = cam.get(field, [])
            if isinstance(values, list):
                targets.extend(str(value) for value in values if isinstance(value, str))
    if isinstance(provenance, dict):
        for field in (
            "instruments_reviewed",
            "instruments_amended",
            "instruments_relied_upon_without_amendment",
        ):
            values = provenance.get(field, [])
            if isinstance(values, list):
                targets.extend(str(value) for value in values if isinstance(value, str))
    return targets


def is_cam_target(value: str) -> bool:
    lowered = value.lower()
    return value.startswith("CAM-") or "caelestis" in lowered


def contains_invalid_patch_ref(value: Any) -> bool:
    if isinstance(value, dict):
        return any(contains_invalid_patch_ref(item) for item in value.values())
    if isinstance(value, list):
        return any(contains_invalid_patch_ref(item) for item in value)
    return isinstance(value, str) and value in INVALID_PATCH_IDS


def validate_failure(path: Path, record: dict[str, Any], errors: list[str]) -> None:
    system = record.get("system_context")
    if isinstance(system, dict):
        product = str(system.get("product_or_service", "")).strip().lower()
        system_type = str(system.get("system_type", "")).strip().lower()
        deployment = str(system.get("deployment_context", "")).strip().lower()
        if product == "vigil":
            errors.append(f"{path}: failure subject cannot be VIGIL; VIGIL is the observatory")
        if "vigil registry" in system_type or "vigil repository" in deployment:
            errors.append(f"{path}: failure system_context describes VIGIL administration rather than an ecosystem failure")

    definition = str(record.get("failure_mode_definition", "")).lower()
    threshold = str(record.get("failure_threshold", "")).lower()
    if "vigil validator" in definition or "vigil schema" in definition or "vigil index" in definition:
        errors.append(f"{path}: failure definition must describe an ecosystem failure, not VIGIL maintenance")
    if "vigil validator" in threshold or "vigil schema" in threshold or "vigil index" in threshold:
        errors.append(f"{path}: failure threshold must describe ecosystem behaviour, not VIGIL maintenance")


def validate_patch(path: Path, record: dict[str, Any], errors: list[str]) -> None:
    record_id = record.get("id")
    if record_id in INVALID_PATCH_IDS:
        errors.append(f"{path}: {record_id} is VIGIL maintenance and must not exist as a PATCH")

    system = record.get("system_context")
    if isinstance(system, dict) and str(system.get("product_or_service", "")).strip().lower() == "vigil":
        errors.append(f"{path}: PATCH product_or_service cannot be VIGIL; PATCH records apply to CAM/Caelestis")

    cam = record.get("cam_internal")
    if isinstance(cam, dict):
        domains = cam.get("changed_domains", [])
        if isinstance(domains, list) and any(str(item).strip().upper() == "VIGIL" for item in domains):
            errors.append(f"{path}: PATCH changed_domains cannot contain VIGIL")
        routing = str(cam.get("routing_note", "")).lower()
        if "vigil-only" in routing or "changes vigil registry" in routing:
            errors.append(f"{path}: PATCH routing cannot represent VIGIL-only maintenance")

    change = record.get("change_classification")
    if isinstance(change, dict):
        combined = " ".join(
            str(change.get(field, ""))
            for field in (
                "change_type",
                "change_scope",
                "implementation_level",
                "doctrine_amendment_status",
            )
        ).lower()
        forbidden = (
            "vigil-only",
            "vigil registry repair",
            "registry-schema-validator-repair",
            "vigil records, schemas, templates, validators",
        )
        if any(term in combined for term in forbidden):
            errors.append(f"{path}: PATCH change classification represents VIGIL maintenance rather than CAM/Caelestis repair")

    targets = cam_targets(record)
    if not any(is_cam_target(target) for target in targets):
        errors.append(
            f"{path}: PATCH requires at least one named CAM/Caelestis instrument reviewed, amended, or relied upon"
        )


def main() -> int:
    errors: list[str] = []
    records: list[tuple[Path, dict[str, Any]]] = []
    for path in sorted(RECORDS.rglob("*.json")):
        try:
            record = load(path)
        except (OSError, json.JSONDecodeError, ValueError) as exc:
            errors.append(f"{path}: unable to load record: {exc}")
            continue
        records.append((path, record))

    for path, record in records:
        if contains_invalid_patch_ref(record):
            errors.append(f"{path}: contains a reference to an invalid VIGIL-maintenance PATCH")
        record_type = record.get("record_type")
        if record_type == "failure_mode":
            validate_failure(path, record, errors)
        elif record_type in {"patch", "patch_note"}:
            validate_patch(path, record, errors)

    if errors:
        print("VIGIL/CAM observatory boundary validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"VIGIL/CAM observatory boundary validation passed for {len(records)} records.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
