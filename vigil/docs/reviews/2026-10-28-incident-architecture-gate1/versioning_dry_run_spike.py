#!/usr/bin/env python3
"""Read-only, isolated Incident version-numbering SPIKE (not a VIGIL validator).

Only in-memory string/snapshot inputs are used. Never opens or writes canonical
records; never integrates with GitHub Actions. The semantic level is supplied by
the reviewer, NOT inferred from JSON content. Gate 1 approval is required before
any version enforcement or pipeline change is implemented.
"""
from __future__ import annotations

import argparse
import json
import re
import unittest

VERSION = re.compile(r"^(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)$")
LEVELS = {"major", "minor", "patch", "none"}
RANK = {"none": 0, "patch": 1, "minor": 2, "major": 3}


def parse_version(text: str) -> tuple[int, int, int]:
    match = VERSION.fullmatch(text or "")
    if match is None:
        raise ValueError(f"invalid Incident version: {text!r}")
    return tuple(map(int, match.groups()))


def bump(published_version: str, level: str) -> str:
    major, minor, patch = parse_version(published_version)
    if level not in LEVELS:
        raise ValueError(f"unknown declared change level: {level!r}")
    if level == "major":
        return f"{major + 1}.0.0"
    if level == "minor":
        return f"{major}.{minor + 1}.0"
    if level == "patch":
        return f"{major}.{minor}.{patch + 1}"
    return published_version


def choose_highest(levels: list[str]) -> str:
    if not levels or any(level not in LEVELS for level in levels):
        raise ValueError("levels must be non-empty and contain only major/minor/patch/none")
    return max(levels, key=lambda value: RANK[value])


def propose(
    *,
    published_version: str | None,
    staged_version: str,
    declared_level: str,
    canonical_payload_changed: bool,
    published_blob_sha: str | None = None,
    observed_main_blob_sha: str | None = None,
    canonical_mapping_changed: bool = False,
) -> dict[str, object]:
    """Calculate a reviewed candidate without performing I/O or edits.

    The caller MUST establish the exact published-main canonical payload and
    whether it differs from the final proposed Incident. The boolean cannot
    substitute for source-first semantic review.
    """
    parse_version(staged_version)
    if declared_level not in LEVELS:
        raise ValueError(f"invalid change level: {declared_level!r}")
    if (published_blob_sha is None) != (observed_main_blob_sha is None):
        raise ValueError("both published blob identities required for freshness comparison")
    if published_blob_sha is not None and published_blob_sha != observed_main_blob_sha:
        raise ValueError("published main Incident changed: rebase/reconcile before version preparation")

    if published_version is None:
        if not canonical_payload_changed:
            raise ValueError("new Incident must have a new canonical payload")
        if declared_level == "none":
            raise ValueError("new Incident must be explicitly declared a first publication")
        return {
            "action": "first-publication-preserve-staged",
            "candidate_version": staged_version,
            "needs_preparation": False,
            "note": "New Incident has no main version baseline; preserve approved staged version and full review history.",
        }

    parse_version(published_version)
    if not canonical_payload_changed:
        if declared_level != "none":
            raise ValueError("unchanged Incident may not declare a revision")
        if staged_version != published_version:
            raise ValueError("unchanged Incident may not increment its version")
        return {"action": "unchanged", "candidate_version": published_version,
                "needs_preparation": False}

    if declared_level == "none":
        raise ValueError("changed canonical Incident requires a non-none revision level")
    if canonical_mapping_changed and RANK[declared_level] < RANK["minor"]:
        raise ValueError("new/removed/revised canonical taxonomy mapping requires at least MINOR")
    candidate = bump(published_version, declared_level)
    return {
        "action": "reconcile-and-prepare-published-version",
        "candidate_version": candidate,
        "needs_preparation": candidate != staged_version,
        "note": "One highest justified revision from fresh published main; never bump per working commit.",
    }


class IsolatedVersioningTests(unittest.TestCase):
    def test_minor_mapping(self):
        got = propose(published_version="1.4.11", staged_version="1.4.12",
                      declared_level="minor", canonical_payload_changed=True,
                      canonical_mapping_changed=True)
        self.assertEqual(got["candidate_version"], "1.5.0")
        self.assertTrue(got["needs_preparation"])

    def test_patch(self):
        self.assertEqual(bump("1.4.11", "patch"), "1.4.12")

    def test_major_existing_2(self):
        self.assertEqual(bump("2.0.7", "major"), "3.0.0")

    def test_minor_old_zero(self):
        self.assertEqual(bump("0.1.16", "minor"), "0.2.0")

    def test_highest_single_increment(self):
        self.assertEqual(choose_highest(["patch", "minor", "patch"]), "minor")

    def test_new_staged_version(self):
        got = propose(published_version=None, staged_version="0.1.1",
                      declared_level="minor", canonical_payload_changed=True)
        self.assertEqual(got["candidate_version"], "0.1.1")
        self.assertFalse(got["needs_preparation"])

    def test_noop(self):
        got = propose(published_version="1.4.11", staged_version="1.4.11",
                      declared_level="none", canonical_payload_changed=False)
        self.assertEqual(got["action"], "unchanged")

    def test_stale_published_main_block(self):
        with self.assertRaisesRegex(ValueError, "main Incident changed"):
            propose(published_version="1.4.11", staged_version="1.4.12",
                    declared_level="patch", canonical_payload_changed=True,
                    published_blob_sha="blob-before", observed_main_blob_sha="blob-after")

    def test_cannot_label_mapping_as_patch(self):
        with self.assertRaisesRegex(ValueError, "MINOR"):
            propose(published_version="1.4.11", staged_version="1.4.12",
                    declared_level="patch", canonical_payload_changed=True,
                    canonical_mapping_changed=True)

    def test_cannot_bump_noop(self):
        with self.assertRaisesRegex(ValueError, "unchanged Incident may not increment"):
            propose(published_version="1.4.11", staged_version="1.4.12",
                    declared_level="none", canonical_payload_changed=False)

    def test_cannot_skip_changed(self):
        with self.assertRaisesRegex(ValueError, "requires a non-none"):
            propose(published_version="1.4.11", staged_version="1.4.11",
                    declared_level="none", canonical_payload_changed=True)

    def test_reject_invalid_version(self):
        with self.assertRaises(ValueError):
            parse_version("01.0.0")

    def test_independent_incidents(self):
        self.assertEqual(bump("1.1.23", "patch"), "1.1.24")
        self.assertEqual(bump("0.1.16", "minor"), "0.2.0")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true", required=True,
                        help="run isolated fixture tests; never access the repository")
    args = parser.parse_args()
    if args.self_test:
        unittest.main(argv=["versioning_dry_run_spike.py"], verbosity=2)
