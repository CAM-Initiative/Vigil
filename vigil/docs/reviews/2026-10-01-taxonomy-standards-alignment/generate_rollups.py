#!/usr/bin/env python3
"""Generate dated review projections from explicit decisions, never infer semantic edges."""
import json,hashlib
from pathlib import Path
from collections import Counter
AUDIT=Path(__file__).resolve().parent
ROOT=AUDIT.parents[3]
V=ROOT/'vigil'
DATE='2026-10-02'
PROVENANCE={'content_origin':'ai-authored','generation_mode':'semi-autonomous','human_role':'contract-approver','human_authorship':False,'human_review_status':'not-reviewed','human_verification_status':'not-verified'}
def read(p):return json.loads(p.read_text())
def write(p,d):p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
def digest(d):return hashlib.sha256(json.dumps(d,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
def edgeid(cid,rid):return 'FCEXTREL-'+hashlib.sha256((cid+'|'+rid).encode()).hexdigest()[:16].upper()
family_docs={p:read(p) for p in (V/'taxonomy/families').glob('*.json')}
classes={c['class_id']:c for d in family_docs.values() for c in d['classes'] if c.get('status')!='retired'}
requirements={r['requirement_id']:r for p in (V/'external_governance/requirements/requirements').glob('*/*.json') for r in read(p)}
sources=read(V/'external_governance/sources/source-registry.json')['entries']
scopes={(s['external_source_id'],s['source_version']):s for s in read(V/'external_governance/requirements/source-scope.json')['entries']}
decisions={};relationships=[]
for p in sorted(AUDIT.glob('*.json')):
 d=read(p)
 if p.stem!=d.get('source_id') or not d.get('status'):continue
 for e in d['entries']:
  rid=e['requirement_id'];assert rid in requirements and rid not in decisions,rid
  assert e['requirement_sha256']==digest(requirements[rid]),rid
  e=dict(e,review_artifact=str(p.relative_to(ROOT)));decisions[rid]=e
  for z in e['relationships']:
   assert e['review_status']=='reviewed' and z['review_status']=='supported'
   c=classes[z['class_id']];q=requirements[rid]
   assert z['invariant']==c['invariant'] and z['fc_property']==c['definition']
   for k in ['external_proposition','supported_component','scope_correspondence','normative_difference','strength_reason','limitation']:assert z[k],(rid,k)
   relationships.append(dict(z,relationship_id=edgeid(c['class_id'],rid),requirement_id=rid,external_source_id=q['external_source_id'],vigil_source_id=q['vigil_source_id'],source_version=q['source_version'],clause_or_control=q['clause_or_control'],source_locator=q['authoritative_locator'],jurisdiction=q['jurisdiction'],source_class=q['source_class'],class_semantic_sha256=digest({k:c[k] for k in ['definition','invariant','exclusions','success_condition','success_recognition','failure_condition','failure_recognition']}),requirement_sha256=digest(q),review_artifact=e['review_artifact'],authorship_provenance=PROVENANCE))
relationships.sort(key=lambda z:(z['class_id'],z['requirement_id']))
assert len({r['relationship_id'] for r in relationships})==len(relationships)
permission={'IEEE-7003','IEEE-7009','IEEE-7014','IEEE-7014.1'}
def pending_reason(q):
 s=q['external_source_id']
 if s in permission:return 'permission-pending','Separate written IEEE AI-use consent is not evidenced; relationship admission held. Existing extraction provenance is retained.'
 if s=='IMDA-AGENTIC-AI-MGF':return 'source-access-pending','Current official landing-page access does not expose the substantive framework body; represented source fidelity cannot be freshly established.'
 if s=='EU-AI-ACT-2024-1689':return 'source-fidelity-pending','Outside the recorded 102 reextracted Article 4a/9–15 successors; consolidated-version source fidelity and atomicity remain unresolved.'
 return 'source-fidelity-pending','No sufficient represented-proposition review is recorded in this dated audit.'
pending=[]
for rid,q in sorted(requirements.items()):
 if rid not in decisions:
  status,why=pending_reason(q);pending.append({'requirement_id':rid,'external_source_id':q['external_source_id'],'source_version':q['source_version'],'requirement_sha256':digest(q),'review_status':'unresolved','disposition':status,'rationale':why,'relationships':[]})
 elif decisions[rid]['review_status']!='reviewed':pending.append(dict(decisions[rid],external_source_id=q['external_source_id'],source_version=q['source_version']))
write(AUDIT/'pending-requirements.json',{'reviewed_on':DATE,'status':'excluded-from-active-registry','authorship_provenance':PROVENANCE,'entries':pending})
by_pair={(r['class_id'],r['requirement_id']):r for r in relationships}
# Preserve first-pass reference snapshots across reruns after canonical annotation repair.
refs_path=AUDIT/'historical-reference-dispositions.json'
if refs_path.exists():original_refs=read(refs_path)['entries']
else:original_refs=[{'class_id':cid,'reference_index':i,'reference_sha256':digest(x),'original_reference':x} for cid,c in sorted(classes.items()) for i,x in enumerate(c.get('external_references',[]))]
no_map_reasons={('VIGIL-FC-000040','EXTREQ-D999E91F3E053E85'):'Design revision on changed priorities does not require operative control restrictions to preserve meaning/force across execution handoffs.',('VIGIL-FC-000041','EXTREQ-DEA2B22466A64818'):'Human interruption to a safe state supports control activation/effectiveness, not traversal of required routes or alternate-route equivalence.'}
refs=[]
for x in original_refs:
 c=classes[x['class_id']];ref=x['original_reference'];rid=ref.get('requirement_id');resolution='explicit-canonical-id'
 if not rid and ref['title'].startswith('Regulation (EU) 2024/1689') and 'Article 5(1)(a)' in ref['title']:rid='EXTREQ-9A63E34FA83EAFA2';resolution='exact-article-title'
 e=decisions.get(rid);r=by_pair.get((c['class_id'],rid));matches=[]
 if r:
  status='reviewed';disp='retain-'+r['strength'];why=r['supported_component']+' '+r['limitation'];matches=[r['relationship_id']]
 elif e and e['review_status']=='reviewed':
  status='reviewed';disp='no-mapping-remove-from-active-relationship';why=no_map_reasons.get((c['class_id'],rid),'The reviewed atomic proposition does not materially support this class invariant. '+e['rationale'])
 elif rid:
  assert rid in requirements;status='unresolved';disp='pending-source-relationship-review';q=requirements[rid];why=pending_reason(q)[1] if not e else e['rationale']
 else:
  # Whole-document references resolve only through already reviewed atomic edges.
  source=None
  if ref['title']=='Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations':source='NIST-AI-100-2'
  if ref['title'].startswith('Reducing Risks Posed by Synthetic Content'):source='NIST-AI-100-4'
  rr=[r for r in relationships if r['class_id']==c['class_id'] and r['external_source_id']==source] if source else []
  if rr:
   status='reviewed';disp='derived-contextual-document-rollup';why='This document reference is supported only through the listed reviewed contextual atomic relationships; the document itself is not an atomic mapping.';matches=[r['relationship_id'] for r in rr if r['strength']=='contextual']
  else:
   status='unresolved';disp='pending-canonical-decomposition-and-source-verification';why='The historical citation has no resolved, source-assured canonical EXTREQ for this class in the current corpus. Its annotation is review material; exact proposition and primary-source verification remain pending. No requirement or strength is inferred from its title or old note.';resolution='no-canonical-endpoint'
 refs.append(dict(x,resolved_requirement_id=rid,endpoint_resolution=resolution,review_status=status,disposition=disp,rationale=why,reviewed_relationship_ids=matches,reviewed_on=DATE,provenance_disposition='Original reference and annotation preserved in this audit; active relationship authority resides in the reviewed registry.'))
write(refs_path,{'reviewed_on':DATE,'authorship_provenance':PROVENANCE,'status':'all-existing-references-explicitly-dispositioned-with-unresolved-substantive-review-separated','entries':refs})
write(V/'external_governance/requirements/taxonomy-relationships.json',{'schema_version':'1.0','reviewed_on':DATE,'status':'reviewed-available-corpus-with-explicit-pending-sources','relationships':relationships,'authorship_provenance':PROVENANCE,'policy':'Only source-assured, substantively reviewed atomic FC/EXTREQ relationships are active. Contextual edges are interpretation references and excluded from compliance candidate derivation. Pending requirements and historical references are recorded separately. Registry admission does not decide occurrence applicability or finding.','review_artifact':'vigil/docs/reviews/2026-10-01-taxonomy-standards-alignment/README.md'})
# Public-compatible evidence_note vocabulary carries dispositions; no new schema fields.
for p,d in family_docs.items():
 for c in d['classes']:
  if c.get('status')=='retired':continue
  for x in (x for x in refs if x['class_id']==c['class_id']):
   ref=c['external_references'][x['reference_index']]
   assert ref['title']==x['original_reference']['title'] and ref['url']==x['original_reference']['url']
   if x['review_status']=='reviewed':note='Taxonomy/standards review '+DATE+': '+x['disposition']+'. '+x['rationale']
   else:note='Taxonomy/standards relationship pending ('+DATE+'). '+x['rationale']
   ref['evidence_note']=note+' Historical annotation is preserved in vigil/docs/reviews/2026-10-01-taxonomy-standards-alignment/historical-reference-dispositions.json.'
 write(p,d)
fc_rows=[]
for cid,c in sorted(classes.items()):
 rr=[r for r in relationships if r['class_id']==cid];support=[r for r in rr if r['strength'] in ['direct','strong-supporting']];xr=[x for x in refs if x['class_id']==cid]
 fc_rows.append({'class_id':cid,'name':c['name'],'family_id':c['family_id'],'definition':c['definition'],'invariant':c['invariant'],'success_condition':c['success_condition'],'success_recognition':c['success_recognition'],'failure_condition':c['failure_condition'],'failure_recognition':c['failure_recognition'],'exclusions':c['exclusions'],'review_status':'available-canonical-evidence-and-boundaries-reviewed','reviewed_on':DATE,'reviewed_relationships':[{k:r[k] for k in ['relationship_id','requirement_id','external_source_id','source_version','strength','supported_component','scope_correspondence','normative_difference','limitation','review_artifact']} for r in rr],'direct_requirement_ids':sorted({r['requirement_id'] for r in rr if r['strength']=='direct'}),'strong_constituent_requirement_ids':sorted({r['requirement_id'] for r in rr if r['strength']=='strong-supporting'}),'contextual_requirement_ids':sorted({r['requirement_id'] for r in rr if r['strength']=='contextual'}),'supporting_source_versions':sorted({r['external_source_id']+'@'+r['source_version'] for r in support}),'jurisdictions':sorted({r['jurisdiction'] for r in support}),'source_types':sorted({r['source_class'] for r in support}),'support_state':'reviewed-constituent-support' if support else ('context-only-no-reviewed-constituent-support' if rr else 'no-reviewed-external-support'),'support_limitation':'No reviewed requirement establishes the entire class invariant. Listed constituent relationships leave the explicitly recorded limitations; absence of support is bounded to available canonical evidence, not proof that no external source exists.','unresolved_historical_candidates':[{'reference_index':x['reference_index'],'title':x['original_reference']['title'],'requirement_id':x['resolved_requirement_id'],'reason':x['rationale']} for x in xr if x['review_status']=='unresolved'],'historical_reference_dispositions':[{'reference_index':x['reference_index'],'disposition':x['disposition']} for x in xr]})
write(AUDIT/'fidelity-class-rollup.json',{'reviewed_on':DATE,'authorship_provenance':PROVENANCE,'classes':fc_rows})
source_rows=[]
for s in sources:
 sid,ver=s['external_source_id'],s['source_version'];qq=[q for q in requirements.values() if (q['external_source_id'],q['source_version'])==(sid,ver)];rr=[r for r in relationships if (r['external_source_id'],r['source_version'])==(sid,ver)];reviewed=[decisions[q['requirement_id']] for q in qq if q['requirement_id'] in decisions and decisions[q['requirement_id']]['review_status']=='reviewed'];pp=[p['requirement_id'] for p in pending if (p['external_source_id'],p['source_version'])==(sid,ver)];sc=scopes.get((sid,ver),{})
 if sid in permission:state='permission-pending';lim='Written AI-use permission not evidenced; no relationship admitted.'
 elif sid=='IMDA-AGENTIC-AI-MGF':state='source-access-pending';lim='Official landing page did not provide substantive source body for current verification.'
 elif pp:state='partially-reviewed';lim='Only listed source-assured propositions reviewed; remaining represented requirements are pending.'
 elif reviewed:state='represented-requirements-reviewed';lim='Scope is the represented canonical requirements, not every provision or annex in the whole source.'
 else:state='no-reviewed-canonical-requirements';lim='Source catalogue review is distinct from substantive atomic requirement review; no source-to-class mapping admitted.'
 support=[r for r in rr if r['strength'] in ['direct','strong-supporting']]
 source_rows.append({'external_source_id':sid,'vigil_source_id':s['vigil_source_id'],'source_version':ver,'title':s['title'],'jurisdiction':s['jurisdiction'],'source_class':s['source_class'],'source_locator':s['official_locator'],'registry_catalogue_review_state':s['review_state'],'relationship_review_state':state,'registered_extraction_state':sc.get('extraction_status'),'registered_access_state':sc.get('source_access_status'),'source_fidelity_limitation':lim,'source_scope_next_action':sc.get('next_action'),'canonical_requirement_count':len(qq),'reviewed_requirement_count':len(reviewed),'direct_relationship_count':sum(r['strength']=='direct' for r in rr),'strong_constituent_relationship_count':sum(r['strength']=='strong-supporting' for r in rr),'contextual_relationship_count':sum(r['strength']=='contextual' for r in rr),'classes_materially_supported':sorted({r['class_id'] for r in support}),'families_materially_supported':sorted({classes[r['class_id']]['family_id'] for r in support}),'contextual_classes':sorted({r['class_id'] for r in rr if r['strength']=='contextual'}),'outside_scope_requirement_ids':[e['requirement_id'] for e in reviewed if e['disposition']=='outside-taxonomy-scope'],'pending_requirement_ids':pp,'reviewed_relationship_ids':[r['relationship_id'] for r in rr]})
write(AUDIT/'source-rollup.json',{'reviewed_on':DATE,'authorship_provenance':PROVENANCE,'sources':source_rows})
write(AUDIT/'reverse-dispositions.json',{'reviewed_on':DATE,'authorship_provenance':PROVENANCE,'entries':[{'requirement_id':rid,'external_source_id':requirements[rid]['external_source_id'],'source_version':requirements[rid]['source_version'],'review_status':e['review_status'],'disposition':e['disposition'],'rationale':e['rationale'],'review_artifact':e['review_artifact'],'relationship_ids':[edgeid(z['class_id'],rid) for z in e['relationships']]} for rid,e in sorted(decisions.items()) if e['review_status']=='reviewed']+pending})
counts={'fidelity_families':len({c['family_id'] for c in classes.values()}),'fidelity_classes_reviewed':len(classes),'registered_source_versions':len(sources),'canonical_requirements':len(requirements),'requirements_substantively_reviewed':sum(e['review_status']=='reviewed' for e in decisions.values()),'requirements_unresolved':len(pending),'relationship_registry_count':len(relationships),'relationship_strength_counts':dict(Counter(r['strength'] for r in relationships)),'reverse_disposition_counts':dict(Counter(e['disposition'] for e in decisions.values() if e['review_status']=='reviewed')),'historical_references_dispositioned':len(refs),'historical_references_substantively_reviewed':sum(x['review_status']=='reviewed' for x in refs),'historical_references_unresolved':sum(x['review_status']=='unresolved' for x in refs),'classes_without_reviewed_constituent_support':[c['class_id'] for c in fc_rows if c['support_state']!='reviewed-constituent-support'],'classes_without_any_reviewed_relationship':[c['class_id'] for c in fc_rows if not c['reviewed_relationships']],'new_class_proposals':0,'class_boundary_changes':0,'incident_compliance_edits':0}
write(AUDIT/'summary.json',{'reviewed_on':DATE,'authorship_provenance':PROVENANCE,'status':'available-canonical-relationship-pass-complete-with-explicit-source-and-reference-holds','counts':counts,'completion_limits':['All current class semantics and available canonical requirement propositions have been reviewed. Pending sources/requirements remain outside the active registry.','Every historical reference has an explicit disposition, but unresolved citations are not falsely counted as substantive primary-source review.','No new Fidelity Class or ontology repair is proposed. Broad institutional/policy duties and fair allocation outcomes remain outside the present taxonomy; unmapped operational privacy/minimization duties do not automatically warrant ontology expansion.','Primary source conflicts and new IEEE permission holds remain recorded. Final source closure and unresolved-reference review are not complete.'],'blocked_sources':[{'external_source_id':s['external_source_id'],'source_version':s['source_version'],'relationship_review_state':s['relationship_review_state'],'access_state':s['registered_access_state'],'reason':s['source_fidelity_limitation']} for s in source_rows if s['relationship_review_state'] in ['permission-pending','source-access-pending'] or s['registered_extraction_state']=='blocked-access']})
# Human-readable summaries link atomic decision files rather than asserting whole-document equivalence.
md=['# Taxonomy / external governance alignment audit — 1–2 October 2026','',f"Reviewed {counts['fidelity_classes_reviewed']} current classes and {counts['requirements_substantively_reviewed']} canonical requirements. {counts['requirements_unresolved']} requirements remain explicitly unresolved. The active registry contains {counts['relationship_registry_count']} reviewed atomic relationships.",'','This is the available canonical relationship pass. It does not close pending source fidelity, source permissions or unresolved historical citations. No Incident applicability or finding was adjudicated.','', 'Authorship: AI-authored analytical review; not human reviewed or verified.','', '## Counts','', '| Measure | Count |','|---|---:|']
for k in ['registered_source_versions','canonical_requirements','requirements_substantively_reviewed','requirements_unresolved','historical_references_dispositioned','historical_references_substantively_reviewed','historical_references_unresolved','relationship_registry_count']:md.append(f'| {k.replace("_"," ")} | {counts[k]} |')
for k in ['direct','strong-supporting','contextual']:md.append(f'| {k} relationships | {counts["relationship_strength_counts"].get(k,0)} |')
md+=['','## Review artefacts','', '- [Class definitions, invariants, boundaries and component-level relationships](fidelity-class-rollup.json)','- [Every represented requirement: reviewed reverse disposition or explicit hold](reverse-dispositions.json)','- [All original historical references and their dispositions](historical-reference-dispositions.json)','- [Source/version roll-ups](source-rollup.json)','- [Pending requirements](pending-requirements.json)','- [Source-copy access and permission review](primary-access-review.json)','', 'Per-source decision files contain proposition, supported component, scope, force, strength reason, limitations and primary-review basis. The registry is `vigil/external_governance/requirements/taxonomy-relationships.json`. Roll-ups can be regenerated with `python vigil/docs/reviews/2026-10-01-taxonomy-standards-alignment/generate_rollups.py`. That script assembles explicit decisions; it performs no semantic inference.','', '## Fidelity Class support','', '| Class | Name | Direct | Constituent | Contextual | Pending historical citations |','|---|---|---:|---:|---:|---:|']
for c in fc_rows:md.append(f"| {c['class_id']} | {c['name']} | {len(c['direct_requirement_ids'])} | {len(c['strong_constituent_requirement_ids'])} | {len(c['contextual_requirement_ids'])} | {len(c['unresolved_historical_candidates'])} |")
md+=['','Classes without constituent support are not ranked as deficient. They may rely on VIGIL normative reasoning, contextual evidence, or pending sources. Counts alone cannot distinguish those explanations. No reviewed source expresses an entire class invariant here; strength was not increased to satisfy a coverage target.','', '## Source/version support','', '| Source | Version | Reviewed requirements | Direct | Constituent | Contextual | Pending requirements | Review state |','|---|---|---:|---:|---:|---:|---:|---|']
for s in source_rows:md.append(f"| {s['external_source_id']} | {s['source_version']} | {s['reviewed_requirement_count']} | {s['direct_relationship_count']} | {s['strong_constituent_relationship_count']} | {s['contextual_relationship_count']} | {len(s['pending_requirement_ids'])} | {s['relationship_review_state']} |")
md+=['','Contextual counts are excluded from material support and resolver candidate derivation. A catalogue entry marked reviewed is not evidence that its normative requirements have been extracted/reviewed.','', '## Outstanding work','', '- IEEE 7003, 7009, 7014 and 7014.1 require evidence of separate written AI-use permission before substantive relationship admission. Other metadata-only/licensed editions retain their registered access limits.', '- IMDA framework-body access remains unresolved; Canada Directive access remains blocked, with no represented canonical requirements.', '- EU review is bounded to the 102 source-assured successors from Articles 4a and 9–15. The other 73 requirements remain pending consolidated-source fidelity/atomicity.', '- Three C2PA AI-disclosure requirements remain unresolved because normative prose, CDDL and examples conflict.', '- Historical citations without a verified atomic canonical endpoint remain pending decomposition/source verification. Their original annotations are preserved; current annotations explicitly state the hold.', '- No genuinely new class or material boundary change is proposed. No-mapping institutional, policy, social-outcome and operational provisions are recorded without forcing them into a class.','', 'New relationships should trigger only the dependent occurrence external-requirement backfill. Existing clause/taxonomy adjudication should be reopened only for a substantive contradiction.','']
(AUDIT/'README.md').write_text('\n'.join(md))
print(json.dumps(counts,indent=2))
