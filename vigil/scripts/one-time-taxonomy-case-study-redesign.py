#!/usr/bin/env python3
"""Apply the approved taxonomy publication refinements once."""
from pathlib import Path

PATH = Path("vigil/taxonomy/render_taxonomy.py")
text = PATH.read_text(encoding="utf-8")

start = text.index("def _case_date(value: object) -> date:")
end = text.index("\ndef publication_class_html", start)
new_block = r'''def _case_date(value: object) -> date:
    try:
        return date.fromisoformat(str(value))
    except (TypeError, ValueError):
        return date.min


def _clean_values(values: object, placeholders: set[str]) -> list[str]:
    raw_values = values if isinstance(values, list) else []
    cleaned: list[str] = []
    seen: set[str] = set()
    for value in raw_values:
        item = str(value).strip()
        key = item.lower()
        if not item or key in placeholders or key in seen:
            continue
        seen.add(key)
        cleaned.append(item)
    return cleaned


def _excerpt(value: object, limit: int = 720) -> str:
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

    external_evidence = [
        source for source in source_records
        if isinstance(source, dict)
        and source.get("source_date")
        and "evidence" in str(source.get("source_role", "")).lower()
        and str(source.get("source_residence", "external")).lower() not in {"internal", "cam-internal"}
    ]
    evidence_sources = [
        source for source in source_records
        if isinstance(source, dict)
        and source.get("source_date")
        and "evidence" in str(source.get("source_role", "")).lower()
    ]
    external_dated = [
        source for source in source_records
        if isinstance(source, dict)
        and source.get("source_date")
        and str(source.get("source_residence", "external")).lower() not in {"internal", "cam-internal"}
    ]
    dated_sources = [source for source in source_records if isinstance(source, dict) and source.get("source_date")]
    source_pool = external_evidence or evidence_sources or external_dated or dated_sources
    evidence_source = max(source_pool, key=lambda source: _case_date(source.get("source_date")), default=None)
    source_date = evidence_source.get("source_date") if evidence_source else None

    source_context = ""
    source_publisher = ""
    source_title = ""
    if evidence_source:
        source_context = str(
            evidence_source.get("confirmed_evidence")
            or evidence_source.get("source_context")
            or evidence_source.get("description")
            or evidence_source.get("finding")
            or ""
        ).strip()
        source_publisher = str(
            evidence_source.get("author_or_publisher")
            or evidence_source.get("publisher")
            or evidence_source.get("source_platform")
            or ""
        ).strip()
        source_title = str(evidence_source.get("source_title") or evidence_source.get("title") or "").strip()

    case_context = _excerpt(
        source_context
        or record.get("summary")
        or record.get("failure_mode_definition")
        or record.get("failure_threshold")
    )

    failure_classification = record.get("failure_classification") if isinstance(record.get("failure_classification"), dict) else {}
    severity = str(failure_classification.get("severity") or "SU").upper()
    return {
        "system_label": system_label,
        "date": publication_date(source_date),
        "source_date": str(source_date or ""),
        "source_publisher": source_publisher,
        "source_title": source_title,
        "case_context": case_context,
        "severity": severity,
        "vendor_known": vendor_known,
    }


def _severity_rank(value: object) -> int:
    return {"S0": 0, "S1": 1, "S2": 2, "S3": 3, "S4": 4, "SU": 5}.get(str(value).upper(), 6)


def _candidate_rank(candidate: dict) -> tuple[int, int, int, int, str]:
    return (
        _severity_rank(candidate["context"].get("severity")),
        -_case_date(candidate["context"].get("source_date")).toordinal(),
        candidate["role_rank"],
        candidate["class_index"],
        str(candidate["example"].get("failure_mode_id", "")),
    )


def select_family_case_examples(data: dict, case_examples: dict[str, list[dict]]) -> dict[str, list[dict]]:
    """Select at most three publication-grade exemplars for one failure family.

    High-confidence taxonomy fit and a known affected vendor remain eligibility gates.
    Severity is a ranking signal rather than a hard threshold. Selection first favours
    coverage across distinct failure classes, then severity and newest evidence date.
    """
    candidates: list[dict] = []
    for class_index, item in enumerate(data.get("classes", [])):
        class_id = str(item.get("class_id", ""))
        for example in case_examples.get(class_id, []):
            if str(example.get("classification_confidence", "")).lower() != "high":
                continue
            context = case_study_context(example)
            if not context.get("vendor_known"):
                continue
            candidates.append({
                "class_id": class_id,
                "class_index": class_index,
                "example": example,
                "context": context,
                "role_rank": 0 if str(example.get("classification_role", "primary")).lower() == "primary" else 1,
            })

    by_class: dict[str, list[dict]] = {}
    for candidate in candidates:
        by_class.setdefault(candidate["class_id"], []).append(candidate)
    for class_candidates in by_class.values():
        class_candidates.sort(key=_candidate_rank)

    champions = sorted((items[0] for items in by_class.values() if items), key=_candidate_rank)
    selected_candidates: list[dict] = []
    used_failure_modes: set[str] = set()

    # Prefer distinct classes so the examples illuminate the class they sit beneath.
    for candidate in champions:
        failure_mode_id = str(candidate["example"].get("failure_mode_id", ""))
        if failure_mode_id in used_failure_modes:
            continue
        selected_candidates.append(candidate)
        used_failure_modes.add(failure_mode_id)
        if len(selected_candidates) == 3:
            break

    # If a family has fewer than three eligible class champions, fill remaining slots
    # from the best remaining high-confidence, known-vendor cases without duplicating FMs.
    if len(selected_candidates) < 3:
        for candidate in sorted(candidates, key=_candidate_rank):
            failure_mode_id = str(candidate["example"].get("failure_mode_id", ""))
            if failure_mode_id in used_failure_modes:
                continue
            selected_candidates.append(candidate)
            used_failure_modes.add(failure_mode_id)
            if len(selected_candidates) == 3:
                break

    selected: dict[str, list[dict]] = {}
    for candidate in selected_candidates:
        selected.setdefault(candidate["class_id"], []).append(candidate["example"])
    return selected


def case_examples_html(examples: list[dict]) -> str:
    if not examples:
        return ""
    studies = []
    for example in examples:
        basis = str(example.get("classification_basis", "")).strip()
        context = case_study_context(example)
        meta_parts = []
        if context.get("system_label"):
            meta_parts.append(str(context["system_label"]))
        if context.get("source_publisher") and str(context["source_publisher"]) not in meta_parts:
            meta_parts.append(str(context["source_publisher"]))
        if context.get("date"):
            meta_parts.append(str(context["date"]))
        meta = " · ".join(esc(value) for value in meta_parts if value)
        case_context = str(context.get("case_context") or "").strip()
        studies.append(
            "<article class=\"case-study\">"
            f"<h5>{esc(example.get('title', ''))}</h5>"
            + (f"<p class=\"case-study-meta\">{meta}</p>" if meta else "")
            + (f"<p class=\"case-study-context\">{esc(case_context)}</p>" if case_context else "")
            + (f"<p class=\"case-study-basis\"><strong>Relevance to this class:</strong> {esc(basis)}</p>" if basis else "")
            + f"<p class=\"case-study-ref\"><code>{esc(example.get('failure_mode_id', ''))}</code></p>"
            + "</article>"
        )
    heading = "Case Study" if len(studies) == 1 else "Case Studies"
    return f"<section class=\"case-studies\"><h4>{heading}</h4>" + "".join(studies) + "</section>"

'''
text = text[:start] + new_block + text[end:]

