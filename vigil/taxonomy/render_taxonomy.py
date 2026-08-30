#!/usr/bin/env python3
"""Generate complete human-readable VIGIL Observatory Failure Taxonomy references."""

from __future__ import annotations

import argparse
import html
import json
import os
from datetime import date
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INDEX = ROOT / "VIGIL.FailureTaxonomy.Index.json"
CASE_EXAMPLES = ROOT / "generated" / "VIGIL.FailureTaxonomy.CaseFileExamples.json"
FAILURE_RECORDS = ROOT.parent / "records" / "failures" / "2026"
BRAND_REGISTRY_COMMIT = "b442cd01a8cc2e2623fccfb1748b9409588a9681"
BRAND_HEADER_URL = (
    "https://raw.githubusercontent.com/CAM-Initiative/Registry/"
    f"{BRAND_REGISTRY_COMMIT}/Branding/CAM%20Initiative/CAM%20INITIATIVE%20HEADER.png"
)
BRAND_FOOTER_URL = (
    "https://raw.githubusercontent.com/CAM-Initiative/Registry/"
    f"{BRAND_REGISTRY_COMMIT}/Branding/CAM%20Initiative/CAM_INITIATIVE_FOOTER_EMERALD.png"
)
FULL_HTML_NAME = "VIGIL.FailureTaxonomy.FullReference.html"
FULL_PDF_NAME = "VIGIL.Observatory.FailureTaxonomy.FullReference.pdf"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def esc(value: object) -> str:
    return html.escape(str(value))


def label(value: str) -> str:
    return value.replace("_", " ").title()


