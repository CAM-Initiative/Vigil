"""Read-only census of admitted relationships. No semantic conclusions inferred."""
import collections, hashlib, json, pathlib, subprocess
ROOT=pathlib.Path(__file__).resolve().parents[4]
OUT=pathlib.Path(__file__).resolve().parent
PIN='032f8a2087a41e35451466e28161842c63433349'
def read(path):
 return subprocess.check_output(['git','show',f'{PIN}:{path}'],cwd=ROOT)
paths=subprocess.check_output(['git','ls-tree','-r','--name-only',PIN,'vigil/records/incidents'],cwd=ROOT,text=True).splitlines()
records=[]; mappings=[]; episodes=[]
for path in paths:
 if not path.endswith('.json'):continue
 raw=read(path);r=json.loads(raw);t=r.get('taxonomy_classification',{});cs=r.get('vigil_assessment',{}).get('source_clause_analysis',{}).get('clauses',[])
 ms=[('primary',t.get('primary_classification'))]+[(f'secondary[{i}]',m) for i,m in enumerate(t.get('secondary_classifications',[]))];ms=[(pos,m) for pos,m in ms if m]
 records.append(dict(incident_id=r['id'],path=path,sha256=hashlib.sha256(raw).hexdigest(),record_version=r.get('record_version'),historical_taxonomy_version=t.get('taxonomy_version'),mapping_count=len(ms),material_clause_count=len(cs),stored_coverage=t.get('adjudication_coverage',{}).get('status'),diagnostic_review_status='pending',note='Inventory is not substantive review. INC-003 scoped pilot is separately recorded; it does not complete that Incident.'))
 for i,c in enumerate(cs):
  episodes.append(dict(incident_id=r['id'],clause_index=i,episode_id=c.get('episode_id'),source_record_refs=c.get('source_record_refs',[]),stored_disposition=c.get('adjudication_status'),diagnostic_review_status='pending'))
 for pos,m in ms:
  support=[c.get('episode_id') for c in cs if any(x.get('class_id')==m['class_id'] and x.get('canonical_taxonomy_mapping') is True for x in c.get('taxonomy_relationships',[]))]
  mappings.append(dict(incident_id=r['id'],position=pos,baseline=m,historical_taxonomy_version=t.get('taxonomy_version'),explicit_episode_refs=support,diagnostic_review_status='pending',boundary_diagnostic='E' if m['classification_role']=='ambiguous-boundary' else None,diagnostic_note='Necessary independent source/criterion examination not completed. No disposition inferred.'))
roles=collections.Counter(x['baseline']['classification_role'] for x in mappings)
bounds=[x for x in mappings if x['baseline']['classification_role']=='ambiguous-boundary']
old=json.loads(read('vigil/docs/reviews/2026-10-18-section03-completion/inventory.json'))
oldmap={(x['incident_id'],x['class_id']):x for x in old['mappings']}
delta=[]
for x in mappings:
 key=(x['incident_id'],x['baseline']['class_id']);prior=oldmap.get(key)
 if prior is None or prior['role']!=x['baseline']['classification_role'] or prior['classification_basis']!=x['baseline'].get('classification_basis'):delta.append(key)
payload=dict(date='2026-10-19',input_commit=PIN,reference_taxonomy_version='0.7.0',scope='AUDIT; actual admitted mappings and recorded source clauses only; not a mandatory coverage matrix',counts=dict(incidents=len(records),mappings=len(mappings),roles=dict(roles),boundary_incidents=len(set(x['incident_id'] for x in bounds)),without_mapping=sum(x['mapping_count']==0 for x in records),source_clauses=len(episodes),unique_incident_episode_pairs=len(set((x['incident_id'],x['episode_id']) for x in episodes)),episode_dispositions=dict(collections.Counter(x['stored_disposition'] for x in episodes)),missing_explicit_episode_relationship=sum(not x['explicit_episode_refs'] for x in mappings)),review_counts=dict(fully_reviewed_incidents=0,completed_boundary_diagnostic_packets=0,pending_full_incident_decisions=len(records),pending_boundary_decisions=len(bounds),scoped_pilot_incidents=1),inventory_reconciliation=dict(previous_inventory_counts=old['counts'],membership_role_or_basis_differences=delta,warning='Previous satisfactory-unchanged explanation labels are not substantive adjudication passes.'),incidents=records,mappings=mappings,episodes=episodes)
(OUT/'census.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(payload['counts'],indent=2));print('inventory deltas',delta)
