#!/usr/bin/env python3
"""One-time release metadata update for the FC-000056 taxonomy addition."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "taxonomy"
FAMILIES = ROOT / "families"
INDEX = ROOT / "VIGIL.FailureTaxonomy.Index.json"
VERSION = "0.2.3-draft"
PUBLICATION_DATE = "2026-08-30"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def digest(loaded):
    payload = [
        {"family": data.get("family"), "classes": data.get("classes", [])}
        for path, data in sorted(loaded, key=lambda row: str(row[1].get("family", {}).get("family_id", row[0])))
    ]
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return f"sha256:{hashlib.sha256(encoded).hexdigest()}"


def main() -> None:
    loaded = []
    for path in sorted(FAMILIES.glob("*.json")):
        data = load(path)
        data["standard"]["version"] = VERSION
        data["standard"]["publication_date"] = PUBLICATION_DATE
        write(path, data)
        loaded.append((path, data))

    family_ids = sorted(data["family"]["family_id"] for _, data in loaded)
    class_count = sum(len(data.get("classes", [])) for _, data in loaded)
    content_digest = digest(loaded)

    index = load(INDEX)
    index["standard"]["version"] = VERSION
    index["standard"]["publication_date"] = PUBLICATION_DATE

    releases = index.setdefault("release_history", [])
    release = {
        "version": VERSION,
        "publication_date": PUBLICATION_DATE,
        "change_level": "patch",
        "content_digest": content_digest,
        "family_ids": family_ids,
        "class_count": class_count,
    }
    if releases and releases[-1].get("version") == VERSION:
        releases[-1] = release
    else:
        releases.append(release)

    for family_entry in index.get("families", []):
        if family_entry.get("family_id") == "VIGIL-FF-0006":
            family_entry["version"] = "0.1.1"
            family_entry["class_count"] = 4

    write(INDEX, index)
    print(f"Finalised {VERSION}: {class_count} classes, {content_digest}")


if __name__ == "__main__":
    main()
