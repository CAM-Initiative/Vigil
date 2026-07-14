#!/usr/bin/env python3
"""Run the one-time VIGIL reconciliation with safe mixed-list handling."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
MODULE_PATH = SCRIPT_DIR / "reconcile-vigil-lifecycle.py"


def load_module():
    spec = importlib.util.spec_from_file_location("vigil_reconciliation", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load reconciliation module from {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def safe_remove_record_reference(value: Any, record_ids: set[str]) -> Any:
    """Remove string record IDs without attempting to hash structured list items."""
    if isinstance(value, list):
        return [
            safe_remove_record_reference(item, record_ids)
            for item in value
            if not (isinstance(item, str) and item in record_ids)
        ]
    if isinstance(value, dict):
        return {key: safe_remove_record_reference(item, record_ids) for key, item in value.items()}
    return value


def normalize_reconciliation_patch(module: Any) -> None:
    """Keep PATCH-0016 source metadata within existing VIGIL conventions."""
    path = module.RECORDS / "patches" / "2026" / "VIGIL-2026-PATCH-0016.json"
    if not path.exists():
        return
    record = json.loads(path.read_text(encoding="utf-8"))
    record["evidence_confidence"] = "verified"
    for source in record.get("source_records", []):
        if isinstance(source, dict) and source.get("source_title", "").startswith("VIGIL-2026-PATCH-0006"):
            source["source_type"] = "repository-source"
    path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    module = load_module()
    module.remove_record_reference = safe_remove_record_reference
    module.main()
    normalize_reconciliation_patch(module)


if __name__ == "__main__":
    main()
