#!/usr/bin/env python3
"""Run VIGIL lifecycle, observatory-boundary, and interpretive-provenance validation."""

from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
MODULE_PATH = SCRIPT_DIR / "validate-vigil-lifecycle.py"
BOUNDARY_PATH = SCRIPT_DIR / "validate-vigil-cam-boundary.py"
PROVENANCE_PATH = SCRIPT_DIR / "validate-vigil-interpretive-provenance.py"
DRAFTS_PATH = SCRIPT_DIR.parent / "drafts"


def load_module() -> Any:
    spec = importlib.util.spec_from_file_location("vigil_lifecycle_validation", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load lifecycle validator from {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_draft_reference_records() -> dict[str, dict[str, Any]]:
    """Load withdrawn records for reference resolution only.

    Draft records are not validated as canonical/public records and are never added to
    generated public registries. Their retained IDs may still be cited by public FM or
    RESEARCH records as historical/provenance relationships.
    """
    records: dict[str, dict[str, Any]] = {}
    for folder in ("proposals", "patches", "learn"):
        root = DRAFTS_PATH / folder
        if not root.exists():
            continue
        for path in sorted(root.rglob("*.json")):
            try:
                record = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                continue
            record_id = record.get("id") if isinstance(record, dict) else None
            if isinstance(record_id, str) and record_id:
                records[record_id] = record
    return records


def main() -> int:
    module = load_module()
    original_failure = module.validate_failure
    original_proposal = module.validate_proposal
    draft_reference_records = load_draft_reference_records()

    def reference_records(records: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
        return {**draft_reference_records, **records}

    def validate_failure(record_id, record, path, records, errors) -> None:
        """Preserve verification-pending semantics and resolve withdrawn draft references.

        A newly routed FM may legitimately await its first exact Caelestis coverage
        assessment. The lifecycle validator historically requires every
        corpus_coverage.corpus_commit value to be non-empty, even for
        classification == "verification-pending". Validate that state with an
        ephemeral marker only; do not write a false commit into the governed source
        record. Draft PROP/PATCH/LEARN records may resolve retained historical links,
        but are not themselves canonical/public validation targets.
        """
        validation_record = record
        coverage = record.get("corpus_coverage")
        if (
            isinstance(coverage, dict)
            and coverage.get("classification") == "verification-pending"
            and not str(coverage.get("corpus_commit", "")).strip()
        ):
            validation_record = copy.deepcopy(record)
            validation_record["corpus_coverage"]["corpus_commit"] = (
                "pending-exact-current-branch-assessment"
            )
        original_failure(
            record_id,
            validation_record,
            path,
            reference_records(records),
            errors,
        )

    def validate_proposal(record, path, records, errors) -> None:
        original_proposal(record, path, reference_records(records), errors)
        resolution = record.get("resolution_status")
        if isinstance(resolution, dict) and resolution.get("status") == "resolved-by-patch":
            resolved_by = resolution.get("resolved_by", [])
            if not isinstance(resolved_by, list) or not resolved_by:
                errors.append(f"{path}: resolved-by-patch proposal requires at least one resolving patch")

    module.validate_failure = validate_failure
    module.validate_proposal = validate_proposal
    lifecycle_status = module.main()
    if lifecycle_status:
        return lifecycle_status

    for validator in (BOUNDARY_PATH, PROVENANCE_PATH):
        completed = subprocess.run([sys.executable, str(validator)], check=False)
        if completed.returncode:
            return completed.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
