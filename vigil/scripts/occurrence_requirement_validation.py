"""Independent occurrence-level external requirement assessment integrity."""
from __future__ import annotations
from datetime import date
import re


def assessment_errors(record: dict, known_ids: set[str] | None, relationships: list[dict]) -> list[str]:
    assessments = record.get('external_requirement_assessments', [])
    if not isinstance(assessments, list):
        return ['external_requirement_assessments must be an array when present']
    clauses = record.get('vigil_assessment', {}).get('source_clause_analysis', {}).get('clauses', [])
    sources = record.get('source_records', [])
    required = {'requirement_id', 'applicability_status', 'applicability_basis', 'assessed_on', 'source_record_refs'}
    allowed = required | {'derived_from_class_ids', 'source_clause_indices', 'finding', 'finding_basis', 'identification_basis'}
    supported = {(r.get('class_id'), r.get('requirement_id')) for r in relationships
                 if r.get('review_status') == 'supported' and r.get('strength') in {'direct', 'strong-supporting'}}
    errors = []
    seen = set()
    for i, a in enumerate(assessments):
        label = f'external_requirement_assessments[{i}]'
        if not isinstance(a, dict):
            errors.append(f'{label} must be an object')
            continue
        if required - a.keys():
            errors.append(f'{label} missing {", ".join(sorted(required - a.keys()))}')
        if a.keys() - allowed:
            errors.append(f'{label} has non-canonical fields: {", ".join(sorted(a.keys() - allowed))}')
        req = a.get('requirement_id')
        if not isinstance(req, str) or re.fullmatch(r'EXTREQ-[A-F0-9]{16}', req) is None:
            errors.append(f'{label}.requirement_id is not canonical')
        elif known_ids is not None and req not in known_ids:
            errors.append(f'{label}.requirement_id does not resolve in the canonical EXTREQ corpus')
        if isinstance(req, str):
            if req in seen:
                errors.append(f'{label}.requirement_id must be unique within the Incident')
            seen.add(req)
        refs = a.get('source_record_refs')
        if not isinstance(refs, list) or not refs or any(not isinstance(r, str) for r in refs):
            errors.append(f'{label}.source_record_refs must be a non-empty evidence reference array')
        else:
            if len(refs) != len(set(refs)):
                errors.append(f'{label}.source_record_refs contains duplicates')
            for ref in refs:
                m = re.fullmatch(r'source_records\[(\d+)\]', ref)
                if m is None or int(m[1]) >= len(sources):
                    errors.append(f'{label}.source_record_refs does not resolve: {ref}')
        status = a.get('applicability_status')
        if status not in {'applicable', 'insufficient-evidence', 'not-applicable'}:
            errors.append(f'{label}.applicability_status is not canonical')
        for key in ('applicability_basis',):
            if not isinstance(a.get(key), str) or not a[key].strip():
                errors.append(f'{label}.{key} must be non-empty')
        try:
            value = a.get('assessed_on')
            if not isinstance(value, str) or re.fullmatch(r'\d{4}-\d{2}-\d{2}', value) is None:
                raise ValueError
            date.fromisoformat(value)
        except (ValueError, TypeError):
            errors.append(f'{label}.assessed_on must be an ISO date')
        if status == 'applicable':
            if a.get('finding') not in {'met', 'not-met', 'evidence-insufficient', 'not-assessable'}:
                errors.append(f'{label}.finding is required and must be an independent requirement outcome')
            if not isinstance(a.get('finding_basis'), str) or not a['finding_basis'].strip():
                errors.append(f'{label}.finding_basis is required')
        elif 'finding' in a or 'finding_basis' in a:
            errors.append(f'{label} must not include finding or finding_basis when applicability_status is {status}')
        ids = a.get('derived_from_class_ids', [])
        indices = a.get('source_clause_indices', [])
        if not isinstance(ids, list) or any(not isinstance(c, str) or re.fullmatch(r'VIGIL-FC-\d{6}', c) is None for c in ids):
            errors.append(f'{label}.derived_from_class_ids must contain canonical Fidelity Class IDs')
        elif ids:
            if len(ids) != len(set(ids)):
                errors.append(f'{label}.derived_from_class_ids contains duplicates')
            if not isinstance(indices, list) or not indices or any(type(c) is not int or c < 0 or c >= len(clauses) for c in indices):
                errors.append(f'{label}.source_clause_indices must resolve for taxonomy derivation')
            else:
                mapped = {r.get('class_id') for index in indices for r in clauses[index].get('taxonomy_relationships', [])
                          if r.get('canonical_taxonomy_mapping') is True}
                for cid in ids:
                    if cid not in mapped or (cid, req) not in supported:
                        errors.append(f'{label}.derived_from_class_ids lacks a supported clause-scoped relationship: {cid}')
        elif not isinstance(a.get('identification_basis'), str) or not a['identification_basis'].strip():
            errors.append(f'{label}.identification_basis is required for independent identification')
    return errors
