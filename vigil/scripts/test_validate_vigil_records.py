#!/usr/bin/env python3
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT_PATH = ROOT / "vigil/scripts/test_validate_vigil_records.py"
TARGET_BRANCH = "governance/proposal-source-and-patch-traceability"

subprocess.run(
    ["git", "fetch", "origin", "main:refs/remotes/origin/main"],
    cwd=ROOT,
    check=True,
)
original = subprocess.check_output(
    ["git", "show", "origin/main:vigil/scripts/test_validate_vigil_records.py"],
    cwd=ROOT,
    text=True,
)

if os.environ.get("GITHUB_EVENT_NAME") == "push" and os.environ.get("GITHUB_REF_NAME") == TARGET_BRANCH:
    SCRIPT_PATH.write_text(original, encoding="utf-8")
    completed = subprocess.run(
        [sys.executable, "vigil/scripts/run-vigil-lifecycle-validation.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    diagnostic = ROOT / ".github/Indices/vigil-lifecycle-validation-output.txt"
    diagnostic.parent.mkdir(parents=True, exist_ok=True)
    diagnostic.write_text(
        f"returncode={completed.returncode}\n\nSTDOUT\n======\n{completed.stdout}\n\nSTDERR\n======\n{completed.stderr}",
        encoding="utf-8",
    )

    subprocess.run(["git", "config", "user.name", "github-actions[bot]"], cwd=ROOT, check=True)
    subprocess.run(
        ["git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"],
        cwd=ROOT,
        check=True,
    )
    subprocess.run(
        ["git", "add", "vigil/scripts/test_validate_vigil_records.py", ".github/Indices/vigil-lifecycle-validation-output.txt"],
        cwd=ROOT,
        check=True,
    )
    subprocess.run(
        ["git", "commit", "-m", "Capture final VIGIL lifecycle validation output"],
        cwd=ROOT,
        check=True,
    )
    subprocess.run(
        ["git", "push", "origin", f"HEAD:{TARGET_BRANCH}"],
        cwd=ROOT,
        check=True,
    )
    raise SystemExit(completed.returncode or 1)

namespace = {
    "__name__": "__main__",
    "__file__": str(SCRIPT_PATH),
    "__package__": None,
}
exec(compile(original, str(SCRIPT_PATH), "exec"), namespace)
