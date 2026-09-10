#!/usr/bin/env python3
"""Render VIGIL taxonomy publications with one consolidated class-reference bibliography.

Failure-class external references remain canonical in family JSON. This wrapper augments only
full-catalogue outputs: individual family pages remain unchanged, while the complete HTML and
maintained PDF receive a deterministic, de-duplicated bibliography at the end.
"""

from __future__ import annotations

import re
from typing import Any

import render_taxonomy as base


_original_combined_html = base.combined_html


def _text(value: object) -> str:
    return str(value or "").strip()


def _reference_key(reference: dict[str, Any]) -> str:
    url = _text(reference.get("url")).rstrip("/").lower()
    if url:
        return f"url:{url}"
    return "meta:" + "|".join(
        _text(reference.get(field)).casefold()
        for field in ("publisher", "title", "date")
    )


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
                    }
                    order.append(key)
                support = {"class_id": class_id, "class_name": class_name}
                if class_id and support not in collected[key]["classes"]:
                    collected[key]["classes"].append(support)

    return [collected[key] for key in order]


def bibliography_html(families: list[dict]) -> str:
    references = collect_external_references(families)
    if not references:
        return ""

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

        supports = ", ".join(
            f"<code>{base.esc(item['class_id'])}</code> — {base.esc(item['class_name'])}"
            for item in reference["classes"]
        )
        role_html = f'<span class="bibliography-role">{base.esc(base.label(role))}</span>' if role else ""
        entries.append(
            '<li class="bibliography-entry">'
            f'<span class="bibliography-number">[{index}]</span>'
            f'<div><p class="bibliography-citation">{citation}</p>'
            + (f'<p class="bibliography-support"><strong>Supports:</strong> {supports}</p>' if supports else "")
            + role_html
            + "</div></li>"
        )

    return (
        '<section class="taxonomy-bibliography" id="taxonomy-bibliography">'
        '<p class="chapter-kicker">Taxonomy evidence</p>'
        '<h1>References</h1>'
        '<p class="bibliography-intro">External sources supporting the definition, boundary, or recognition criteria of VIGIL failure classes. Incident-specific evidence remains cited within the relevant Case Studies.</p>'
        f'<ol>{"".join(entries)}</ol>'
        '</section>'
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
    return _inject_before_main_close(rendered, bibliography_html(families))


# base.generate_catalogue and base.main resolve this module-global function in render_taxonomy;
# replace it before delegating so every full-catalogue render uses the bibliography projection.
base.combined_html = combined_html
base.STYLE += """
.taxonomy-bibliography{background:#fff;border:1px solid #d6d3d1;border-radius:16px;padding:26px;margin-top:52px}
.taxonomy-bibliography h1{color:#022c1b}.taxonomy-bibliography ol{list-style:none;padding:0;margin:20px 0 0}
.bibliography-entry{display:grid;grid-template-columns:3rem 1fr;gap:.75rem;border-top:1px solid #e7e5e4;padding:14px 0}
.bibliography-number{font-weight:700;color:#a47d27}.bibliography-citation,.bibliography-support{margin:0}.bibliography-support{margin-top:6px;color:#57534e;font-size:.9em}.bibliography-role{display:inline-block;margin-top:6px;color:#78716c;font-size:.75em;text-transform:uppercase;letter-spacing:.06em}
"""
base.PRINT_STYLE += """
.taxonomy-bibliography{break-before:page;page-break-before:always;margin:0;padding:0;border:0;border-radius:0}
.taxonomy-bibliography h1{font-family:Georgia,\"Times New Roman\",serif;font-size:24pt;line-height:1.08;color:#022c1b;font-weight:500;margin:0 0 4mm}
.bibliography-intro{font-size:9pt;line-height:1.45;color:#504a40;margin:0 0 6mm;max-width:165mm}
.taxonomy-bibliography ol{list-style:none;padding:0;margin:0}
.bibliography-entry{display:grid;grid-template-columns:10mm 1fr;gap:2mm;break-inside:avoid;border-top:.35pt solid #ddd8ca;padding:3mm 0}
.bibliography-number{font-family:Helvetica,Arial,sans-serif;font-size:8pt;color:#b8943f;font-weight:700}
.bibliography-citation{font-family:Helvetica,Arial,sans-serif;font-size:8.7pt;line-height:1.45;margin:0;color:#2f302d;overflow-wrap:anywhere}
.bibliography-support{font-family:Helvetica,Arial,sans-serif;font-size:7.8pt;line-height:1.4;margin:1.5mm 0 0;color:#6f6657}
.bibliography-role{display:inline-block;margin-top:1.5mm;font-family:Helvetica,Arial,sans-serif;font-size:6.8pt;text-transform:uppercase;letter-spacing:.07em;color:#6f6657}
"""


if __name__ == "__main__":
    base.main()
