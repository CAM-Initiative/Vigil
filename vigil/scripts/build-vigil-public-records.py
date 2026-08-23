#!/usr/bin/env python3
"""Build VIGIL public registries from published record classes only.

PROP, PATCH and LEARN records are currently retained under ``vigil/drafts`` and are
not publication inputs. This wrapper deliberately constrains the legacy registry
builder to OBS, FM and RESEARCH without loading or resolving draft material.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
MODULE_PATH = SCRIPT_DIR / "build-vigil-records.py"


def load_builder() -> Any:
    spec = importlib.util.spec_from_file_location("build_vigil_records", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load VIGIL registry builder from {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    builder = load_builder()
    public_registry_types = ("failure_modes", "observations", "research")

    builder.TYPE_CONFIG = {
        registry_type: builder.TYPE_CONFIG[registry_type]
        for registry_type in public_registry_types
    }
    builder.RECORD_TYPE_DIRS = [
        builder.RECORDS_ROOT / builder.TYPE_CONFIG[registry_type]["directory"]
        for registry_type in public_registry_types
    ]
    builder.RECORD_TYPE_TO_REGISTRY = {
        "failure_mode": "failure_modes",
        "observation": "observations",
        "research": "research",
    }
    builder.OUTPUT_PATHS = {
        registry_type: builder.VIGIL_DIR / builder.TYPE_CONFIG[registry_type]["output"]
        for registry_type in public_registry_types
    }

    builder.build()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
