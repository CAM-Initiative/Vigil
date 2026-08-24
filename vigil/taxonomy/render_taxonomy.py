#!/usr/bin/env python3
"""Generate complete human-readable VIGIL Failure Taxonomy references."""

from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INDEX = ROOT / "VIGIL.FailureTaxonomy.Index.json"


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


def class_html(item: dict) -> str:
    recognition = "".join(f"<li>{esc(x)}</li>" for x in item["recognition"]["required_conditions"])
    indicators = ""
    if item["recognition"].get("indicators"):
        indicators = "<h4>Indicators</h4><ul>" + "".join(
            f"<li>{esc(x)}</li>" for x in item["recognition"]["indicators"]
        ) + "</ul>"
    exclusions = "".join(f"<li>{esc(x)}</li>" for x in item["exclusions"])
    examples = "".join(f"<li>{esc(x)}</li>" for x in item["examples"])
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
  <h4>Illustrative examples</h4><ul>{examples}</ul>{aliases}{relationships}{mappings}
</article>"""


def family_html(data: dict, heading_level: int = 1) -> str:
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
<section class="hero"><p class="eyebrow">VIGIL Failure Taxonomy · Technical Standard</p><{tag}>{esc(family['name'])}</{tag}><p class="plain">{esc(family['plain_english'])}</p>
<p><strong>Immutable ID:</strong> <code>{esc(family['family_id'])}</code> · <strong>Semantic code:</strong> <code>{esc(family['family_code'])}</code> · <strong>Version:</strong> {esc(family['version'])} · <strong>Status:</strong> {esc(family['status'])}</p>
<h2>Technical definition</h2><p>{esc(family['definition'])}</p><h2>Governing invariant</h2><p class="invariant">{esc(family['invariant'])}</p>
<h2>Classification boundary</h2><div class="grid"><section><h3>Include when</h3><p>{esc(family['inclusion_rule'])}</p></section><section><h3>Exclude when</h3><p>{esc(family['exclusion_rule'])}</p></section></div>
<h2>Scope</h2><ul>{scope}</ul><details><summary><strong>Allowed identifiers</strong></summary><ul>{allowed}</ul></details><details><summary><strong>Prior codes and aliases</strong></summary><ul>{aliases}</ul></details></section>
<h2>Failure classes</h2>{''.join(class_html(item) for item in data['classes'])}</section>"""


STYLE = """
:root{font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;color:#171717;background:#f5f5f4}body{margin:0;line-height:1.55}main{max-width:1100px;margin:auto;padding:36px 20px 80px}.hero,.card,.contents{background:#fff;border:1px solid #d6d3d1;border-radius:16px;padding:26px;margin-bottom:20px}h1{font-size:clamp(2rem,5vw,3.2rem);line-height:1.05}h3{font-size:1.4rem;margin:.4rem 0}code{background:#f5f5f4;border:1px solid #e7e5e4;border-radius:5px;padding:2px 5px;overflow-wrap:anywhere}.plain{background:#fafaf9;padding:14px 16px;border-radius:10px;font-size:1.06rem}.invariant{border-left:4px solid #44403c;background:#fafaf9;padding:12px 16px}.grid{display:grid;grid-template-columns:1fr 1fr;gap:14px}.grid section{background:#fafaf9;border-radius:10px;padding:14px}.top{display:flex;justify-content:space-between;gap:20px;align-items:start}.pill{font-size:.73rem;border:1px solid #d6d3d1;border-radius:999px;padding:3px 8px;text-transform:uppercase;letter-spacing:.05em}.eyebrow{text-transform:uppercase;letter-spacing:.08em;font-size:.78rem;font-weight:700}.family+.family{border-top:3px solid #a8a29e;padding-top:52px;margin-top:52px}.contents a{color:#1c4b69}@media(max-width:760px){.grid{grid-template-columns:1fr}.top{display:block}}
"""


def document(title: str, body: str) -> str:
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)}</title><style>{STYLE}</style></head><body><main>{body}</main></body></html>
"""


def html_family(data: dict) -> str:
    return document(data["family"]["name"], family_html(data))


def load_catalogue(index_path: Path = INDEX) -> list[dict]:
    index = load(index_path)
    return [load(index_path.parent / item["file"]) for item in index["families"]]


def combined_html(families: list[dict]) -> str:
    contents = ["<section class=\"contents\"><h1>VIGIL Failure Taxonomy</h1><p>Full reference book</p><h2>Contents</h2><ol>"]
    for data in families:
        family = data["family"]
        contents.append(f"<li><a href=\"#{esc(anchor(family['family_id']))}\">{esc(family['name'])}</a><ul>")
        contents.extend(
            f"<li><a href=\"#{esc(anchor(item['class_id']))}\">{esc(item['name'])}</a></li>"
            for item in data["classes"]
        )
        contents.append("</ul></li>")
    contents.append("</ol></section>")
    return document("VIGIL Failure Taxonomy — Full Reference", "".join(contents) + "".join(family_html(d, 1) for d in families))


def generate_catalogue(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    families = load_catalogue()
    for data in families:
        family_id = data["family"]["family_id"]
        index = load(INDEX)
        entry = next(item for item in index["families"] if item["family_id"] == family_id)
        stem = Path(entry["file"]).stem
        (output_dir / f"{stem}.html").write_text(html_family(data), encoding="utf-8")
    (output_dir / "VIGIL.FailureTaxonomy.FullReference.html").write_text(combined_html(families), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--format", choices=("markdown", "html"))
    parser.add_argument("--output", type=Path)
    parser.add_argument("--catalogue", action="store_true", help="generate every family page and the full reference book")
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    if args.catalogue:
        if args.input or args.format or args.output or not args.output_dir:
            parser.error("--catalogue requires --output-dir and no single-file arguments")
        generate_catalogue(args.output_dir)
        return
    if not args.input or not args.format or not args.output:
        parser.error("single-family rendering requires input, --format and --output")
    data = load(args.input)
    rendered = markdown_family(data) if args.format == "markdown" else html_family(data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(rendered, encoding="utf-8")


if __name__ == "__main__":
    main()
