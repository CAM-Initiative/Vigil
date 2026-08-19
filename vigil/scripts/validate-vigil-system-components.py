#!/usr/bin/env python3
"""Validate optional architectural component roles in VIGIL system_context blocks."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
VIGIL_DIR = ROOT / "vigil"
SCHEMA_PATH = VIGIL_DIR / "VIGIL.Schema.json"
RECORD_ROOTS = (
    VIGIL_DIR / "records" / "observations",
    VIGIL_DIR / "records" / "failures",
    VIGIL_DIR / "records" / "proposals",
    VIGIL_DIR / "records" / "patches",
)


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def allowed_component_roles() -> set[str]:
    schema = load_json(SCHEMA_PATH)
    values = schema.get("system_context_rules", {}).get("allowed_component_role_values", [])
    if not isinstance(values, list) or not values:
        raise ValueError("VIGIL.Schema.json must define non-empty allowed_component_role_values")
    roles = {value for value in values if isinstance(value, str) and value.strip()}
    if len(roles) != len(values):
        raise ValueError("allowed_component_role_values must contain unique non-empty strings")
    return roles


def record_files() -> list[Path]:
    files: list[Path] = []
    for root in RECORD_ROOTS:
        if root.exists():
            files.extend(root.rglob("*.json"))
    return sorted(files, key=lambda path: path.as_posix())


def validate() -> int:
    errors: list[str] = []
    try:
        allowed = allowed_component_roles()
    except Exception as exc:  # noqa: BLE001
        print(f"VIGIL component-role validation failed: {exc}", file=sys.stderr)
        return 1

    checked = 0
    classified = 0
    for path in record_files():
        checked += 1
        try:
            record = load_json(path)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{path}: unable to read JSON: {exc}")
            continue
        if not isinstance(record, dict):
            continue
        context = record.get("system_context")
        if not isinstance(context, dict) or "component_role" not in context:
            continue
        classified += 1
        roles = context.get("component_role")
        if not isinstance(roles, list) or not roles:
            errors.append(f"{path}: system_context.component_role must be a non-empty array when present")
            continue
        if any(not isinstance(role, str) or not role.strip() for role in roles):
            errors.append(f"{path}: system_context.component_role must contain only non-empty strings")
            continue
        if len(roles) != len(set(roles)):
            errors.append(f"{path}: system_context.component_role must not contain duplicates")
        unknown = sorted(set(roles) - allowed)
        if unknown:
            errors.append(
                f"{path}: system_context.component_role contains non-canonical values: {', '.join(unknown)}"
            )

    if errors:
        print("VIGIL component-role validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "VIGIL component-role validation passed: "
        f"{checked} records checked, {classified} records carry component_role."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(validate())
