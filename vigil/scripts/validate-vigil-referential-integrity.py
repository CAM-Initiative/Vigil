#!/usr/bin/env python3
"""Thin cross-dataset ID integrity; no substantive adjudication or global matrix."""
import json
from pathlib import Path
from external_requirements_io import load_requirements

ROOT = Path(__file__).resolve().parents[1]


def main():
    requirements = {r['requirement_id'] for r in load_requirements()}
    families = {}
    classes = {}
    errors = []
    for p in sorted((ROOT / 'taxonomy/families').glob('*.json')):
        d = json.loads(p.read_text())
        families[d['family']['family_id']] = d['family']
        for c in d['classes']:
            classes[c['class_id']] = c
    for cid, c in classes.items():
        if c['family_id'] not in families:
            errors.append(f'{cid}: family ID does not resolve')
        for ref in c.get('external_references', []):
            if ref.get('requirement_id') and ref['requirement_id'] not in requirements:
                errors.append(f'{cid}: requirement ID does not resolve: {ref["requirement_id"]}')
    for p in sorted((ROOT / 'records/incidents').glob('*.json')):
        d = json.loads(p.read_text())
        for clause in d.get('vigil_assessment', {}).get('source_clause_analysis', {}).get('clauses', []):
            for r in clause.get('taxonomy_relationships', []):
                if r.get('class_id') and r['class_id'] not in classes:
                    errors.append(f'{d["id"]}: clause class ID does not resolve: {r["class_id"]}')
        for a in d.get('external_requirement_assessments', []):
            if a.get('requirement_id') not in requirements:
                errors.append(f'{d["id"]}: requirement ID does not resolve: {a.get("requirement_id")}')
    for r in json.loads((ROOT / 'external_governance/requirements/taxonomy-relationships.json').read_text())['relationships']:
        if r.get('requirement_id') not in requirements or r.get('class_id') not in classes:
            errors.append(f'{r.get("relationship_id")}: relationship endpoint does not resolve')
    if errors:
        raise SystemExit('\n'.join(errors))
    print('Cross-dataset referential integrity OK; no substantive adjudication performed')


if __name__ == '__main__':
    main()
