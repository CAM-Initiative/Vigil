#!/usr/bin/env python3
"""Render VIGIL taxonomy publications with Harm & Severity methodology and consolidated references."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import render_taxonomy as base


_original_combined_html = base.combined_html
REFERENCE_REGISTRY = base.ROOT.parent / "references" / "VIGIL.ObservatoryReferenceRegistry.json"
HARM_METHODOLOGIES = base.ROOT.parent / "methodologies"
HARM_PUBLICATION_TITLE = "VIGIL Harm & Severity Methodology"


def _text(value: object) -> str:
    return str(value or "").strip()


def _reference_key(reference: dict[str, Any]) -> str:
    url = _text(reference.get("url")).rstrip("/").lower()
    if url:
        return f"url:{url}|title:{_text(reference.get('title')).casefold()}"
    return "meta:" + "|".join(
        _text(reference.get(field)).casefold()
        for field in ("publisher", "title", "date")
    )


def _version_key(value: object) -> tuple[int, int, int]:
    match = re.match(r"^(\d+)\.(\d+)\.(\d+)", _text(value))
    return tuple(int(part) for part in match.groups()) if match else (0, 0, 0)


def load_harm_methodology() -> dict[str, Any]:
    candidates: list[dict[str, Any]] = []
    for path in sorted(HARM_METHODOLOGIES.glob("VIGIL.HarmImpactMatrix.v*.json")):
        candidates.append(json.loads(path.read_text(encoding="utf-8")))
    if not candidates:
        raise FileNotFoundError("No canonical VIGIL-HIM methodology document found")
    return max(candidates, key=lambda item: _version_key(item.get("version")))


def load_reference_registry() -> dict[str, dict[str, Any]]:
    source = json.loads(REFERENCE_REGISTRY.read_text(encoding="utf-8"))
    rows = source if isinstance(source, list) else source.get("references", [])
    return {
        _text(item.get("reference_id")): item
        for item in rows
        if isinstance(item, dict) and _text(item.get("reference_id"))
    }


def collect_external_references(families: list[dict]) -> list[dict[str, Any]]:
    """Collect class references once, retaining every class that cites each source."""
    collected: dict[str, dict[str, Any]] = {}
    order: list[str] = []

    for family_document in families:
        for failure_class in family_document.get("classes", []):
            if not isinstance(failure_class, dict):
                continue
            class_id = _text(failure_class.get("class_id"))
            class_name = _text(failure_class.get("name"))
            references = failure_class.get("external_references", [])
            if not isinstance(references, list):
                continue
            for reference in references:
                if not isinstance(reference, dict):
                    continue
                key = _reference_key(reference)
                if key not in collected:
                    collected[key] = {
                        "title": _text(reference.get("title")),
                        "publisher": _text(reference.get("publisher")),
                        "date": _text(reference.get("date")),
                        "url": _text(reference.get("url")),
                        "reference_role": _text(reference.get("reference_role")),
                        "classes": [],
                        "harm_severity_note": "",
                    }
                    order.append(key)
                support = {
                    "class_id": class_id,
                    "class_name": class_name,
                    "evidence_note": _text(reference.get("evidence_note")),
                }
                if class_id and support not in collected[key]["classes"]:
                    collected[key]["classes"].append(support)

    return [collected[key] for key in order]


def collect_publication_references(families: list[dict]) -> list[dict[str, Any]]:
    """Merge taxonomy references with the canonical Harm & Severity evidence base."""
    references = collect_external_references(families)
    collected = {_reference_key(reference): reference for reference in references}
    order = list(collected)

    matrix = load_harm_methodology()
    registry = load_reference_registry()
    for reference_id in matrix.get("reference_ids", []):
        reference = registry.get(_text(reference_id))
        if not reference:
            continue
        normalised = {
            "title": _text(reference.get("title")),
            "publisher": _text(reference.get("publisher")),
            "date": _text(reference.get("date")),
            "url": _text(reference.get("url")),
        }
        key = _reference_key(normalised)
        if key not in collected:
            collected[key] = {
                **normalised,
                "reference_role": _text(reference.get("reference_type")),
                "classes": [],
                "harm_severity_note": "",
            }
            order.append(key)
        collected[key]["harm_severity_note"] = _text(reference.get("use_note"))

    return [collected[key] for key in order]

def _criterion_html(value: object) -> str:
    rendered = base.esc(value)
    rendered = re.sub(
        r"(USD\s+[0-9][0-9,]*(?:\.[0-9]+)?(?:\s+(?:million|billion))?)",
        r"<strong>\1</strong>",
        rendered,
        flags=re.I,
    )
    rendered = re.sub(
        r"\b(Death|suicide|multiple grave casualties)\b",
        r"<strong>\1</strong>",
        rendered,
        flags=re.I,
    )
    return rendered


def harm_severity_html() -> str:
    matrix = load_harm_methodology()
    version = _text(matrix.get("version"))
    effective = base.publication_date(matrix.get("effective_on"))
    methodology_id = _text(matrix.get("methodology_id"))

    band_rows = "".join(
        f"<tr><th>{base.esc(band)}</th><td>{_criterion_html(meaning)}</td></tr>"
        for band, meaning in matrix.get("bands", {}).items()
    )
    status_rows = "".join(
        f"<tr><th>{base.esc(status.replace('-', ' ').title())}</th><td>{base.esc(meaning)}</td></tr>"
        for status, meaning in matrix.get("assessment_statuses", {}).items()
    )

    dimensions: list[str] = []
    for dimension in matrix.get("dimensions", []):
        threshold_rows = "".join(
            f"<tr><th>{base.esc(band)}</th><td>{_criterion_html(threshold.get('criterion', ''))}</td></tr>"
            for band, threshold in dimension.get("thresholds", {}).items()
        )
        adaptation = _text(dimension.get("adaptation_note"))
        dimensions.append(
            '<section class="harm-dimension">'
            f"<h2>{base.esc(dimension.get('label', ''))}</h2>"
            '<table class="harm-threshold-table"><thead><tr><th>Band</th><th>Criterion</th></tr></thead>'
            f"<tbody>{threshold_rows}</tbody></table>"
            + (f'<p class="harm-adaptation-note"><strong>Method note:</strong> {base.esc(adaptation)}</p>' if adaptation else "")
            + "</section>"
        )

    return (
        '<section class="harm-severity-methodology" id="harm-severity-methodology">'
        '<p class="chapter-kicker">Assessment methodology</p>'
        f"<h1>{base.esc(HARM_PUBLICATION_TITLE)}</h1>"
        f'<p class="harm-methodology-meta"><code>{base.esc(methodology_id)}</code> · Version {base.esc(version)} · Effective {base.esc(effective)}</p>'
        '<p class="harm-methodology-lead">VIGIL Incident severity records the highest supported materialised harm in a bounded occurrence. It is separate from Failure Taxonomy classification, likelihood, source prestige, workflow priority and hypothetical worst-case capability.</p>'
        "<h2>Derivation</h2>"
        f'<p class="harm-derivation">{base.esc(matrix.get("derivation_statement", ""))}</p>'
        "<h2>Severity bands</h2>"
        '<table class="harm-band-table"><thead><tr><th>Band</th><th>Canonical meaning</th></tr></thead>'
        f"<tbody>{band_rows}</tbody></table>"
        "<h2>Assessment statuses</h2>"
        '<table class="harm-status-table"><thead><tr><th>Status</th><th>Meaning</th></tr></thead>'
        f"<tbody>{status_rows}</tbody></table>"
        "<h2>Harm dimensions</h2>"
        '<p class="harm-methodology-intro">Each dimension is assessed independently against its S1–S5 criteria. Overall severity is the highest supported assessed band; dimensions are not averaged or summed. Methodological sources are consolidated in the References section.</p>'
        + "".join(dimensions)
        + "</section>"
    )


def bibliography_html(families: list[dict]) -> str:
    references = collect_publication_references(families)
    if not references:
        return ""

    matrix = load_harm_methodology()
    harm_label = f"{HARM_PUBLICATION_TITLE} {matrix.get('version', '')}".strip()
    entries: list[str] = []
    for index, reference in enumerate(references, start=1):
        publisher = base.esc(reference["publisher"])
        title = base.esc(reference["title"])
        date = base.esc(reference["date"])
        url = _text(reference["url"])
        role = _text(reference["reference_role"])
        parts = [part for part in (publisher, f"<em>{title}</em>" if title else "", date) if part]
        citation = ". ".join(parts)
        if citation and not citation.endswith("."):
            citation += "."
        if url:
            citation += f' <a href="{base.esc(url)}">{base.esc(url)}</a>'

        supports = "".join(
            '<li class="bibliography-support-item">'
            f"<p><code>{base.esc(item['class_id'])}</code> — {base.esc(item['class_name'])}</p>"
            + (
                f'<p class="bibliography-evidence-note">{base.esc(item["evidence_note"])}</p>'
                if item["evidence_note"]
                else ""
            )
            + "</li>"
            for item in reference["classes"]
        )
        if reference.get("harm_severity_note"):
            supports += (
                '<li class="bibliography-support-item">'
                f"<p><strong>{base.esc(harm_label)}</strong></p>"
                f'<p class="bibliography-evidence-note">{base.esc(reference["harm_severity_note"])}</p>'
                "</li>"
            )
        role_html = f'<span class="bibliography-role">{base.esc(base.label(role.replace("-", "_")))}</span>' if role else ""
        entries.append(
            '<li class="bibliography-entry">'
            f'<span class="bibliography-number">[{index}]</span>'
            f'<div><p class="bibliography-citation">{citation}</p>'
            + (f'<p class="bibliography-support-label"><strong>Supports:</strong></p><ul class="bibliography-support">{supports}</ul>' if supports else "")
            + role_html
            + "</div></li>"
        )

    return (
        '<section class="taxonomy-bibliography" id="taxonomy-bibliography">'
        '<p class="chapter-kicker">Evidence base</p>'
        '<h1>References</h1>'
        '<p class="bibliography-intro">External sources supporting VIGIL failure-class definitions and the Harm &amp; Severity Methodology. Incident-specific evidence remains cited within the relevant Case Studies.</p>'
        f'<ol>{"".join(entries)}</ol>'
        "</section>"
    )


def _inject_before_main_close(html_text: str, addition: str) -> str:
    if not addition:
        return html_text
    return re.sub(r"</main>", addition + "</main>", html_text, count=1)


def combined_html(
    families: list[dict],
    case_examples: dict[str, list[dict]] | None = None,
    *,
    publication: bool = False,
) -> str:
    rendered = _original_combined_html(families, case_examples, publication=publication)
    if not publication:
        return _inject_before_main_close(rendered, bibliography_html(families))
    return _inject_before_main_close(
        rendered,
        harm_severity_html() + bibliography_html(families),
    )


base.combined_html = combined_html
base.STYLE += """
.harm-severity-methodology,.taxonomy-bibliography{background:#fff;border:1px solid #d6d3d1;border-radius:16px;padding:26px;margin-top:52px}
.harm-severity-methodology h1,.taxonomy-bibliography h1{color:#022c1b}
.harm-severity-methodology table{width:100%;border-collapse:collapse;margin:12px 0 22px}.harm-severity-methodology th,.harm-severity-methodology td{border-top:1px solid #e7e5e4;padding:9px;text-align:left;vertical-align:top}.harm-severity-methodology th{color:#022c1b}
.taxonomy-bibliography ol{list-style:none;padding:0;margin:20px 0 0}
.bibliography-entry{display:grid;grid-template-columns:3rem 1fr;gap:.75rem;border-top:1px solid #e7e5e4;padding:14px 0}
.bibliography-number{font-weight:700;color:#a47d27}.bibliography-citation,.bibliography-support-label{margin:0}.bibliography-support-label{margin-top:6px;color:#57534e;font-size:.9em}.bibliography-support{list-style:none;padding:0;margin:2px 0 0;color:#57534e;font-size:.9em}.bibliography-support-item{margin-top:5px}.bibliography-support-item p{margin:0}.bibliography-evidence-note{margin-top:2px!important;color:#78716c}.bibliography-role{display:inline-block;margin-top:6px;color:#78716c;font-size:.75em;text-transform:uppercase;letter-spacing:.06em}
"""
base.PRINT_STYLE += """
.book-class{break-before:auto;margin-top:10mm}
.book-class>.class-kicker,.book-class>.class-title,.book-class>.class-meta{break-after:avoid}
.book-class .criteria-grid{display:block;break-inside:auto}
.book-class .criteria-grid section{break-inside:auto;margin-bottom:4mm}
.book-class .invariant-exemplars>h3{break-after:avoid}
.book-class .invariant-exemplar{break-inside:avoid}
.book-class .invariant-exemplar>h4{break-after:avoid}
.book-class .case-studies>h4{break-after:avoid}
.harm-severity-methodology{break-before:page;page-break-before:always;margin:0;padding:0;border:0;border-radius:0}
.harm-severity-methodology>h1{font-family:Georgia,"Times New Roman",serif;font-size:24pt;line-height:1.08;color:#022c1b;font-weight:500;margin:0 0 3mm}
.harm-methodology-meta{font-family:Helvetica,Arial,sans-serif;font-size:8.5pt;color:#6f6657;margin:0 0 5mm}.harm-methodology-lead{font-family:Georgia,"Times New Roman",serif;font-size:11pt;line-height:1.4;color:#2f302d;margin:0 0 6mm}
.harm-severity-methodology>h2,.harm-dimension h2{font-family:Georgia,"Times New Roman",serif;color:#022c1b;font-weight:500}.harm-severity-methodology>h2{font-size:16pt;margin:6mm 0 2mm}.harm-dimension h2{font-size:14pt;margin:6mm 0 2mm}
.harm-derivation,.harm-methodology-intro,.harm-adaptation-note{font-family:Helvetica,Arial,sans-serif;font-size:9.5pt;line-height:1.48;color:#504a40}.harm-adaptation-note{margin:2mm 0 0}.harm-dimension{break-inside:avoid;margin-top:5mm}
.harm-severity-methodology table{width:100%;border-collapse:collapse;margin:0 0 5mm}.harm-severity-methodology th,.harm-severity-methodology td{font-family:Helvetica,Arial,sans-serif;font-size:9pt;line-height:1.42;text-align:left;vertical-align:top;border-top:.35pt solid #ddd8ca;padding:2.4mm 2mm}.harm-severity-methodology th{width:18mm;color:#022c1b;font-weight:700}.harm-severity-methodology thead th{font-size:8pt;text-transform:uppercase;letter-spacing:.05em;color:#6f6657;border-top:0;border-bottom:.6pt solid #b8943f}
.taxonomy-bibliography{break-before:page;page-break-before:always;margin:0;padding:0;border:0;border-radius:0}
.taxonomy-bibliography h1{font-family:Georgia,"Times New Roman",serif;font-size:24pt;line-height:1.08;color:#022c1b;font-weight:500;margin:0 0 4mm}
.bibliography-intro{font-size:9.5pt;line-height:1.48;color:#504a40;margin:0 0 6mm;max-width:165mm}
.taxonomy-bibliography ol{list-style:none;padding:0;margin:0}
.bibliography-entry{display:grid;grid-template-columns:10mm 1fr;gap:2mm;break-inside:avoid;border-top:.35pt solid #ddd8ca;padding:3mm 0}
.bibliography-number{font-family:Helvetica,Arial,sans-serif;font-size:8pt;color:#b8943f;font-weight:700}
.bibliography-citation{font-family:Helvetica,Arial,sans-serif;font-size:8.7pt;line-height:1.45;margin:0;color:#2f302d;overflow-wrap:anywhere}
.bibliography-support-label{font-family:Helvetica,Arial,sans-serif;font-size:7.8pt;line-height:1.4;margin:1.5mm 0 0;color:#6f6657}.bibliography-support{list-style:none;padding:0;font-family:Helvetica,Arial,sans-serif;font-size:7.8pt;line-height:1.4;margin:.5mm 0 0;color:#6f6657}.bibliography-support-item{margin-top:1.4mm}.bibliography-support-item p{margin:0}.bibliography-evidence-note{margin-top:.5mm!important;color:#756f67}
.bibliography-role{display:inline-block;margin-top:1.5mm;font-family:Helvetica,Arial,sans-serif;font-size:6.8pt;text-transform:uppercase;letter-spacing:.07em;color:#6f6657}
"""


if __name__ == "__main__":
    base.main()
