"""Opt-in, incident-local source-episode identity and provenance validation.

Does not infer chronological order, episode distinctness or evidence completeness.
Existing records without episode_id remain valid; migrated records are checked
as a whole so that half-migrated positional pointers cannot pass silently.
"""
from __future__ import annotations

import re

EPISODE_ID = re.compile(r"E[0-9]{3,}")
SOURCE_RECORD_REF = re.compile(r"source_records\[([0-9]+)\]")


def episode_errors(record: dict) -> list[str]:
    errors: list[str] = []
    assessment = record.get("vigil_assessment")
    analysis = assessment.get("source_clause_analysis") if isinstance(assessment, dict) else None
    clauses = analysis.get("clauses") if isinstance(analysis, dict) else None
    if not isinstance(clauses, list):
        return errors
    migrated = any(isinstance(c, dict) and "episode_id" in c for c in clauses)
    if not migrated:
        return errors
    sources = record.get("source_records")
    sources = sources if isinstance(sources, list) else []
    seen: set[str] = set()
    for index, clause in enumerate(clauses):
        label = f"vigil_assessment.source_clause_analysis.clauses[{index}]"
        if not isinstance(clause, dict):
            errors.append(f"{label} must be an object in an episode-migrated record")
            continue
        eid = clause.get("episode_id")
        if not isinstance(eid, str) or EPISODE_ID.fullmatch(eid) is None:
            errors.append(f"{label}.episode_id must use an incident-local E001-style identifier")
        elif eid in seen:
            errors.append(f"{label}.episode_id duplicates {eid}")
        else:
            seen.add(eid)
        refs = clause.get("source_record_refs")
        if not isinstance(refs, list) or not refs or len(refs) != len(set(map(str, refs))):
            errors.append(f"{label}.source_record_refs must be a unique non-empty array")
            continue
        for ref in refs:
            match = SOURCE_RECORD_REF.fullmatch(ref) if isinstance(ref, str) else None
            if match is None or int(match[1]) >= len(sources):
                errors.append(f"{label}.source_record_refs does not resolve: {ref!r}")
    return errors
