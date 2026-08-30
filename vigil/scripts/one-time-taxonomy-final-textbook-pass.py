#!/usr/bin/env python3
"""Apply the approved final textbook information-architecture pass once."""
from pathlib import Path
import re

PATH = Path("vigil/taxonomy/render_taxonomy.py")
text = PATH.read_text(encoding="utf-8")

# --- Case Study context: preserve primary external source URL and ranking quality. ---
old_context_tail = '''    return {
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
new_context_tail = '''    source_url = ""
    source_quality = -999
    if evidence_source:
        source_url = str(evidence_source.get("source_url") or evidence_source.get("archive_url") or "").strip()
        source_quality = _source_quality(evidence_source)
    vendor_key = "|".join(vendors) if vendors else str(system_context.get("platform_or_vendor") or "").strip().lower()
    return {
        "system_label": system_label,
        "vendor_key": vendor_key,
        "date": publication_date(source_date),
        "source_date": str(source_date or ""),
        "source_publisher": source_label,
        "source_title": source_title,
        "source_url": source_url,
        "source_quality": source_quality,
        "case_context": case_context,
        "severity": severity,
        "vendor_known": vendor_known,
    }
'''
if old_context_tail not in text:
    raise SystemExit("Case Study context return block not found")
text = text.replace(old_context_tail, new_context_tail, 1)

# --- Selection: up to three high-confidence, known-vendor exemplars PER class. ---
selection_start = text.index("def _candidate_rank(candidate: dict)")
selection_end = text.index("\ndef case_examples_html", selection_start)
new_selection = r'''def _candidate_rank(candidate: dict) -> tuple[int, int, int, int, str]:
    """Publication ranking: primary mapping, severity, recency, then source quality."""
    return (
        candidate["role_rank"],
        _severity_rank(candidate["context"].get("severity")),
        -_case_date(candidate["context"].get("source_date")).toordinal(),
        -int(candidate["context"].get("source_quality", -999)),
        str(candidate["example"].get("failure_mode_id", "")),
    )


def select_class_case_examples(data: dict, case_examples: dict[str, list[dict]]) -> dict[str, list[dict]]:
    """Select up to three publication-grade exemplars for every failure class.

    Eligibility gates are intentionally stricter than the underlying VIGIL corpus:
    taxonomy mapping confidence must be High and an affected vendor/system must be known.
    Within each class, primary mappings rank before secondary mappings, followed by
    severity, newest substantive evidence publication date and evidence-source quality.
    A first pass favours different affected-system/vendor contexts before filling any
    remaining slots from the next-best qualifying cases.
    """
    selected: dict[str, list[dict]] = {}
    for item in data.get("classes", []):
        class_id = str(item.get("class_id", ""))
        candidates: list[dict] = []
        seen_failure_modes: set[str] = set()
        for example in case_examples.get(class_id, []):
            if str(example.get("classification_confidence", "")).lower() != "high":
                continue
            failure_mode_id = str(example.get("failure_mode_id", ""))
            if not failure_mode_id or failure_mode_id in seen_failure_modes:
                continue
            context = case_study_context(example)
            if not context.get("vendor_known"):
                continue
            seen_failure_modes.add(failure_mode_id)
            candidates.append({
                "example": example,
                "context": context,
                "role_rank": 0 if str(example.get("classification_role", "primary")).lower() == "primary" else 1,
            })

        candidates.sort(key=_candidate_rank)
        chosen: list[dict] = []
        used_vendor_keys: set[str] = set()

        # First pass: favour diversity of affected-system/vendor context.
        for candidate in candidates:
            vendor_key = str(candidate["context"].get("vendor_key") or candidate["context"].get("system_label") or "")
            if vendor_key and vendor_key in used_vendor_keys:
                continue
            chosen.append(candidate)
            if vendor_key:
                used_vendor_keys.add(vendor_key)
            if len(chosen) == 3:
                break

        # Second pass: fill unused slots from the remaining best-ranked cases.
        if len(chosen) < 3:
            chosen_ids = {str(candidate["example"].get("failure_mode_id", "")) for candidate in chosen}
            for candidate in candidates:
                failure_mode_id = str(candidate["example"].get("failure_mode_id", ""))
                if failure_mode_id in chosen_ids:
                    continue
                chosen.append(candidate)
                chosen_ids.add(failure_mode_id)
                if len(chosen) == 3:
                    break

        if chosen:
            selected[class_id] = [candidate["example"] for candidate in chosen]
    return selected

