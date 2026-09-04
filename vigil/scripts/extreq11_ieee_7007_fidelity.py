#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
REQ=ROOT/"external_governance"/"requirements"
SHARD=REQ/"requirements"/"IEEE-7007"/"2021.json"
LEDGER=REQ/"metadata-review.json"
ASSURANCE=REQ/"source-review-assurance.json"
FIDELITY=REQ/"source-fidelity.json"
SCOPE=REQ/"source-scope.json"
DATE="2026-09-04"
SOURCE_ID="EXT-7E4B8ED73AA5"
EXTERNAL_ID="IEEE-7007"
VERSION="2021"
LOCATOR="https://standards.ieee.org/ieee/7007/7070/"
FINGERPRINT="2e3fc549fcfee0ac04575a50119a42a19ec7cd4d186dee14956066d3acb17d57"
DIGEST="8689b98d77141330e380394ce7eef5961c9539227340949357fc860c74e683d7"
FIELDS=("applicable_actor","governed_object","timing_or_frequency","required_artefacts","evidence_expectation","verification_method","applicability_conditions","exceptions_or_qualifications")

def dump(p,o): Path(p).write_text(json.dumps(o,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

META={
"7007-eras-top-level-concepts":(
 ["Applies when using the ERAS top-level concepts to complete formalization of the four ERAS subdomains."],
 ["The ERAS top-level formalizations are a minimal set for this standard and are not intended to function as a general-purpose top-level ontology in other contexts."]
),
"7007-norms-and-ethical-principles":(
 ["Applies when representing norms, ethical theories, principles, roles and norm modalities in the ERAS Norms and Ethical Principles subdomain."],
 ["This record is definitional ontology content rather than an independently imposed operational control."]
),
"7007-ethical-agent":(
 ["Applies when representing agents whose conduct is characterized using the ERAS Norms and Ethical Principles concepts and relationships."],
 ["This record preserves an ontology concept and its formal relationships; it does not independently prescribe a system-development process."]
),
"7007-data-protection-privacy-domain":(
 ["Applies when using the ERAS Data Privacy and Protection subdomain to represent data-protection/privacy rules and relationships relevant to ethical agents and autonomous systems."],
 ["Data-protection law evolves and varies by jurisdiction; users of the standard remain responsible for keeping apprised of applicable laws and regulations."]
),
"7007-data-subject-and-controller-relations":(
 ["Applies when representing persons/data subjects, data controllers, processing, access and protection relationships in the ERAS Data Privacy and Protection subdomain."],
 ["The ontology's privacy/data-protection relationships do not replace applicable legal definitions or jurisdiction-specific obligations."]
),
"7007-transparency-accountability-domain":(
 ["Applies when using the ERAS Transparency and Accountability subdomain to represent explanations, transparency, accountability, responsibility and answerability relationships."],
 ["This record is a semantic/ontological representation, not a standalone transparency procedure."]
),
"7007-transparency-accountability-distinction":(
 ["Applies when modelling transparency-related explanation capabilities and accountability for explanations within the ERAS Transparency and Accountability subdomain."],
 ["Transparency and accountability are related through the ontology but remain distinct concepts and relationships."]
),
"7007-ethical-violation-management-domain":(
 ["Applies when using the ERAS Ethical Violation Management subdomain to represent norm violations, detection, incident information, responsibility and governance relationships."],
 ["This record captures ontology semantics for violation management rather than prescribing a separate incident-management process."]
),
"7007-government-no-capacity-pattern":(
 ["Applies to the ERAS Ethical Violation Management axiom pattern for a government whose socio-technology governance maturity is represented as no-capacity."],
 ["The axiom pattern is an ontological/legal-world-view formalization within the standard and should not be treated as a statement of universally applicable law."]
),
"7007-government-evolving-capacity-pattern":(
 ["Applies to the ERAS Ethical Violation Management axiom pattern for a government whose socio-technology governance maturity is represented as evolving-capacity."],
 ["The distributed-responsibility pattern is an ontological formalization conditioned on the source-defined government maturity and multi-agent-team relationships, not a universal legal rule."]
),
}

records=json.loads(SHARD.read_text(encoding="utf-8"))
assert len(records)==10 and {r["identity_key"] for r in records}==set(META)
ids={r["requirement_id"] for r in records}
assert len(ids)==10

for r in records:
    cond,qual=META[r["identity_key"]]
    r["source_review_date"]=DATE
    r["timing_or_frequency"]=[]
    r["required_artefacts"]=[]
    r["evidence_expectation"]=[]
    r["verification_method"]=[]
    r["applicability_conditions"]=cond
    r["exceptions_or_qualifications"]=qual
    p=r["interpretation_provenance"]
    p["basis"]="licensed-primary-text"
    p["source_analysis_method"]="Direct clause-level fidelity review of IEEE Std 7007-2021 licensed primary text, focused on the ERAS top-level concepts and four governance-relevant ontology subdomains; analytical paraphrase only."
    p["source_locator"]=LOCATOR
    p["source_metadata_fingerprint"]=FINGERPRINT
    p["reviewed_source_digest"]=DIGEST
    p["reviewed_source_digest_algorithm"]="sha256"
    p["reviewed_source_digest_status"]="recorded"
    r["review_limitations"]=[
      "IEEE 7007-2021 is primarily an ontological standard. VIGIL preserves governance-relevant source-defined concepts and relationships as definitional records without converting them into unsupported operational duties.",
      "Licensed IEEE text is not stored in VIGIL."
    ]
    r["assurance_provenance"]=[]
dump(SHARD,records)

ledger=json.loads(LEDGER.read_text(encoding="utf-8"))
ledger["updated_at"]=DATE
by={e["requirement_id"]:e for e in ledger["entries"]}
for r in records:
    by[r["requirement_id"]]={
      "requirement_id":r["requirement_id"],"reviewed_at":DATE,"review_basis":"licensed-primary-text",
      "review_notes":["Direct review of IEEE 7007-2021 confirmed definitional ontology scope; source-silent operational metadata fields are explicitly not inferred."],
      "field_status":{f:("populated-reviewed" if r[f] else "not-specified-by-source") for f in FIELDS}
    }
ledger["entries"]=sorted(by.values(),key=lambda e:e["requirement_id"])
dump(LEDGER,ledger)

ass=json.loads(ASSURANCE.read_text(encoding="utf-8")); ass["updated_at"]=DATE
ae={"vigil_source_id":SOURCE_ID,"external_source_id":EXTERNAL_ID,"source_version":VERSION,"source_metadata_fingerprint":FINGERPRINT,
"reviewed_source_digest":{"algorithm":"sha256","digest":DIGEST,"recorded_at":DATE,"artefact_role":"reviewed-primary-source","access_basis":"licensed-primary","evidence_ref":LOCATOR},"assurance_provenance":[]}
for i,e in enumerate(ass["source_reviews"]):
    if e["external_source_id"]==EXTERNAL_ID and e["source_version"]==VERSION: ass["source_reviews"][i]=ae; break
else: ass["source_reviews"].append(ae)
dump(ASSURANCE,ass)

fid=json.loads(FIDELITY.read_text(encoding="utf-8")); fid["reviewed_at"]=DATE
fe={"vigil_source_id":SOURCE_ID,"external_source_id":EXTERNAL_ID,"source_version":VERSION,"fidelity_status":"assured","effective_extraction_status":"complete",
"assessment_basis":"Direct review against the complete lawfully accessed IEEE 7007-2021 licensed primary PDF confirmed that the 10 established definitional records provide bounded governance-relevant coverage of the ERAS top-level concepts and the Norms and Ethical Principles, Data Privacy and Protection, Transparency and Accountability, and Ethical Violation Management subdomains, including the two government-capacity axiom patterns. All established identities and definitional postures are preserved. Operational metadata not specified by this ontological source is explicitly recorded as source-silent rather than inferred.",
"known_fidelity_gaps":[],"audited_requirement_ids":sorted(ids),"next_action":"Retain the 10 reviewed identities and repeat fidelity review on material revision of IEEE 7007."}
for i,e in enumerate(fid["entries"]):
    if e["external_source_id"]==EXTERNAL_ID and e["source_version"]==VERSION: fid["entries"][i]=fe; break
else: fid["entries"].append(fe)
dump(FIDELITY,fid)

scope=json.loads(SCOPE.read_text(encoding="utf-8"))
for e in scope["entries"]:
    if e["external_source_id"]==EXTERNAL_ID and e["source_version"]==VERSION:
        e["extraction_status"]="complete"
        e["extraction_scope_notes"]="Direct licensed-primary fidelity review confirmed bounded governance-relevant definitional coverage in 10 stable records. Operational duties are not inferred from ontology concepts."
        e["known_unreviewed_sections"]=[]
        e["next_action"]="Monitor for material source revision."
        e["maintainer_action_required"]=False;e["maintainer_action"]=None
        break
else: raise AssertionError("IEEE-7007 source-scope entry missing")
dump(SCOPE,scope)
print("IEEE 7007 fidelity enrichment valid: 10 established IDs preserved; no operational duties invented.")
print("Digest",DIGEST)
