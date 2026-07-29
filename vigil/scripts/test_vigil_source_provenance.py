#!/usr/bin/env python3
"""Focused tests for deterministic source provenance classification."""

from __future__ import annotations

import importlib.util
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve()
MIGRATION_PATH = SCRIPT_PATH.with_name("migrate-vigil-source-provenance.py")

spec = importlib.util.spec_from_file_location("source_provenance_migration", MIGRATION_PATH)
assert spec and spec.loader
migration = importlib.util.module_from_spec(spec)
spec.loader.exec_module(migration)


def classify(source, record_type="failure_mode"):
    residence = migration.classify_residence(source)
    role = migration.classify_role(source, record_type, residence)
    return residence, role


def main() -> int:
    assert classify({
        "source_title": "OpenAI incident disclosure",
        "author_or_publisher": "OpenAI",
        "source_url": "https://openai.com/example",
        "source_type": "official-source",
    }) == ("external", "incident-evidence")

    assert classify({
        "source_title": "Security incident disclosure — July 2026",
        "author_or_publisher": "Hugging Face",
        "source_url": "https://huggingface.co/blog/security-incident",
        "source_type": "official-source",
        "source_context": "Affected-party incident disclosure",
    }) == ("external", "affected-party-evidence")

    assert classify({
        "source_title": "Current Caelestis ETHICS and SECURITY instruments",
        "author_or_publisher": "CAM Initiative",
        "source_url": "https://github.com/CAM-Initiative/Caelestis",
        "source_type": "repository-source",
    }, "proposal") == ("cam-internal", "governance-basis")

    assert classify({
        "source_title": "CAM-EQ2026-OPERATIONS-003-SUP-01 failure taxonomy",
        "author_or_publisher": "CAM Initiative",
        "source_url": "https://github.com/CAM-Initiative/Caelestis",
        "source_type": "repository-source",
    }, "failure_mode") == ("cam-internal", "taxonomy-basis")

    assert classify({
        "source_title": "VIGIL-2026-FM-0044 — linked failure mode",
        "author_or_publisher": "VIGIL",
        "source_type": "linked-failure-mode",
    }, "proposal") == ("vigil-internal", "record-cross-reference")

    assert classify({
        "source_title": "Account-holder incident testimony",
        "author_or_publisher": "Anonymous account holder",
        "source_url_status": "not applicable — direct incident testimony",
        "source_type": "other",
    }, "observation") == ("user-supplied", "direct-testimony")

    print("Source provenance classification tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
