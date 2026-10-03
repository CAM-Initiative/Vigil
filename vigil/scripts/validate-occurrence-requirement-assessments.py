#!/usr/bin/env python3
"""Validate independent occurrence assessments without a candidate matrix."""
import json
from pathlib import Path
from external_requirements_io import load_requirements
from occurrence_requirement_validation import assessment_errors
ROOT = Path(__file__).resolve().parents[1]

def main():
    known = {r['requirement_id'] for r in load_requirements()}
    relationships = json.loads((ROOT / 'external_governance/requirements/taxonomy-relationships.json').read_text())['relationships']
    errors = []
    for p in sorted((ROOT / 'records/incidents').glob('*.json')):
        errors.extend(f'{p.name}: {e}' for e in assessment_errors(json.loads(p.read_text()), known, relationships))
    if errors:
        raise SystemExit('\n'.join(errors))
    print('Occurrence requirement assessments: evidence, derivation and independent alignment results OK')

if __name__ == '__main__':
    main()
