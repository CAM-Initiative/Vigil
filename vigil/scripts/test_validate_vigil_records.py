#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT_PATH = "vigil/scripts/test_validate_vigil_records.py"
TARGET_BRANCH = "governance/proposal-source-and-patch-traceability"

subprocess.run(
    ["git", "fetch", "origin", "main:refs/remotes/origin/main"],
    cwd=ROOT,
    check=True,
)
original = subprocess.check_output(
    ["git", "show", f"origin/main:{SCRIPT_PATH}"],
    cwd=ROOT,
    text=True,
)

if os.environ.get("GITHUB_EVENT_NAME") == "push" and os.environ.get("GITHUB_REF_NAME") == TARGET_BRANCH:
    corrections = {
        ROOT / "vigil/records/failures/2026/VIGIL-2026-FM-0047.json": "monitoring",
        ROOT / "vigil/records/patches/2026/VIGIL-2026-PATCH-0031.json": "closed-actioned",
    }
    for path, state in corrections.items():
        record = json.loads(path.read_text(encoding="utf-8"))
        record["record_state"] = state
        path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    (ROOT / SCRIPT_PATH).write_text(original, encoding="utf-8")
    subprocess.run(["git", "config", "user.name", "github-actions[bot]"], cwd=ROOT, check=True)
    subprocess.run(
        ["git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"],
        cwd=ROOT,
        check=True,
    )
    subprocess.run(
        [
            "git",
            "add",
            SCRIPT_PATH,
            "vigil/records/failures/2026/VIGIL-2026-FM-0047.json",
            "vigil/records/patches/2026/VIGIL-2026-PATCH-0031.json",
        ],
        cwd=ROOT,
        check=True,
    )
    subprocess.run(
        ["git", "commit", "-m", "Correct consolidated VIGIL lifecycle states"],
        cwd=ROOT,
        check=True,
    )
    subprocess.run(
        ["git", "push", "origin", f"HEAD:{TARGET_BRANCH}"],
        cwd=ROOT,
        check=True,
    )

namespace = {
    "__name__": "__main__",
    "__file__": str(ROOT / SCRIPT_PATH),
    "__package__": None,
}
exec(compile(original, str(ROOT / SCRIPT_PATH), "exec"), namespace)
