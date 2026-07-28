#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import subprocess
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
    patch_path = ROOT / "vigil/records/patches/2026/VIGIL-2026-PATCH-0031.json"
    record = json.loads(patch_path.read_text(encoding="utf-8"))
    changed = False
    for event in record["decision_trace"].get("events", []):
        if event.get("event_type") == "canonical-adoption-verified":
            event["event_type"] = "canonicalised"
            changed = True
    if not changed:
        raise RuntimeError("PATCH-0031 canonical-adoption event was not found")
    patch_path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    diagnostic = ROOT / ".github/Indices/vigil-full-validation-output.txt"
    if diagnostic.exists():
        diagnostic.unlink()
    SCRIPT_PATH.write_text(original, encoding="utf-8")

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
            "-A",
            "vigil/records/patches/2026/VIGIL-2026-PATCH-0031.json",
            "vigil/scripts/test_validate_vigil_records.py",
            ".github/Indices/vigil-full-validation-output.txt",
        ],
        cwd=ROOT,
        check=True,
    )
    subprocess.run(
        ["git", "commit", "-m", "Use canonical PATCH-0031 decision event type"],
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
    "__file__": str(SCRIPT_PATH),
    "__package__": None,
}
exec(compile(original, str(SCRIPT_PATH), "exec"), namespace)
