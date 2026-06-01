#!/usr/bin/env python3
"""Route misplaced individual VIGIL record files into canonical type/year folders."""

from __future__ import annotations

import json
import shutil
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
VIGIL_DIR = ROOT / "vigil"
RECORDS_ROOT = VIGIL_DIR / "records"
TYPE_DIR = {
    "observation": "observations",
    "failure_mode": "failures",
    "proposal": "proposals",
    "patch": "patches",
    "patch_note": "patches",
}


def record_files() -> list[Path]:
    """Recursively scan individual VIGIL record JSON files under vigil/records/."""
    if not RECORDS_ROOT.exists():
        return []
    return sorted(RECORDS_ROOT.rglob("*.json"), key=lambda path: path.as_posix())


def load_record(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        record = json.load(handle)
    if not isinstance(record, dict):
        raise TypeError(f"{path} must contain one JSON object")
    return record


def id_year(record: dict[str, Any]) -> str | None:
    record_id = record.get("id")
    if not isinstance(record_id, str):
        return None
    parts = record_id.split("-")
    if len(parts) < 4 or parts[0] != "VIGIL":
        return None
    return parts[1]


def target_directory(record: dict[str, Any]) -> Path | None:
    """Return canonical type/year directory; record_state never controls the path."""
    record_state = record.get("record_state")
    if record_state is None:
        print(f"Skipped record without record_state: {record.get('id')!r}")
        return None
    folder = TYPE_DIR.get(str(record.get("record_type", "")))
    year = id_year(record)
    if folder is None or year is None:
        return None
    return RECORDS_ROOT / folder / year


def route() -> int:
    moved = 0
    for path in record_files():
        record = load_record(path)
        target_dir = target_directory(record)
        if target_dir is None:
            print(f"Skipped {path}: unable to derive canonical type/year path")
            continue
        target_dir.mkdir(parents=True, exist_ok=True)
        target_path = target_dir / path.name
        if path.resolve() == target_path.resolve():
            continue
        if target_path.exists():
            raise FileExistsError(f"Refusing to overwrite {target_path}")
        shutil.move(path.as_posix(), target_path.as_posix())
        moved += 1
        print(f"Moved {path} -> {target_path}")
    print(f"VIGIL record routing complete: {moved} file(s) moved.")
    return 0


if __name__ == "__main__":
    raise SystemExit(route())
