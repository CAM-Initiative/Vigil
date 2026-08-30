#!/usr/bin/env python3
"""Canonical sharded storage and compatibility I/O for the EXTREQ corpus."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any


VIGIL_ROOT = Path(__file__).resolve().parents[1]
EXTERNAL_REQUIREMENTS_ROOT = VIGIL_ROOT / "external_governance" / "requirements"
REQUIREMENTS_ROOT = EXTERNAL_REQUIREMENTS_ROOT / "requirements"
REQUIREMENTS_MANIFEST_PATH = REQUIREMENTS_ROOT / "manifest.json"
REQUIREMENTS_AGGREGATE_PATH = EXTERNAL_REQUIREMENTS_ROOT / "requirements.json"

SOURCE_COMPONENT_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
REQUIREMENT_ID_RE = re.compile(r"^EXTREQ-[A-F0-9]{16}$")
MANIFEST_FIELDS = {"schema_version", "updated_at", "authorship_provenance"}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def json_text(value: Any) -> str:
    return json.dumps(value, indent=2, ensure_ascii=False) + "\n"


def source_version_key(requirement: dict[str, Any]) -> tuple[str, str]:
    return str(requirement.get("external_source_id", "")), str(requirement.get("source_version", ""))


def shard_path(external_source_id: str, source_version: str) -> Path:
    for label, value in (("external_source_id", external_source_id), ("source_version", source_version)):
        if not SOURCE_COMPONENT_RE.fullmatch(value):
            raise ValueError(f"invalid {label} for EXTREQ shard path: {value!r}")
    return REQUIREMENTS_ROOT / external_source_id / f"{source_version}.json"


def iter_shard_paths() -> list[Path]:
    if not REQUIREMENTS_ROOT.is_dir():
        raise ValueError(f"canonical EXTREQ shard directory is absent: {REQUIREMENTS_ROOT}")
    unexpected = sorted(
        path.relative_to(REQUIREMENTS_ROOT).as_posix()
        for path in REQUIREMENTS_ROOT.rglob("*.json")
        if path != REQUIREMENTS_MANIFEST_PATH and len(path.relative_to(REQUIREMENTS_ROOT).parts) != 2
    )
    if unexpected:
        raise ValueError(f"unexpected EXTREQ JSON outside source/version shard layout: {unexpected}")
    paths = sorted(path for path in REQUIREMENTS_ROOT.glob("*/*.json") if path.is_file())
    if not paths:
        raise ValueError(f"canonical EXTREQ shard directory contains no source/version shards: {REQUIREMENTS_ROOT}")
    return paths


def load_requirements_manifest() -> dict[str, Any]:
    manifest = load_json(REQUIREMENTS_MANIFEST_PATH)
    if not isinstance(manifest, dict):
        raise ValueError(f"{REQUIREMENTS_MANIFEST_PATH}: expected JSON object")
    missing = sorted(MANIFEST_FIELDS - set(manifest))
    unexpected = sorted(set(manifest) - MANIFEST_FIELDS)
    if missing or unexpected:
        raise ValueError(
            f"{REQUIREMENTS_MANIFEST_PATH}: manifest fields differ; missing={missing}, unexpected={unexpected}"
        )
    return manifest


def load_requirements() -> list[dict[str, Any]]:
    requirements: list[dict[str, Any]] = []
    seen_ids: dict[str, Path] = {}
    for path in iter_shard_paths():
        source_id = path.parent.name
        source_version = path.stem
        records = load_json(path)
        if not isinstance(records, list):
            raise ValueError(f"{path}: source/version shard must be a JSON array")
        ids: list[str] = []
        for index, record in enumerate(records):
            if not isinstance(record, dict):
                raise ValueError(f"{path}[{index}]: EXTREQ record must be a JSON object")
            if source_version_key(record) != (source_id, source_version):
                raise ValueError(
                    f"{path}[{index}]: record source/version {source_version_key(record)!r} differs from shard path"
                )
            requirement_id = record.get("requirement_id")
            if not isinstance(requirement_id, str) or not REQUIREMENT_ID_RE.fullmatch(requirement_id):
                raise ValueError(f"{path}[{index}]: invalid requirement_id {requirement_id!r}")
            if requirement_id in seen_ids:
                raise ValueError(
                    f"duplicate requirement_id {requirement_id} across {seen_ids[requirement_id]} and {path}"
                )
            seen_ids[requirement_id] = path
            ids.append(requirement_id)
            requirements.append(record)
        if ids != sorted(ids):
            raise ValueError(f"{path}: records must be sorted by requirement_id")
    return sorted(requirements, key=lambda record: record["requirement_id"])


def load_requirements_document() -> dict[str, Any]:
    requirements = load_requirements()
    return {
        **load_requirements_manifest(),
        "requirement_count": len(requirements),
        "requirements": requirements,
    }


def render_requirements_document() -> str:
    return json_text(load_requirements_document())


def write_requirements_document(document: dict[str, Any]) -> None:
    """Write a complete EXTREQ document into canonical shards and refresh its aggregate."""
    if not isinstance(document, dict):
        raise ValueError("EXTREQ document must be a JSON object")
    requirements = document.get("requirements")
    if not isinstance(requirements, list) or not all(isinstance(item, dict) for item in requirements):
        raise ValueError("EXTREQ document requirements must be an array of objects")
    declared_count = document.get("requirement_count")
    if declared_count != len(requirements):
        raise ValueError(
            f"EXTREQ document requirement_count {declared_count!r} differs from {len(requirements)} records"
        )
    manifest = {field: document.get(field) for field in ("schema_version", "updated_at", "authorship_provenance")}
    missing_manifest = sorted(field for field, value in manifest.items() if value is None)
    if missing_manifest:
        raise ValueError(f"EXTREQ document lacks manifest fields: {missing_manifest}")

    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    seen_ids: set[str] = set()
    for record in requirements:
        requirement_id = record.get("requirement_id")
        if not isinstance(requirement_id, str) or not REQUIREMENT_ID_RE.fullmatch(requirement_id):
            raise ValueError(f"invalid requirement_id {requirement_id!r}")
        if requirement_id in seen_ids:
            raise ValueError(f"duplicate requirement_id {requirement_id}")
        seen_ids.add(requirement_id)
        grouped[source_version_key(record)].append(record)

    REQUIREMENTS_ROOT.mkdir(parents=True, exist_ok=True)
    expected_paths: set[Path] = set()
    for (source_id, source_version), records in grouped.items():
        path = shard_path(source_id, source_version)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json_text(sorted(records, key=lambda record: record["requirement_id"])), encoding="utf-8")
        expected_paths.add(path)
    for path in REQUIREMENTS_ROOT.glob("*/*.json"):
        if path not in expected_paths:
            path.unlink()
    for directory in sorted(REQUIREMENTS_ROOT.iterdir() if REQUIREMENTS_ROOT.exists() else [], reverse=True):
        if directory.is_dir() and not any(directory.iterdir()):
            directory.rmdir()

    REQUIREMENTS_MANIFEST_PATH.write_text(json_text(manifest), encoding="utf-8")
    REQUIREMENTS_AGGREGATE_PATH.write_text(render_requirements_document(), encoding="utf-8")


def refresh_requirements_aggregate() -> None:
    REQUIREMENTS_AGGREGATE_PATH.write_text(render_requirements_document(), encoding="utf-8")


def aggregate_is_current() -> bool:
    return (
        REQUIREMENTS_AGGREGATE_PATH.exists()
        and REQUIREMENTS_AGGREGATE_PATH.read_text(encoding="utf-8") == render_requirements_document()
    )
