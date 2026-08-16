#!/usr/bin/env python3
"""Build VIGIL's effective external-requirements corpus from frozen baseline + reviewed extension packs."""
from __future__ import annotations
import argparse, importlib.util, json
from pathlib import Path
from typing import Any

ROOT=Path(__file__).resolve().parents[1]; SOURCES=ROOT/'external_sources'; REQ=ROOT/'external_requirements'; EXT=REQ/'extensions'

def imod(path,name):
    s=importlib.util.spec_from_file_location(name,path); m=importlib.util.module_from_spec(s); assert s.loader; s.loader.exec_module(m); return m
base=imod(ROOT/'scripts/manage-external-requirements.py','base_req')
led=imod(ROOT/'scripts/manage-external-governance-ledger.py','base_ledger')
ELED=SOURCES/'effective-ledger.json'; EVIEW=SOURCES/'EFFECTIVE-GOVERNANCE-SOURCES.md'; EREQ=REQ/'effective-requirements.json'
XDATA=REQ/'derivative-crosswalks.json'; XIDX=REQ/'derivative-crosswalk-index.json'; XVIEW=REQ/'DERIVATIVE-CROSSWALKS.md'

def load(p): return json.loads(p.read_text(encoding='utf-8'))
def jtxt(v): return json.dumps(v,indent=2,ensure_ascii=False)+'\n'
def sk(v): return str(v.get('vigil_source_id','')),str(v.get('source_version',''))
def packs(): return [load(p) for p in sorted(EXT.glob('*.json'))]

def new_source(seed,date):
    x=dict(seed); x.update(vigil_source_id=led.stable_id(str(x['external_source_id'])),fingerprint='',change_state='new',alignment_state='review-required',alignment_eligible=True,caelestis_assessed_commit=None,caelestis_crosswalk_refs=[],first_seen=f'{date}T00:00:00Z',last_seen=f'{date}T00:00:00Z'); x['fingerprint']=led.fingerprint(x); return x

def scope(u):
    sid=u['external_source_id']; status=u['extraction_status']
    if sid=='IEEE-2863': notes='Official IEEE metadata/abstract available; full primary text not reviewed.'; detail='Primary source remains access-blocked; no requirements inferred from metadata.'; un=['Normative/recommended-practice clauses beyond metadata']; nxt='Obtain lawful primary text before extraction.'
    elif sid=='IEEE-7003': notes='IEEE GET access is available; primary text was not supplied in this work package.'; detail='Primary text is accessible, but Layer 1 extraction has not started.'; un=['Full clause-level primary-text review']; nxt='Retrieve GET primary text and perform bounded analytical extraction.'
    elif sid=='AAM-SDOS-RUNTIME-GOVERNANCE': notes='Owner-authored public SDOS v1.10 control catalog directly reviewed.'; detail='All 24 public v1.10 controls represented as private-sector recommended practice; no standards authority is implied.'; un=[]; nxt='Monitor SDOS changelog for material changes.'
    elif status=='partial': notes='Licensed IEEE primary text directly reviewed; VIGIL stores abstractions, not standard text.'; detail='Annex A.3 baseline ASOI requirements atomised; remaining normative content not yet represented.'; un=['Normative content outside Annex A.3 baseline ASOI requirements']; nxt='Continue bounded clause-level extraction.'
    elif status=='in-progress': notes='Licensed IEEE primary text supplied for bounded analytical review; VIGIL stores abstractions, not standard text.'; detail='Primary text is available and review has begun; no completeness claim is made.'; un=['Full clause-level analytical extraction remains in progress']; nxt='Complete bounded clause-level analytical extraction.'
    else: notes='Licensed IEEE primary text available under supporting-source scope.'; detail='Primary text access recorded; comprehensive first-class decomposition is not planned under current scope.'; un=[]; nxt='Retain licensed-primary provenance under supporting-source scope.'
    pri=u['alignment_priority']; rationale={'critical-alignment-source':'Foundational AI governance/assurance source.','high-value-alignment-source':'Material governance source for ethical design, transparency, safety, human impacts, runtime governance or relational AI.','supporting-specialist-source':'Specialist semantic or implementation guidance.','low-immediate-priority':'Supporting authority rather than comprehensive first-class baseline.'}[pri]
    if sid=='IEEE-7009': rationale='Fail-safe authorization, inhibition and behavior-limit controls directly relevant to runtime safety and authority separation.'
    if sid=='AAM-SDOS-RUNTIME-GOVERNANCE': rationale='Private-sector runtime-governance control model for comparative assessment; no standards authority implied.'
    maint=status not in {'complete','supporting-only'}
    return {'vigil_source_id':u['vigil_source_id'],'external_source_id':sid,'source_version':u['source_version'],'canonical_source_identifier':{'scheme':'SDOS' if sid.startswith('AAM-SDOS') else 'IEEE','value':u['canonical_value']},'source_role':u['source_role'],'source_access_status':u['source_access_status'],'access_checked_at':'2026-08-16','access_locator':u['access_locator'],'source_access_notes':notes,'extraction_status':status,'extraction_scope_notes':detail,'inaccessible_sections':un if status=='blocked-access' else [],'known_unreviewed_sections':un,'next_action':nxt,'alignment_priority':pri,'alignment_priority_rationale':rationale,'maintainer_action_required':maint,'maintainer_action':nxt if maint else None}

