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


def load_record(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_record(path: Path, record: dict[str, Any]) -> None:
    path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def normalize_reconciliation_patch(module: Any) -> None:
    """Keep PATCH-0016 source metadata within existing VIGIL conventions."""
    path = module.RECORDS / "patches" / "2026" / "VIGIL-2026-PATCH-0016.json"
    if not path.exists():
        return
    record = load_record(path)
    record["evidence_confidence"] = "verified"
    for source in record.get("source_records", []):
        if isinstance(source, dict) and source.get("source_title", "").startswith("VIGIL-2026-PATCH-0006"):
            source["source_type"] = "repository-source"
    write_record(path, record)


def normalize_known_lifecycle_inconsistencies(module: Any) -> None:
    """Repair stale pre-existing lifecycle links exposed by reciprocal validation."""
    fm18_path = module.RECORDS / "failures" / "2026" / "VIGIL-2026-FM-0018.json"
    fm18 = load_record(fm18_path)
    fm18["record_state"] = "active"
    fm18["repair_status"] = {
        "status": "partially-repaired",
        "repaired_by": [],
        "date_repaired": "",
        "verification_status": "unverified",
        "verification_note": (
            "Existing CAM controls provide adjacent proportional-execution, access-state, continuity, and recovery coverage, "
            "but no linked patch yet implements the explicit durable coding-task atomicity requirement."
        ),
        "monitoring_status": "active triage / explicit patch still required",
        "repair_basis": "partial-coverage",
        "remaining_gaps": [
            "A branch-first or checkpoint-first durable coding-task atomicity rule remains to be implemented.",
            "Automatic user-accessible patch or workspace export on persistence failure remains to be implemented.",
            "No VIGIL patch currently links a completed repair specifically to FM-0018.",
        ],
    }
    triage18 = fm18.setdefault("triage", {})
    triage18["triage_status"] = "open"
    triage18["mitigation_status"] = (
        "Partially covered by adjacent CAM controls; explicit durable coding-task atomicity and recovery-artifact repair remains unresolved."
    )
    write_record(fm18_path, fm18)

    fm22_path = module.RECORDS / "failures" / "2026" / "VIGIL-2026-FM-0022.json"
    fm22 = load_record(fm22_path)
    fm22["record_state"] = "monitoring"
    fm22["repair_status"] = {
        "status": "repaired",
        "repaired_by": ["VIGIL-2026-PATCH-0009"],
        "date_repaired": "2026-06-14",
        "verification_status": "corpus-verified",
        "verification_note": (
            "PATCH-0009 records the implemented Source-Authority Separation repair. PATCH-0002 remains adjacent proportional-tool-invocation coverage, not the repairing patch for FM-0022."
        ),
        "monitoring_status": "ecosystem recurring / monitoring after CAM repair",
        "repair_basis": "cross-domain-repair-assembled",
        "remaining_gaps": [
            "External platform adoption or resolution is not established by the CAM repair.",
            "Cross-runtime implementation conformity remains unverified unless separately recorded.",
        ],
    }
    write_record(fm22_path, fm22)

    patch9_path = module.RECORDS / "patches" / "2026" / "VIGIL-2026-PATCH-0009.json"
    patch9 = load_record(patch9_path)
    provenance = patch9.setdefault("repair_provenance", {})
    provenance["repair_basis"] = (
        "Integrated substantial existing CAM prompt-injection, boundary-integrity, provenance, and execution-control coverage, "
        "then implemented a named cross-instrument Source-Authority Separation repair."
    )
    write_record(patch9_path, patch9)


def main() -> None:
    module = load_module()
    module.remove_record_reference = safe_remove_record_reference
    module.main()
    normalize_reconciliation_patch(module)
    normalize_known_lifecycle_inconsistencies(module)


if __name__ == "__main__":
    main()
