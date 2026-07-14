#!/usr/bin/env python3
"""Run VIGIL lifecycle, observatory-boundary, and interpretive-provenance validation."""

from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
MODULE_PATH = SCRIPT_DIR / "validate-vigil-lifecycle.py"
BOUNDARY_PATH = SCRIPT_DIR / "validate-vigil-cam-boundary.py"
PROVENANCE_PATH = SCRIPT_DIR / "validate-vigil-interpretive-provenance.py"


def load_module() -> Any:
    spec = importlib.util.spec_from_file_location("vigil_lifecycle_validation", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load lifecycle validator from {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load_module()
    original = module.validate_proposal

    def validate_proposal(record, path, records, errors) -> None:
        original(record, path, records, errors)
        resolution = record.get("resolution_status")
        if isinstance(resolution, dict) and resolution.get("status") == "resolved-by-patch":
            resolved_by = resolution.get("resolved_by", [])
            if not isinstance(resolved_by, list) or not resolved_by:
                errors.append(f"{path}: resolved-by-patch proposal requires at least one resolving patch")

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
