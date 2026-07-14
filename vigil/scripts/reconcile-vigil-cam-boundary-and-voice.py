#!/usr/bin/env python3
"""One-time VIGIL/CAM boundary correction and July 2026 voice evidence migration.

This migration has been applied on the reconciliation branch. It remains only as
an auditable, idempotent record of the deterministic transformation. VIGIL is
the observatory; CAM/Caelestis is the patched corpus.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
RECORDS = VIGIL / "records"
INVALID_PATCHES = {"VIGIL-2026-PATCH-0016", "VIGIL-2026-PATCH-0020"}


def load(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain one JSON object")
    return value


def write(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def cleanse_refs(value: Any) -> Any:
    if isinstance(value, list):
        return [
            cleanse_refs(item)
            for item in value
            if not (isinstance(item, str) and item in INVALID_PATCHES)
        ]
    if isinstance(value, dict):
        cleaned = {key: cleanse_refs(item) for key, item in value.items()}
        follow = cleaned.get("follow_on_reconciliation")
        if isinstance(follow, dict) and (
            follow.get("completed_by") in INVALID_PATCHES
            or follow.get("resolved_by") in INVALID_PATCHES
        ):
            cleaned.pop("follow_on_reconciliation", None)
        return cleaned
    if isinstance(value, str) and value in INVALID_PATCHES:
        return ""
    return value


def remove_invalid_patch_records_and_references() -> None:
    for patch_id in INVALID_PATCHES:
        path = RECORDS / "patches" / "2026" / f"{patch_id}.json"
        if path.exists():
            path.unlink()

    for path in sorted(RECORDS.rglob("*.json")):
        write(path, cleanse_refs(load(path)))


def assert_migration_outputs() -> None:
    required = [
        RECORDS / "observations" / "2026" / "VIGIL-2026-OBS-0011.json",
        RECORDS / "observations" / "2026" / "VIGIL-2026-OBS-0012.json",
        RECORDS / "observations" / "2026" / "VIGIL-2026-OBS-0013.json",
        RECORDS / "failures" / "2026" / "VIGIL-2026-FM-0029.json",
        RECORDS / "failures" / "2026" / "VIGIL-2026-FM-0030.json",
        RECORDS / "failures" / "2026" / "VIGIL-2026-FM-0031.json",
        RECORDS / "failures" / "2026" / "VIGIL-2026-FM-0032.json",
        RECORDS / "proposals" / "2026" / "VIGIL-2026-PROP-0012.json",
        RECORDS / "proposals" / "2026" / "VIGIL-2026-PROP-0013.json",
        RECORDS / "patches" / "2026" / "VIGIL-2026-PATCH-0021.json",
    ]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise RuntimeError(
            "Voice reconciliation outputs are missing. Restore them from the "
            "applied reconciliation commit rather than recreating VIGIL-only patches:\n- "
            + "\n- ".join(missing)
        )


def main() -> None:
    remove_invalid_patch_records_and_references()
    assert_migration_outputs()
    print(
        "VIGIL/CAM boundary migration already applied: invalid VIGIL-maintenance "
        "patches removed and voice evidence records present."
    )


if __name__ == "__main__":
    main()