'''
text = text[:selection_start] + new_selection + text[selection_end:]

# --- Case Study rendering: visible/clickable primary source URL. ---
case_start = text.index("def case_examples_html(examples: list[dict]) -> str:")
case_end = text.index("\ndef publication_class_html", case_start)
new_case_html = r'''def case_examples_html(examples: list[dict]) -> str:
    if not examples:
        return ""
    studies = []
    for example in examples:
        basis = str(example.get("classification_basis", "")).strip()
        context = case_study_context(example)
        meta_parts = []
        if context.get("system_label"):
            meta_parts.append(str(context["system_label"]))
        if context.get("date"):
            meta_parts.append(str(context["date"]))
        meta = " · ".join(esc(value) for value in meta_parts if value)
        case_context = str(context.get("case_context") or "").strip()
        source_title = str(context.get("source_title") or context.get("source_publisher") or "Primary evidence source").strip()
        source_publisher = str(context.get("source_publisher") or "").strip()
        source_url = str(context.get("source_url") or "").strip()
        source_label = source_title
        if source_publisher and source_publisher.lower() not in source_title.lower():
            source_label = f"{source_title} — {source_publisher}"
        source_html = ""
        if source_url:
            source_html = (
                "<p class=\"case-study-source\"><strong>Source:</strong> "
                f"{esc(source_label)}<br><a href=\"{esc(source_url)}\">{esc(source_url)}</a></p>"
            )
        elif source_label:
            source_html = f"<p class=\"case-study-source\"><strong>Source:</strong> {esc(source_label)}</p>"
        studies.append(
            "<article class=\"case-study\">"
            f"<h5>{esc(example.get('title', ''))}</h5>"
            + (f"<p class=\"case-study-meta\">{meta}</p>" if meta else "")
            + (f"<p class=\"case-study-context\">{esc(case_context)}</p>" if case_context else "")
            + (f"<p class=\"case-study-basis\"><strong>Relevance to this class:</strong> {esc(basis)}</p>" if basis else "")
            + source_html
            + f"<p class=\"case-study-ref\"><strong>VIGIL record:</strong> <code>{esc(example.get('failure_mode_id', ''))}</code></p>"
            + "</article>"
        )
    heading = "Case Study" if len(studies) == 1 else "Case Studies"
    return f"<section class=\"case-studies\"><h4>{heading}</h4>" + "".join(studies) + "</section>"

