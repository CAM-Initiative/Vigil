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


def case_examples_html(examples: list[dict]) -> str:
    if not examples:
        return ""
    rows = []
    for example in examples:
        role = str(example.get("classification_role", "primary")).title()
        confidence = str(example.get("classification_confidence", "unknown"))
        basis = str(example.get("classification_basis", ""))
        rows.append(
            f"<li><strong>{esc(role)}:</strong> <code>{esc(example.get('failure_mode_id', ''))}</code> — "
            f"{esc(example.get('title', ''))} <span class=\"pill\">{esc(confidence)}</span>"
            + (f"<p>{esc(basis)}</p>" if basis else "")
            + "</li>"
        )
    return (
        f"<details class=\"case-files\"><summary><strong>VIGIL Observatory Case File classifications ({len(rows)})</strong>"
        "</summary><ul>" + "".join(rows) + "</ul></details>"
    )


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
  @top-left{content:"CAM INITIATIVE | GOVERNANCE FAILURE TAXONOMY";font-size:7.2pt;color:#0b4a3b;letter-spacing:.07em;font-weight:600}
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
.cover-title{font-family:Georgia,"Times New Roman",serif;font-size:35pt;line-height:.98;text-transform:uppercase;color:#073f34;letter-spacing:.012em;margin:0 0 7mm;font-weight:500;max-width:155mm}
.cover-rule{display:flex;align-items:center;gap:4mm;margin:0 0 6mm;width:138mm}.cover-rule:before,.cover-rule:after{content:"";height:.45pt;background:#b8943f;flex:1}.cover-rule span{width:2mm;height:2mm;background:#b8943f;border-radius:50%}
.cover-subtitle{font-family:Georgia,"Times New Roman",serif;font-size:18pt;line-height:1.1;color:#a47d27;margin:0 0 4mm;font-weight:500}
.cover-descriptors{font-family:Georgia,"Times New Roman",serif;font-size:10.5pt;color:#17231f;margin:0;letter-spacing:.01em}.cover-descriptors .dot{color:#b8943f;padding:0 2.2mm}
.cover-band{position:absolute;left:0;right:0;bottom:0;height:63mm;background:#063d32;color:#fff;border-top:1.1mm solid #b8943f;overflow:hidden;padding:9mm 16mm 8mm;box-sizing:border-box}
.cover-footer-art{position:absolute;left:0;right:0;bottom:0;width:210mm;height:auto;opacity:.72;z-index:0}.cover-band-content{position:relative;z-index:1;height:100%}
.cover-meta{display:flex;gap:0;align-items:flex-start}.cover-meta-block{padding:0 9mm 0 0;margin-right:9mm;border-right:.35pt solid rgba(214,177,84,.75);min-width:31mm}.cover-meta-block:last-child{border-right:0;margin-right:0}.cover-meta-label{font-size:6.8pt;text-transform:uppercase;letter-spacing:.09em;color:#d7b35b;font-weight:700;margin-bottom:2mm}.cover-meta-value{font-family:Georgia,"Times New Roman",serif;font-size:15pt;color:#fff;line-height:1}
.cover-publisher{position:absolute;left:0;bottom:1mm}.cover-publisher strong{display:block;color:#d7b35b;font-size:11pt;letter-spacing:.07em;text-transform:uppercase}.cover-publisher span{font-size:8.5pt;color:#fff}
.publication-imprint{page:imprint;min-height:249mm;page-break-after:always;display:flex;flex-direction:column;color:#2a2a2a}.imprint-kicker{color:#0b4a3b;text-transform:uppercase;letter-spacing:.08em;font-size:7.5pt;font-weight:700;margin-bottom:4mm}.publication-imprint h1{font-family:Georgia,"Times New Roman",serif;color:#073f34;font-size:22pt;font-weight:500;margin:0 0 13mm}.publication-meta{display:grid;grid-template-columns:42mm 1fr;gap:3mm 6mm;margin:0}.publication-meta dt{color:#6f6657}.publication-meta dd{margin:0;font-weight:600}.imprint-rule{height:.6pt;background:#b8943f;width:100%;margin:14mm 0 8mm}.copyright{margin-top:auto;font-size:9pt;color:#504a40}.copyright strong{color:#073f34}.website{margin-top:2mm;color:#0b4a3b}
.contents{border:0;padding:0;page-break-after:always}.contents h1{font-family:Georgia,"Times New Roman",serif;font-size:22pt;color:#073f34;font-weight:500}.contents h2{color:#0b4a3b}.contents a{color:#073f34}
.family{page-break-before:always;border-top:0!important;padding-top:0!important;margin-top:0!important}.family>.hero{border:0;padding:0;margin:0 0 8mm}.family>.hero h1,.family>.hero h2{font-family:Georgia,"Times New Roman",serif;color:#073f34;font-weight:500}.family>.hero .eyebrow{color:#0b4a3b}.card{break-inside:auto;border:1px solid #c8d1c8;border-radius:6px;padding:5mm;margin:0 0 5mm}.card h3{font-family:Georgia,"Times New Roman",serif;font-size:15pt;color:#073f34;font-weight:500}.plain{background:#eef4e8!important;border-left:2.2pt solid #b8943f;border-radius:0!important}.invariant{background:#f6f4eb!important;border-left:2.2pt solid #073f34!important}.grid{grid-template-columns:1fr 1fr;gap:4mm}.grid section{break-inside:avoid;background:#f6f4eb!important}.top{break-inside:avoid}.case-files{break-inside:auto}a{color:#073f34;text-decoration:none}details{display:block}details>summary{list-style:none}details>*{display:block!important}
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
    <div class="cover-rule"><span></span></div>
    <h2 class="cover-subtitle">Technical Reference</h2>
    <p class="cover-descriptors">Failure Families<span class="dot">•</span>Failure Classes<span class="dot">•</span><br>Classification Boundaries<span class="dot">•</span>Recognition Criteria</p>
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
    <dt>Author and rights holder</dt><dd>Dr Michelle O'Rourke</dd>
  </dl>
  <div class="imprint-rule"></div>
  <p>This technical reference provides the maintained classification structure for governance failure families and failure classes, including classification boundaries and recognition criteria.</p>
  <div class="copyright"><strong>Copyright © 2026 Dr Michelle O'Rourke.</strong><div class="website">cam-initiative.org</div></div>
</section>"""

def combined_html(families: list[dict], case_examples: dict[str, list[dict]] | None = None, *, publication: bool = False) -> str:
    index = load(INDEX)
    contents = ["<section class=\"contents\"><h1>Governance Failure Taxonomy</h1><p>Technical Reference</p><h2>Contents</h2><ol>"]
    for data in families:
        family = data["family"]
        contents.append(f"<li><a href=\"#{esc(anchor(family['family_id']))}\">{esc(family['name'])}</a><ul>")
        contents.extend(
            f"<li><a href=\"#{esc(anchor(item['class_id']))}\">{esc(item['name'])}</a></li>"
            for item in data["classes"]
        )
        contents.append("</ul></li>")
    contents.append("</ol></section>")
    frontmatter = publication_frontmatter(index, families) if publication else ""
    return document(
        "Governance Failure Taxonomy — Technical Reference",
        frontmatter + "".join(contents) + "".join(family_html(d, 1, case_examples) for d in families),
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