def anchor(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def markdown_family(data: dict, level: int = 1) -> str:
    family = data["family"]
    h = "#" * level
    out = [
        f"{h} {family['name']}", "",
        f"{h}# Family definition", "",
        "| Field | Value |", "|---|---|",
        f"| Immutable ID | `{family['family_id']}` |",
        f"| Semantic code | `{family['family_code']}` |",
        f"| Status | {family['status']} |",
        f"| Version | {family['version']} |",
        f"| Abstraction | {family['abstraction']} |", "",
        f"{h}## Plain English", "", family["plain_english"], "",
        f"{h}## Technical definition", "", family["definition"], "",
        f"{h}## Governing invariant", "", f"> {family['invariant']}", "",
        f"{h}## Classification boundary", "",
        f"**Include when:** {family['inclusion_rule']}", "",
        f"**Exclude when:** {family['exclusion_rule']}", "",
        f"{h}## Scope", "",
    ]
    out.extend(f"- {item}" for item in family["scope"])
    out.extend(["", f"{h}## Allowed identifiers", ""])
    out.extend(
        f"- `{class_id}` — `{class_code}`"
        for class_id, class_code in zip(family["allowed_class_ids"], family["allowed_class_codes"])
    )
    if family.get("aliases"):
        out.extend(["", f"**Prior codes / aliases:** {'; '.join(f'`{x}`' for x in family['aliases'])}"])
    out.extend(["", f"{h}# Failure classes", ""])

    for item in data["classes"]:
        out.extend([
            f"{h}# {item['name']}", "",
            f"**Immutable ID:** `{item['class_id']}`  ",
            f"**Semantic code:** `{item['class_code']}`  ",
            f"**Family ID:** `{item['family_id']}`  ",
            f"**Abstraction:** {item['abstraction']}  ",
            f"**Status:** {item['status']}", "",
            f"**Plain English:** {item['plain_english']}", "",
            f"{h}## Technical definition", "", item["definition"], "",
            f"{h}## Recognition criteria", "",
        ])
        out.extend(f"- {x}" for x in item["recognition"]["required_conditions"])
        if item["recognition"].get("indicators"):
            out.extend(["", "**Indicators**", ""])
            out.extend(f"- {x}" for x in item["recognition"]["indicators"])
        out.extend(["", f"{h}## Exclusions", ""])
        out.extend(f"- {x}" for x in item["exclusions"])
        out.extend(["", f"{h}## Illustrative examples", ""])
        out.extend(f"- {x}" for x in item["examples"])
        if item.get("aliases"):
            out.extend(["", f"**Prior codes / aliases:** {'; '.join(f'`{x}`' for x in item['aliases'])}"])
        if item.get("relationships"):
            out.extend(["", f"{h}## Relationships", ""])
            for relation in item["relationships"]:
                note = f" — {relation['note']}" if relation.get("note") else ""
                out.append(f"- {label(relation['type'])}: `{relation['target_id']}`{note}")
        if item.get("external_mappings"):
            out.extend(["", f"{h}## External mappings", ""])
            for mapping in item["external_mappings"]:
                note = f" — {mapping['note']}" if mapping.get("note") else ""
                out.append(
                    f"- {mapping['scheme']} `{mapping['identifier']}` ({mapping['relationship']}){note}"
                )
        out.extend(["", "---", ""])
    return "\n".join(out).rstrip() + "\n"


def publication_date(value: object) -> str:
    if not value:
        return ""
    try:
        parsed = date.fromisoformat(str(value))
        return f"{parsed.day} {parsed.strftime('%B %Y')}"
    except ValueError:
        return str(value)


def _case_date(value: object) -> date:
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


def publication_class_html(item: dict, section_number: str, class_lookup: dict[str, tuple[str, str]], case_examples: list[dict] | None = None) -> str:
    recognition = "".join(f"<li>{esc(x)}</li>" for x in item["recognition"]["required_conditions"])
    indicators = ""
    if item["recognition"].get("indicators"):
        indicators = "<h4>Indicators</h4><ul>" + "".join(f"<li>{esc(x)}</li>" for x in item["recognition"]["indicators"]) + "</ul>"
    exclusions = "".join(f"<li>{esc(x)}</li>" for x in item["exclusions"])
    illustrative_examples = "".join(f"<li>{esc(x)}</li>" for x in item["examples"])
    aliases = ""
    if item.get("aliases"):
        aliases = "<h3>Prior codes and aliases</h3><ul>" + "".join(f"<li><code>{esc(x)}</code></li>" for x in item["aliases"]) + "</ul>"
    relationships = ""
    if item.get("relationships"):
        relationships = "<h3>Relationships</h3><ul>" + "".join(
            f"<li><strong>{esc(label(r['type']))}:</strong> <code>{esc(r['target_id'])}</code>" + (f" — {esc(r['note'])}" if r.get("note") else "") + "</li>"
            for r in item["relationships"]
        ) + "</ul>"
    mappings = ""
    if item.get("external_mappings"):
        mappings = "<h3>External mappings</h3><ul>" + "".join(
            f"<li>{esc(m['scheme'])} <code>{esc(m['identifier'])}</code> ({esc(m['relationship'])})" + (f" — {esc(m['note'])}" if m.get("note") else "") + "</li>"
            for m in item["external_mappings"]
        ) + "</ul>"
    parent_note = ""
    if str(item.get("abstraction", "")).lower() == "variant":
        relation = next((r for r in item.get("relationships", []) if str(r.get("type", "")).lower().replace("_", " ") == "child of"), None)
        if relation:
            parent = class_lookup.get(str(relation.get("target_id", "")))
            if parent:
                parent_note = f"<p class=\"variant-parent\">Variant of {esc(parent[0])} {esc(parent[1])}</p>"
    return f"""
<section class="book-class" id="{esc(anchor(item['class_id']))}">
  <p class="class-kicker">{esc(section_number)} · {esc(str(item['abstraction']).upper())}</p>
  <h2 class="class-title">{esc(item['name'])}</h2>
  <p class="class-meta"><code>{esc(item['class_id'])}</code> · <code>{esc(item['class_code'])}</code> · {esc(str(item['status']).title())}</p>
  {parent_note}
  <p class="plain"><strong>Plain English:</strong> {esc(item['plain_english'])}</p>
  <h3>Technical definition</h3><p>{esc(item['definition'])}</p>
  <div class="grid criteria-grid"><section><h3>Recognition criteria</h3><ul>{recognition}</ul>{indicators}</section><section><h3>Exclusions</h3><ul>{exclusions}</ul></section></div>
  <h3>Illustrative examples</h3><ul>{illustrative_examples}</ul>{aliases}{relationships}{mappings}{case_examples_html(case_examples or [])}
</section>"""


def publication_family_html(data: dict, chapter_number: int, case_examples: dict[str, list[dict]] | None = None) -> str:
    family = data["family"]
    scope = "".join(f"<li>{esc(x)}</li>" for x in family["scope"])
    chapter_rows = []
    class_lookup: dict[str, tuple[str, str]] = {}
    for index, item in enumerate(data["classes"], start=1):
        number = f"{chapter_number}.{index}"
        class_lookup[item["class_id"]] = (number, item["name"])
        suffix = " · Variant" if str(item.get("abstraction", "")).lower() == "variant" else ""
        chapter_rows.append(f"<li><span class=\"chapter-item-number\">{esc(number)}</span><span class=\"chapter-item-title\">{esc(item['name'])}</span><span class=\"chapter-item-id\"><code>{esc(item['class_id'])}</code>{suffix}</span></li>")
    aliases = " · ".join(f"<code>{esc(x)}</code>" for x in family.get("aliases", [])) or "None recorded"
    selected_case_examples = select_family_case_examples(data, case_examples or {})
    classes = "".join(publication_class_html(item, f"{chapter_number}.{index}", class_lookup, selected_case_examples.get(item["class_id"], [])) for index, item in enumerate(data["classes"], start=1))
    return f"""
<section class="book-family" id="{esc(anchor(family['family_id']))}">
  <section class="chapter-opener">
    <p class="chapter-kicker">Chapter {chapter_number}</p>
    <h1>{esc(family['name'])}</h1>
    <p class="chapter-lead">{esc(family['plain_english'])}</p>
    <p class="chapter-meta"><code>{esc(family['family_id'])}</code> · <code>{esc(family['family_code'])}</code> · Version {esc(family['version'])} · {esc(str(family['status']).title())}</p>
  </section>
  <section class="chapter-map">
    <p class="chapter-kicker">Chapter {chapter_number}</p><h2>Outline</h2>
    <h3>Scope</h3><ul>{scope}</ul>
    <h3>In this chapter</h3>
    <ol class="chapter-list">{''.join(chapter_rows)}</ol>
    <h3>Reference metadata</h3><p><strong>Failure family:</strong> <code>{esc(family['family_id'])}</code><br><strong>Semantic code:</strong> <code>{esc(family['family_code'])}</code><br><strong>Prior codes and aliases:</strong> {aliases}</p>
  </section>
  <section class="chapter-overview">
    <p class="chapter-kicker">Chapter {chapter_number} · Failure family overview</p>
    <h2>Technical definition</h2><p>{esc(family['definition'])}</p>
    <h2>Governing invariant</h2><p class="invariant">{esc(family['invariant'])}</p>
    <h2>Classification boundary</h2><div class="grid"><section><h3>Include when</h3><p>{esc(family['inclusion_rule'])}</p></section><section><h3>Exclude when</h3><p>{esc(family['exclusion_rule'])}</p></section></div>
  </section>{classes}
</section>"""


def class_html(item: dict, case_examples: list[dict] | None = None) -> str:
    recognition = "".join(f"<li>{esc(x)}</li>" for x in item["recognition"]["required_conditions"])
    indicators = ""
    if item["recognition"].get("indicators"):
        indicators = "<h4>Indicators</h4><ul>" + "".join(
            f"<li>{esc(x)}</li>" for x in item["recognition"]["indicators"]
        ) + "</ul>"
    exclusions = "".join(f"<li>{esc(x)}</li>" for x in item["exclusions"])
    illustrative_examples = "".join(f"<li>{esc(x)}</li>" for x in item["examples"])
    aliases = ""
    if item.get("aliases"):
        aliases = "<h4>Prior codes and aliases</h4><ul>" + "".join(
            f"<li><code>{esc(x)}</code></li>" for x in item["aliases"]
        ) + "</ul>"
    relationships = ""
    if item.get("relationships"):
        relationships = "<h4>Relationships</h4><ul>" + "".join(
            f"<li><strong>{esc(label(r['type']))}:</strong> <code>{esc(r['target_id'])}</code>"
            + (f" — {esc(r['note'])}" if r.get("note") else "") + "</li>"
            for r in item["relationships"]
        ) + "</ul>"
    mappings = ""
    if item.get("external_mappings"):
        mappings = "<h4>External mappings</h4><ul>" + "".join(
            f"<li>{esc(m['scheme'])} <code>{esc(m['identifier'])}</code> ({esc(m['relationship'])})"
            + (f" — {esc(m['note'])}" if m.get("note") else "") + "</li>"
            for m in item["external_mappings"]
        ) + "</ul>"
    return f"""
<article class="card" id="{esc(anchor(item['class_id']))}">
  <div class="top"><div><span class="pill">{esc(item['abstraction'])}</span><h3>{esc(item['name'])}</h3><p><code>{esc(item['class_id'])}</code> · <code>{esc(item['class_code'])}</code></p></div><span class="pill">{esc(item['status'])}</span></div>
  <p class="plain"><strong>Plain English:</strong> {esc(item['plain_english'])}</p>
  <h4>Technical definition</h4><p>{esc(item['definition'])}</p>
  <div class="grid"><section><h4>Recognition criteria</h4><ul>{recognition}</ul>{indicators}</section><section><h4>Exclusions</h4><ul>{exclusions}</ul></section></div>
  <h4>Illustrative examples</h4><ul>{illustrative_examples}</ul>{aliases}{relationships}{mappings}{case_examples_html(case_examples or [])}
</article>"""


def family_html(data: dict, heading_level: int = 1, case_examples: dict[str, list[dict]] | None = None) -> str:
    family = data["family"]
    tag = f"h{heading_level}"
    scope = "".join(f"<li>{esc(x)}</li>" for x in family["scope"])
    allowed = "".join(
        f"<li><code>{esc(class_id)}</code> — <code>{esc(class_code)}</code></li>"
        for class_id, class_code in zip(family["allowed_class_ids"], family["allowed_class_codes"])
    )
    aliases = "".join(f"<li><code>{esc(x)}</code></li>" for x in family.get("aliases", []))
    return f"""
<section class="family" id="{esc(anchor(family['family_id']))}">
<section class="hero"><p class="eyebrow">Governance Failure Taxonomy · Technical Reference</p><{tag}>{esc(family['name'])}</{tag}><p class="plain">{esc(family['plain_english'])}</p>
<p><strong>Immutable ID:</strong> <code>{esc(family['family_id'])}</code> · <strong>Semantic code:</strong> <code>{esc(family['family_code'])}</code> · <strong>Version:</strong> {esc(family['version'])} · <strong>Status:</strong> {esc(family['status'])}</p>
<h2>Technical definition</h2><p>{esc(family['definition'])}</p><h2>Governing invariant</h2><p class="invariant">{esc(family['invariant'])}</p>
<h2>Classification boundary</h2><div class="grid"><section><h3>Include when</h3><p>{esc(family['inclusion_rule'])}</p></section><section><h3>Exclude when</h3><p>{esc(family['exclusion_rule'])}</p></section></div>
<h2>Scope</h2><ul>{scope}</ul><details><summary><strong>Allowed identifiers</strong></summary><ul>{allowed}</ul></details><details><summary><strong>Prior codes and aliases</strong></summary><ul>{aliases}</ul></details></section>
<h2>Failure classes</h2>{''.join(class_html(item, (case_examples or {}).get(item['class_id'], [])) for item in data['classes'])}</section>"""


STYLE = """
:root{font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;color:#171717;background:#f5f5f4}body{margin:0;line-height:1.55}main{max-width:1100px;margin:auto;padding:36px 20px 80px}.hero,.card,.contents,.publication-frontmatter{background:#fff;border:1px solid #d6d3d1;border-radius:16px;padding:26px;margin-bottom:20px}h1{font-size:clamp(2rem,5vw,3.2rem);line-height:1.05}h3{font-size:1.4rem;margin:.4rem 0}code{background:#f5f5f4;border:1px solid #e7e5e4;border-radius:5px;padding:2px 5px;overflow-wrap:anywhere}.plain{background:#fafaf9;padding:14px 16px;border-radius:10px;font-size:1.06rem}.invariant{border-left:4px solid #44403c;background:#fafaf9;padding:12px 16px}.grid{display:grid;grid-template-columns:1fr 1fr;gap:14px}.grid section{background:#fafaf9;border-radius:10px;padding:14px}.top{display:flex;justify-content:space-between;gap:20px;align-items:start}.pill{font-size:.73rem;border:1px solid #d6d3d1;border-radius:999px;padding:3px 8px;text-transform:uppercase;letter-spacing:.05em}.eyebrow{text-transform:uppercase;letter-spacing:.08em;font-size:.78rem;font-weight:700}.family+.family{border-top:3px solid #a8a29e;padding-top:52px;margin-top:52px}.contents a{color:#1c4b69}.publication-frontmatter h1{max-width:760px}.publication-meta{display:grid;grid-template-columns:auto 1fr;gap:6px 16px}.publication-note{margin-top:28px;padding-top:18px;border-top:1px solid #d6d3d1;color:#57534e}@media(max-width:760px){.grid{grid-template-columns:1fr}.top{display:block}}
"""

PRINT_STYLE = """
@page{size:A4;margin:18mm 16mm 18mm;
  @top-left{content:"CAM INITIATIVE | GOVERNANCE FAILURE TAXONOMY";font-size:7.2pt;color:#022c1b;letter-spacing:.07em;font-weight:600}
  @top-right{content:"TECHNICAL REFERENCE";font-size:7.2pt;color:#78716c;letter-spacing:.06em}
  @bottom-left{content:"cam-initiative.org";font-size:7.2pt;color:#78716c}
  @bottom-right{content:"Page " counter(page);font-size:7.2pt;color:#78716c}
}
@page cover{size:A4;margin:0;@top-left{content:none}@top-right{content:none}@bottom-left{content:none}@bottom-right{content:none}}
@page imprint{size:A4;margin:24mm 20mm;@top-left{content:none}@top-right{content:none}@bottom-left{content:none}@bottom-right{content:none}}
html,body{background:#fff!important}body{font-size:9.5pt;line-height:1.48}main{max-width:none;padding:0}
.publication-frontmatter{page:cover;height:297mm;min-height:0;position:relative;overflow:hidden;box-sizing:border-box;background:#f7f3e9!important;border:0!important;border-radius:0!important;padding:0!important;margin:0!important;page-break-after:always}
.cover-masthead{position:absolute;top:0;left:0;width:210mm;height:auto;display:block}
.cover-body{position:absolute;left:25mm;right:18mm;top:94mm}
.cover-title{font-family:Georgia,"Times New Roman",serif;font-size:35pt;line-height:.98;text-transform:uppercase;color:#022c1b;letter-spacing:.012em;margin:0 0 7mm;font-weight:500;max-width:155mm}
.cover-subtitle{font-family:Georgia,"Times New Roman",serif;font-size:18pt;line-height:1.1;color:#a47d27;margin:0 0 4mm;font-weight:500}
.cover-descriptors{font-family:Georgia,"Times New Roman",serif;font-size:10.5pt;color:#17231f;margin:0;letter-spacing:.01em}
.cover-band{position:absolute;left:0;right:0;bottom:0;height:63mm;background:#022c1b;color:#fff;overflow:hidden;padding:9mm 16mm 8mm;box-sizing:border-box}
.cover-footer-art{position:absolute;left:0;right:0;bottom:0;width:210mm;height:auto;opacity:.72;z-index:0}.cover-band-content{position:relative;z-index:1;height:100%}
.cover-meta{display:flex;gap:0;align-items:flex-start}.cover-meta-block{padding:0 9mm 0 0;margin-right:9mm;min-width:31mm}.cover-meta-block:last-child{border-right:0;margin-right:0}.cover-meta-label{font-size:6.8pt;text-transform:uppercase;letter-spacing:.09em;color:#d7b35b;font-weight:700;margin-bottom:2mm}.cover-meta-value{font-family:Georgia,"Times New Roman",serif;font-size:15pt;color:#fff;line-height:1}
.cover-publisher{position:absolute;left:0;bottom:1mm}.cover-publisher strong{display:block;color:#d7b35b;font-size:11pt;letter-spacing:.07em;text-transform:uppercase}.cover-publisher span{font-size:8.5pt;color:#fff}
.publication-imprint{page:imprint;min-height:249mm;page-break-after:always;display:flex;flex-direction:column;color:#2a2a2a;font-family:Helvetica,Arial,sans-serif}.imprint-kicker{font-family:Helvetica,Arial,sans-serif;color:#022c1b;text-transform:uppercase;letter-spacing:.08em;font-size:7.5pt;font-weight:700;margin-bottom:4mm}.publication-imprint h1{font-family:Helvetica,Arial,sans-serif;color:#022c1b;font-size:22pt;font-weight:700;margin:0 0 9mm}.publication-meta{display:grid;grid-template-columns:42mm 1fr;gap:2.1mm 6mm;margin:0;font-family:Helvetica,Arial,sans-serif}.publication-meta dt{color:#6f6657}.publication-meta dd{margin:0;font-weight:600}.imprint-rule{height:.6pt;background:#b8943f;width:100%;margin:8mm 0 5mm}.publication-imprint>p{font-family:Helvetica,Arial,sans-serif}.reliance-notice{margin-top:auto;padding-top:4mm;border-top:.6pt solid #d8d5cc;font-family:Helvetica,Arial,sans-serif}.reliance-notice h2{font-family:Helvetica,Arial,sans-serif;font-size:9pt;font-weight:700;color:#022c1b;margin:0 0 2.5mm}.reliance-notice p{font-family:Helvetica,Arial,sans-serif;font-size:8.3pt;line-height:1.45;color:#504a40;margin:0}.publisher-block{margin-top:5mm;padding-top:4mm;border-top:.6pt solid #d8d5cc;font-family:Helvetica,Arial,sans-serif}.publisher-block h2{font-family:Helvetica,Arial,sans-serif;font-size:9pt;font-weight:700;color:#022c1b;margin:0 0 2.5mm}.publisher-block p{font-family:Helvetica,Arial,sans-serif;font-size:8.5pt;line-height:1.5;color:#504a40;margin:0}.publisher-block strong{color:#022c1b}
.contents{border:0;padding:0;page-break-after:always}.contents h1{font-family:Georgia,"Times New Roman",serif;font-size:22pt;color:#022c1b;font-weight:500}.contents h2{color:#022c1b}.contents a{color:#022c1b}
.family{page-break-before:always;border-top:0!important;padding-top:0!important;margin-top:0!important}.family>.hero{border:0;padding:0;margin:0 0 8mm}.family>.hero h1,.family>.hero h2{font-family:Georgia,"Times New Roman",serif;color:#022c1b;font-weight:500}.family>.hero .eyebrow{color:#022c1b}.card{break-inside:auto;border:1px solid #c8d1c8;border-radius:6px;padding:5mm;margin:0 0 5mm}.card h3{font-family:Georgia,"Times New Roman",serif;font-size:15pt;color:#022c1b;font-weight:500}.plain{background:#eef4e8!important;border-left:3pt solid #022c1b;border-radius:0!important}.invariant{background:#f6f4eb!important;border-left:2.2pt solid #022c1b!important}.grid{grid-template-columns:1fr 1fr;gap:4mm}.grid section{break-inside:avoid;background:#f6f4eb!important}.top{break-inside:avoid}.case-files{break-inside:auto}a{color:#022c1b;text-decoration:none}details{display:block}details>summary{list-style:none}details>*{display:block!important}
.chapter-opener{break-before:page;break-after:page}.chapter-opener h1{font-family:Georgia,"Times New Roman",serif;font-size:30pt;line-height:1.02;color:#022c1b;font-weight:500;margin:3mm 0 7mm;max-width:165mm}.chapter-kicker,.class-kicker{text-transform:uppercase;letter-spacing:.11em;font-size:8pt;font-weight:700;color:#b8943f;margin:0 0 3mm}.chapter-lead{background:#eef4e8!important;border-left:3pt solid #022c1b;padding:4mm 5mm;font-family:Georgia,"Times New Roman",serif;font-size:13pt;line-height:1.28;margin:0 0 4mm}.chapter-meta,.class-meta{font-size:8pt;color:#6f6657;margin:0 0 6mm}.chapter-opener h2,.chapter-map h2,.chapter-overview h2,.chapter-overview h3,.book-class h2,.book-class h3{font-family:Georgia,"Times New Roman",serif;color:#022c1b;font-weight:500}.chapter-opener h2{font-size:16pt;margin:5mm 0 2mm}.chapter-opener .grid h3{font-family:Helvetica,Arial,sans-serif;font-size:12pt;color:#171717;font-weight:700}.chapter-map{break-after:page}.chapter-map h2{font-size:23pt;margin:0 0 6mm}.chapter-map h3{font-size:13pt;color:#022c1b;margin:5mm 0 2mm}.chapter-overview{break-after:page}.chapter-overview h2{font-size:16pt;margin:5mm 0 2mm}.chapter-overview .grid h3{font-family:Helvetica,Arial,sans-serif;font-size:10pt;font-weight:700;color:#171717;margin:0 0 2mm}.chapter-list{list-style:none;padding:0;margin:3mm 0 7mm}.chapter-list li{display:grid;grid-template-columns:13mm 1fr 55mm;gap:3mm;border-bottom:.35pt solid #ddd8ca;padding:2.5mm 0;align-items:start}.chapter-item-number{font-weight:700;color:#b8943f}.chapter-item-title{font-weight:600}.chapter-item-id{font-size:7.4pt;color:#6f6657;text-align:right}.book-class{break-before:page}.class-title{font-size:23pt;line-height:1.08;margin:0 0 2mm}.class-meta{margin-bottom:4mm}.variant-parent{font-family:Georgia,"Times New Roman",serif;font-style:italic;color:#6f6657;margin:-1mm 0 4mm}.book-class>.plain{font-size:11pt;line-height:1.32;padding:4mm 5mm;margin:0 0 5mm}.book-class h3{font-size:13pt;margin:5mm 0 2mm}.book-class .grid h3{font-family:Helvetica,Arial,sans-serif;font-size:10pt;font-weight:700;color:#171717;margin:0 0 2mm}.criteria-grid{break-inside:avoid}.book-class ul{margin-top:1.5mm}.case-studies{margin-top:7mm}.case-studies>h4{font-family:Georgia,"Times New Roman",serif;font-size:15pt;color:#022c1b;font-weight:500;margin:0 0 3mm}.case-study{background:#eef4e8;border-left:3pt solid #022c1b;border-radius:2mm;padding:4mm 5mm;margin:0 0 4mm;break-inside:avoid}.case-study h5{font-family:Georgia,"Times New Roman",serif;font-size:11.5pt;line-height:1.2;color:#022c1b;margin:0 0 1.2mm}.case-study-meta{font-family:Helvetica,Arial,sans-serif;font-size:8pt;color:#6f6657;margin:0 0 3mm}.case-study-context{font-family:Helvetica,Arial,sans-serif;font-size:9.5pt;line-height:1.45;margin:0 0 3mm;color:#2f302d}.case-study-basis{font-family:Helvetica,Arial,sans-serif;font-size:9pt;line-height:1.4;margin:0;padding-top:3mm;border-top:.45pt solid #c7d5c9;color:#3f463f}.case-study-basis strong{color:#022c1b}.case-study-ref{font-family:Helvetica,Arial,sans-serif;font-size:7.5pt;color:#78716c;margin:3mm 0 0}.book-family code,.book-class code{font-size:.88em}.book-family+.book-family{border:0!important;padding:0!important;margin:0!important}
"""


def document(title: str, body: str, *, publication: bool = False) -> str:
    print_style = f"<style>{PRINT_STYLE}</style>" if publication else ""
    publication_class = " class=\"publication\"" if publication else ""
    return f"""<!doctype html>
<html lang="en"{publication_class}><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)}</title><style>{STYLE}</style>{print_style}</head><body><main>{body}</main></body></html>
"""


def html_family(data: dict, case_examples: dict[str, list[dict]] | None = None) -> str:
    return document(data["family"]["name"], family_html(data, case_examples=case_examples))


def load_catalogue(index_path: Path = INDEX) -> list[dict]:
    index = load(index_path)
    return [load(index_path.parent / item["file"]) for item in index["families"]]


def load_case_examples(path: Path = CASE_EXAMPLES) -> dict[str, list[dict]]:
    if not path.exists():
        return {}
    source = load(path)
    classes = source.get("classes", {})
    return classes if isinstance(classes, dict) else {}


def publication_frontmatter(index: dict, families: list[dict]) -> str:
    standard = index.get("standard", {})
    class_count = sum(len(data.get("classes", [])) for data in families)
    publication_date = standard.get("publication_date")
    try:
        parsed_date = date.fromisoformat(publication_date)
        edition_date = f"{parsed_date.day} {parsed_date.strftime('%B %Y')}"
        edition_year = str(parsed_date.year)
    except (TypeError, ValueError):
        edition_date = "Unspecified"
        edition_year = "Unspecified"
    version = standard.get("version", "Unversioned")
    status = standard.get("status", "Unspecified")
    return f"""
<section class="publication-frontmatter">
  <img class="cover-masthead" src="{esc(BRAND_HEADER_URL)}" alt="">
  <div class="cover-body">
    <h1 class="cover-title">Governance<br>Failure<br>Taxonomy</h1>
    <h2 class="cover-subtitle">Technical Reference</h2>
    <p class="cover-descriptors">Failure Families · Failure Classes<br>Classification Boundaries · Recognition Criteria</p>
  </div>
  <footer class="cover-band">
    <img class="cover-footer-art" src="{esc(BRAND_FOOTER_URL)}" alt="">
    <div class="cover-band-content">
      <div class="cover-meta">
        <div class="cover-meta-block"><div class="cover-meta-label">Version</div><div class="cover-meta-value">{esc(version)}</div></div>
        <div class="cover-meta-block"><div class="cover-meta-label">Publication date</div><div class="cover-meta-value">{esc(edition_date)}</div></div>
        <div class="cover-meta-block"><div class="cover-meta-label">Edition</div><div class="cover-meta-value">{esc(edition_year)}</div></div>
      </div>
      <div class="cover-publisher"><strong>CAM Initiative</strong><span>cam-initiative.org</span></div>
    </div>
  </footer>
</section>
<section class="publication-imprint">
  <p class="imprint-kicker">CAM Initiative · Technical Reference</p>
  <h1>Publication information</h1>
  <dl class="publication-meta">
    <dt>Title</dt><dd>Governance Failure Taxonomy</dd>
    <dt>Edition</dt><dd>Technical Reference</dd>
    <dt>Version</dt><dd>{esc(version)}</dd>
    <dt>Status</dt><dd>{esc(status).title()}</dd>
    <dt>Publication date</dt><dd>{esc(edition_date)}</dd>
    <dt>Failure families</dt><dd>{len(families)}</dd>
    <dt>Failure classes</dt><dd>{class_count}</dd>
  </dl>
  <div class="imprint-rule"></div>
  <p>This technical reference provides the maintained classification structure for governance failure families and failure classes, including classification boundaries and recognition criteria.</p>
  <section class="reliance-notice">
    <h2>Use and reliance notice</h2>
    <p>This report is provided for research and informational purposes. It does not constitute legal, regulatory, security, assurance, certification, risk, or other professional advice, and should not be relied upon as a substitute for independent assessment. Third parties remain responsible for verifying the cited source material, the current state of the underlying VIGIL Observatory records and taxonomy, the applicability of the analysis to their circumstances, and any decision or action taken in reliance on this report.</p>
  </section>
  <section class="publisher-block">
    <h2>Publisher</h2>
    <p><strong>CAM Initiative</strong><br>Business entity: Phoenix Covenant Pty Ltd<br>ABN 14 692 195 529<br>cam-initiative.org</p>
  </section>
</section>"""

def combined_html(families: list[dict], case_examples: dict[str, list[dict]] | None = None, *, publication: bool = False) -> str:
    index = load(INDEX)
    contents = ["<section class=\"contents\"><h1>Contents</h1><ol>"]
    for chapter_number, data in enumerate(families, start=1):
        family = data["family"]
        contents.append(f"<li><a href=\"#{esc(anchor(family['family_id']))}\"><strong>{chapter_number}. {esc(family['name'])}</strong></a><ul>")
        contents.extend(
            f"<li><a href=\"#{esc(anchor(item['class_id']))}\">{chapter_number}.{class_number} {esc(item['name'])}</a></li>"
            for class_number, item in enumerate(data["classes"], start=1)
        )
        contents.append("</ul></li>")
    contents.append("</ol></section>")
    frontmatter = publication_frontmatter(index, families) if publication else ""
    family_body = (
        "".join(publication_family_html(data, chapter_number, case_examples) for chapter_number, data in enumerate(families, start=1))
        if publication
        else "".join(family_html(d, 1, case_examples) for d in families)
    )
    return document(
        "Governance Failure Taxonomy — Technical Reference",
        frontmatter + "".join(contents) + family_body,
        publication=publication,
    )


def write_pdf(html_text: str, output: Path) -> None:
    # Stabilise embedded font timestamps so identical canonical input produces
    # byte-identical publication output. Callers may supply another fixed epoch.
    os.environ.setdefault("SOURCE_DATE_EPOCH", "0")
    try:
        from weasyprint import HTML
    except ImportError as exc:
        raise SystemExit(
            "PDF generation requires WeasyPrint. Install with `python -m pip install weasyprint`."
        ) from exc
    output.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=html_text, base_url=str(ROOT)).write_pdf(str(output))


