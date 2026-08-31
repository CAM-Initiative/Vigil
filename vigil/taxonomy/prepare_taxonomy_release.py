#!/usr/bin/env python3
"""Prepare one taxonomy dataset release after canonical changes land on main."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

import validate_taxonomy as validator

ROOT = Path(__file__).resolve().parent
INDEX_PATH = ROOT / "VIGIL.FailureTaxonomy.Index.json"
FAMILIES_DIR = ROOT / "families"


def next_release_version(previous: str, previous_families: set[str], current_families: set[str]) -> tuple[str, str]:
    parsed = validator.parse_version(previous)
    if parsed is None:
        raise ValueError(f"invalid current taxonomy version: {previous!r}")
    major, minor, patch, draft = parsed
    if not previous_families.issubset(current_families):
        major, minor, patch = major + 1, 0, 0
        change_level = "major"
    elif current_families != previous_families:
        minor, patch = minor + 1, 0
        change_level = "minor"
    else:
        patch += 1
        change_level = "patch"
    suffix = "-draft" if draft else ""
    return f"{major}.{minor}.{patch}{suffix}", change_level


def write_json(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def prepare_release(publication_date: str) -> bool:
    if not validator.valid_calendar_date(publication_date):
        raise ValueError("publication date must be YYYY-MM-DD")

    index = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    family_paths = sorted(FAMILIES_DIR.glob("*.json"))
    loaded = [(path, json.loads(path.read_text(encoding="utf-8"))) for path in family_paths]

    preflight, _ = validator.validate_catalogue(family_paths, enforce_current_release=False)
    if preflight:
        raise SystemExit("Working taxonomy is invalid before release preparation:\n" + "\n".join(preflight))

    family_ids = sorted(
        data["family"]["family_id"]
        for _, data in loaded
    )
    class_count = sum(len(data.get("classes", [])) for _, data in loaded)
    digest = validator.catalogue_content_digest(loaded)

    releases = index.get("release_history", [])
    if not releases or not isinstance(releases[-1], dict):
        raise ValueError("taxonomy release_history is missing a current release")
    current = releases[-1]

    already_published = (
        current.get("content_digest") == digest
        and current.get("family_ids") == family_ids
        and current.get("class_count") == class_count
    )
    if already_published:
        print(f"Taxonomy content already matches published release {current.get('version')}; no version bump required.")
        return False

    previous_version = current.get("version")
    previous_families = set(current.get("family_ids", []))
    new_version, change_level = next_release_version(previous_version, previous_families, set(family_ids))

    release = {
        "version": new_version,
        "publication_date": publication_date,
        "change_level": change_level,
        "content_digest": digest,
        "family_ids": family_ids,
        "class_count": class_count,
    }
    releases.append(release)
    index["standard"]["version"] = new_version
    index["standard"]["publication_date"] = publication_date
    for mapping in index.get("retired_class_mappings", []):
        if isinstance(mapping, dict) and mapping.get("retirement_release_status") == "pending-main-publication":
            mapping["retirement_release_status"] = "published"
            mapping["retired_in_version"] = new_version
    write_json(INDEX_PATH, index)

    for path, data in loaded:
        data["standard"]["version"] = new_version
        data["standard"]["publication_date"] = publication_date
        write_json(path, data)

    print(
        f"Prepared taxonomy release {new_version} ({change_level}) for {publication_date}: "
        f"{len(family_ids)} families, {class_count} classes."
    )
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--publication-date",
        default=date.today().isoformat(),
        help="fixed publication date for the main-branch release (default: current UTC runner date)",
    )
    args = parser.parse_args()
    prepare_release(args.publication_date)


if __name__ == "__main__":
    main()
