#!/usr/bin/env python3
"""Run the corpus reconciliation with canonical proposal lifecycle values."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
MODULE_PATH = SCRIPT_DIR / "reconcile-vigil-corpus-coverage.py"


def load_module() -> Any:
    spec = importlib.util.spec_from_file_location("vigil_corpus_reconciliation", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load corpus reconciliation module from {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    module = load_module()
    original = module.reconcile_proposal

    def reconcile_with_canonical_status(proposal_id: str, patch_id: str, note: str) -> None:
        original(proposal_id, patch_id, note)
        path = module.PROPOSAL_DIR / f"{proposal_id}.json"
        record = json.loads(path.read_text(encoding="utf-8"))
        record.setdefault("resolution_status", {})["status"] = "resolved-by-patch"
        path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    module.reconcile_proposal = reconcile_with_canonical_status
    module.main()


if __name__ == "__main__":
    main()
