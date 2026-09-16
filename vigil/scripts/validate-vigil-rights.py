#!/usr/bin/env python3
"""Check active VIGIL Observatory metadata for the proprietary rights contract."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[2]
ACTIVE_FILES = [
    ROOT / "README.md",
    ROOT / "CITATION.cff",
    ROOT / "vigil" / "taxonomy" / "README.md",
    ROOT / "vigil" / "external_governance" / "requirements" / "dataset" / "CITATION.cff",
    ROOT / "vigil" / "taxonomy" / "render_taxonomy.py",
]
LEGACY = re.compile(r"CC[- ]?BY|Creative Commons|BY[- ]?NC|creativecommons\.org/licenses", re.I)

def find_errors():
    errors = []
    if not (ROOT / "LICENSE.md").exists():
        errors.append("LICENSE.md is missing")
    if (ROOT / "Licence.md").exists():
        errors.append("legacy Licence.md must not remain")

    rights = ROOT / "RIGHTS.json"
    try:
        data = json.loads(rights.read_text(encoding="utf-8"))
        if data.get("project") != "VIGIL Observatory":
            errors.append("RIGHTS.json project must be VIGIL Observatory")
        if data.get("technical_namespace") != "VIGIL":
            errors.append("RIGHTS.json technical_namespace must remain VIGIL")
        if data.get("protected_materials_name") != "VIGIL Observatory Materials":
            errors.append("RIGHTS.json protected_materials_name is incorrect")
        if data.get("rights_status") != "proprietary":
            errors.append("RIGHTS.json must declare proprietary rights_status")
        if data.get("copyright_holder") != "Phoenix Covenant Pty Ltd trading as CAM Initiative":
            errors.append("RIGHTS.json copyright holder is incorrect")
        if data.get("abn") != "14 692 195 529":
            errors.append("RIGHTS.json ABN is incorrect")
        if "author" in data:
            errors.append("RIGHTS.json must not assign personal authorship in the corporate rights contract")
    except Exception as exc:
        errors.append(f"RIGHTS.json is invalid: {exc}")

    for path in ACTIVE_FILES:
        text = path.read_text(encoding="utf-8")
        if LEGACY.search(text):
            errors.append(f"legacy open-licence declaration in {path.relative_to(ROOT)}")

    license_text = (ROOT / "LICENSE.md").read_text(encoding="utf-8")
    for needle in (
        "VIGIL Observatory Proprietary Licence",
        "VIGIL Observatory Materials",
        "CAM Initiative and VIGIL Observatory",
        "Phoenix Covenant Pty Ltd trading as CAM Initiative",
        "ABN 14 692 195 529",
        "16 September 2026",
        "research@cam-initiative.org",
        "Third-party reliance",
        "machine-learning",
    ):
        if needle not in license_text:
            errors.append(f"LICENSE.md missing: {needle}")

    for forbidden in (
        "Dr Michelle O'Rourke",
        "CAM Initiative and Dr Michelle O'Rourke",
        "VIGIL Materials",
    ):
        if forbidden in license_text:
            errors.append(f"LICENSE.md retains superseded legal identity wording: {forbidden}")

    return errors

if __name__ == "__main__":
    errors = find_errors()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    print("VIGIL Observatory rights validation passed")
