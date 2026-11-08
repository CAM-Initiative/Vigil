#!/usr/bin/env python3
"""PR guard: require a current, changed decision packet for mapping losses/role changes.

This is a provenance gate, NOT an automated Fidelity Class adjudicator. A dropped
mapping must never disappear from a canonical Incident merely because a later
review focuses on its surviving classes.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import PurePosixPath


REVIEW_PREFIX = "vigil/docs/reviews/"
INCIDENT_PREFIX = "vigil/records/incidents/"
REMOVAL_ROLES = {"removed-unsupported", "superseded"}
ROLE_CHANGE_ROLES = {"role-changed", "role-confidence-changed"}


def git(*args: str) -> str:
    process = subprocess.run(["git", *args], text=True, capture_output=True)
    if process.returncode:
        raise ValueError("git " + " ".join(args) + ": " + process.stderr.strip())
    return process.stdout


def read_at(ref: str, path: str) -> dict:
    value = json.loads(git("show", f"{ref}:{path}"))
    if not isinstance(value, dict):
        raise ValueError(f"{ref}:{path} must be a JSON object")
    return value


def mappings(record: dict) -> dict[str, dict]:
    taxonomy = record.get("taxonomy_classification") or {}
    items = [taxonomy.get("primary_classification"), *(taxonomy.get("secondary_classifications") or [])]
    return {item["class_id"]: item for item in items if isinstance(item, dict) and item.get("class_id")}


def changed_mapping_roles(before: dict, after: dict) -> dict[str, str]:
    old, new = mappings(before), mappings(after)
    changes = {}
    for class_id, item in old.items():
        if class_id not in new:
            changes[class_id] = "removed"
        elif item.get("classification_role") != new[class_id].get("classification_role"):
            changes[class_id] = "role-changed"
    return changes


def packet_decisions(packet: dict) -> dict[str, dict]:
    entries = packet.get("taxonomy_mapping_dispositions")
    if not isinstance(entries, list):
        entries = packet.get("mapping_decisions")
    if not isinstance(entries, list):
        return {}
    return {item["class_id"]: item for item in entries
            if isinstance(item, dict) and isinstance(item.get("class_id"), str)}


def verify_change(before: dict, after: dict, packet: dict,
                  changed_packet: bool, ref: str) -> list[str]:
    errors = []
    changes = changed_mapping_roles(before, after)
    if not changes:
        return errors
    if not changed_packet:
        errors.append(f"{ref}: mapping change requires a new or updated dated decision packet in this PR")
    decisions = packet_decisions(packet)
    for class_id, kind in changes.items():
        item = decisions.get(class_id)
        if not item:
            errors.append(f"{ref}: {class_id} ({kind}) has no per-mapping decision")
            continue
        role = item.get("disposition")
        allowed = REMOVAL_ROLES if kind == "removed" else ROLE_CHANGE_ROLES
        if role not in allowed:
            errors.append(f"{ref}: {class_id} expected {kind}, packet says {role!r}")
        reason = item.get("reason") or item.get("decisive_blocker") or item.get("classification_basis")
        if not isinstance(reason, str) or not reason.strip():
            errors.append(f"{ref}: {class_id} needs occurrence-specific rationale")
        if not isinstance(item.get("before") or item.get("baseline_mapping"), dict):
            errors.append(f"{ref}: {class_id} missing before snapshot")
        if kind == "removed":
            if item.get("after", item.get("canonical_mapping_after")) is not None:
                errors.append(f"{ref}: {class_id} removed from canonical but packet retains an after mapping")
        else:
            expected = mappings(after)[class_id].get("classification_role")
            actual = item.get("after", item.get("canonical_mapping_after"))
            if not isinstance(actual, dict) or actual.get("classification_role") != expected:
                errors.append(f"{ref}: {class_id} missing or inconsistent new-role snapshot")
    return errors


def check(base: str, head: str) -> list[str]:
    changed = set(git("diff", "--name-only", "--diff-filter=ACMRT", base, head).splitlines())
    errors = []
    for path in sorted(p for p in changed if p.startswith(INCIDENT_PREFIX) and p.endswith(".json")):
        try:
            old = read_at(base, path)
        except ValueError:
            continue  # New Incident, without a previously admitted mapping.
        new = read_at(head, path)
        changes = changed_mapping_roles(old, new)
        if not changes:
            continue
        prov = (new.get("taxonomy_classification") or {}).get("classification_review_provenance") or {}
        ref = prov.get("review_reference") or ""
        if (not isinstance(ref, str) or not ref.startswith(REVIEW_PREFIX)
                or not ref.endswith(".json") or ".." in PurePosixPath(ref).parts):
            errors.append(f"{path}: changed mappings require a dated JSON review_reference under {REVIEW_PREFIX}")
            continue
        try:
            packet = read_at(head, ref)
        except (ValueError, json.JSONDecodeError) as exc:
            errors.append(f"{path}: cannot read decision packet {ref}: {exc}")
            continue
        errors.extend(verify_change(old, new, packet, ref in changed, path))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True)
    parser.add_argument("--head", default="HEAD")
    args = parser.parse_args()
    errors = check(args.base, args.head)
    if errors:
        print("VIGIL mapping-change provenance gate failed:", file=sys.stderr)
        for error in errors:
            print(" - " + error, file=sys.stderr)
        return 1
    print("VIGIL mapping-change provenance gate passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
