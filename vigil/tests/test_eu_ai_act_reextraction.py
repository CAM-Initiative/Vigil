#!/usr/bin/env python3
"""Regression checks for the canonical EU AI Act atomic migration."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQ = ROOT / "external_governance" / "requirements"
DIR = REQ / "reextractions"
CANONICAL_SHARD = REQ / "requirements" / "EU-AI-ACT-2024-1689" / "2026-07-27.json"
AGGREGATE = REQ / "requirements.json"
MANIFEST = REQ / "requirements" / "manifest.json"
RETIREMENT = REQ / "retirements" / "EU-AI-ACT-2024-1689.json"
NORMALIZATION = DIR / "EU-AI-ACT-2026-07-27-metadata-normalization.json"

RETIRED = {
    "EXTREQ-F30E6B9A906370B9",
    "EXTREQ-44B7BB17CB030468",
    "EXTREQ-09AD2F5442A55B55",
    "EXTREQ-901AD2C0A909E790",
    "EXTREQ-33898CCD26FBF5D5",
    "EXTREQ-126CB22D1FF08066",
    "EXTREQ-1B4CA7A04D63F038",
    "EXTREQ-E640D3CE18685E25",
}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def rid(source_id: str, version: str, clause: str, identity: str) -> str:
    seed = "|".join((source_id, version, clause.strip(), identity.strip()))
    return "EXTREQ-" + hashlib.sha256(seed.encode()).hexdigest()[:16].upper()


def main():
    paths = [
        path
        for path in sorted(DIR.glob("EU-AI-ACT-2026-07-27-*.json"))
        if path.name != NORMALIZATION.name
    ]
    docs = [load(path) for path in paths]
    normalization = load(NORMALIZATION)
    assert len(docs) == 5
    assert normalization["policy"]["mode"] == "source-explicit-overlay"

    staged = []
    retired = []
    for doc in docs:
        source = doc["source"]
        for record in doc["requirements"]:
            assert record["requirement_id"] == rid(
                source["vigil_source_id"], source["source_version"],
                record["clause_or_control"], record["identity_key"],
            )
            assert record["semantic_atomicity"] in {"atomic", "source-defined-compound"}
            if record["semantic_atomicity"] == "source-defined-compound":
                assert record.get("constituent_propositions")
            staged.append(record)
        retired.extend(doc["retired_requirements"])

    staged_ids = {record["requirement_id"] for record in staged}
    retired_ids = {item["requirement_id"] for item in retired}
    assert len(staged) == 102
    assert len(staged_ids) == 102
    assert retired_ids == RETIRED
    assert set(normalization["overrides"]) <= staged_ids
    assert len(normalization["overrides"]) == 18

    shard = load(CANONICAL_SHARD)
    shard_ids = [record["requirement_id"] for record in shard]
    assert len(shard) == 175
    assert len(shard_ids) == len(set(shard_ids))
    assert shard_ids == sorted(shard_ids)
    assert not (RETIRED & set(shard_ids))
    assert staged_ids <= set(shard_ids)

    by_id = {record["requirement_id"]: record for record in shard}
    for record in staged:
        canonical = by_id[record["requirement_id"]]
        assert canonical["requirement_id"] == rid(
            canonical["vigil_source_id"], canonical["source_version"],
            canonical["clause_or_control"], canonical["identity_key"],
        )
        assert canonical["semantic_atomicity"] == record["semantic_atomicity"]
        if record["semantic_atomicity"] == "source-defined-compound":
            assert canonical["constituent_propositions"] == record["constituent_propositions"]

    for requirement_id, override in normalization["overrides"].items():
        for field, value in override.items():
            assert by_id[requirement_id][field] == value

    aggregate = load(AGGREGATE)
    aggregate_by_id = {record["requirement_id"]: record for record in aggregate["requirements"]}
    assert aggregate["requirement_count"] == len(aggregate["requirements"])
    assert len(aggregate_by_id) == aggregate["requirement_count"]
    assert all(aggregate_by_id[record["requirement_id"]] == record for record in shard)
    assert load(MANIFEST)["updated_at"] == aggregate["updated_at"] == "2026-09-20"

    retirement = load(RETIREMENT)
    retirement_ids = {item["requirement_id"] for item in retirement["retired_requirements"]}
    successor_ids = {
        successor
        for item in retirement["retired_requirements"]
        for successor in item["successor_requirement_ids"]
    }
    assert retirement_ids == RETIRED
    assert successor_ids == staged_ids
    assert successor_ids <= set(shard_ids)
    assert not (RETIRED & set(aggregate_by_id))
    assert not any(RETIRED & set(record.get("related_external_requirements", [])) for record in shard)

    print("EU AI Act canonical migration valid: 8 retired identities -> 102 successors; EU shard contains 175 records")


if __name__ == "__main__":
    main()
