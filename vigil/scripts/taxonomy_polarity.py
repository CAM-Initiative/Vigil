"""Evidence-admission structure, never an automatic semantic adjudicator."""
from __future__ import annotations


def established_polarities(class_record: dict, *, success_evidence: list[list[str]],
                           failure_evidence: list[list[str]], failure_excluded: bool = False) -> set[str]:
    """Admit only complete independently adjudicated criterion evidence sets.

    Callers must first adjudicate whether each cited source supports its condition.
    Empty or incomplete evidence never proves the opposite polarity. Both may hold
    for distinct bounded pathways; callers must retain those scopes separately.
    """
    result = set()
    for role, field, evidence in (
        ('successful-invariant', 'success_recognition', success_evidence),
        ('failure-occurrence', 'failure_recognition', failure_evidence),
    ):
        conditions = class_record[field]['required_conditions']
        if len(evidence) == len(conditions) and all(
            isinstance(refs, list) and refs and all(isinstance(ref, str) and ref.strip() for ref in refs)
            for refs in evidence
        ) and not (role == 'failure-occurrence' and failure_excluded):
            result.add(role)
    return result
