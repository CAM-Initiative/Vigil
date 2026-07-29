#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATCH_DIR = ROOT / "records" / "patches" / "2026"
SHA_RE = re.compile(r"^[0-9a-f]{40}$", re.I)
ALLOWED_MODES = {"contemporaneous-vigil-trace", "retrospective-reconstruction"}
ALLOWED_RELEASE_STATUS = {"verified", "not-established-from-current-record", "not-applicable"}


def main() -> int:
    errors: list[str] = []
    paths = sorted(PATCH_DIR.glob("VIGIL-*-PATCH-*.json"))
    for path in paths:
        record = json.loads(path.read_text(encoding="utf-8"))
        provenance = record.get("corpus_release_provenance")
        prefix = str(path)
        if not isinstance(provenance, dict):
            errors.append(f"{prefix}: corpus_release_provenance is required")
            continue
        if provenance.get("repository") != "CAM-Initiative/Caelestis":
            errors.append(f"{prefix}: corpus_release_provenance.repository must be CAM-Initiative/Caelestis")
        if provenance.get("provenance_mode") not in ALLOWED_MODES:
            errors.append(f"{prefix}: invalid corpus_release_provenance.provenance_mode")
        implementation = provenance.get("implementation_corpus_state")
        if not isinstance(implementation, dict):
            errors.append(f"{prefix}: implementation_corpus_state is required")
        else:
            commit = implementation.get("commit")
            if commit is not None and not SHA_RE.fullmatch(str(commit)):
                errors.append(f"{prefix}: implementation_corpus_state.commit must be a 40-character SHA or null")
            if not implementation.get("repository_ref"):
                errors.append(f"{prefix}: implementation_corpus_state.repository_ref is required")
            if not implementation.get("canonical_state_at_recording"):
                errors.append(f"{prefix}: implementation_corpus_state.canonical_state_at_recording is required")
        canonical = provenance.get("canonical_corpus_state")
        if not isinstance(canonical, dict):
            errors.append(f"{prefix}: canonical_corpus_state is required")
        else:
            commit = canonical.get("commit")
            if commit is not None and not SHA_RE.fullmatch(str(commit)):
                errors.append(f"{prefix}: canonical_corpus_state.commit must be a 40-character SHA or null")
        release = provenance.get("published_release_at_implementation")
        if not isinstance(release, dict) or release.get("status") not in ALLOWED_RELEASE_STATUS:
            errors.append(f"{prefix}: published_release_at_implementation.status is invalid")
        current = provenance.get("current_public_archive_reference")
        if not isinstance(current, dict):
            errors.append(f"{prefix}: current_public_archive_reference is required")
        elif current.get("version") == "1.1.0" and "not asserted" not in str(current.get("relationship", "")):
            errors.append(f"{prefix}: v1.1.0 current archive reference must not imply unverified historical release inclusion")

    if errors:
        print("PATCH corpus provenance validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Validated corpus release provenance on {len(paths)} PATCH record(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
