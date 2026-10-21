#!/usr/bin/env python3
"""Reject additional taxonomy releases in a PR relative to the published main ledger."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INDEX_RELATIVE_PATH = "vigil/taxonomy/VIGIL.FailureTaxonomy.Index.json"


def main() -> None:
    branch = json.loads((ROOT / "VIGIL.FailureTaxonomy.Index.json").read_text(encoding="utf-8"))
    main_text = subprocess.check_output(
        ["git", "show", f"refs/remotes/origin/main:{INDEX_RELATIVE_PATH}"],
        text=True,
    )
    published = json.loads(main_text)
    problems = []
    if branch.get("release_history") != published.get("release_history"):
        problems.append(
            "working branches must preserve main's published release_history unchanged; "
            "remove intermediate 0.8.0/0.8.1 release entries"
        )

    branch_standard = branch.get("standard", {})
    published_standard = published.get("standard", {})
    for field in ("version", "publication_date"):
        if branch_standard.get(field) != published_standard.get(field):
            problems.append(
                f"working branch standard.{field} must retain published main's value "
                "(put the one unpublished candidate in working_release)"
            )

    working = branch.get("working_release")
    if working is not None and working.get("base_version") != published_standard.get("version"):
        problems.append("working_release.base_version must equal main's latest published version")

    if problems:
        raise SystemExit("Taxonomy PR single-release guard failed:\n- " + "\n- ".join(problems))

    candidate = working.get("version") if isinstance(working, dict) else "(none)"
    print(
        "Single-release PR guard passed: "
        f"main={published_standard.get('version')}, working candidate={candidate}; "
        "no unpublished intermediate ledger entries."
    )


if __name__ == "__main__":
    main()