def req_common(src,ver,clause,ikey,summary,posture,etype,actors,objects,stages,concepts,access,basis,method,limits):
    return {'requirement_id':base.requirement_id(src['vigil_source_id'],ver,clause,ikey),'identity_key':ikey,'vigil_source_id':src['vigil_source_id'],'external_source_id':src['external_source_id'],'source_version':ver,'canonical_source_identifier':src['canonical_identifier'],'issuer':src['issuer'],'jurisdiction':src['jurisdiction'],'source_class':src['source_class'],'source_lifecycle_state':src['source_lifecycle_state'],'source_role':'primary-ai-governance','authoritative_locator':src['official_locator'],'clause_or_control':clause,'parent_section_or_group':None,'source_access_status':access,'source_review_date':'2026-08-16','source_access_notes':'Direct primary-source analytical review; source text is not reproduced in VIGIL.','requirement_summary':summary,'requirement_posture':posture,'expectation_type':etype,'applicable_actor':actors,'governed_object':objects,'lifecycle_stage':stages,'governance_expectation':summary,'evidence_expectation':[],'timing_or_frequency':[],'required_artefacts':[],'verification_method':[],'applicability_conditions':[],'exceptions_or_qualifications':[],'governance_concepts':concepts,'source_defined_tags':[],'related_external_requirements':[],'interpretation_status':'reviewed-analytical-summary','interpretation_provenance':{'basis':basis,'reviewed_by':'OpenAI research agent under human governance direction','review_method':method,'source_locator':src['official_locator'],'source_fingerprint':src['fingerprint']},'review_limitations':limits}

def sdos_req(c,src):
    cid=c['control']; r=req_common(src,'1.10',cid,cid.lower(),c['summary'],'recommended-practice','guidance',['AI agent platform operator or implementer'],['agentic AI runtime governance system'],c['lifecycle_stage'],c['governance_concepts'],'direct-public-primary','direct-primary-text','Direct review of owner-authored SDOS v1.10 control catalog; each control paraphrased and evidence types preserved.',['SDOS is a private-sector framework; no statutory, ISO, IEEE or NIST authority is implied.','No Caelestis coverage or conformity is asserted.'])
    r['parent_section_or_group']=f"Control Catalog — {c['domain']}"; r['evidence_expectation']=[f'Demonstrate implementation/operation using SDOS-listed evidence type: {e}.' for e in c['evidence_types']]; r['required_artefacts']=c['evidence_types']; r['verification_method']=["Review listed evidence against the control's runtime-governance function."]; r['applicability_conditions']=['Agentic AI workflows in which agents invoke tools, make decisions, or produce outputs on behalf of an operator.']; r['exceptions_or_qualifications']=['SDOS states it is not designed for static LLM-chat interfaces without tool invocation or autonomous action.']; r['source_defined_tags']=[{'scheme':'SDOS-domain','values':[c['domain']]},{'scheme':'SDOS-control','values':[cid]}]; return r

