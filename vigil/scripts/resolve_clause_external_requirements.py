#!/usr/bin/env python3
"""Resolve one adjudicated clause to disposable, non-authoritative candidates."""
from __future__ import annotations
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RELATIONSHIPS = ROOT / 'external_governance/requirements/taxonomy-relationships.json'


def resolve_clause(clause: dict, relationships: list[dict], known_ids: set[str]) -> list[dict]:
    if clause.get('adjudication_status') != 'mapped':
        return []
    class_ids = {r.get('class_id') for r in clause.get('taxonomy_relationships', [])
                 if r.get('canonical_taxonomy_mapping') is True and
                 r.get('relationship') in {'failure-occurrence', 'successful-invariant', 'ambiguous-boundary'}}
    candidates = {}
    for r in relationships:
        if (r.get('review_status') != 'supported' or r.get('strength') not in {'direct', 'strong-supporting'}
                or r.get('class_id') not in class_ids or r.get('requirement_id') not in known_ids):
            continue
        candidate = candidates.setdefault(r['requirement_id'], {
            'requirement_id': r['requirement_id'], 'derived_from_class_ids': [],
            'relationship_ids': [], 'requires_independent_applicability': True})
        candidate['derived_from_class_ids'].append(r['class_id'])
        candidate['relationship_ids'].append(r['relationship_id'])
    for candidate in candidates.values():
        for key in ('derived_from_class_ids', 'relationship_ids'):
            candidate[key] = sorted(set(candidate[key]))
    return [candidates[k] for k in sorted(candidates)]


def main():
    from external_requirements_io import load_requirements
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('incident', type=Path)
    parser.add_argument('--clause-index', required=True, type=int, help='zero-based canonical clause index')
    args = parser.parse_args()
    record = json.loads(args.incident.read_text())
    clauses = record['vigil_assessment']['source_clause_analysis']['clauses']
    if not 0 <= args.clause_index < len(clauses):
        parser.error('clause index is outside the Incident')
    relationships = json.loads(RELATIONSHIPS.read_text())['relationships']
    requirements = load_requirements()
    known_ids = {r['requirement_id'] for r in requirements}
    print(json.dumps({'incident_id': record['id'], 'clause_index': args.clause_index,
                      'authority': 'disposable-candidates-only',
                      'candidates': resolve_clause(clauses[args.clause_index], relationships, known_ids)}, indent=2))


if __name__ == '__main__':
    main()
