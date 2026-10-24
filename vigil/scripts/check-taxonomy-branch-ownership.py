#!/usr/bin/env python3
"""Block normative taxonomy edits coming from the wrong PR source branch.

Incident-derived invariant_exemplars, generated publications and assets are not
canonical taxonomy recognition criteria, and do not require a taxonomy PR.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys

TAXONOMY = "vigil/taxonomy/"
FAMILIES = TAXONOMY + "families/"
ALLOWED_BRANCH = "agent/taxonomy-development"
EXEMPT = (TAXONOMY + "generated/", TAXONOMY + "assets/")


def controlled(path):
    return path.startswith(TAXONOMY) and not path.startswith(EXEMPT)


def stripped_family(data):
    body = json.loads(data)
    if not isinstance(body, dict) or not isinstance(body.get("classes"), list):
        raise ValueError("Not a taxonomy family document")
    result = dict(body)
    result["classes"] = []
    for entry in body["classes"]:
        item = dict(entry)
        item.pop("invariant_exemplars", None)
        result["classes"].append(item)
    return result


def normative_change(path, old, new):
    if not controlled(path):
        return False
    if path.startswith(FAMILIES) and path.endswith(".json") and old is not None and new is not None:
        return stripped_family(old) != stripped_family(new)
    return old != new


def git(*args):
    return subprocess.check_output(("git", *args), stderr=subprocess.PIPE)


def read_blob(ref, path):
    proc = subprocess.run(("git", "cat-file", "-e", f"{ref}:{path}"), capture_output=True)
    return git("show", f"{ref}:{path}") if proc.returncode == 0 else None


def changed_paths(base, head):
    raw = git("diff", "--no-renames", "--name-only", "-z", base, head, "--", TAXONOMY)
    return sorted(p.decode("utf-8") for p in raw.split(b"\0") if p)


def check(base, head, source_branch):
    if source_branch == ALLOWED_BRANCH:
        return []
    violations = []
    for path in changed_paths(base, head):
        try:
            if normative_change(path, read_blob(base, path), read_blob(head, path)):
                violations.append(path)
        except (ValueError, TypeError) as exc:
            violations.append(f"{path} (cannot verify exemplar-only scope: {exc})")
    return violations


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True)
    parser.add_argument("--head", required=True)
    parser.add_argument("--head-branch", required=True)
    args = parser.parse_args()
    errors = check(args.base, args.head, args.head_branch)
    if errors:
        print("Normative taxonomy changes must originate on " + ALLOWED_BRANCH, file=sys.stderr)
        for path in errors:
            print(" - " + path, file=sys.stderr)
        return 1
    print("Taxonomy branch ownership passed:", args.head_branch)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
