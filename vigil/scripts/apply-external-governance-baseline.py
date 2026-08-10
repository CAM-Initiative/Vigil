#!/usr/bin/env python3
"""Apply a versioned external-governance baseline without semantic alignment.

Baseline files contain already-normalised official-source observations. This builder
feeds them through the canonical ledger machinery, fixes release timestamps for
reproducibility, and renders the human-readable source table. It never edits
Caelestis and never creates substantive VIGIL records.
"""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXT = ROOT / "external_sources"
LEDGER = EXT / "ledger.json"
QUEUE = EXT / "alignment-queue.json"
VIEW = EXT / "EXTERNAL-GOVERNANCE-SOURCES.md"
RELEASE_DIR = EXT / "baseline-release-2"
RELEASE_TS = "2026-08-10T00:50:00Z"
RELEASE_NAME = "Baseline Release 2"

MANAGER_PATH = ROOT / "scripts" / "manage-external-governance-ledger.py"
spec = importlib.util.spec_from_file_location("external_ledger", MANAGER_PATH)
manager = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(manager)

SEEDS = [
    ("iso-open-data", RELEASE_DIR / "iso-sc42.json"),
    ("ieee-standards", RELEASE_DIR / "ieee.json"),
    ("nist-csrc", RELEASE_DIR / "nist.json"),
    ("eu-eurlex", RELEASE_DIR / "eu.json"),
]


def dump(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, separators=(",", ":"), ensure_ascii=False) + "\n", encoding="utf-8")


def render(entries: list[dict]) -> None:
    lines = [
        f"# External Governance Sources — {RELEASE_NAME}",
        "",
        f"Generated from `vigil/external_sources/ledger.json` for the fixed release observation `{RELEASE_TS}`.",
        "",
        "This is a maintenance view, not a statement that Caelestis conforms to every listed source. `review-required` means the external source is final/alignment-eligible and requires human semantic disposition against Caelestis.",
        "",
        "| VIGIL Source | External Source | Version | Issuer | Jurisdiction | Lifecycle | CAM Alignment | Canonical Identifier |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for e in entries:
        lines.append(
            f"| `{e['vigil_source_id']}` | {e.get('title') or ''} | `{e['source_version']}` | "
            f"{e['issuer']} | {e['jurisdiction']} | `{e['source_lifecycle_state']}` | "
            f"`{e['alignment_state']}` | `{e['canonical_identifier']['value']}` |"
        )
    lines += [
        "",
        f"## {RELEASE_NAME}",
        "",
        f"{len(entries)} final/current external source versions are registered. Draft and under-development instruments remain monitor-only and are not added to the alignment queue until their publisher reports a final/alignment-eligible lifecycle state.",
        "",
        "## Provenance boundary",
        "",
        "Official publishers and regulators are authoritative for lifecycle and version status. Third-party trackers are discovery-only. Vorp Labs is excluded from this intake design.",
        "",
    ]
    VIEW.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    for source, path in SEEDS:
        manager.ingest(source, path)

    ledger = manager.load_json(LEDGER)
    ledger["updated_at"] = RELEASE_TS
    # Keep the release snapshot deterministic: rows introduced by Release 2 remain
    # represented as new baseline observations rather than flipping to unchanged on
    # repeated local/CI reconstruction.
    for entry in ledger.get("entries", []):
        if entry.get("upstream_release") == "baseline-release-2":
            entry["change_state"] = "new"
            entry["last_seen"] = RELEASE_TS
    ledger["entries"] = sorted(
        ledger.get("entries", []), key=lambda x: (x["external_source_id"], x["source_version"])
    )
    dump(LEDGER, ledger)

    manager.build_queue()
    queue = manager.load_json(QUEUE)
    queue["generated_at"] = RELEASE_TS
    dump(QUEUE, queue)
    render(ledger["entries"])
    manager.validate()
    print(f"{RELEASE_NAME} applied: {len(ledger['entries'])} external source versions")


if __name__ == "__main__":
    main()
