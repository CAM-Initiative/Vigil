#!/usr/bin/env python3
"""Read-only publication checker for final VIGIL Incident PRs targeting main.

PR body convention, using a tilde fenced block with language vigil-incident-release:
~~~vigil-incident-release
{"records":[{"incident_id":"VIGIL-INC-000001","level":"minor","reason":"Source-grounded new class mapping","base_version":"1.4.11","base_blob":"<published main blob SHA>"}]}
~~~
New IDs: level initial and null base_version/base_blob.
This checker NEVER edits canonical Incident records or adjudicates class membership.
"""
from __future__ import annotations
import argparse
import copy
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

RECORD_DIR = "vigil/records/incidents/"
RECORD_PATH = re.compile(r"^vigil/records/incidents/(VIGIL-INC-[0-9]{6})\.json$")
VERSION = re.compile(r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$")
LEVELS = {"major", "minor", "patch", "initial"}
BLOCK = re.compile(r"(?ms)^~~~vigil-incident-release[ \t]*\n(.*?)\n~~~[ \t]*$")
BLOB = re.compile(r"^(?:[0-9a-f]{40}|[0-9a-f]{64})$")

class ReleaseError(ValueError):
    """A change cannot safely be published."""

def git(*args: str, root: Path | None = None) -> str:
    cmd = ["git", *(["-C", str(root)] if root else []), *args]
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if result.returncode:
        raise ReleaseError(f"git {' '.join(args)}: {result.stderr.strip()}")
    return result.stdout.strip()

def parse_version(value: str) -> tuple[int, int, int]:
    match = VERSION.fullmatch(value or "")
    if match is None:
        raise ReleaseError(f"invalid Incident version: {value!r}")
    return tuple(map(int, match.groups()))

def next_version(published: str, level: str) -> str:
    major, minor, patch = parse_version(published)
    if level == "major":
        return f"{major + 1}.0.0"
    if level == "minor":
        return f"{major}.{minor + 1}.0"
    if level == "patch":
        return f"{major}.{minor}.{patch + 1}"
    raise ReleaseError(f"unsupported published revision level: {level!r}")

def declaration_from_body(body: str, changed: bool) -> dict[str, dict[str, Any]]:
    blocks = BLOCK.findall(body or "")
    if not blocks:
        if changed:
            raise ReleaseError("changed Incident files require a vigil-incident-release block in PR body")
        return {}
    if len(blocks) != 1:
        raise ReleaseError("exactly one vigil-incident-release block is required")
    try:
        packet = json.loads(blocks[0])
    except json.JSONDecodeError as exc:
        raise ReleaseError(f"malformed PR version declaration: {exc}") from exc
    if not isinstance(packet, dict) or set(packet) != {"records"} or not isinstance(packet["records"], list):
        raise ReleaseError("declaration must contain exactly a records array")
    entries = {}
    for item in packet["records"]:
        expected = {"incident_id", "level", "reason", "base_version", "base_blob"}
        if not isinstance(item, dict) or set(item) != expected:
            raise ReleaseError("declaration row must have incident_id, level, reason, base_version, base_blob")
        ident = item["incident_id"]
        if not isinstance(ident, str) or not re.fullmatch(r"VIGIL-INC-[0-9]{6}", ident):
            raise ReleaseError(f"invalid Incident ID: {ident!r}")
        if ident in entries:
            raise ReleaseError(f"duplicate declaration {ident}")
        if item["level"] not in LEVELS or not isinstance(item["reason"], str) or len(item["reason"].strip()) < 16:
            raise ReleaseError(f"{ident}: invalid level or insufficient source-linked reason")
        if item["base_version"] is not None:
            parse_version(item["base_version"])
        if item["base_blob"] is not None and (
            not isinstance(item["base_blob"], str) or BLOB.fullmatch(item["base_blob"]) is None
        ):
            raise ReleaseError(f"{ident}: invalid baseline blob")
        entries[ident] = item
    if not changed and entries:
        raise ReleaseError("PR describes Incident revisions but does not alter canonical Incidents")
    return entries

def meaningful_payload(record: dict[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(record)
    identity = result.get("record_identity")
    if isinstance(identity, dict):
        identity.pop("version", None)
        identity.pop("updated", None)
    return result

def mapping_fingerprint(record: dict[str, Any]) -> str:
    """A deterministic lower bound for a MINOR change, not an AI semantic verdict."""
    taxonomy = record.get("taxonomy_classification") or {}
    mapped = []
    for item in [taxonomy.get("primary_classification"), *(taxonomy.get("secondary_classifications") or [])]:
        if isinstance(item, dict):
            mapped.append([item.get("class_id"), item.get("classification_role")])
    clauses = ((record.get("vigil_assessment") or {}).get("source_clause_analysis") or {}).get("clauses") or []
    episode_mappings = []
    for index, clause in enumerate(clauses):
        if not isinstance(clause, dict):
            continue
        rels = []
        for rel in clause.get("taxonomy_relationships") or []:
            if isinstance(rel, dict) and rel.get("canonical_taxonomy_mapping") is True:
                rels.append([rel.get("class_id"), rel.get("relationship")])
        episode_mappings.append([
            clause.get("episode_id") or f"legacy-index-{index}",
            clause.get("adjudication_status"),
            sorted(rels, key=str),
        ])
    return json.dumps({
        "classification_status": taxonomy.get("classification_status"),
        "top_level": sorted(mapped, key=str),
        "episodes": sorted(episode_mappings, key=str),
    }, sort_keys=True)

def verify_record(*, ident: str, published: dict[str, Any] | None,
                  candidate: dict[str, Any], declaration: dict[str, Any],
                  blob: str | None) -> str:
    if candidate.get("id") != ident or (candidate.get("record_identity") or {}).get("record_id") != ident:
        raise ReleaseError(f"{ident}: record identity does not match filename")
    version = (candidate.get("record_identity") or {}).get("version")
    parse_version(version)
    if published is None:
        if declaration["level"] != "initial" or declaration["base_version"] is not None or declaration["base_blob"] is not None:
            raise ReleaseError(f"{ident}: new Incident requires initial and null baseline fields")
        return version
    base_version = (published.get("record_identity") or {}).get("version")
    parse_version(base_version)
    if declaration["level"] == "initial":
        raise ReleaseError(f"{ident}: already published; initial invalid")
    if declaration["base_version"] != base_version or declaration["base_blob"] != blob:
        raise ReleaseError(f"{ident}: declaration does not match published main version/blob")
    if meaningful_payload(published) == meaningful_payload(candidate):
        raise ReleaseError(f"{ident}: version-only/updated-only change is not a revision")
    if mapping_fingerprint(published) != mapping_fingerprint(candidate) and declaration["level"] == "patch":
        raise ReleaseError(f"{ident}: changed canonical taxonomy mappings or dispositions require MINOR")
    expected = next_version(base_version, declaration["level"])
    if version != expected:
        raise ReleaseError(f"{ident}: expected {expected} from main {base_version} ({declaration['level']}), got {version}")
    return expected

def json_at(ref: str, path: str, root: Path) -> dict[str, Any] | None:
    # Distinguish an absent path (a genuinely new Incident) from Git/object
    # errors. Treating every show failure as absence can bypass the published
    # version baseline when a checkout is incomplete or corrupt.
    entry = git("ls-tree", "-z", ref, "--", path, root=root)
    if not entry:
        return None
    rows = [row for row in entry.split("\0") if row]
    if len(rows) != 1 or "\t" not in rows[0]:
        raise ReleaseError(f"{ref}:{path}: unexpected Git tree entry")
    metadata, found_path = rows[0].split("\t", 1)
    fields = metadata.split()
    if found_path != path or len(fields) != 3 or fields[1] != "blob":
        raise ReleaseError(f"{ref}:{path}: expected one canonical file blob")
    data = git("show", f"{ref}:{path}", root=root)
    try:
        parsed = json.loads(data)
    except json.JSONDecodeError as exc:
        raise ReleaseError(f"{ref}:{path}: invalid JSON: {exc}") from exc
    if not isinstance(parsed, dict):
        raise ReleaseError(f"{ref}:{path}: expected JSON object")
    return parsed

def inspect(event: dict[str, Any], root: Path) -> list[dict[str, str]]:
    pr = event.get("pull_request")
    if not isinstance(pr, dict) or (pr.get("base") or {}).get("ref") != "main":
        raise ReleaseError("only for pull_request events targeting main")
    base, head = pr["base"]["sha"], pr["head"]["sha"]
    actual_main = git("rev-parse", "refs/remotes/origin/main", root=root)
    if actual_main != base:
        raise ReleaseError(f"stale main PR base {base}; origin/main is {actual_main}")
    for rev in (base, head):
        git("cat-file", "-t", rev, root=root)
    changed: dict[str, str] = {}
    for line in git("diff", "--name-status", "--no-renames", base, head, "--", RECORD_DIR, root=root).splitlines():
        status, _, path = line.partition("\t")
        match = RECORD_PATH.fullmatch(path)
        if not match:
            raise ReleaseError(f"unsupported canonical path {path}")
        ident = match.group(1)
        if status == "D":
            raise ReleaseError(f"{ident}: canonical deletion needs separate approval")
        if status not in {"A", "M"}:
            raise ReleaseError(f"{ident}: unsupported change type {status}")
        changed[ident] = path
    declarations = declaration_from_body(pr.get("body") or "", bool(changed))
    if set(declarations) != set(changed):
        raise ReleaseError(f"declaration coverage mismatch; missing={sorted(set(changed)-set(declarations))}, extra={sorted(set(declarations)-set(changed))}")
    releases = []
    for ident, path in sorted(changed.items()):
        old, new = json_at(base, path, root), json_at(head, path, root)
        if new is None:
            raise ReleaseError(f"{ident}: head lacks source record")
        blob = git("rev-parse", f"{base}:{path}", root=root) if old is not None else None
        version = verify_record(ident=ident, published=old, candidate=new,
                                declaration=declarations[ident], blob=blob)
        releases.append({"incident_id": ident, "level": declarations[ident]["level"],
                         "candidate_version": version, "main_baseline_blob": blob or ""})
    return releases

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--event", type=Path, required=True, help="GitHub pull_request JSON event path")
    parser.add_argument("--repo", type=Path, default=Path("."))
    args = parser.parse_args()
    try:
        event = json.loads(args.event.read_text(encoding="utf-8"))
        releases = inspect(event, args.repo.resolve())
    except (ReleaseError, OSError, json.JSONDecodeError, KeyError, TypeError) as exc:
        print(f"VIGIL Incident publication check failed: {exc}", file=sys.stderr)
        return 1
    print(json.dumps({"status": "validated", "changed_incidents": len(releases),
                      "release_candidates": releases}, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
