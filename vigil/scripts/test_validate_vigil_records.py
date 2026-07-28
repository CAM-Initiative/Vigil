#!/usr/bin/env python3
from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT_PATH = "vigil/scripts/test_validate_vigil_records.py"
original = subprocess.check_output(
    ["git", "show", f"HEAD^:{SCRIPT_PATH}"],
    cwd=ROOT,
    text=True,
)

from _one_time_consolidate_prs import run

run(original)
namespace = {
    "__name__": "__main__",
    "__file__": str(ROOT / SCRIPT_PATH),
    "__package__": None,
}
exec(compile(original, str(ROOT / SCRIPT_PATH), "exec"), namespace)
