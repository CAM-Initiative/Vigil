#!/usr/bin/env python3
from __future__ import annotations

import os
import subprocess
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT_PATH = "vigil/scripts/test_validate_vigil_records.py"
TARGET_BRANCH = "governance/proposal-source-and-patch-traceability"

subprocess.run(["git", "fetch", "origin", "main:refs/remotes/origin/main"], cwd=ROOT, check=True)
original = subprocess.check_output(
    ["git", "show", f"origin/main:{SCRIPT_PATH}"],
    cwd=ROOT,
    text=True,
)

from _one_time_consolidate_prs import run

try:
    run(original)
except Exception:
    if os.environ.get("GITHUB_EVENT_NAME") == "push" and os.environ.get("GITHUB_REF_NAME") == TARGET_BRANCH:
        diagnostic = ROOT / ".github/Indices/vigil-consolidation-error.txt"
        diagnostic.parent.mkdir(parents=True, exist_ok=True)
        diagnostic.write_text(traceback.format_exc(), encoding="utf-8")
        (ROOT / SCRIPT_PATH).write_text(original, encoding="utf-8")
        temporary_workflow = ROOT / ".github/workflows/one-time-consolidate-vigil-prs.yml"
        if temporary_workflow.exists():
            temporary_workflow.unlink()
        subprocess.run(["git", "config", "user.name", "github-actions[bot]"], cwd=ROOT, check=True)
        subprocess.run(["git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"], cwd=ROOT, check=True)
        subprocess.run(
            ["git", "add", SCRIPT_PATH, ".github/Indices/vigil-consolidation-error.txt", ".github/workflows/one-time-consolidate-vigil-prs.yml"],
            cwd=ROOT,
            check=True,
        )
        subprocess.run(["git", "commit", "-m", "Capture VIGIL consolidation diagnostic"], cwd=ROOT, check=True)
        subprocess.run(["git", "push", "origin", f"HEAD:{TARGET_BRANCH}"], cwd=ROOT, check=True)
    raise

namespace = {
    "__name__": "__main__",
    "__file__": str(ROOT / SCRIPT_PATH),
    "__package__": None,
}
exec(compile(original, str(ROOT / SCRIPT_PATH), "exec"), namespace)
