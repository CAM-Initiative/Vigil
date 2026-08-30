#!/usr/bin/env python3
"""Focused regression checks for source-provenance classification and origin detection."""

from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "vigil" / "scripts"
MIGRATION_PATH = SCRIPTS / "migrate-vigil-source-provenance.py"
VALIDATOR_PATH = SCRIPTS / "validate-vigil-source-provenance.py"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


migration = load_module(MIGRATION_PATH, "source_provenance_migration")
validator = load_module(VALIDATOR_PATH, "source_provenance_validator")


def classify(source, record_type="failure_mode"):
    residence = migration.classify_residence(source)
    role = migration.classify_role(source, record_type, residence)
    return residence, role


def main() -> int:
    assert classify({
        "source_title": "OpenAI and Hugging Face partner to address security incident during model evaluation",
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

    # Source origin is determined from identity/provenance fields. VIGIL's own
    # interpretive commentary must not convert an external source into an
    # internal source merely because it says how VIGIL uses the source.
    external_with_vigil_commentary = {
        "source_title": "Incident 1661: external incident registry entry",
        "author_or_publisher": "AI Incident Database",
        "source_url": "https://incidentdatabase.ai/cite/1661/",
        "source_platform": "AI Incident Database",
        "source_type": "incident-database record",
        "relevance_note": "VIGIL uses this external registry entry as corroboration only.",
        "source_context": "VIGIL preserves the source's stated incident metadata without strengthening it.",
    }
    assert validator.origin_markers(external_with_vigil_commentary) == (False, False)

    vigil_cross_reference = {
        "source_title": "VIGIL-2026-FM-0044 — linked failure mode",
        "author_or_publisher": "VIGIL",
        "source_url": "https://github.com/CAM-Initiative/Vigil/blob/main/example.json",
        "source_platform": "VIGIL",
        "source_type": "linked-failure-mode",
    }
    assert validator.origin_markers(vigil_cross_reference) == (True, True)

    vigil_review_session = {
        "source_title": "Three ChatGPT systems repeat responses without synthetic turn-taking",
        "author_or_publisher": "CAM Initiative / VIGIL review session",
        "source_url": "https://vt.tiktok.com/example/",
        "source_platform": "TikTok",
        "source_type": "platform-behaviour-observation",
    }
    assert validator.origin_markers(vigil_review_session) == (True, True)

    vigil_governance_note = {
        "source_title": "VIGIL maintainer discussion of repeated user reports",
        "author_or_publisher": "Maintainer discussion",
        "source_url": "https://chatgpt.com/example",
        "source_platform": "ChatGPT",
        "source_type": "governance-note",
    }
    assert validator.origin_markers(vigil_governance_note) == (True, False)

    relayed_external_report = {
        "source_title": "User-reported ChatGPT refusal screenshot",
        "author_or_publisher": "Third-party user report relayed to VIGIL maintainer",
        "source_url": "https://x.com/example/status/1",
        "source_platform": "X",
        "source_type": "social-platform-observation",
    }
    assert validator.origin_markers(relayed_external_report) == (False, False)

    cam_governance_source = {
        "source_title": "Current Caelestis SECURITY instrument",
        "author_or_publisher": "CAM Initiative",
        "source_url": "https://github.com/CAM-Initiative/Caelestis/blob/main/example.md",
        "source_platform": "GitHub",
        "source_type": "repository-source",
    }
    looks_vigil, looks_cam = validator.origin_markers(cam_governance_source)
    assert not looks_vigil
    assert looks_cam

    print("Source provenance classification and origin-detection tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
