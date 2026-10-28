#!/usr/bin/env python3
"""One-time maintainer-approved Gate 2 reconciliation. Remove after #174 declaration is published.

Only record_identity.version may change; all existing case-file evidence and adjudications
are preserved. Published-main per-record Git blob and release level are pinned in a
temporary Git-recoverable declaration packet, not a new permanent database.
"""
from __future__ import annotations
import copy
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
INC = ROOT / "vigil/records/incidents"
REPORT = ROOT / "vigil/docs/reviews/2026-10-28-incident-publication-reconciliation/working-declarations.json"
EXPECTED_MAIN = "0fdabb940cef157609e3cd2a20efa213cdfca2ef"
SUBSTANTIVE = {
    "vigil_assessment", "taxonomy_classification", "source_records",
    "harm_impact_assessment", "external_requirement_assessments",
    "incident_identity", "system_context", "governance_context",
}
ALLOWED_OTHER = {"interpretive_provenance"}

def git(*args: str) -> str:
    return subprocess.check_output(["git", "-C", str(ROOT), *args], text=True).strip()

def normalise(record: dict) -> dict:
    item = copy.deepcopy(record)
    item.get("interpretive_provenance", {}).pop("review_history", None)
    item["record_identity"].pop("version", None)
    item["record_identity"].pop("updated", None)
    return item

def main() -> None:
    subprocess.check_call(["git", "-C", str(ROOT), "fetch", "--no-tags", "origin", "main"])
    baseline = git("rev-parse", "refs/remotes/origin/main")
    if baseline != EXPECTED_MAIN:
        raise ValueError(f"STOP: main changed, expected {EXPECTED_MAIN}, found {baseline}")
    existing = set(git("ls-tree", "-r", "--name-only", "origin/main", "--", "vigil/records/incidents").splitlines())
    current = sorted(INC.glob("VIGIL-INC-*.json"))
    if len(existing) != 200 or len(current) != 206:
        raise ValueError(f"STOP: unexpected inventory main={len(existing)} branch={len(current)}")

    rows, edits, details = [], [], []
    for file in current:
        rel = file.relative_to(ROOT).as_posix()
        raw = file.read_text(encoding="utf-8")
        case = json.loads(raw)
        ident = file.stem
        if case["id"] != ident or case["record_identity"]["record_id"] != ident:
            raise ValueError(f"STOP: inconsistent ID for {rel}")
        if rel not in existing:
            row = dict(incident_id=ident, level="initial",
                       reason="First published source-grounded Incident and staged review",
                       base_version=None, base_blob=None)
        else:
            old = json.loads(git("show", "origin/main:" + rel))
            if old["id"] != ident:
                raise ValueError(f"STOP: published identity mismatch for {rel}")
            a, b = normalise(old), normalise(case)
            keys = sorted(k for k in a.keys() | b.keys() if a.get(k) != b.get(k))
            unknown = set(keys) - SUBSTANTIVE - ALLOWED_OTHER
            if unknown:
                raise ValueError(f"STOP: independently assess unrecognised material keys {rel}: {sorted(unknown)}")
            level = "minor" if set(keys) & SUBSTANTIVE else "patch"
            major, minor, patch = map(int, old["record_identity"]["version"].split("."))
            desired = f"{major}.{minor+1}.0" if level == "minor" else f"{major}.{minor}.{patch+1}"
            old_current = case["record_identity"]["version"]
            if old_current != desired:
                match = re.search(r'("record_identity"\s*:\s*\{[^{}]*?"version"\s*:\s*")([^"]+)(")', raw)
                if not match or match.group(2) != old_current:
                    raise ValueError(f"STOP: record version cannot be precisely replaced: {rel}")
                revised = raw[:match.start(2)] + desired + raw[match.end(2):]
                check = copy.deepcopy(case)
                check["record_identity"]["version"] = desired
                if json.loads(revised) != check:
                    raise ValueError(f"STOP: unexpected substantive mutation {rel}")
                edits.append((file, revised))
            row = dict(incident_id=ident, level=level,
                       reason=("Accepted source-grounded case assessment and taxonomy revision"
                               if level == "minor" else
                               "Historical-review cleanup under PR #180; findings unchanged"),
                       base_version=old["record_identity"]["version"],
                       base_blob=git("rev-parse", "origin/main:" + rel))
            details.append((ident, level, keys, old_current, desired))
        rows.append(row)

    if len(rows) != 206 or sum(row["level"] == "initial" for row in rows) != 6:
        raise ValueError("STOP: unexpected canonical coverage")
    print(json.dumps({"records": len(rows), "edits_pending": len(edits),
                      "minor": sum(x["level"] == "minor" for x in rows),
                      "patch": sum(x["level"] == "patch" for x in rows),
                      "initial": sum(x["level"] == "initial" for x in rows)}, sort_keys=True))
    print("Substantive revision IDs:",
          [ident for ident, level, *_ in details if level == "minor"])
    # The independent validator remains authoritative; never change it here.
    for file, revised in edits:
        file.write_text(revised, encoding="utf-8")
    REPORT.write_text(json.dumps({"published_main_baseline": baseline, "rows": rows,
                                  "purpose": "Temporary Gate 2 publication declarations; remove after PR #174 update"},
                                 indent=2) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
