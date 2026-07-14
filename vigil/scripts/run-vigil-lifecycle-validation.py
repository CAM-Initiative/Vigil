#!/usr/bin/env python3
"""Run lifecycle validation with canonical resolved-by-patch proposal checks."""

from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
MODULE_PATH = SCRIPT_DIR / "validate-vigil-lifecycle.py"


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
    return module.main()


if __name__ == "__main__":
    raise SystemExit(main())
