#!/usr/bin/env python3
"""Render a VIGIL Failure Taxonomy family JSON file as Markdown or HTML."""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def label(value: str) -> str:
    return value.replace("_", " ").title()


def markdown(data: dict) -> str:
    family = data["family"]
    out = [
        f"# {family['name']}", "",
        "## Family", "",
        "| Field | Value |", "|---|---|",
        f"| Code | `{family['code']}` |",
        f"| Status | {family['status']} |",
        f"| Version | {family['version']} |",
        f"| Abstraction | {family['abstraction']} |", "",
        "### Plain English", "", family["plain_english"], "",
        "### Technical definition", "", family["definition"], "",
        "### Governing invariant", "", f"> {family['invariant']}", "",
        "### Classification boundary", "",
        f"**Include when:** {family['inclusion_rule']}", "",
        f"**Do not use when:** {family['exclusion_rule']}", "",
        "### Scope", "",
    ]
    out.extend(f"- {x}" for x in family["scope"])
    out.extend(["", "## Allowed failure codes", ""])
    out.extend(f"- `{x}`" for x in family["allowed_codes"])
    out.extend(["", "## Failure classes", ""])

    for item in data["classes"]:
        out.extend([
            f"### {item['name']}", "",
            f"**Code:** `{item['code']}`  ",
            f"**Abstraction:** {item['abstraction']}  ",
            f"**Status:** {item['status']}", "",
            f"**Plain English:** {item['plain_english']}", "",
            "**Technical definition**", "", item["definition"], "",
            "**Recognise this class when**", "",
        ])
        out.extend(f"- {x}" for x in item["recognition"]["required_conditions"])
        out.extend(["", "**Do not classify as this when**", ""])
        out.extend(f"- {x}" for x in item["exclusions"])
        out.extend(["", "**Illustrative examples**", ""])
        out.extend(f"- {x}" for x in item["examples"])
        if item.get("aliases"):
            out.extend(["", "**Aliases / search terms:** " + "; ".join(f"`{x}`" for x in item["aliases"])])
        if item.get("relationships"):
            out.extend(["", "**Relationships**", ""])
            for rel in item["relationships"]:
                note = f" — {rel['note']}" if rel.get("note") else ""
                out.append(f"- {label(rel['type'])}: `{rel['target_code']}`{note}")
        out.extend(["", "---", ""])
    return "\n".join(out).rstrip() + "\n"


def html_view(data: dict) -> str:
    family = data["family"]
    esc = lambda x: html.escape(str(x))
    cards = []
    for item in data["classes"]:
        recog = "".join(f"<li>{esc(x)}</li>" for x in item["recognition"]["required_conditions"])
        excl = "".join(f"<li>{esc(x)}</li>" for x in item["exclusions"])
        examples = "".join(f"<li>{esc(x)}</li>" for x in item["examples"])
        rels = ""
        if item.get("relationships"):
            rels = "<h4>Relationships</h4><ul>" + "".join(
                f"<li><strong>{esc(label(r['type']))}:</strong> <code>{esc(r['target_code'])}</code>"
                + (f" — {esc(r['note'])}" if r.get("note") else "") + "</li>"
                for r in item["relationships"]
            ) + "</ul>"
        cards.append(f"""
<article class="card">
  <div class="top"><div><span class="pill">{esc(item['abstraction'])}</span><h3>{esc(item['name'])}</h3><code>{esc(item['code'])}</code></div><span class="pill">{esc(item['status'])}</span></div>
  <p class="plain"><strong>Plain English:</strong> {esc(item['plain_english'])}</p>
  <h4>Technical definition</h4><p>{esc(item['definition'])}</p>
  <div class="grid"><section><h4>Recognise this class when</h4><ul>{recog}</ul></section><section><h4>Do not classify as this when</h4><ul>{excl}</ul></section></div>
  <h4>Illustrative examples</h4><ul>{examples}</ul>{rels}
</article>""")

    scope = "".join(f"<li>{esc(x)}</li>" for x in family["scope"])
    allowed = "".join(f"<li><code>{esc(x)}</code></li>" for x in family["allowed_codes"])
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(family['name'])}</title>
<style>
:root{{font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;color:#171717;background:#f5f5f4}}body{{margin:0;line-height:1.55}}main{{max-width:1100px;margin:auto;padding:36px 20px 80px}}.hero,.card{{background:#fff;border:1px solid #d6d3d1;border-radius:16px;padding:26px;margin-bottom:20px}}h1{{font-size:clamp(2rem,5vw,3.2rem);line-height:1.05}}h3{{font-size:1.4rem;margin:.4rem 0}}code{{background:#f5f5f4;border:1px solid #e7e5e4;border-radius:5px;padding:2px 5px;overflow-wrap:anywhere}}.plain{{background:#fafaf9;padding:14px 16px;border-radius:10px;font-size:1.06rem}}.invariant{{border-left:4px solid #44403c;background:#fafaf9;padding:12px 16px}}.grid{{display:grid;grid-template-columns:1fr 1fr;gap:14px}}.grid section{{background:#fafaf9;border-radius:10px;padding:14px}}.top{{display:flex;justify-content:space-between;gap:20px;align-items:start}}.pill{{font-size:.73rem;border:1px solid #d6d3d1;border-radius:999px;padding:3px 8px;text-transform:uppercase;letter-spacing:.05em}}@media(max-width:760px){{.grid{{grid-template-columns:1fr}}.top{{display:block}}}}
</style></head><body><main>
<section class="hero"><p><strong>VIGIL Failure Taxonomy · Prototype family</strong></p><h1>{esc(family['name'])}</h1><p class="plain">{esc(family['plain_english'])}</p><p><strong>Code:</strong> <code>{esc(family['code'])}</code> · <strong>Version:</strong> {esc(family['version'])} · <strong>Status:</strong> {esc(family['status'])}</p><h2>Technical definition</h2><p>{esc(family['definition'])}</p><h2>Governing invariant</h2><p class="invariant">{esc(family['invariant'])}</p><h2>Classification boundary</h2><div class="grid"><section><h3>Include when</h3><p>{esc(family['inclusion_rule'])}</p></section><section><h3>Do not use when</h3><p>{esc(family['exclusion_rule'])}</p></section></div><h2>Scope</h2><ul>{scope}</ul><details><summary><strong>Allowed failure codes</strong></summary><ul>{allowed}</ul></details></section>
<h2>Failure classes</h2>{''.join(cards)}</main></body></html>"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--format", choices=("markdown", "html"), required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    data = load(args.input)
    output = markdown(data) if args.format == "markdown" else html_view(data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(output, encoding="utf-8")


if __name__ == "__main__":
    main()
