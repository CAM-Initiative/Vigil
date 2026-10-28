#!/usr/bin/env python3
"""Generate an idempotent, main-only VIGIL Incident publication manifest.

Output is a derived CURRENT publication index, not a replacement for Git's
immutable history or a new canonical Incident database. Never edits records.
Use full Git history; last first-parent source-file change supplies a stable
commit/date even if Actions subsequently commits generated indexes.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

RECORDS = Path("vigil/records/incidents")
OUTPUT = Path("vigil/VIGIL.Incidents.Publications.json")
PATH = re.compile(r"VIGIL-INC-[0-9]{6}\.json$")
VERSION = re.compile(r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$")

def git(root: Path, *args: str, allow_missing: bool = False) -> str | None:
    run = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True)
    if run.returncode:
        if allow_missing:
            return None
        raise ValueError(f"git {' '.join(args)}: {run.stderr.strip()}")
    return run.stdout.strip()

def predecessor_text(root: Path, commit: str, path: str) -> str | None:
    """Read a first-parent predecessor, returning None only for a root/addition."""
    metadata = git(root, "cat-file", "-p", commit)
    parent = next((line.split(" ", 1)[1] for line in metadata.splitlines()
                   if line.startswith("parent ")), None)
    if parent is None:
        return None
    # A missing tree entry means the record is newly added. Git failures while
    # resolving the parent/tree must propagate rather than hiding history loss.
    entry = git(root, "ls-tree", "-z", parent, "--", path)
    if not entry:
        return None
    rows = [row for row in entry.split("\\0") if row]
    if len(rows) != 1 or "\\t" not in rows[0]:
        raise ValueError(f"{path}: unexpected predecessor tree entry")
    metadata, found_path = rows[0].split("\\t", 1)
    fields = metadata.split()
    if found_path != path or len(fields) != 3 or fields[1] != "blob":
        raise ValueError(f"{path}: predecessor is not a canonical file blob")
    return git(root, "show", f"{parent}:{path}")


def build(root: Path) -> dict[str, Any]:
    if git(root, "rev-parse", "--is-inside-work-tree") != "true":
        raise ValueError("a Git checkout is required")
    entries = []
    for file in sorted((root / RECORDS).glob("VIGIL-INC-*.json")):
        if PATH.fullmatch(file.name) is None:
            raise ValueError(f"unrecognised Incident path: {file}")
        relative = file.relative_to(root).as_posix()
        raw = file.read_bytes()
        record = json.loads(raw)
        ident = file.stem
        identity = record.get("record_identity") or {}
        version = identity.get("version")
        if record.get("id") != ident or identity.get("record_id") != ident or not isinstance(version, str) or not VERSION.fullmatch(version):
            raise ValueError(f"{relative}: invalid canonical Incident identity/version")
        # Commit is the last change to this path on the main first-parent line.
        # It does not change when a generated-index bot appends a commit.
        source = git(root, "log", "--first-parent", "-1", "--format=%H%x09%cI", "HEAD", "--", relative)
        if not source or "\t" not in source:
            raise ValueError(f"{relative}: no recoverable committed publication source")
        commit, published_at = source.split("\t", 1)
        committed_blob = git(root, "rev-parse", f"HEAD:{relative}")
        disk_blob = git(root, "hash-object", str(file))
        if committed_blob != disk_blob:
            raise ValueError(f"{relative}: current file differs from committed canonical source")
        predecessor = predecessor_text(root, commit, relative)
        previous_version = None
        if predecessor is not None:
            prior_record = json.loads(predecessor)
            if not isinstance(prior_record, dict):
                raise ValueError(f"{relative}: predecessor is not a JSON object")
            prior_identity = prior_record.get("record_identity") or {}
            if not isinstance(prior_identity, dict):
                raise ValueError(f"{relative}: predecessor record_identity is not an object")
            previous_version = prior_identity.get("version")
            if previous_version is not None and (
                not isinstance(previous_version, str) or not VERSION.fullmatch(previous_version)
            ):
                raise ValueError(f"{relative}: predecessor has invalid version")
        taxonomy = record.get("taxonomy_classification") or {}
        him = record.get("harm_impact_assessment") or {}
        entries.append({
            "incident_id": ident,
            "version": version,
            "canonical_path": relative,
            "sha256": hashlib.sha256(raw).hexdigest(),
            "git_blob": committed_blob,
            "source_commit": commit,
            "published_at": published_at,
            "previous_version": previous_version if previous_version != version else None,
            "taxonomy_version_as_applied": taxonomy.get("taxonomy_version"),
            "him_version_as_applied": him.get("methodology_version"),
        })
    if not entries:
        raise ValueError("no canonical Incidents found")
    return {
        "registry_type": "vigil_incident_publications",
        "schema_version": 1,
        "generated_notice": (
            "Deterministic main-only projection of committed canonical Incident versions. "
            "Not a second Incident database or authority to reinterpret historical decisions. "
            "source_commit is the last first-parent commit changing that canonical file; "
            "published_at is its Git committer timestamp. Full prior states remain in Git."
        ),
        "generated_from": RECORDS.as_posix()+"/",
        "record_count": len(entries),
        "records": entries,
    }

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, default=OUTPUT)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="compare with existing manifest; no writes")
    mode.add_argument("--dry-run", action="store_true", help="report count but do not write")
    args = parser.parse_args()
    root = args.repo.resolve()
    target = args.output if args.output.is_absolute() else root / args.output
    try:
        document = build(root)
        generated = json.dumps(document, indent=2, ensure_ascii=False) + "\n"
        if args.check:
            if not target.exists() or target.read_text(encoding="utf-8") != generated:
                raise ValueError(f"stale or missing generated manifest: {target}")
        elif not args.dry_run:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(generated, encoding="utf-8")
        print(json.dumps({"status": "check" if args.check else "dry-run" if args.dry_run else "written",
                          "records": document["record_count"], "manifest": str(target)}))
        return 0
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(f"VIGIL publication manifest failed: {exc}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
