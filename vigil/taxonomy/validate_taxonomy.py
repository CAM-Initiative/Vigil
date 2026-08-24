#!/usr/bin/env python3
"""Validate the VIGIL Failure Taxonomy schema and catalogue invariants."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
SCHEMA_PATH = ROOT / "VIGIL.FailureTaxonomy.Schema.json"
INDEX_PATH = ROOT / "VIGIL.FailureTaxonomy.Index.json"
FAMILIES_DIR = ROOT / "families"
MIGRATION_LEDGER = ROOT / "migration" / "Caelestis.LegacyFailure.MigrationLedger.json"
RELATION_TYPES = {
    "child_of", "parent_of", "peer_of", "distinguish_from",
    "can_cooccur_with", "may_result_in", "may_be_result_of",
}
MIGRATION_DISPOSITIONS = {
    "EXISTING_FAMILY", "NEW_FAMILY_CANDIDATE", "NEW_CLASS_IN_EXISTING_FAMILY",
    "VARIANT_OF_EXISTING_CLASS", "SPLIT_REQUIRED", "DUPLICATE_OR_SEMANTIC_OVERLAP",
    "HARM_OR_CONSEQUENCE_AXIS", "MANIFESTATION_OR_LOCUS_AXIS", "OTHER_ORTHOGONAL_AXIS",
    "NOT_A_FAILURE_MECHANISM", "REQUIRES_REVIEW",
}


def load_json(path: Path) -> tuple[Any | None, list[str]]:
    try:
        return json.loads(path.read_text(encoding="utf-8")), []
    except Exception as exc:
        return None, [f"{path}: invalid JSON: {exc}"]


def resolve_ref(schema_root: dict, ref: str) -> dict:
    if not ref.startswith("#/"):
        raise ValueError(f"unsupported non-local schema reference {ref!r}")
    value: Any = schema_root
    for part in ref[2:].split("/"):
        value = value[part.replace("~1", "/").replace("~0", "~")]
    if not isinstance(value, dict):
        raise ValueError(f"schema reference {ref!r} does not resolve to an object")
    return value


def schema_errors(value: Any, schema: dict, schema_root: dict, location: str = "$") -> list[str]:
    """Validate the JSON-Schema keywords used by the taxonomy contract.

    Keeping this small validator in-tree makes schema validation deterministic in
    environments that do not ship the optional ``jsonschema`` package.
    """
    if "$ref" in schema:
        return schema_errors(value, resolve_ref(schema_root, schema["$ref"]), schema_root, location)

    errors: list[str] = []
    expected = schema.get("type")
    type_ok = {
        "object": isinstance(value, dict),
        "array": isinstance(value, list),
        "string": isinstance(value, str),
        "integer": isinstance(value, int) and not isinstance(value, bool),
        "number": isinstance(value, (int, float)) and not isinstance(value, bool),
        "boolean": isinstance(value, bool),
        "null": value is None,
    }.get(expected, True)
    if not type_ok:
        return [f"{location}: expected {expected}, found {type(value).__name__}"]

    if "const" in schema and value != schema["const"]:
        errors.append(f"{location}: must equal {schema['const']!r}")
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{location}: {value!r} is not an allowed value")

    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0):
            errors.append(f"{location}: string is shorter than {schema['minLength']}")
        if "pattern" in schema and re.fullmatch(schema["pattern"], value) is None:
            errors.append(f"{location}: {value!r} does not match {schema['pattern']!r}")

    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            errors.append(f"{location}: array has fewer than {schema['minItems']} item(s)")
        if schema.get("uniqueItems"):
            encoded = [json.dumps(item, sort_keys=True, ensure_ascii=False) for item in value]
            if len(encoded) != len(set(encoded)):
                errors.append(f"{location}: array items must be unique")
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for index, item in enumerate(value):
                errors.extend(schema_errors(item, item_schema, schema_root, f"{location}[{index}]"))

    if isinstance(value, dict):
        properties = schema.get("properties", {})
        for required in schema.get("required", []):
            if required not in value:
                errors.append(f"{location}: missing required property {required!r}")
        if schema.get("additionalProperties") is False:
            for key in value.keys() - properties.keys():
                errors.append(f"{location}: unexpected property {key!r}")
        for key, child_schema in properties.items():
            if key in value:
                errors.extend(schema_errors(value[key], child_schema, schema_root, f"{location}.{key}"))
    return errors


def validate_migration_ledger(family_ids: set[str], class_ids: set[str]) -> list[str]:
    errors: list[str] = []
    ledger, load_errors = load_json(MIGRATION_LEDGER)
    errors.extend(load_errors)
    if not isinstance(ledger, dict):
        return errors
    if set(ledger.get("controlled_dispositions", [])) != MIGRATION_DISPOSITIONS:
        errors.append(f"{MIGRATION_LEDGER}: controlled_dispositions does not match the validator contract")
    if ledger.get("portable_taxonomy_dependency") is not False:
        errors.append(f"{MIGRATION_LEDGER}: portable_taxonomy_dependency must be false")
    entries = ledger.get("entries")
    if not isinstance(entries, list) or not entries:
        return errors + [f"{MIGRATION_LEDGER}: entries must be a non-empty array"]
    inventory_ids: set[str] = set()
    source_ids: set[str] = set()
    primary_sources = set(ledger.get("source_corpus", {}).get("primary_sources", []))
    required = {
        "inventory_id", "source_identifier", "source_name", "legacy_family", "source_location",
        "concise_source_definition", "structural_invariant_inferred", "candidate_portable_family",
        "candidate_class", "disposition", "rationale", "overlap_notes", "split_notes",
        "related_source_entries", "review_state", "evidence_basis",
    }
    for number, item in enumerate(entries):
        where = f"{MIGRATION_LEDGER}: entries[{number}]"
        if not isinstance(item, dict):
            errors.append(f"{where} must be an object")
            continue
        missing = required - item.keys()
        if missing:
            errors.append(f"{where} missing fields: {', '.join(sorted(missing))}")
        inventory_id = item.get("inventory_id")
        source_id = item.get("source_identifier")
        if inventory_id in inventory_ids:
            errors.append(f"{where}: duplicate inventory_id {inventory_id}")
        inventory_ids.add(inventory_id)
        if source_id in source_ids:
            errors.append(f"{where}: duplicate source_identifier {source_id}")
        source_ids.add(source_id)
        source_location = item.get("source_location")
        if not isinstance(source_location, dict):
            errors.append(f"{where}: source_location must be an object")
        else:
            for field in ("repository", "ref", "commit", "path", "section", "line"):
                if field not in source_location:
                    errors.append(f"{where}: source_location missing {field}")
            if source_location.get("path") not in primary_sources:
                errors.append(f"{where}: source path is absent from source_corpus.primary_sources")
        if item.get("disposition") not in MIGRATION_DISPOSITIONS:
            errors.append(f"{where}: invalid disposition {item.get('disposition')!r}")
        if item.get("disposition") == "SPLIT_REQUIRED" and not item.get("split_notes"):
            errors.append(f"{where}: SPLIT_REQUIRED requires split_notes")
        for field in ("source_name", "concise_source_definition", "structural_invariant_inferred", "rationale"):
            if not isinstance(item.get(field), str) or not item[field].strip():
                errors.append(f"{where}: {field} must be meaningful text")
        family_candidate = item.get("candidate_portable_family")
        if isinstance(family_candidate, dict) and "family_id" in family_candidate:
            if family_candidate["family_id"] not in family_ids:
                errors.append(f"{where}: unknown candidate family ID {family_candidate['family_id']}")
        class_candidate = item.get("candidate_class")
        if isinstance(class_candidate, dict) and "class_id" in class_candidate:
            if class_candidate["class_id"] not in class_ids:
                errors.append(f"{where}: unknown candidate class ID {class_candidate['class_id']}")
    return errors


def validate_catalogue(paths: list[Path]) -> tuple[list[str], int]:
    errors: list[str] = []
    schema, schema_load_errors = load_json(SCHEMA_PATH)
    index, index_load_errors = load_json(INDEX_PATH)
    errors.extend(schema_load_errors)
    errors.extend(index_load_errors)
    if not isinstance(schema, dict) or not isinstance(index, dict):
        return errors, 0

    indexed = index.get("families")
    if not isinstance(indexed, list):
        return errors + [f"{INDEX_PATH}: families must be an array"], 0

    actual_files = {p.resolve() for p in FAMILIES_DIR.glob("*.json")}
    selected_files = {p.resolve() for p in paths}
    if selected_files != actual_files:
        missing = sorted(str(p) for p in actual_files - selected_files)
        extra = sorted(str(p) for p in selected_files - actual_files)
        if missing:
            errors.append(f"catalogue validation omitted family file(s): {', '.join(missing)}")
        if extra:
            errors.append(f"catalogue validation included non-family file(s): {', '.join(extra)}")

    index_files: set[Path] = set()
    index_by_id: dict[str, dict] = {}
    for number, entry in enumerate(indexed):
        if not isinstance(entry, dict):
            errors.append(f"{INDEX_PATH}: families[{number}] must be an object")
            continue
        family_id = entry.get("family_id")
        file_value = entry.get("file")
        if not isinstance(family_id, str):
            errors.append(f"{INDEX_PATH}: families[{number}].family_id must be a string")
        elif family_id in index_by_id:
            errors.append(f"{INDEX_PATH}: duplicate indexed family ID {family_id}")
        else:
            index_by_id[family_id] = entry
        if not isinstance(file_value, str):
            errors.append(f"{INDEX_PATH}: families[{number}].file must be a string")
        else:
            index_files.add((ROOT / file_value).resolve())
    if index_files != actual_files:
        errors.append(f"{INDEX_PATH}: indexed files do not exactly match families/*.json")

    loaded: list[tuple[Path, dict]] = []
    for path in sorted(actual_files):
        data, load_errors = load_json(path)
        errors.extend(load_errors)
        if not isinstance(data, dict):
            continue
        loaded.append((path, data))
        for error in schema_errors(data, schema, schema):
            errors.append(f"{path}: schema {error}")

    family_by_id: dict[str, tuple[Path, dict]] = {}
    family_code_owner: dict[str, Path] = {}
    class_by_id: dict[str, tuple[Path, dict]] = {}
    class_code_owner: dict[str, Path] = {}
    relation_rows: list[tuple[Path, dict, dict]] = []

    for path, data in loaded:
        family = data.get("family", {})
        classes = data.get("classes", [])
        if not isinstance(family, dict) or not isinstance(classes, list):
            continue
        family_id = family.get("family_id")
        family_code = family.get("family_code")
        if isinstance(family_id, str):
            if family_id in family_by_id:
                errors.append(f"{path}: duplicate family ID {family_id}; first in {family_by_id[family_id][0]}")
            else:
                family_by_id[family_id] = (path, family)
            if not path.name.startswith(f"{family_id}-"):
                errors.append(f"{path}: filename must begin with immutable family ID {family_id}-")
        if isinstance(family_code, str):
            if family_code in family_code_owner:
                errors.append(f"{path}: duplicate family code {family_code}; first in {family_code_owner[family_code]}")
            else:
                family_code_owner[family_code] = path

        class_ids = [item.get("class_id") for item in classes if isinstance(item, dict)]
        class_codes = [item.get("class_code") for item in classes if isinstance(item, dict)]
        if family.get("allowed_class_ids") != class_ids:
            errors.append(f"{path}: family.allowed_class_ids does not match class order and membership")
        if family.get("allowed_class_codes") != class_codes:
            errors.append(f"{path}: family.allowed_class_codes does not match class order and membership")

        index_entry = index_by_id.get(family_id)
        if not index_entry:
            errors.append(f"{path}: family {family_id!r} is absent from the index")
        else:
            expected = {
                "family_code": family_code,
                "name": family.get("name"),
                "version": family.get("version"),
                "status": family.get("status"),
                "class_count": len(classes),
                "file": str(path.relative_to(ROOT)),
            }
            for key, value in expected.items():
                if index_entry.get(key) != value:
                    errors.append(f"{INDEX_PATH}: {family_id}.{key} is {index_entry.get(key)!r}; expected {value!r}")

        for item in classes:
            if not isinstance(item, dict):
                continue
            class_id = item.get("class_id")
            class_code = item.get("class_code")
            if item.get("family_id") != family_id:
                errors.append(f"{path}: {class_id} has family_id {item.get('family_id')!r}; expected {family_id!r}")
            if isinstance(class_id, str):
                if class_id in class_by_id:
                    errors.append(f"{path}: duplicate class ID {class_id}; first in {class_by_id[class_id][0]}")
                else:
                    class_by_id[class_id] = (path, item)
            if isinstance(class_code, str):
                if class_code in class_code_owner:
                    errors.append(f"{path}: duplicate class code {class_code}; first in {class_code_owner[class_code]}")
                else:
                    class_code_owner[class_code] = path
            relationships = item.get("relationships", [])
            if not isinstance(relationships, list):
                continue
            seen: set[tuple[str, str]] = set()
            for relation in relationships:
                if not isinstance(relation, dict):
                    continue
                key = (str(relation.get("type")), str(relation.get("target_id")))
                if key in seen:
                    errors.append(f"{path}: {class_id} repeats relationship {key[0]} -> {key[1]}")
                seen.add(key)
                relation_rows.append((path, item, relation))

    removed = index.get("removed_ids", [])
    if not isinstance(removed, list) or len(removed) != len(set(removed)):
        errors.append(f"{INDEX_PATH}: removed_ids must be a unique array")
        removed = []
    allocated_ids = set(family_by_id) | set(class_by_id)
    for removed_id in removed:
        if removed_id in allocated_ids:
            errors.append(f"{INDEX_PATH}: removed ID {removed_id} is still allocated")

    for path, item, relation in relation_rows:
        source_id = item.get("class_id")
        target_id = relation.get("target_id")
        relation_type = relation.get("type")
        if relation_type not in RELATION_TYPES:
            errors.append(f"{path}: {source_id} has invalid relationship type {relation_type!r}")
        if target_id == source_id:
            errors.append(f"{path}: {source_id} cannot relate to itself")
        if target_id in removed:
            errors.append(f"{path}: {source_id} references removed ID {target_id}")
        target = class_by_id.get(target_id)
        if target is None:
            errors.append(f"{path}: {source_id} references missing class {target_id!r}")
            continue
        if relation_type == "child_of":
            parent = target[1]
            if item.get("abstraction") != "variant":
                errors.append(f"{path}: only a variant may use child_of ({source_id})")
            if parent.get("abstraction") != "class":
                errors.append(f"{path}: variant parent {target_id} must be a class")
            if parent.get("family_id") != item.get("family_id"):
                errors.append(f"{path}: variant {source_id} cannot have a parent in another family")

    for class_id, (path, item) in class_by_id.items():
        if item.get("abstraction") == "variant":
            parents = [r for r in item.get("relationships", []) if r.get("type") == "child_of"]
            if len(parents) != 1:
                errors.append(f"{path}: variant {class_id} must declare exactly one child_of relationship")

    supersession_targets: dict[str, str] = {}
    for identifier, (_, value) in {**family_by_id, **class_by_id}.items():
        supersession = value.get("supersession")
        if supersession is None:
            continue
        target = supersession.get("superseded_by_id")
        if value.get("status") != "deprecated":
            errors.append(f"{identifier}: supersession metadata requires deprecated status")
        if target:
            if target == identifier:
                errors.append(f"{identifier}: cannot supersede itself")
            elif target not in allocated_ids:
                errors.append(f"{identifier}: supersession target {target} is not allocated")
            supersession_targets[identifier] = target
    for start in supersession_targets:
        seen: set[str] = set()
        current = start
        while current in supersession_targets:
            if current in seen:
                errors.append(f"{start}: cyclic supersession chain")
                break
            seen.add(current)
            current = supersession_targets[current]

    errors.extend(validate_migration_ledger(set(family_by_id), set(class_by_id)))

    return errors, sum(len(data.get("classes", [])) for _, data in loaded)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path, help="all family files; defaults to the indexed catalogue")
    args = parser.parse_args()
    paths = args.paths or sorted(FAMILIES_DIR.glob("*.json"))
    errors, class_count = validate_catalogue(paths)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        sys.exit(1)
    print(f"Validated {len(paths)} family file(s) against JSON Schema: {class_count} classes; catalogue integrity OK")


if __name__ == "__main__":
    main()
