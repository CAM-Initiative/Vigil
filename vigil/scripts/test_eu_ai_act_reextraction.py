#!/usr/bin/env python3
"""Regression checks for staged EU AI Act semantic re-extractions."""
from __future__ import annotations
import hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DIR=ROOT/"external_requirements"/"reextractions"
def rid(s,v,c,i): return "EXTREQ-"+hashlib.sha256("|".join((s,v,c.strip(),i.strip())).encode()).hexdigest()[:16].upper()
def main():
    docs=[json.loads(p.read_text(encoding="utf-8")) for p in sorted(DIR.glob("EU-AI-ACT-2026-07-27-*.json"))]
    assert len(docs)>=3
    records=[]; retired=[]
    for doc in docs:
        assert doc["status"]=="migration-candidate"; source=doc["source"]
        for record in doc["requirements"]:
            assert record["requirement_id"]==rid(source["vigil_source_id"],source["source_version"],record["clause_or_control"],record["identity_key"])
            assert record["semantic_atomicity"] in {"atomic","source-defined-compound"}
            if record["semantic_atomicity"]=="source-defined-compound": assert record.get("constituent_propositions")
        records.extend(doc["requirements"]); retired.extend(doc["retired_requirements"])
    assert {x["requirement_id"] for x in retired}=={
        "EXTREQ-F30E6B9A906370B9","EXTREQ-44B7BB17CB030468","EXTREQ-09AD2F5442A55B55","EXTREQ-126CB22D1FF08066"}
    assert len(records)==63
    ids=[r["requirement_id"] for r in records]; assert len(ids)==len(set(ids))
    for clause in ("Article 4a(1)(f)","Article 9(5)(a)","Article 9(8)","Article 10(2)(f)","Article 13(3)(b)(ii)","Article 13(3)(f)"):
        assert any(r["clause_or_control"]==clause for r in records)
    print("EU AI Act staged re-extraction valid: 4 coarse records -> 63 deterministic candidates")
if __name__=="__main__": main()
