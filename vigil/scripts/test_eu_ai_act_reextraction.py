#!/usr/bin/env python3
"""Regression checks for staged EU AI Act semantic re-extractions."""
from __future__ import annotations
import hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DIR=ROOT/"external_requirements"/"reextractions"
NORMALIZATION=DIR/"EU-AI-ACT-2026-07-27-metadata-normalization.json"
def rid(s,v,c,i): return "EXTREQ-"+hashlib.sha256("|".join((s,v,c.strip(),i.strip())).encode()).hexdigest()[:16].upper()
def main():
    paths=[p for p in sorted(DIR.glob("EU-AI-ACT-2026-07-27-*.json")) if p.name!=NORMALIZATION.name]
    docs=[json.loads(p.read_text(encoding="utf-8")) for p in paths]
    normalization=json.loads(NORMALIZATION.read_text(encoding="utf-8"))
    assert len(docs)>=5
    assert normalization["policy"]["mode"]=="source-explicit-overlay"
    records=[]; retired=[]
    for doc in docs:
        assert doc["status"]=="migration-candidate"; source=doc["source"]
        for record in doc["requirements"]:
            assert record["requirement_id"]==rid(source["vigil_source_id"],source["source_version"],record["clause_or_control"],record["identity_key"])
            assert record["semantic_atomicity"] in {"atomic","source-defined-compound"}
            if record["semantic_atomicity"]=="source-defined-compound": assert record.get("constituent_propositions")
        records.extend(doc["requirements"]); retired.extend(doc["retired_requirements"])
    assert {x["requirement_id"] for x in retired}=={
        "EXTREQ-F30E6B9A906370B9","EXTREQ-44B7BB17CB030468","EXTREQ-09AD2F5442A55B55","EXTREQ-901AD2C0A909E790",
        "EXTREQ-33898CCD26FBF5D5","EXTREQ-126CB22D1FF08066","EXTREQ-1B4CA7A04D63F038","EXTREQ-E640D3CE18685E25"}
    assert len(records)==102
    ids=[r["requirement_id"] for r in records]; assert len(ids)==len(set(ids))
    staged=set(ids); overrides=normalization["overrides"]
    assert set(overrides)<=staged
    assert len(overrides)>=18
    assert overrides["EXTREQ-B9775B02872296D0"]["timing_or_frequency"]
    assert overrides["EXTREQ-E7072B9D822AE4CC"]["timing_or_frequency"]
    assert overrides["EXTREQ-8406A6A9A7ECFCB6"]["required_artefacts"]
    assert overrides["EXTREQ-BAA343B6CDB1862E"]["verification_method"]
    assert overrides["EXTREQ-20379EF0C7E97FDF"]["evidence_expectation"]
    assert any(r["requirement_id"]=="EXTREQ-7D000D6868EDE244" and r["clause_or_control"]=="Article 11(1)" for r in records)
    for clause in ("Article 4a(1)(f)","Article 9(5)(a)","Article 10(2)(f)","Article 11(3)","Article 12(3)(d)","Article 13(3)(f)","Article 14(5)","Article 15(5)"):
        assert any(r["clause_or_control"]==clause for r in records)
    print(f"EU AI Act staged re-extraction valid: 8 coarse records -> 102 deterministic candidates; {len(overrides)} source-explicit metadata normalizations")
if __name__=="__main__": main()
