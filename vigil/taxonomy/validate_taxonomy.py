#!/usr/bin/env python3
"""Validate structural integrity of VIGIL Failure Taxonomy family JSON files.

This validator uses only the Python standard library. JSON Schema remains the
machine-readable shape contract; this script checks cross-field and cross-file
invariants that matter as the taxonomy grows.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

RELATION_TYPES = {
    "child_of", "parent_of", "peer_of", "distinguish_from",
    "can_cooccur_with", "may_result_in", "may_be_result_of",
}


def load_family(path: Path) -> tuple[dict | None, list[str]]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return None, [f"{path}: invalid JSON: {exc}"]
    if not isinstance(data, dict):
        return None, [f"{path}: top-level value must be an object"]
    return data, []


def validate_family(path: Path, data: dict) -> list[str]:
    errors: list[str] = []
    family = data.get("family")
    classes = data.get("classes")
    if not isinstance(family, dict):
        return [f"{path}: missing object 'family'"]
    if not isinstance(classes, list) or not classes:
        return [f"{path}: 'classes' must be a non-empty array"]

    family_code = family.get("code")
    if not isinstance(family_code, str) or not family_code:
        errors.append(f"{path}: family.code must be a non-empty string")

    codes = [item.get("code") for item in classes if isinstance(item, dict)]
    if len(codes) != len(classes) or any(not isinstance(code, str) for code in codes):
        return errors + [f"{path}: every class must have a string code"]

    duplicates = sorted({code for code in codes if codes.count(code) > 1})
    if duplicates:
        errors.append(f"{path}: duplicate class codes: {', '.join(duplicates)}")

    allowed = family.get("allowed_codes")
    if not isinstance(allowed, list):
        errors.append(f"{path}: family.allowed_codes must be an array")
    else:
        missing = sorted(set(codes) - set(allowed))
        extra = sorted(set(allowed) - set(codes))
        if missing:
            errors.append(f"{path}: allowed_codes missing: {', '.join(missing)}")
        if extra:
            errors.append(f"{path}: allowed_codes contains undefined codes: {', '.join(extra)}")
        if len(allowed) != len(set(allowed)):
            errors.append(f"{path}: allowed_codes contains duplicates")

    code_set = set(codes)
    for item in classes:
        code = item["code"]
        if family_code and not code.startswith(f"{family_code}."):
            errors.append(f"{path}: {code} does not use family prefix {family_code}.")

        abstraction = item.get("abstraction")
        if abstraction not in {"class", "variant"}:
            errors.append(f"{path}: {code} has invalid abstraction {abstraction!r}")

        relationships = item.get("relationships", [])
        if not isinstance(relationships, list):
            errors.append(f"{path}: {code}.relationships must be an array")
            continue

        has_parent = False
        seen_relations: set[tuple[str, str]] = set()
        for relation in relationships:
            if not isinstance(relation, dict):
                errors.append(f"{path}: {code} has non-object relationship")
                continue
            relation_type = relation.get("type")
            target = relation.get("target_code")
            if relation_type not in RELATION_TYPES:
                errors.append(f"{path}: {code} has invalid relationship type {relation_type!r}")
            if not isinstance(target, str) or not target:
                errors.append(f"{path}: {code} has relationship without target_code")
                continue
            key = (str(relation_type), target)
            if key in seen_relations:
                errors.append(f"{path}: {code} repeats relationship {relation_type} -> {target}")
            seen_relations.add(key)
            if target == code:
                errors.append(f"{path}: {code} cannot relate to itself")
            if family_code and target.startswith(f"{family_code}.") and target not in code_set:
                errors.append(f"{path}: {code} references undefined in-family target {target}")
            if relation_type == "child_of":
                has_parent = True

        if abstraction == "variant" and not has_parent:
            errors.append(f"{path}: variant {code} must declare at least one child_of relationship")

        recognition = item.get("recognition", {})
        required = recognition.get("required_conditions") if isinstance(recognition, dict) else None
        if not isinstance(required, list) or not required:
            errors.append(f"{path}: {code} must have recognition.required_conditions")

        exclusions = item.get("exclusions")
        if not isinstance(exclusions, list) or not exclusions:
            errors.append(f"{path}: {code} must have at least one exclusion boundary")

        if not isinstance(item.get("plain_english"), str) or not item["plain_english"].strip():
            errors.append(f"{path}: {code} must have plain_english")
        if not isinstance(item.get("definition"), str) or not item["definition"].strip():
            errors.append(f"{path}: {code} must have definition")

    return errors


def validate_catalogue(loaded: list[tuple[Path, dict]]) -> list[str]:
    """Check invariants that can only be enforced across the whole catalogue."""
    errors: list[str] = []
    family_owners: dict[str, Path] = {}
    class_owners: dict[str, Path] = {}
    all_codes: set[str] = set()

    for path, data in loaded:
        family = data.get("family")
        classes = data.get("classes")
        if not isinstance(family, dict) or not isinstance(classes, list):
            continue
        family_code = family.get("code")
        if isinstance(family_code, str) and family_code:
            if family_code in family_owners:
                errors.append(
                    f"{path}: duplicate family code {family_code}; already defined in {family_owners[family_code]}"
                )
            else:
                family_owners[family_code] = path
            all_codes.add(family_code)
        for item in classes:
            if not isinstance(item, dict):
                continue
            code = item.get("code")
            if not isinstance(code, str) or not code:
                continue
            if code in class_owners:
                errors.append(
                    f"{path}: duplicate catalogue class code {code}; already defined in {class_owners[code]}"
                )
            else:
                class_owners[code] = path
            all_codes.add(code)

    for path, data in loaded:
        classes = data.get("classes")
        if not isinstance(classes, list):
            continue
        for item in classes:
            if not isinstance(item, dict):
                continue
            code = item.get("code")
            for relation in item.get("relationships", []):
                if not isinstance(relation, dict):
                    continue
                target = relation.get("target_code")
                if isinstance(target, str) and target.startswith("VIGIL.FF.") and target not in all_codes:
                    errors.append(f"{path}: {code} references undefined catalogue target {target}")

    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()

    errors: list[str] = []
    loaded: list[tuple[Path, dict]] = []
    for path in args.paths:
        data, load_errors = load_family(path)
        errors.extend(load_errors)
        if data is None:
            continue
        loaded.append((path, data))
        errors.extend(validate_family(path, data))

    errors.extend(validate_catalogue(loaded))

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        sys.exit(1)
    print(
        f"Validated {len(loaded)} taxonomy family file(s): "
        f"{sum(len(data.get('classes', [])) for _, data in loaded)} class(es), catalogue integrity OK"
    )


if __name__ == "__main__":
    main()
