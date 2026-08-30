#!/usr/bin/env python3
"""Build VIGIL public registries from active published record classes only.

PROP, PATCH and LEARN records are retained under ``vigil/drafts`` and are not
publication inputs. During Incident migration stabilisation, legacy FM records remain
preserved under ``vigil/records/failures`` for migration provenance only; they are not
loaded into, regenerated as, or published through active registry indexes.
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
    public_registry_types = ("incidents", "observations", "research")

    builder.TYPE_CONFIG = {
        registry_type: builder.TYPE_CONFIG[registry_type]
        for registry_type in public_registry_types
    }
    builder.RECORD_TYPE_DIRS = [
        builder.RECORDS_ROOT / builder.TYPE_CONFIG[registry_type]["directory"]
        for registry_type in public_registry_types
    ]
    builder.RECORD_TYPE_TO_REGISTRY = {
        "incident": "incidents",
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
