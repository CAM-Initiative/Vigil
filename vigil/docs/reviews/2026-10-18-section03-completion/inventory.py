"""One-off reproducible Section 03 explanation inventory; not a semantic validator.
Run from repository root. Enumerates existing mappings, never Incident × class pairs.
"""
import collections, hashlib, json, pathlib, re, subprocess
ROOT = pathlib.Path(__file__).resolve().parents[4]
OUT = pathlib.Path(__file__).resolve().parent
changes = json.loads((OUT / 'basis-changes.json').read_text())
baseline = changes['baseline_ref']
changed = {(c['incident_id'], c['class_id']): c for c in changes['changes']}
held = {
 ('VIGIL-INC-000194','VIGIL-FC-000049'): 'The engagement mechanics and attachment cues are specific, but the basis and two source episodes do not identify the fourth required failure condition: material impairment of bounded disengagement or independent choice. Proposed separate review: locate that fact in the cited evaluation and retain with evidence, or consider Boundary if material engagement but unresolved polarity is established. No role or confidence edit authorised by this audit.',
 ('VIGIL-INC-000197','VIGIL-FC-000086'): 'No explicitly canonical source-episode relationship for the admitted secondary mapping. Do not silently assign E001/E002 by similarity. Proposed separate review: decide which preserved interaction materially engages the relational-authority boundary and add a relationship only with maintainer approval, or disposition the unsupported mapping.',
 ('VIGIL-INC-000198','VIGIL-FC-000087'): 'No explicitly canonical source-episode relationship for the admitted secondary mapping. Medical vulnerability in the account does not itself prove which signal reached the model. Proposed separate review: identify evidence of system-visible protection engagement before admitting an episode relationship, or disposition the unsupported mapping.',
}
rows=[]; incidents=[]
for path in sorted((ROOT/'vigil/records/incidents').glob('*.json')):
 r=json.loads(path.read_text()); t=r.get('taxonomy_classification',{})
 old=json.loads(subprocess.check_output(['git','show',f'{baseline}:{path.relative_to(ROOT)}'],cwd=ROOT,text=True))
 cs=r.get('vigil_assessment',{}).get('source_clause_analysis',{}).get('clauses',[])
 mappings=[('primary',t.get('primary_classification'))]+[(f'secondary[{i}]',m) for i,m in enumerate(t.get('secondary_classifications',[]))]
 incidents.append({'incident_id':r['id'],'classification_status':t.get('classification_status'),'coverage':t.get('adjudication_coverage',{}).get('status'),'mapping_count':sum(bool(m) for _,m in mappings),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
 for position,m in mappings:
  if not m:continue
  evidence=[]
  for c in cs:
   matches=[x for x in c.get('taxonomy_relationships',[]) if x.get('class_id')==m['class_id'] and x.get('canonical_taxonomy_mapping') is True]
   if matches:evidence.append({'episode_id':c.get('episode_id'),'source_record_refs':c.get('source_record_refs',[]),'observation':c.get('source_paraphrase'),'relationships':matches})
  key=(r['id'],m['class_id']);basis=m.get('classification_basis','')
  flags=[]
  if not basis.strip():flags.append('missing mapping basis')
  if not evidence:flags.append('no explicit canonical episode relationship')
  row={'incident_id':r['id'],'mapping':position,'class_id':m['class_id'],'role':m['classification_role'],'confidence':m.get('classification_confidence'),'recorded_taxonomy_version':t.get('taxonomy_version'),'classification_basis':basis,'supporting_episodes':evidence,'structural_flags':flags,'explanation_disposition':'held' if key in held else 'improved' if key in changed else 'satisfactory-unchanged','issue_url': ('https://github.com/CAM-Initiative/Vigil/issues/139' if key[0]=='VIGIL-INC-000194' else 'https://github.com/CAM-Initiative/Vigil/issues/138') if key in held else None,'review_note':held.get(key) or changed.get(key,{}).get('reason') or 'Occurrence-specific action and mechanism are stated; preserve existing explanation and its bounded role. This explanation review does not certify all classification recognition conditions or fresh source access.'}
  rows.append(row)
counts=collections.Counter(r['explanation_disposition'] for r in rows)
payload={'scope':'Dated explanation-only review of actual admitted mappings; not a new canonical dataset, re-adjudication or mandatory validator. Existing source packets inspected; no fresh originating-source authentication claimed.','baseline_ref':baseline,'current_taxonomy_reference_version':json.loads((ROOT/'vigil/taxonomy/VIGIL.FailureTaxonomy.Index.json').read_text())['standard']['version'],'counts':{'incidents':len(incidents),'mappings':len(rows),**counts,'missing_bases':sum('missing mapping basis' in r['structural_flags'] for r in rows),'no_explicit_episode_relationship':sum(not r['supporting_episodes'] for r in rows)},'incidents':incidents,'mappings':rows}
(OUT/'inventory.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(payload['counts']))