'''
text = text[:case_start] + new_case_html + text[case_end:]

# --- Chapter structure: integrate title + chapter outline, remove Scope and standalone opener. ---
family_start = text.index("def publication_family_html(data: dict, chapter_number: int")
family_end = text.index("\ndef class_html", family_start)
new_family = r'''def publication_family_html(data: dict, chapter_number: int, case_examples: dict[str, list[dict]] | None = None) -> str:
    family = data["family"]
    chapter_rows = []
    class_lookup: dict[str, tuple[str, str]] = {}
    for index, item in enumerate(data["classes"], start=1):
        number = f"{chapter_number}.{index}"
        class_lookup[item["class_id"]] = (number, item["name"])
        suffix = " · Variant" if str(item.get("abstraction", "")).lower() == "variant" else ""
        chapter_rows.append(
            f"<li><span class=\"chapter-item-number\">{esc(number)}</span>"
            f"<span class=\"chapter-item-title\">{esc(item['name'])}</span>"
            f"<span class=\"chapter-item-id\"><code>{esc(item['class_id'])}</code>{suffix}</span></li>"
        )
    aliases = " · ".join(f"<code>{esc(x)}</code>" for x in family.get("aliases", []))
    alias_html = f"<p class=\"chapter-aliases\"><strong>Prior codes and aliases:</strong> {aliases}</p>" if aliases else ""
    selected_case_examples = select_class_case_examples(data, case_examples or {})
    classes = "".join(
        publication_class_html(
            item,
            f"{chapter_number}.{index}",
            class_lookup,
            selected_case_examples.get(item["class_id"], []),
        )
        for index, item in enumerate(data["classes"], start=1)
    )
    return f"""
<section class="book-family" id="{esc(anchor(family['family_id']))}">
  <section class="chapter-opener">
    <p class="chapter-kicker">Chapter {chapter_number}</p>
    <h1>{esc(family['name'])}</h1>
    <p class="chapter-lead">{esc(family['plain_english'])}</p>
    <p class="chapter-meta"><code>{esc(family['family_id'])}</code> · <code>{esc(family['family_code'])}</code> · Version {esc(family['version'])} · {esc(str(family['status']).title())}</p>
    <h2 class="chapter-outline-title">In this chapter</h2>
    <ol class="chapter-list">{''.join(chapter_rows)}</ol>
    {alias_html}
  </section>
  <section class="chapter-overview">
    <p class="chapter-kicker">Chapter {chapter_number} · Failure family overview</p>
    <h2>Technical definition</h2><p>{esc(family['definition'])}</p>
    <h2>Governing invariant</h2><p class="invariant">{esc(family['invariant'])}</p>
    <h2>Classification boundary</h2><div class="grid"><section><h3>Include when</h3><p>{esc(family['inclusion_rule'])}</p></section><section><h3>Exclude when</h3><p>{esc(family['exclusion_rule'])}</p></section></div>
  </section>{classes}
</section>"""

'''
text = text[:family_start] + new_family + text[family_end:]

# --- Publication information: institutional publisher + reviewer + AI disclosure. ---
old_publisher = '''  <section class="publisher-block">
    <h2>Publisher</h2>
    <p><strong>CAM Initiative</strong><br>Business entity: Phoenix Covenant Pty Ltd<br>ABN 14 692 195 529<br>cam-initiative.org</p>
  </section>
'''
new_publisher = '''  <section class="publisher-block">
    <h2>Publisher</h2>
    <p><strong>CAM Initiative</strong><br>Phoenix Covenant Pty Ltd · ABN 14 692 195 529<br>Reviewer: Dr M.V. O'Rourke<br>cam-initiative.org</p>
    <p class="ai-disclosure"><strong>Generative AI disclosure.</strong> This publication was prepared with the assistance of generative AI tools for research, synthesis and drafting. The reviewer has reviewed the substantive claims, references and classifications and accepts responsibility for the accuracy and content of the text. Where generative AI is used in the preparation or maintenance of VIGIL data, the specific model used is captured in the applicable metadata records.</p>
  </section>
'''
if old_publisher not in text:
    raise SystemExit("Publisher block not found")
text = text.replace(old_publisher, new_publisher, 1)

# --- Main Contents: nine failure families only, linked with generated PDF page numbers. ---
contents_start = text.index("def combined_html(families: list[dict]")
contents_end = text.index("\ndef write_pdf", contents_start)
new_combined = r'''def combined_html(families: list[dict], case_examples: dict[str, list[dict]] | None = None, *, publication: bool = False) -> str:
    index = load(INDEX)
    if publication:
        contents = ["<section class=\"contents book-contents\"><h1>Contents</h1><ol>"]
        for chapter_number, data in enumerate(families, start=1):
            family = data["family"]
            contents.append(
                f"<li><a href=\"#{esc(anchor(family['family_id']))}\">"
                f"<span class=\"contents-chapter-number\">{chapter_number}</span>"
                f"<span class=\"contents-family-title\">{esc(family['name'])}</span>"
                "<span class=\"contents-leader\"></span></a></li>"
            )
        contents.append("</ol></section>")
    else:
        contents = ["<section class=\"contents\"><h1>Contents</h1><ol>"]
        for chapter_number, data in enumerate(families, start=1):
            family = data["family"]
            contents.append(f"<li><a href=\"#{esc(anchor(family['family_id']))}\"><strong>{esc(family['name'])}</strong></a><ul>")
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

