#!/usr/bin/env python3
"""Render the non-normative legacy failure migration ledger for human review."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path


def name(candidate: dict | None, kind: str) -> str:
    if not candidate:
        return "—"
    return candidate.get(f"{kind}_id") or candidate.get(f"{kind}_name") or "—"


def render(data: dict) -> str:
    entries = data["entries"]
    counts = Counter(item["disposition"] for item in entries)
    clusters: dict[str, list[dict]] = defaultdict(list)
    for item in entries:
        candidate = item.get("candidate_portable_family")
        if isinstance(candidate, dict) and candidate.get("family_name"):
            clusters[candidate["family_name"]].append(item)

    out = [
        "# Caelestis Legacy Failure Inventory and Clustering Review", "",
        "> Migration evidence only. This report is not part of the portable normative taxonomy and creates no runtime dependency on Caelestis.", "",
        "## Review scope", "",
        f"- Source repository: `{data['source_corpus']['repository']}`",
        f"- Source ref and commit: `{data['source_corpus']['ref']}` at `{data['source_corpus']['commit']}`",
        f"- Review date: `{data['review_date']}`",
        f"- Inventory entries: **{len(entries)}**", "",
        "The inventory covers all 13 controlled `OPS.FF` values, every named §3 failure entry in the Runtime & Governance Failure Taxonomy, the controlled values in `PFAIL`, `SEC.BF`, `OPS.RGRF`, and `OPS.VFC`, every value in the source taxonomy's `OPS.FCS`, `OPS.FMA`, and `OPS.AGMA` status/metadata axes, and named embedded failure classifications from MENTIS, governance observability, economic attribution, relation, and stewardship routing instruments. Broad headings are treated as historical organisation, not presumptive portable families.", "",
        "## Disposition summary", "",
        "| Disposition | Count |", "|---|---:|",
    ]
    out.extend(f"| `{value}` | {counts.get(value, 0)} |" for value in data["controlled_dispositions"])

    out.extend(["", "## Candidate family clusters", ""])
    out.append("These clusters are evidence for TAXONOMY-03 review, not admitted families. A cluster must still satisfy the bounded-invariant, inclusion, exclusion, and multi-mechanism tests.")
    out.extend(["", "| Candidate cluster | Source entries | Distinct proposed mechanisms |", "|---|---:|---:|"])
    for cluster, items in sorted(clusters.items()):
        proposed = {name(item.get("candidate_class"), "class") for item in items} - {"—"}
        out.append(f"| {cluster} | {len(items)} | {len(proposed)} |")

    decisions = data.get("taxonomy_03_decisions", {})
    if decisions:
        out.extend(["", "## TAXONOMY-03 decisions", ""])
        out.append(f"Decision review date: `{decisions['review_date']}`.")
        out.extend(["", "### Admitted families", ""])
        for item in decisions.get("admitted_families", []):
            evidence = ", ".join(f"`{value}`" for value in item["evidence_entries"])
            out.extend([
                f"#### `{item['family_id']}` — {item['name']}", "",
                item["admission_rationale"], "",
                f"**Boundary:** {item['boundary']}", "",
                f"**Evidence entries:** {evidence}", "",
            ])
        out.extend(["### Existing-family additions", "", "| Class | Family | Evidence entries |", "|---|---|---|"])
        for item in decisions.get("existing_family_additions", []):
            evidence = ", ".join(f"`{value}`" for value in item["evidence_entries"])
            out.append(f"| `{item['class_id']}` | `{item['family_id']}` | {evidence} |")
        out.extend(["", "### Rejected or deferred candidate families", ""])
        for item in decisions.get("deferred_candidates", []):
            evidence = ", ".join(f"`{value}`" for value in item["source_entries"])
            out.append(f"- **{item['name']} — `{item['decision']}`:** {item['reason']} Evidence: {evidence}.")

    out.extend(["", "## Complete disposition ledger", "", "| Source | Source name | Legacy family | Disposition | Candidate family | Candidate class | Review |", "|---|---|---|---|---|---|---|"])
    for item in entries:
        out.append(
            f"| `{item['source_identifier']}` | {item['source_name']} | `{item['legacy_family']}` | "
            f"`{item['disposition']}` | {name(item.get('candidate_portable_family'), 'family')} | "
            f"{name(item.get('candidate_class'), 'class')} | `{item['review_state']}` |"
        )

    out.extend(["", "## Entries requiring split", ""])
    for item in entries:
        if item["disposition"] != "SPLIT_REQUIRED":
            continue
        out.extend([
            f"### `{item['source_identifier']}` — {item['source_name']}", "",
            item["rationale"], "",
            *[f"- {note}" for note in item["split_notes"]], "",
        ])

    out.extend(["", "## Entries that are not portable failure mechanisms", ""])
    non_mechanisms = {
        "NOT_A_FAILURE_MECHANISM", "HARM_OR_CONSEQUENCE_AXIS", "MANIFESTATION_OR_LOCUS_AXIS", "OTHER_ORTHOGONAL_AXIS"
    }
    for item in entries:
        if item["disposition"] in non_mechanisms:
            out.append(f"- `{item['source_identifier']}` — **{item['disposition']}**: {item['rationale']}")

    out.extend(["", "## Unresolved judgement boundaries", ""])
    for item in entries:
        if item["review_state"] == "requires_judgment":
            out.append(
                f"- `{item['source_identifier']}` — {item['source_name']}: {item['structural_invariant_inferred']} "
                f"Disposition remains `{item['disposition']}`."
            )

    out.extend([
        "", "## Remaining migration work", "",
        "Unresolved entries and split components remain non-normative migration evidence. Future batches must derive their scope from this remaining evidence and must not treat the deferred candidate labels as predetermined families.", "",
    ])
    return "\n".join(out)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    data = json.loads(args.input.read_text(encoding="utf-8"))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render(data), encoding="utf-8")


if __name__ == "__main__":
    main()
