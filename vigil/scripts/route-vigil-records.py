#!/usr/bin/env python3
"""Route individual VIGIL record files into their status/type folders."""

from __future__ import annotations

import json
import shutil
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
VIGIL_DIR = ROOT / "vigil"
RECORDS_ROOT = VIGIL_DIR / "records"
OPEN_DIR = RECORDS_ROOT / "open"
CLUSTERS_DIR = RECORDS_ROOT / "clusters"
CLOSED_DIR = RECORDS_ROOT / "closed"
RECORD_DIRS = [OPEN_DIR, CLUSTERS_DIR, CLOSED_DIR]
CLOSED_STATUSES = {"closed-no-action", "closed-actioned"}
OPEN_STATUSES = {"active", "proposal", "deferred", "watching", "routed", "open", "clustered"}


def record_files() -> list[Path]:
    files: list[Path] = []
    for directory in RECORD_DIRS:
        if directory.exists():
            files.extend(directory.glob("*.json"))
    return sorted(files, key=lambda path: path.as_posix())


def load_record(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        record = json.load(handle)
    if not isinstance(record, dict):
        raise TypeError(f"{path} must contain one JSON object")
    return record


def target_directory(record: dict[str, Any]) -> Path | None:
    status = record.get("status")
    if status in CLOSED_STATUSES:
        return CLOSED_DIR
    if record.get("record_type") == "cluster":
        return CLUSTERS_DIR
    if status in OPEN_STATUSES:
        return OPEN_DIR
    return None


def route() -> int:
    moved = 0
    for path in record_files():
        record = load_record(path)
        target_dir = target_directory(record)
        if target_dir is None:
            print(f"Skipped {path}: unrecognised status {record.get('status')!r}")
            continue
        target_dir.mkdir(parents=True, exist_ok=True)
        target_path = target_dir / path.name
        if path == target_path:
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
