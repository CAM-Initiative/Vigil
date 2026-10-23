#!/usr/bin/env python3
"""Deterministic preflight SHA-256 inventory of the frozen SIAI research corpus.

Read Git blobs from the exact source commit, not from a mutable branch.
Does not publish or authorise the candidate v1.0.0 release.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
SOURCE = "f031c4421f772e1af5b945bc388363aa81e1a179"
OUTPUT = Path(__file__).resolve().parent / "RESEARCH-SNAPSHOT.preflight.json"
PREFIXES = (
    "vigil/records/", "vigil/taxonomy/", "vigil/methodologies/",
    "vigil/external_governance/", "vigil/cam_assessment/",
    "vigil/references/", "vigil/templates/", "vigil/tests/",
    "vigil/scripts/", "vigil/docs/maintenance/", "vigil/docs/reviews/",
)
EXACT = (
    "vigil/VIGIL.Schema.json", "vigil/VIGIL.Incidents.Index.json",
    "vigil/VIGIL.Registry.Index.json",
    "vigil/VIGIL.Incidents.Jurisdictions.Index.json",
    "LICENSE.md", "RIGHTS.json",
)


def git(*args: str) -> bytes:
    return subprocess.check_output(["git", *args], cwd=ROOT)


def in_scope(path: str) -> bool:
    return path in EXACT or path.startswith(PREFIXES)


def generate() -> dict:
    git("cat-file", "-e", SOURCE + "^{commit}")
    source_tree = git("ls-tree", "-r", "-z", SOURCE)
    items = []
    record_count = 0
    version_counts: Counter[str] = Counter()
    status_counts: Counter[str] = Counter()
    source_records = 0
    taxonomy = None
    for line in source_tree.split(b"\0"):
        if not line:
            continue
        info, path_bytes = line.split(b"\t", 1)
        mode, kind, oid = info.decode("ascii").split()
        path = path_bytes.decode("utf-8")
        if kind != "blob" or not in_scope(path):
            continue
        content = git("cat-file", "blob", oid)
        items.append({
            "path": path, "size_bytes": len(content),
            "git_blob_sha1": oid,
            "sha256": hashlib.sha256(content).hexdigest(),
        })
        if path.startswith("vigil/records/incidents/") and path.endswith(".json"):
            item = json.loads(content)
            tc = item.get("taxonomy_classification") or {}
            version_counts[str(tc.get("taxonomy_version") or "unspecified")] += 1
            status_counts[str(tc.get("classification_status") or "unspecified")] += 1
            source_records += len(item.get("source_records") or [])
            record_count += 1
        if path == "vigil/taxonomy/VIGIL.FailureTaxonomy.Index.json":
            taxonomy = json.loads(content)

    if record_count != 200:
        raise SystemExit(f"Expected exactly 200 canonical Incident records, found {record_count}")
    if taxonomy is None:
        raise SystemExit("Published taxonomy index not included")
    standard = taxonomy.get("standard", {})
    release = next((x for x in taxonomy.get("release_history", [])
                    if x.get("version") == standard.get("version")), None)
    if (standard.get("version"), len(taxonomy.get("families", [])),
            (release or {}).get("class_count")) != ("0.8.0", 17, 80):
        raise SystemExit("Unexpected published taxonomy metadata; expected 0.8.0 / 17 / 80")
    items.sort(key=lambda x: x["path"])
    aggregate = b"".join(
        x["path"].encode("utf-8") + b"\0" +
        x["sha256"].encode("ascii") + b"\n"
        for x in items
    )
    return {
        "manifest_schema": "vigil-research-snapshot-preflight/1",
        "project": "VIGIL Observatory",
        "candidate_dataset_version": "1.0.0",
        "state": "PREFLIGHT_ONLY_NOT_PUBLISHED",
        "source_repository": "CAM-Initiative/Vigil",
        "source_commit": SOURCE,
        "hash_method": "SHA-256 of exact Git blob bytes at immutable source commit",
        "scope": {
            "file_path_prefixes": list(PREFIXES),
            "exact_files": sorted(EXACT),
            "exclusions": [
                "this manifest and release-preparation scaffolding",
                "mutable README and provisional citation metadata",
                "GitHub Actions metadata and agent operating notes",
            ],
        },
        "taxonomy": {
            "published_version": standard["version"],
            "published_date": standard.get("publication_date"),
            "status": standard.get("status"),
            "fidelity_family_count": len(taxonomy["families"]),
            "selectable_fidelity_class_count": release["class_count"],
            "published_content_digest": release.get("content_digest"),
        },
        "corpus": {
            "incident_json_count": record_count,
            "source_record_entries": source_records,
            "classification_status_counts": dict(sorted(status_counts.items())),
            "adjudication_taxonomy_version_counts": dict(sorted(version_counts.items())),
            "independent_human_validation_established": False,
        },
        "rights": {
            "status": "proprietary/all-rights-reserved",
            "rights_files_included": list(EXACT[-2:]),
            "zenodo_licence_approved": False,
        },
        "inventory": {
            "file_count": len(items),
            "canonical_entry_stream_sha256": hashlib.sha256(aggregate).hexdigest(),
            "files": items,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    opt = parser.add_mutually_exclusive_group(required=True)
    opt.add_argument("--write", action="store_true")
    opt.add_argument("--check", action="store_true")
    parser.add_argument("--verify-preservation", action="store_true")
    args = parser.parse_args()
    if args.verify_preservation:
        altered = git("diff", "--name-only", SOURCE, "HEAD", "--", *PREFIXES, *EXACT)
        if altered.strip():
            print("ERROR: release branch alters frozen research files:", file=sys.stderr)
            print(altered.decode("utf-8", "replace"), file=sys.stderr)
            return 1
    manifest = generate()
    payload = (json.dumps(manifest, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")
    if args.write:
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT.write_bytes(payload)
        print(f"Built preflight: {manifest['corpus']['incident_json_count']} Incidents, "
              f"{manifest['inventory']['file_count']} frozen files, "
              f"SHA-256 {manifest['inventory']['canonical_entry_stream_sha256']}")
        return 0
    if not OUTPUT.exists() or OUTPUT.read_bytes() != payload:
        print("ERROR: manifest missing or does not match pinned scientific commit", file=sys.stderr)
        return 1
    print("PASS: manifest matches immutable Git source and per-file SHA-256")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
