#!/usr/bin/env python3
"""Regression checks for the staged EU AI Act semantic re-extraction."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "external_requirements" / "reextractions" / "EU-AI-ACT-2026-07-27-articles-10-13.json"


def rid(source_id: str, version: str, clause: str, identity: str) -> str:
    seed = "|".join((source_id, version, clause.strip(), identity.strip()))
    return "EXTREQ-" + hashlib.sha256(seed.encode("utf-8")).hexdigest()[:16].upper()


def main() -> None:
    doc = json.loads(PACKAGE.read_text(encoding="utf-8"))
    source = doc["source"]
    records = doc["requirements"]
    assert doc["status"] == "migration-candidate"
    assert len(doc["retired_requirements"]) == 2
    assert {x["requirement_id"] for x in doc["retired_requirements"]} == {
        "EXTREQ-09AD2F5442A55B55", "EXTREQ-126CB22D1FF08066"
    }
    assert len(records) == 32
    ids = [r["requirement_id"] for r in records]
    assert len(ids) == len(set(ids))
    for record in records:
        assert record["requirement_id"] == rid(
            source["vigil_source_id"], source["source_version"],
            record["clause_or_control"], record["identity_key"]
        )
        assert record["semantic_atomicity"] in {"atomic", "source-defined-compound"}
        if record["semantic_atomicity"] == "source-defined-compound":
            assert record.get("constituent_propositions")
    assert any(r["clause_or_control"] == "Article 10(2)(f)" for r in records)
    assert any(r["clause_or_control"] == "Article 10(2)(g)" for r in records)
    assert any(r["clause_or_control"] == "Article 13(3)(b)(ii)" for r in records)
    assert any(r["clause_or_control"] == "Article 13(3)(f)" for r in records)
    print("EU AI Act staged re-extraction valid: 2 coarse records -> 32 deterministic candidates")


if __name__ == "__main__":
    main()
