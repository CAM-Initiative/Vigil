#!/usr/bin/env python3
from __future__ import annotations

import os
import subprocess
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT_PATH = "vigil/scripts/test_validate_vigil_records.py"
TARGET_BRANCH = "governance/proposal-source-and-patch-traceability"
HELPER_PATH = ROOT / "vigil/scripts/_one_time_consolidate_prs.py"

subprocess.run(["git", "fetch", "origin", "main:refs/remotes/origin/main"], cwd=ROOT, check=True)
original = subprocess.check_output(
    ["git", "show", f"origin/main:{SCRIPT_PATH}"],
    cwd=ROOT,
    text=True,
)

helper_text = HELPER_PATH.read_text(encoding="utf-8")
old_extract = '''        if "entire instrument" in section.lower():
            resulting_text = extract_substantive_instrument(current_text)
        elif resulting_text not in current_text:
            resulting_text = extract_heading_block(current_text, heading)
        if heading and heading not in resulting_text:
'''
new_extract = '''        if "entire instrument" in section.lower():
            resulting_text = extract_substantive_instrument(current_text)
            canonical_heading = current_text.splitlines()[0].strip()
            entry["section_heading"] = canonical_heading
            entry["section"] = f"Entire instrument {canonical_heading.lstrip('# ').strip()}"
            heading = canonical_heading
        elif resulting_text not in current_text:
            resulting_text = extract_heading_block(current_text, heading)
        if heading and heading not in resulting_text:
'''
if old_extract not in helper_text:
    raise RuntimeError("Unable to patch canonical whole-instrument extraction")
helper_text = helper_text.replace(old_extract, new_extract)
old_add = '    command("git", "add", "vigil/records", "vigil/scripts/test_validate_vigil_records.py", "vigil/scripts/_one_time_consolidate_prs.py", ".github/workflows/one-time-consolidate-vigil-prs.yml")\n'
new_add = '    diagnostic = ROOT / ".github/Indices/vigil-consolidation-error.txt"\n    if diagnostic.exists():\n        diagnostic.unlink()\n    command("git", "add", "-A", "vigil/records", "vigil/scripts", ".github/Indices", ".github/workflows")\n'
if old_add not in helper_text:
    raise RuntimeError("Unable to patch consolidation staging command")
HELPER_PATH.write_text(helper_text.replace(old_add, new_add), encoding="utf-8")

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
            ["git", "add", "-A", SCRIPT_PATH, ".github/Indices/vigil-consolidation-error.txt", ".github/workflows"],
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
