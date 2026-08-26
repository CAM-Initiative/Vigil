#!/usr/bin/env python3
"""Regression checks for staged EU AI Act semantic re-extractions."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGES = [
    ROOT / "external_requirements" / "reextractions" / "EU-AI-ACT-2026-07-27-article-4a.json",
    ROOT / "external_requirements" / "reextractions" / "EU-AI-ACT-2026-07-27-articles-10-13.json",
]


def rid(source_id: str, version: str, clause: str, identity: str) -> str:
    seed = "|".join((source_id, version, clause.strip(), identity.strip()))
    return "EXTREQ-" + hashlib.sha256(seed.encode("utf-8")).hexdigest()[:16].upper()


def main() -> None:
    docs = [json.loads(path.read_text(encoding="utf-8")) for path in PACKAGES]
    records = []
    retired = []
    for doc in docs:
        assert doc["status"] == "migration-candidate"
        source = doc["source"]
        for record in doc["requirements"]:
            assert record["requirement_id"] == rid(
                source["vigil_source_id"], source["source_version"],
                record["clause_or_control"], record["identity_key"]
            )
            assert record["semantic_atomicity"] in {"atomic", "source-defined-compound"}
            if record["semantic_atomicity"] == "source-defined-compound":
                assert record.get("constituent_propositions")
        records.extend(doc["requirements"])
        retired.extend(doc["retired_requirements"])

    assert {x["requirement_id"] for x in retired} == {
        "EXTREQ-F30E6B9A906370B9",
        "EXTREQ-09AD2F5442A55B55",
        "EXTREQ-126CB22D1FF08066",
    }
    assert len(records) == 41
    ids = [r["requirement_id"] for r in records]
    assert len(ids) == len(set(ids))
    assert any(r["clause_or_control"] == "Article 4a(1)(f)" for r in records)
    assert any(r["clause_or_control"] == "Article 4a(2)(a)" for r in records)
    assert any(r["clause_or_control"] == "Article 10(2)(f)" for r in records)
    assert any(r["clause_or_control"] == "Article 10(2)(g)" for r in records)
    assert any(r["clause_or_control"] == "Article 13(3)(b)(ii)" for r in records)
    assert any(r["clause_or_control"] == "Article 13(3)(f)" for r in records)
    print("EU AI Act staged re-extraction valid: 3 coarse records -> 41 deterministic candidates")


if __name__ == "__main__":
    main()
