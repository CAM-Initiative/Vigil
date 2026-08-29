#!/usr/bin/env python3
"""Refine taxonomy Case Study source selection and evidence focus once."""
from pathlib import Path

PATH = Path("vigil/taxonomy/render_taxonomy.py")
text = PATH.read_text(encoding="utf-8")

start = text.index("def _excerpt(value: object, limit: int = 720) -> str:")
end = text.index("\ndef _severity_rank", start)
new_block = r'''def _excerpt(value: object, limit: int = 720) -> str:
    text = " ".join(str(value or "").split())
    if not text or len(text) <= limit:
        return text
    sentences = re.split(r"(?<=[.!?])\s+", text)
    selected: list[str] = []
    length = 0
    for sentence in sentences:
        next_length = length + len(sentence) + (1 if selected else 0)
        if selected and next_length > limit:
            break
        selected.append(sentence)
        length = next_length
        if length >= int(limit * 0.72):
            break
    excerpt = " ".join(selected).strip()
    if excerpt and len(excerpt) <= limit:
        return excerpt
    clipped = text[:limit].rsplit(" ", 1)[0].rstrip(" ,;:")
    return clipped + "…"


_CASE_STOPWORDS = {
    "about", "above", "after", "again", "against", "another", "because", "being", "between",
    "class", "content", "despite", "does", "during", "evidence", "external", "failure", "from",
    "into", "itself", "more", "other", "over", "same", "system", "than", "that", "their",
    "there", "these", "this", "through", "under", "where", "which", "while", "with", "without",
}


def _focus_terms(example: dict) -> set[str]:
    focus_text = " ".join(
        str(example.get(key, ""))
        for key in ("title", "classification_basis")
    ).lower()
    return {
        token
        for token in re.findall(r"[a-z0-9][a-z0-9-]{3,}", focus_text)
        if token not in _CASE_STOPWORDS
    }


def _focused_excerpt(value: object, example: dict, limit: int = 720) -> str:
    text = " ".join(str(value or "").split())
    if not text:
        return ""
    focus = _focus_terms(example)
    if not focus:
        return _excerpt(text, limit)

    units = [
        unit.strip()
        for unit in re.split(r"(?<=[.!?])\s+|;\s+", text)
        if unit.strip()
    ]
    if not units:
        return _excerpt(text, limit)

    scored: list[tuple[int, int, str]] = []
    for index, unit in enumerate(units):
        unit_terms = set(re.findall(r"[a-z0-9][a-z0-9-]{3,}", unit.lower()))
        overlap = len(focus & unit_terms)
        phrase_bonus = sum(1 for term in focus if term in unit.lower())
        scored.append((overlap * 4 + phrase_bonus, index, unit))

    best_score = max(score for score, _, _ in scored)
    if best_score <= 0:
        return _excerpt(text, limit)

    selected = sorted(
        [item for item in scored if item[0] == best_score],
        key=lambda item: item[1],
    )[:2]
    result = "; ".join(item[2] for item in selected).strip()
    if len(result) > limit:
        result = _excerpt(result, limit)
    if result and result[-1] not in ".!?…":
        result = "The evidence records " + result[0].lower() + result[1:].rstrip(" ,;:") + "."
    return result


def _source_quality(source: dict) -> int:
    score = 0
    role = str(source.get("source_role", "")).lower()
    source_type = str(source.get("source_type", "")).lower()
    context = str(source.get("source_context", "")).lower()
    relevance = str(source.get("relevance_note", "")).lower()
    access = source.get("primary_artefact_access") if isinstance(source.get("primary_artefact_access"), dict) else {}

    if access.get("direct_primary_artefact_review") is True:
        score += 8
    if any(term in role for term in ("research-evidence", "primary-evidence", "technical-evidence", "authoritative-evidence")):
        score += 7
    elif "incident-evidence" in role:
        score += 3
    elif "evidence" in role:
        score += 2
    elif "governance-basis" in role:
        score += 1

    if any(term in source_type for term in ("research-source", "peer-reviewed", "security-research", "technical-report", "official", "standard")):
        score += 5
    if any(term in source_type for term in ("social-platform", "social-media", "commentary")):
        score -= 6

    low_value_markers = (
        "dissemination context", "discovery provenance", "discovery and public-framing",
        "discovery and public framing", "not used as the technical", "context only",
        "public-framing source only", "public framing source only",
    )
    if any(marker in context or marker in relevance for marker in low_value_markers):
        score -= 12
    return score


def _multi_value_label(values: list[str], single_fallback: str) -> tuple[str, bool]:
    if len(values) == 1:
        return values[0], True
    if len(values) > 1:
        return "Multi-vendor evidence", True
    fallback = single_fallback.strip()
    if not fallback:
        return "", False
    lowered = fallback.lower()
    if any(token in lowered for token in (",", " + ", ";", " / ")) or "multi-vendor" in lowered or "multi vendor" in lowered:
        return "Multi-vendor evidence", True
    return fallback, True


def case_study_context(example: dict) -> dict[str, object]:
    failure_mode_id = str(example.get("failure_mode_id", ""))
    if not failure_mode_id:
        return {}
    record_path = FAILURE_RECORDS / f"{failure_mode_id}.json"
    if not record_path.exists():
        return {}
    record = load(record_path)
    system_context = record.get("system_context") if isinstance(record.get("system_context"), dict) else {}
    source_records = record.get("source_records")
    if not isinstance(source_records, list):
        source_records = []

    placeholder_vendors = {
        "", "unknown", "unknown vendor", "unknown provider", "other", "not applicable",
        "n/a", "provider unresolved", "provider-unresolved", "system unresolved", "system-unresolved",
        "multi vendor", "multi-vendor",
    }
    vendors = _clean_values(system_context.get("evidenced_vendors"), placeholder_vendors)
    system_label, vendor_known = _multi_value_label(vendors, str(system_context.get("platform_or_vendor") or ""))
    if system_label.lower() in placeholder_vendors:
        system_label = ""
        vendor_known = False

    source_pool = [source for source in source_records if isinstance(source, dict)]
    evidence_source = max(
        source_pool,
        key=lambda source: (
            _source_quality(source),
            _case_date(source.get("source_date")).toordinal(),
        ),
        default=None,
    )
    source_date = evidence_source.get("source_date") if evidence_source else None

    source_context = ""
    source_label = ""
    source_title = ""
    if evidence_source:
        source_context = str(
            evidence_source.get("confirmed_evidence")
            or evidence_source.get("source_context")
            or evidence_source.get("description")
            or evidence_source.get("finding")
            or ""
        ).strip()
        source_label = str(
            evidence_source.get("source_platform")
            or evidence_source.get("publisher")
            or evidence_source.get("author_or_publisher")
            or ""
        ).strip()
        if len(source_label) > 44:
            source_label = str(evidence_source.get("source_type") or "Evidence source").replace("-", " ").title()
        source_title = str(evidence_source.get("source_title") or evidence_source.get("title") or "").strip()

    case_context = _focused_excerpt(
        source_context
        or record.get("summary")
        or record.get("failure_mode_definition")
        or record.get("failure_threshold"),
        example,
    )

    failure_classification = record.get("failure_classification") if isinstance(record.get("failure_classification"), dict) else {}
    severity = str(failure_classification.get("severity") or "SU").upper()
    return {
        "system_label": system_label,
        "date": publication_date(source_date),
        "source_date": str(source_date or ""),
        "source_publisher": source_label,
        "source_title": source_title,
        "case_context": case_context,
        "severity": severity,
        "vendor_known": vendor_known,
    }

'''
text = text[:start] + new_block + text[end:]
PATH.write_text(text, encoding="utf-8")
print("Refined Case Study evidence-source selection and focused narrative")
