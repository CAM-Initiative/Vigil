#!/usr/bin/env python3
"""Apply approved textbook structure, contents and publisher-imprint refinements once."""
from pathlib import Path

PATH = Path("vigil/taxonomy/render_taxonomy.py")
text = PATH.read_text(encoding="utf-8")

# 1. Rebuild the publication-only family structure so the outline precedes substantive family analysis.
start = text.index("def publication_family_html(data: dict, chapter_number: int, case_examples: dict[str, list[dict]] | None = None) -> str:")
end = text.index("\ndef class_html", start)
new_family = r'''def publication_family_html(data: dict, chapter_number: int, case_examples: dict[str, list[dict]] | None = None) -> str:
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

'''
text = text[:start] + new_family + text[end:]

# 2. Simplify the Contents page because the running header already names the publication.
old_contents = 'contents = ["<section class=\\"contents\\"><h1>Governance Failure Taxonomy</h1><p>Technical Reference</p><h2>Contents</h2><ol>"]'
new_contents = 'contents = ["<section class=\\"contents\\"><h1>Contents</h1><ol>"]'
if old_contents not in text:
    raise SystemExit("contents opening block not found")
text = text.replace(old_contents, new_contents, 1)

# 3. End the publication metadata at Failure classes, then put institutional publisher information below the reliance notice.
old_meta = '''    <dt>Failure families</dt><dd>{len(families)}</dd>\n    <dt>Failure classes</dt><dd>{class_count}</dd>\n    <dt>Publisher</dt><dd>CAM Initiative</dd>\n    <dt>Governance editor</dt><dd>Dr M.V. O'Rourke</dd>\n    <dt>Business entity</dt><dd>Phoenix Covenant Pty Ltd</dd>\n    <dt>ABN</dt><dd>14 692 195 529</dd>\n    <dt>Rights holder</dt><dd>Dr Michelle O'Rourke</dd>'''
new_meta = '''    <dt>Failure families</dt><dd>{len(families)}</dd>\n    <dt>Failure classes</dt><dd>{class_count}</dd>'''
if old_meta not in text:
    raise SystemExit("publication metadata identity block not found")
text = text.replace(old_meta, new_meta, 1)

old_bottom = '''  <section class="reliance-notice">\n    <h2>Use and reliance notice</h2>\n    <p>This report is provided for research and informational purposes. It does not constitute legal, regulatory, security, assurance, certification, risk, or other professional advice, and should not be relied upon as a substitute for independent assessment. Third parties remain responsible for verifying the cited source material, the current state of the underlying VIGIL Observatory records and taxonomy, the applicability of the analysis to their circumstances, and any decision or action taken in reliance on this report.</p>\n  </section>\n  <div class="copyright"><strong>Copyright © 2026 Dr Michelle O'Rourke.</strong><div class="website">cam-initiative.org</div></div>'''
new_bottom = '''  <section class="reliance-notice">\n    <h2>Use and reliance notice</h2>\n    <p>This report is provided for research and informational purposes. It does not constitute legal, regulatory, security, assurance, certification, risk, or other professional advice, and should not be relied upon as a substitute for independent assessment. Third parties remain responsible for verifying the cited source material, the current state of the underlying VIGIL Observatory records and taxonomy, the applicability of the analysis to their circumstances, and any decision or action taken in reliance on this report.</p>\n  </section>\n  <section class="publisher-block">\n    <h2>Publisher</h2>\n    <p><strong>CAM Initiative</strong><br>Business entity: Phoenix Covenant Pty Ltd<br>ABN 14 692 195 529<br>cam-initiative.org</p>\n  </section>'''
if old_bottom not in text:
    raise SystemExit("reliance/copyright block not found")
text = text.replace(old_bottom, new_bottom, 1)

# 4. Publication CSS for the separated overview and institutional publisher block.
old_css = '.chapter-opener h2,.chapter-map h2,.book-class h2,.book-class h3{font-family:Georgia,"Times New Roman",serif;color:#022c1b;font-weight:500}'
new_css = '.chapter-opener h2,.chapter-map h2,.chapter-overview h2,.chapter-overview h3,.book-class h2,.book-class h3{font-family:Georgia,"Times New Roman",serif;color:#022c1b;font-weight:500}'
if old_css not in text:
    raise SystemExit("chapter heading CSS selector not found")
text = text.replace(old_css, new_css, 1)

old_map_css = '.chapter-map{break-after:page}.chapter-map h2{font-size:23pt;margin:0 0 6mm}.chapter-map h3{font-size:13pt;color:#022c1b;margin:5mm 0 2mm}'
new_map_css = '.chapter-map{break-after:page}.chapter-map h2{font-size:23pt;margin:0 0 6mm}.chapter-map h3{font-size:13pt;color:#022c1b;margin:5mm 0 2mm}.chapter-overview{break-after:page}.chapter-overview h2{font-size:16pt;margin:5mm 0 2mm}.chapter-overview .grid h3{font-family:Helvetica,Arial,sans-serif;font-size:10pt;font-weight:700;color:#171717;margin:0 0 2mm}'
if old_map_css not in text:
    raise SystemExit("chapter map CSS block not found")
text = text.replace(old_map_css, new_map_css, 1)

old_identity_css = '.copyright{font-family:Helvetica,Arial,sans-serif;margin-top:3.5mm;font-size:9pt;color:#504a40}.copyright strong{color:#022c1b}.website{margin-top:2mm;color:#022c1b}'
new_identity_css = '.publisher-block{margin-top:5mm;padding-top:4mm;border-top:.6pt solid #d8d5cc;font-family:Helvetica,Arial,sans-serif}.publisher-block h2{font-family:Helvetica,Arial,sans-serif;font-size:9pt;font-weight:700;color:#022c1b;margin:0 0 2.5mm}.publisher-block p{font-family:Helvetica,Arial,sans-serif;font-size:8.5pt;line-height:1.5;color:#504a40;margin:0}.publisher-block strong{color:#022c1b}'
if old_identity_css not in text:
    raise SystemExit("copyright CSS block not found")
text = text.replace(old_identity_css, new_identity_css, 1)

PATH.write_text(text, encoding="utf-8")
print("Applied textbook outline, contents and publisher-imprint refinements")