'''
text = text[:contents_start] + new_combined + text[contents_end:]

# --- Print CSS refinements. ---
text = text.replace(
    '.publisher-block p{font-family:Helvetica,Arial,sans-serif;font-size:8.5pt;line-height:1.5;color:#504a40;margin:0}.publisher-block strong{color:#022c1b}',
    '.publisher-block p{font-family:Helvetica,Arial,sans-serif;font-size:8.5pt;line-height:1.5;color:#504a40;margin:0}.publisher-block strong{color:#022c1b}.publisher-block .ai-disclosure{margin-top:3mm;font-size:8pt;line-height:1.42;color:#504a40}'
)
old_contents_css = '.contents{border:0;padding:0;page-break-after:always}.contents h1{font-family:Georgia,"Times New Roman",serif;font-size:22pt;color:#022c1b;font-weight:500}.contents h2{color:#022c1b}.contents a{color:#022c1b}'
new_contents_css = '.contents{border:0;padding:0;page-break-after:always}.contents h1{font-family:Georgia,"Times New Roman",serif;font-size:22pt;color:#022c1b;font-weight:500}.contents h2{color:#022c1b}.contents a{color:#022c1b}.book-contents ol{list-style:none;padding:0;margin:9mm 0 0}.book-contents li{margin:0 0 4.5mm}.book-contents a{display:flex;align-items:baseline;gap:3mm;text-decoration:none}.contents-chapter-number{font-family:Helvetica,Arial,sans-serif;font-weight:700;color:#b8943f;width:8mm}.contents-family-title{font-family:Georgia,"Times New Roman",serif;font-size:12.5pt;color:#022c1b}.contents-leader{flex:1;border-bottom:.5pt dotted #b9b4a9;transform:translateY(-1.5mm);min-width:8mm}.book-contents a::after{content:target-counter(attr(href), page);font-family:Helvetica,Arial,sans-serif;font-size:9pt;color:#6f6657;margin-left:1mm}'
if old_contents_css not in text:
    raise SystemExit("Contents CSS block not found")
text = text.replace(old_contents_css, new_contents_css, 1)

# Merge opener and outline styling; remove obsolete chapter-map references.
text = text.replace('.chapter-opener{break-before:page;break-after:page}', '.chapter-opener{break-before:page;break-after:page}')
text = text.replace('.chapter-opener h2,.chapter-map h2,.chapter-overview h2,.chapter-overview h3,.book-class h2,.book-class h3', '.chapter-opener h2,.chapter-overview h2,.chapter-overview h3,.book-class h2,.book-class h3')
text = re.sub(r'\.chapter-map\{break-after:page\}\.chapter-map h2\{[^}]*\}\.chapter-map h3\{[^}]*\}', '', text, count=1)
text = text.replace('.chapter-opener h2{font-size:16pt;margin:5mm 0 2mm}', '.chapter-opener h2{font-size:16pt;margin:5mm 0 2mm}.chapter-outline-title{font-family:Helvetica,Arial,sans-serif!important;font-size:13pt!important;font-weight:700!important;margin:7mm 0 2mm!important}.chapter-aliases{font-size:7.8pt;color:#6f6657;margin:4mm 0 0}')

# Case Study visible source line.
text = text.replace(
    '.case-study-basis strong{color:#022c1b}.case-study-ref{font-family:Helvetica,Arial,sans-serif;font-size:7.5pt;color:#78716c;margin:3mm 0 0}',
    '.case-study-basis strong{color:#022c1b}.case-study-source{font-family:Helvetica,Arial,sans-serif;font-size:8pt;line-height:1.35;margin:3mm 0 0;color:#504a40;overflow-wrap:anywhere}.case-study-source strong{color:#022c1b}.case-study-source a{color:#315f50;text-decoration:underline;overflow-wrap:anywhere}.case-study-ref{font-family:Helvetica,Arial,sans-serif;font-size:7.5pt;color:#78716c;margin:3mm 0 0}'
)

PATH.write_text(text, encoding="utf-8")
print("Applied final textbook information architecture, case-study coverage and publisher disclosure pass")