def generate_catalogue(output_dir: Path, *, pdf: bool = False) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    families = load_catalogue()
    case_examples = load_case_examples()
    index = load(INDEX)
    for data in families:
        family_id = data["family"]["family_id"]
        entry = next(item for item in index["families"] if item["family_id"] == family_id)
        stem = Path(entry["file"]).stem
        (output_dir / f"{stem}.html").write_text(html_family(data, case_examples), encoding="utf-8")
    full_html = combined_html(families, case_examples)
    (output_dir / FULL_HTML_NAME).write_text(full_html, encoding="utf-8")
    if pdf:
        write_pdf(combined_html(families, case_examples, publication=True), output_dir / FULL_PDF_NAME)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--format", choices=("markdown", "html"))
    parser.add_argument("--output", type=Path)
    parser.add_argument("--catalogue", action="store_true", help="generate every family page and the full reference book")
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--pdf", action="store_true", help="also generate the full-reference PDF (requires WeasyPrint)")
    args = parser.parse_args()
    if args.catalogue:
        if args.input or args.format or args.output or not args.output_dir:
            parser.error("--catalogue requires --output-dir and no single-file arguments")
        generate_catalogue(args.output_dir, pdf=args.pdf)
        return
    if args.pdf:
        parser.error("--pdf is only supported with --catalogue")
    if not args.input or not args.format or not args.output:
        parser.error("single-family rendering requires input, --format and --output")
    data = load(args.input)
    rendered = markdown_family(data) if args.format == "markdown" else html_family(data, load_case_examples())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(rendered, encoding="utf-8")


if __name__ == "__main__":
    main()
