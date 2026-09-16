#!/usr/bin/env python3
"""Check active VIGIL metadata for the proprietary rights contract."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[2]
ACTIVE_FILES = [ROOT / "README.md", ROOT / "CITATION.cff", ROOT / "vigil" / "taxonomy" / "README.md", ROOT / "vigil" / "external_governance" / "requirements" / "dataset" / "CITATION.cff", ROOT / "vigil" / "taxonomy" / "render_taxonomy.py"]
LEGACY = re.compile(r"CC[- ]?BY|Creative Commons|BY[- ]?NC|creativecommons\.org/licenses", re.I)

def find_errors():
    errors = []
    if not (ROOT / "LICENSE.md").exists(): errors.append("LICENSE.md is missing")
    if (ROOT / "Licence.md").exists(): errors.append("legacy Licence.md must not remain")
    rights = ROOT / "RIGHTS.json"
    try:
        data = json.loads(rights.read_text(encoding="utf-8"))
        if data.get("rights_status") != "proprietary": errors.append("RIGHTS.json must declare proprietary rights_status")
        if data.get("copyright_holder") != "Phoenix Covenant Pty Ltd trading as CAM Initiative": errors.append("RIGHTS.json copyright holder is incorrect")
    except Exception as exc:
        errors.append(f"RIGHTS.json is invalid: {exc}")
    for path in ACTIVE_FILES:
        text = path.read_text(encoding="utf-8")
        if LEGACY.search(text): errors.append(f"legacy open-licence declaration in {path.relative_to(ROOT)}")
    license_text = (ROOT / "LICENSE.md").read_text(encoding="utf-8")
    for needle in ("Phoenix Covenant Pty Ltd trading as CAM Initiative", "16 September 2026", "research@cam-initiative.org", "Third-party", "machine-learning"):
        if needle not in license_text: errors.append(f"LICENSE.md missing: {needle}")
    return errors

if __name__ == "__main__":
    errors = find_errors()
    if errors:
        for error in errors: print(f"ERROR: {error}")
        raise SystemExit(1)
    print("VIGIL rights validation passed")
