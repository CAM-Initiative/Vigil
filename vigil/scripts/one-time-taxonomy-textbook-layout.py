#!/usr/bin/env python3
from pathlib import Path

path = Path("vigil/taxonomy/render_taxonomy.py")
text = path.read_text(encoding="utf-8")

old = 'CASE_EXAMPLES = ROOT / "generated" / "VIGIL.FailureTaxonomy.CaseFileExamples.json"\n'
new = old + 'FAILURE_RECORDS = ROOT.parent / "records" / "failures" / "2026"\n'
if text.count(old) != 1:
    raise SystemExit(f"Refusing constant patch: {text.count(old)} anchors")
text = text.replace(old, new, 1)

start = text.index("def case_examples_html(examples: list[dict]) -> str:\n")
end = text.index("\ndef class_html(item: dict, case_examples: list[dict] | None = None) -> str:\n", start)
replacement = r'''def publication_date(value: object) -> str:
    if not value:
        return ""
    try:
        parsed = date.fromisoformat(str(value))
        return f"{parsed.day} {parsed.strftime('%B %Y')}"
    except ValueError:
        return str(value)


def case_study_context(example: dict) -> dict[str, str]:
    failure_mode_id = str(example.get("failure_mode_id", ""))
    if not failure_mode_id:
        return {}
    record_path = FAILURE_RECORDS / f"{failure_mode_id}.json"
    if not record_path.exists():
        return {}
    record = load(record_path)
    system_context = record.get("system_context") if isinstance(record.get("system_context"), dict) else {}
    identity = record.get("record_identity") if isinstance(record.get("record_identity"), dict) else {}
    provider = str(system_context.get("platform_or_vendor") or "").strip()
    if not provider:
        vendors = system_context.get("evidenced_vendors")
        if isinstance(vendors, list) and vendors:
            provider = str(vendors[0]).strip()
    product = str(system_context.get("product_or_service") or "").strip()
    if not product:
        products = system_context.get("evidenced_products_or_services")
        if isinstance(products, list) and products:
            product = str(products[0]).strip()
    recorded = record.get("date_recorded") or identity.get("created")
    return {"provider": provider, "product": product, "date": publication_date(recorded)}


def case_examples_html(examples: list[dict]) -> str:
    if not examples:
        return ""
    studies = []
    for example in examples:
        role = str(example.get("classification_role", "primary")).title()
        confidence = str(example.get("classification_confidence", "unknown")).title()
        basis = str(example.get("classification_basis", "")).strip()
        context = case_study_context(example)
        meta = " · ".join(esc(value) for value in (context.get("provider"), context.get("product"), context.get("date")) if value)
        studies.append(
            "<article class=\"case-study\">"
            f"<h5>{esc(example.get('title', ''))}</h5>"
            + (f"<p class=\"case-study-meta\">{meta}</p>" if meta else "")
            + (f"<p class=\"case-study-what\"><strong>What happened</strong><br>{esc(basis)}</p>" if basis else "")
            + f"<p class=\"case-study-ref\"><code>{esc(example.get('failure_mode_id', ''))}</code> · {esc(role)} classification · {esc(confidence)} confidence</p>"
            + "</article>"
        )
    return "<section class=\"case-studies\"><h4>Case Studies</h4>" + "".join(studies) + "</section>"


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
    classes = "".join(publication_class_html(item, f"{chapter_number}.{index}", class_lookup, (case_examples or {}).get(item["class_id"], [])) for index, item in enumerate(data["classes"], start=1))
    return f"""
<section class="book-family" id="{esc(anchor(family['family_id']))}">
  <section class="chapter-opener">
    <p class="chapter-kicker">Chapter {chapter_number}</p><h1>{esc(family['name'])}</h1>
    <p class="chapter-lead">{esc(family['plain_english'])}</p>
    <p class="chapter-meta"><code>{esc(family['family_id'])}</code> · <code>{esc(family['family_code'])}</code> · Version {esc(family['version'])} · {esc(str(family['status']).title())}</p>
    <h2>Technical definition</h2><p>{esc(family['definition'])}</p>
    <h2>Governing invariant</h2><p class="invariant">{esc(family['invariant'])}</p>
    <h2>Classification boundary</h2><div class="grid"><section><h3>Include when</h3><p>{esc(family['inclusion_rule'])}</p></section><section><h3>Exclude when</h3><p>{esc(family['exclusion_rule'])}</p></section></div>
  </section>
  <section class="chapter-map">
    <p class="chapter-kicker">Chapter {chapter_number}</p><h2>Scope &amp; chapter map</h2>
    <h3>Scope</h3><ul>{scope}</ul>
    <h3>In this chapter</h3><p class="chapter-map-note">Publication numbering is navigational only. Immutable VIGIL identifiers remain authoritative.</p>
    <ol class="chapter-list">{''.join(chapter_rows)}</ol>
    <h3>Reference metadata</h3><p><strong>Failure family:</strong> <code>{esc(family['family_id'])}</code><br><strong>Semantic code:</strong> <code>{esc(family['family_code'])}</code><br><strong>Prior codes and aliases:</strong> {aliases}</p>
  </section>{classes}
</section>"""
'''
text = text[:start] + replacement + text[end:]

