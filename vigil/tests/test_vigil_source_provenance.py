#!/usr/bin/env python3
"""Regression checks for Incident source-origin detection."""

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "vigil" / "scripts" / "source_provenance.py"
SPEC = importlib.util.spec_from_file_location("source_provenance", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)


def main() -> int:
    external = {
        "source_title": "Incident 1661: external registry entry",
        "author_or_publisher": "AI Incident Database",
        "source_url": "https://incidentdatabase.ai/cite/1661/",
        "source_platform": "AI Incident Database",
        "source_type": "incident database entry",
        "relevance_note": "VIGIL preserves this external source.",
    }
    assert MODULE.origin_markers(external) == (False, False)

    historical_token = {
        "source_title": "VIGIL-2026-FM-0044 — historical migration source",
        "author_or_publisher": "VIGIL",
        "source_url": "https://github.com/CAM-Initiative/Vigil/blob/main/example.json",
        "source_platform": "VIGIL",
        "source_type": "governance record",
    }
    assert MODULE.origin_markers(historical_token) == (True, True)

    incident_reference = {
        "source_title": "VIGIL-INC-000003 — related Incident",
        "author_or_publisher": "VIGIL",
        "source_platform": "VIGIL",
        "source_type": "governance record",
    }
    assert MODULE.origin_markers(incident_reference)[0]

    cam_source = {
        "source_title": "Current Caelestis SECURITY instrument",
        "author_or_publisher": "CAM Initiative",
        "source_url": "https://github.com/CAM-Initiative/Caelestis/blob/main/example.md",
        "source_platform": "GitHub",
        "source_type": "governance record",
    }
    looks_vigil, looks_cam = MODULE.origin_markers(cam_source)
    assert not looks_vigil
    assert looks_cam
    print("Incident source provenance origin tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