note = '<h3>In this chapter</h3><p class="chapter-map-note">Publication numbering is navigational only. Immutable VIGIL identifiers remain authoritative.</p>'
if note not in text:
    raise SystemExit("chapter-map handoff note not found")
text = text.replace(note, '<h3>In this chapter</h3>', 1)

# Standardise the publication-information / reliance page to one sans-serif family.
imprint_start = text.index('.publication-imprint{')
imprint_end = text.index('\n.contents{', imprint_start)
new_imprint_css = '''.publication-imprint{page:imprint;min-height:249mm;page-break-after:always;display:flex;flex-direction:column;color:#2a2a2a;font-family:Helvetica,Arial,sans-serif}.imprint-kicker{font-family:Helvetica,Arial,sans-serif;color:#022c1b;text-transform:uppercase;letter-spacing:.08em;font-size:7.5pt;font-weight:700;margin-bottom:4mm}.publication-imprint h1{font-family:Helvetica,Arial,sans-serif;color:#022c1b;font-size:22pt;font-weight:700;margin:0 0 13mm}.publication-meta{display:grid;grid-template-columns:42mm 1fr;gap:3mm 6mm;margin:0;font-family:Helvetica,Arial,sans-serif}.publication-meta dt{color:#6f6657}.publication-meta dd{margin:0;font-weight:600}.imprint-rule{height:.6pt;background:#b8943f;width:100%;margin:14mm 0 8mm}.publication-imprint>p{font-family:Helvetica,Arial,sans-serif}.reliance-notice{margin-top:auto;padding-top:6mm;border-top:.6pt solid #d8d5cc;font-family:Helvetica,Arial,sans-serif}.reliance-notice h2{font-family:Helvetica,Arial,sans-serif;font-size:9pt;font-weight:700;color:#022c1b;margin:0 0 2.5mm}.reliance-notice p{font-family:Helvetica,Arial,sans-serif;font-size:8.3pt;line-height:1.45;color:#504a40;margin:0}.copyright{font-family:Helvetica,Arial,sans-serif;margin-top:5mm;font-size:9pt;color:#504a40}.copyright strong{color:#022c1b}.website{margin-top:2mm;color:#022c1b}'''
text = text[:imprint_start] + new_imprint_css + text[imprint_end:]