css_anchor = 'details>*{display:block!important}\n"""'
css = r'''details>*{display:block!important}
.chapter-opener{break-before:page;break-after:page}.chapter-opener h1{font-family:Georgia,"Times New Roman",serif;font-size:30pt;line-height:1.02;color:#073f34;font-weight:500;margin:3mm 0 7mm;max-width:165mm}.chapter-kicker,.class-kicker{text-transform:uppercase;letter-spacing:.11em;font-size:8pt;font-weight:700;color:#b8943f;margin:0 0 3mm}.chapter-lead{background:#eef4e8!important;border-left:2.2pt solid #b8943f;padding:4mm 5mm;font-family:Georgia,"Times New Roman",serif;font-size:13pt;line-height:1.28;margin:0 0 4mm}.chapter-meta,.class-meta{font-size:8pt;color:#6f6657;margin:0 0 6mm}.chapter-opener h2,.chapter-map h2,.book-class h2,.book-class h3{font-family:Georgia,"Times New Roman",serif;color:#073f34;font-weight:500}.chapter-opener h2{font-size:16pt;margin:5mm 0 2mm}.chapter-opener .grid h3{font-family:Helvetica,Arial,sans-serif;font-size:12pt;color:#171717;font-weight:700}.chapter-map{break-after:page}.chapter-map h2{font-size:23pt;margin:0 0 6mm}.chapter-map h3{font-size:13pt;color:#073f34;margin:5mm 0 2mm}.chapter-map-note{font-size:8.5pt;color:#6f6657}.chapter-list{list-style:none;padding:0;margin:3mm 0 7mm}.chapter-list li{display:grid;grid-template-columns:13mm 1fr 55mm;gap:3mm;border-bottom:.35pt solid #ddd8ca;padding:2.5mm 0;align-items:start}.chapter-item-number{font-weight:700;color:#b8943f}.chapter-item-title{font-weight:600}.chapter-item-id{font-size:7.4pt;color:#6f6657;text-align:right}.book-class{break-before:page}.class-title{font-size:23pt;line-height:1.08;margin:0 0 2mm}.class-meta{margin-bottom:4mm}.variant-parent{font-family:Georgia,"Times New Roman",serif;font-style:italic;color:#6f6657;margin:-1mm 0 4mm}.book-class>.plain{font-size:11pt;line-height:1.32;padding:4mm 5mm;margin:0 0 5mm}.book-class h3{font-size:13pt;margin:5mm 0 2mm}.book-class .grid h3{font-family:Helvetica,Arial,sans-serif;font-size:10pt;font-weight:700;color:#171717;margin:0 0 2mm}.criteria-grid{break-inside:avoid}.book-class ul{margin-top:1.5mm}.case-studies{margin-top:7mm}.case-studies>h4{font-family:Georgia,"Times New Roman",serif;font-size:15pt;color:#073f34;font-weight:500;margin:0 0 3mm}.case-study{border-top:.7pt solid #b8943f;padding:4mm 0 3mm;break-inside:avoid}.case-study h5{font-family:Georgia,"Times New Roman",serif;font-size:11.5pt;line-height:1.2;color:#073f34;margin:0 0 1mm}.case-study-meta{font-size:8pt;color:#6f6657;margin:0 0 2.5mm}.case-study-what{font-size:9.5pt;line-height:1.4;margin:0 0 2.5mm}.case-study-what strong{color:#073f34}.case-study-ref{font-size:7.5pt;color:#78716c;margin:0}.book-family code,.book-class code{font-size:.88em}.book-family+.book-family{border:0!important;padding:0!important;margin:0!important}
"""'''
if text.count(css_anchor) != 1:
    raise SystemExit(f"Refusing CSS patch: {text.count(css_anchor)} anchors")
text = text.replace(css_anchor, css, 1)

old = '''    contents = ["<section class=\\"contents\\"><h1>Governance Failure Taxonomy</h1><p>Technical Reference</p><h2>Contents</h2><ol>"]
    for data in families:
        family = data["family"]
        contents.append(f"<li><a href=\\"#{esc(anchor(family['family_id']))}\\">{esc(family['name'])}</a><ul>")
        contents.extend(
            f"<li><a href=\\"#{esc(anchor(item['class_id']))}\\">{esc(item['name'])}</a></li>"
            for item in data["classes"]
        )
        contents.append("</ul></li>")
    contents.append("</ol></section>")
    frontmatter = publication_frontmatter(index, families) if publication else ""
    return document(
        "Governance Failure Taxonomy — Technical Reference",
        frontmatter + "".join(contents) + "".join(family_html(d, 1, case_examples) for d in families),
        publication=publication,
    )'''
new = '''    contents = ["<section class=\\"contents\\"><h1>Governance Failure Taxonomy</h1><p>Technical Reference</p><h2>Contents</h2><ol>"]
    for chapter_number, data in enumerate(families, start=1):
        family = data["family"]
        contents.append(f"<li><a href=\\"#{esc(anchor(family['family_id']))}\\"><strong>{chapter_number}. {esc(family['name'])}</strong></a><ul>")
        contents.extend(
            f"<li><a href=\\"#{esc(anchor(item['class_id']))}\\">{chapter_number}.{class_number} {esc(item['name'])}</a></li>"
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
    )'''
if text.count(old) != 1:
    raise SystemExit(f"Refusing combined_html patch: {text.count(old)} anchors")
text = text.replace(old, new, 1)

path.write_text(text, encoding="utf-8")