def ieee_req(c,src):
    cid=c['control']; clause=f'Annex A.3 / {cid}'; r=req_common(src,'2024',clause,cid.lower(),c['summary'],'mandatory-normative','positive-duty',['ASOI developer or system integrator'],['autonomous or semi-autonomous system of interest (ASOI)'],['design','development','testing-evaluation','operation-use'],c['governance_concepts'],'direct-licensed-primary','licensed-primary-text','Direct review of IEEE Std 7009-2024 Annex A.3; mandatory statements and conditions paraphrased without reproducing licensed text.',['Only Annex A.3 baseline ASOI requirements are represented; other IEEE 7009 normative content is not yet atomised.','Licensed IEEE text is not stored in VIGIL.'])
    r['parent_section_or_group']='Annex A.3 — System Requirements'; r['evidence_expectation']=['Provide verifiable design/test evidence that the ASOI incorporates the stated capability under the source-defined conditions.']; r['timing_or_frequency']=c['timing_or_frequency']; r['applicability_conditions']=c['applicability_conditions']; r['source_defined_tags']=[{'scheme':'IEEE-7009-requirement-id','values':[cid]}]; return r

def effective():
    errors=[]; bled=load(base.LEDGER_PATH); sources={sk(x):x for x in bled['entries']}; byext={(x['external_source_id'],x['source_version']):x for x in sources.values()}; bs=load(base.SCOPE_PATH); scopes={sk(x):x for x in bs['entries']}; br=load(base.REQUIREMENTS_PATH); reqs=list(br['requirements']); date=bs['reviewed_at']; xwalk=[]
    for p in packs():
        date=max(date,p.get('reviewed_at',''))
        for seed in p.get('sources',[]):
            x=new_source(seed,p['reviewed_at']); k=sk(x)
            if k in sources: errors.append(f'duplicate extension source {k}')
            else: sources[k]=x; byext[(x['external_source_id'],x['source_version'])]=x
        for u in p.get('source_scope_updates',[]): scopes[(u['vigil_source_id'],u['source_version'])]=scope(u)
        s=byext.get(('AAM-SDOS-RUNTIME-GOVERNANCE','1.10')); i=byext.get(('IEEE-7009','2024'))
        if s: reqs += [sdos_req(c,s) for c in p.get('sdos_controls',[])]
        if i: reqs += [ieee_req(c,i) for c in p.get('ieee_7009_annex_a3',[])]
        xwalk += p.get('derivative_crosswalks',[])
    srcs=sorted(sources.values(),key=lambda x:(x['external_source_id'],x['source_version'])); sc=sorted(scopes.values(),key=lambda x:(x['external_source_id'],x['source_version'])); sm={sk(x):x for x in srcs}; scm=base.validate_scope(sm,sc,errors); base.validate_requirements(reqs,sm,scm,errors)
    seen=set()
    for x in xwalk:
        xid=x.get('crosswalk_id');
        if xid in seen: errors.append(f'duplicate crosswalk {xid}')
        seen.add(xid)
        if x.get('derivative_not_source_authority') is not True or x.get('may_assert_target_requirement_text_from_crosswalk') is not False or x.get('may_assert_conformance') is not False: errors.append(f'{xid}: invalid derivative boundary')
        if x.get('completeness',{}).get('ingested_row_count') != len(x.get('mappings',[])): errors.append(f'{xid}: row count mismatch')
    out=base.build_outputs(sm,sc,reqs,date); idx=json.loads(out[base.INDEX_PATH]); idx['generated_from']='requirements.json + external_requirements/extensions/*.json'; out[base.INDEX_PATH]=base.json_text(idx)
    out[ELED]=jtxt({'schema_version':'1.0','updated_at':date,'generated_from':['external_sources/ledger.json','external_requirements/extensions/*.json'],'entries':srcs}); out[EREQ]=jtxt({'schema_version':'1.1','updated_at':date,'generated_from':['external_requirements/requirements.json','external_requirements/extensions/*.json'],'requirement_count':len(reqs),'requirements':sorted(reqs,key=lambda x:x['requirement_id'])})
    sl=['# Effective External Governance Sources','','Frozen Layer 0 plus reviewed extension sources. Inventory only; no Caelestis conformity is asserted.','',f'- Effective source versions: {len(srcs)}',f'- Reviewed through: {date}','','| VIGIL Source | External Source | Version | Issuer | Lifecycle | Canonical identifier |','| --- | --- | --- | --- | --- | --- |']+[f"| `{x['vigil_source_id']}` | {x.get('title') or ''} | `{x['source_version']}` | {x['issuer']} | `{x['source_lifecycle_state']}` | `{x['canonical_identifier']['value']}` |" for x in srcs]+['','Private-sector frameworks retain their actual publisher authority; inclusion does not elevate them to standards or regulatory authority.','']; out[EVIEW]='\n'.join(sl)
    xwalk=sorted(xwalk,key=lambda x:x['crosswalk_id']); out[XDATA]=jtxt({'schema_version':'1.0','updated_at':date,'crosswalk_count':len(xwalk),'crosswalks':xwalk}); out[XIDX]=jtxt({'schema_version':'1.0','generated_at':date,'crosswalk_count':len(xwalk),'mapping_row_count':sum(len(x.get('mappings',[])) for x in xwalk),'crosswalks':[{'crosswalk_id':x['crosswalk_id'],'mapping_name':x['mapping_name'],'mapping_version':x['mapping_version'],'mapping_status':x['mapping_status'],'relationship_type':x['relationship_type'],'reference_document':x['reference_document'],'focal_document':x['focal_document'],'mapping_locator':x['mapping_locator'],'ingested_row_count':len(x.get('mappings',[])),'row_ingestion_status':x['completeness']['row_ingestion_status'],'may_assert_conformance':False} for x in xwalk]})
    xl=['# Derivative External-Governance Crosswalks','','Separate from Layer 1 direct-source requirements. Crosswalks record developer-asserted relationships; they do not supply target normative text or establish Caelestis conformity.','',f'- Crosswalk records: {len(xwalk)}',f"- Ingested mapping rows: {sum(len(x.get('mappings',[])) for x in xwalk)}",'']
    for x in xwalk: xl += [f"## {x['mapping_name']}",'',f"- ID: `{x['crosswalk_id']}`",f"- Version/status: `{x['mapping_version']}` / `{x['mapping_status']}`",f"- Relationship: `{x['relationship_type']}`",f"- Developer / host: {x['mapping_developer']} / {x['mapping_host']}",f"- Rows represented: {len(x.get('mappings',[]))} (`{x['completeness']['row_ingestion_status']}`)",'- Conformance assertion permitted: `false`','']+[f'- Provenance: {n}' for n in x.get('provenance_notes',[])]+['']
    out[XVIEW]='\n'.join(xl).rstrip()+'\n'; return out,errors

def run(build=False,check=False):
    out,err=effective()
    if build and not err:
        for p,c in out.items(): p.write_text(c,encoding='utf-8'); print('Wrote',p)
    if check:
        for p,c in out.items():
            if (p.read_text(encoding='utf-8') if p.exists() else '') != c: err.append(f'generated output is stale: {p}')
    if err: raise ValueError('\n'.join(err))
    l=json.loads(out[ELED]); r=json.loads(out[EREQ]); x=json.loads(out[XDATA]); print(f"Effective external requirements valid: {len(l['entries'])} source versions, {r['requirement_count']} requirements, {x['crosswalk_count']} derivative crosswalks")

def main():
    p=argparse.ArgumentParser(); s=p.add_subparsers(dest='cmd',required=True); s.add_parser('build'); v=s.add_parser('validate'); v.add_argument('--check-generated',action='store_true'); a=p.parse_args(); run(build=a.cmd=='build',check=getattr(a,'check_generated',False))
if __name__=='__main__': main()
