#!/usr/bin/env python3
"""Verify literal PATCH corpus evidence against the cited Caelestis Git objects."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
PATCHES = ROOT / "vigil" / "records" / "patches"


def git(caelestis_root: Path, *arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(caelestis_root), *arguments],
        check=False,
        capture_output=True,
        text=True,
    )


def git_text(caelestis_root: Path, revision: str, path: str) -> tuple[str | None, str | None]:
    completed = git(caelestis_root, "show", f"{revision}:{path}")
    if completed.returncode:
        detail = completed.stderr.strip() or completed.stdout.strip() or "git show failed"
        return None, detail
    return completed.stdout, None


def resolve_ref(caelestis_root: Path, ref: str) -> str | None:
    completed = git(caelestis_root, "rev-parse", "--verify", f"{ref}^{{commit}}")
    return completed.stdout.strip() if completed.returncode == 0 else None


def is_ancestor(caelestis_root: Path, ancestor: str, descendant: str) -> bool:
    return git(caelestis_root, "merge-base", "--is-ancestor", ancestor, descendant).returncode == 0


def record_files(records_root: Path) -> list[Path]:
    return sorted(records_root.rglob("*.json"), key=lambda path: path.as_posix())


def validate(
    caelestis_root: Path,
    records_root: Path = PATCHES,
    main_ref: str = "origin/main",
) -> list[str]:
    errors: list[str] = []
    if not (caelestis_root / ".git").exists():
        return [f"{caelestis_root}: Caelestis Git checkout is required"]

    main_commit = resolve_ref(caelestis_root, main_ref)
    if main_commit is None and main_ref == "origin/main":
        main_commit = resolve_ref(caelestis_root, "main")
    if main_commit is None:
        return [f"{caelestis_root}: unable to resolve Caelestis main ref {main_ref!r}"]

    for record_path in record_files(records_root):
        try:
            record = json.loads(record_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{record_path}: unable to load PATCH JSON: {exc}")
            continue
        implementation = record.get("corpus_implementation")
        if not isinstance(implementation, dict):
            errors.append(f"{record_path}: missing corpus_implementation")
            continue
        canonical_state = implementation.get("canonical_state")
        entries = implementation.get("entries")
        if not isinstance(entries, list):
            errors.append(f"{record_path}: corpus_implementation.entries must be an array")
            continue

        for index, entry in enumerate(entries):
            prefix = f"{record_path}: corpus_implementation.entries[{index}]"
            if not isinstance(entry, dict):
                errors.append(f"{prefix} must be an object")
                continue
            source = entry.get("source")
            verification = entry.get("verification")
            if not isinstance(source, dict) or not isinstance(verification, dict):
                errors.append(f"{prefix} requires source and verification objects")
                continue
            commit = source.get("commit")
            path = source.get("path")
            resulting_text = entry.get("resulting_text")
            if not all(isinstance(value, str) and value for value in (commit, path, resulting_text)):
                errors.append(f"{prefix} requires commit, path, and literal resulting_text")
                continue
            if resolve_ref(caelestis_root, commit) is None:
                errors.append(f"{prefix}: source commit {commit!r} does not resolve")
                continue
            source_text, source_error = git_text(caelestis_root, commit, path)
            if source_text is None:
                errors.append(f"{prefix}: {source_error}")
                continue
            if resulting_text not in source_text:
                errors.append(f"{prefix}: resulting_text is not an exact substring of {commit}:{path}")
            heading = entry.get("section_heading")
            if isinstance(heading, str) and heading and heading not in resulting_text:
                errors.append(f"{prefix}: section_heading is absent from resulting_text")

            prior_status = entry.get("prior_text_status")
            prior_text = entry.get("prior_text")
            if prior_status == "captured":
                parent = resolve_ref(caelestis_root, f"{commit}^")
                if parent is None:
                    errors.append(f"{prefix}: cannot resolve parent commit for captured prior_text")
                else:
                    parent_source, parent_error = git_text(caelestis_root, parent, path)
                    if parent_source is None:
                        errors.append(f"{prefix}: {parent_error}")
                    elif not isinstance(prior_text, str) or prior_text not in parent_source:
                        errors.append(f"{prefix}: prior_text is not an exact substring of {parent}:{path}")

            if canonical_state == "canonical-main":
                current_text, current_error = git_text(caelestis_root, main_commit, path)
                if current_text is None:
                    errors.append(f"{prefix}: canonical-main path unavailable: {current_error}")
                elif verification.get("current_clause_status") == "current" and resulting_text not in current_text:
                    errors.append(f"{prefix}: current clause wording is absent from Caelestis main")
                if not is_ancestor(caelestis_root, commit, main_commit):
                    errors.append(f"{prefix}: cited canonical source commit is not an ancestor of Caelestis main")
            elif canonical_state == "branch-only" and is_ancestor(caelestis_root, commit, main_commit):
                errors.append(f"{prefix}: branch-only source is already an ancestor of Caelestis main")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--caelestis-root",
        type=Path,
        default=ROOT.parent / "Caelestis",
        help="Path to a full Caelestis Git checkout.",
    )
    parser.add_argument("--records-root", type=Path, default=PATCHES)
    parser.add_argument("--main-ref", default="origin/main")
    arguments = parser.parse_args()

    errors = validate(arguments.caelestis_root.resolve(), arguments.records_root.resolve(), arguments.main_ref)
    if errors:
        print("VIGIL PATCH trace validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    count = len(record_files(arguments.records_root))
    print(f"VIGIL PATCH trace validation passed for {count} records.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