# Replace the loose gold-rule Case Study treatment with a contained publication panel.
case_css_start = text.index('.case-studies{', text.index('PRINT_STYLE ='))
case_css_end = text.index('.book-family code', case_css_start)
new_case_css = '''.case-studies{margin-top:7mm}.case-studies>h4{font-family:Georgia,"Times New Roman",serif;font-size:15pt;color:#022c1b;font-weight:500;margin:0 0 3mm}.case-study{background:#eef4e8;border-left:3pt solid #022c1b;border-radius:2mm;padding:4mm 5mm;margin:0 0 4mm;break-inside:avoid}.case-study h5{font-family:Georgia,"Times New Roman",serif;font-size:11.5pt;line-height:1.2;color:#022c1b;margin:0 0 1.2mm}.case-study-meta{font-family:Helvetica,Arial,sans-serif;font-size:8pt;color:#6f6657;margin:0 0 3mm}.case-study-context{font-family:Helvetica,Arial,sans-serif;font-size:9.5pt;line-height:1.45;margin:0 0 3mm;color:#2f302d}.case-study-basis{font-family:Helvetica,Arial,sans-serif;font-size:9pt;line-height:1.4;margin:0;padding-top:3mm;border-top:.45pt solid #c7d5c9;color:#3f463f}.case-study-basis strong{color:#022c1b}.case-study-ref{font-family:Helvetica,Arial,sans-serif;font-size:7.5pt;color:#78716c;margin:3mm 0 0}.book-family code,.book-class code{font-size:.88em}'''
text = text[:case_css_start] + new_case_css + text[case_css_end + len('.book-family code,.book-class code{font-size:.88em}'):]

# Remove obsolete CSS for the deleted handoff note.
text = re.sub(r'\.chapter-map-note\{[^}]*\}', '', text, count=1)

PATH.write_text(text, encoding="utf-8")
print("Applied taxonomy case-study redesign and imprint typography standardisation")
