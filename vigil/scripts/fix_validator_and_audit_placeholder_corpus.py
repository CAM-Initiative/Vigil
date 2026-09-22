#!/usr/bin/env python3
"""Repair known validator defects and census placeholder/thin Incident records.

This is a bounded corpus-maintenance script for the 2026-09-22 evidence-first
re-adjudication campaign. It does not invent occurrence evidence or taxonomy
mappings. It repairs structural validator defects and emits a deterministic
triage report identifying records that require full evidence rebuild.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INCIDENT_DIR = ROOT / "vigil" / "records" / "incidents"
OUT = ROOT / "vigil" / "docs" / "reviews" / "2026-09-22-placeholder-corpus-rewrite-census.md"

NONCANONICAL_SYSTEM_KEYS = {
    "affected_population", "deployment_context", "embodiment_status", "evidence_scope",
    "evidenced_models_or_runtimes", "evidenced_products_or_services", "evidenced_systems",
    "evidenced_vendors", "interaction_mode", "model_or_product", "primary_evidenced_vendors",
    "system_type", "user_role", "vendor_cluster",
}

SOURCE_TYPE_MAP = {
    "official post-incident statement": "official announcement",
    "official product and safety announcement": "official announcement",
    "regulatory guidance": "government report",
    "technical standard guidance": "standards document",
    "legislation": "standards document",
    "official report": "technical report",
}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def save(path: Path, obj):
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def fix_record(record_id: int):
    path = INCIDENT_DIR / f"VIGIL-INC-{record_id:06d}.json"
    d = load(path)
    system = d.get("system_context")
    if isinstance(system, dict):
        for key in NONCANONICAL_SYSTEM_KEYS:
            system.pop(key, None)
    for src in d.get("source_records", []):
        st = src.get("source_type")
        if st in SOURCE_TYPE_MAP:
            src["source_type"] = SOURCE_TYPE_MAP[st]
    if record_id == 1:
        ident = d.get("incident_identity", {})
        if ident.get("date_precision") == "reported-date-range":
            ident["date_precision"] = "date-range"
        env = d.get("system_context", {}).get("occurrence_environment")
        if isinstance(env, dict) and env.get("operational_setting") == "live":
            env["testing_actor"] = "not-applicable"
        for dim in d.get("harm_impact_assessment", {}).get("dimensions", []):
            if dim.get("assessment_status") == "assessed" and not isinstance(dim.get("observed_values"), list):
                dim["observed_values"] = []
    save(path, d)


def placeholder_signals(d):
    signals = []
    sources = d.get("source_records") or []
    assessment = d.get("vigil_assessment") or {}
    clauses = (assessment.get("source_clause_analysis") or {}).get("clauses") or []
    taxonomy = d.get("taxonomy_classification") or {}
    summary = str(d.get("summary", ""))
    factual = str(assessment.get("factual_basis", ""))
    governance = str(assessment.get("governance_interpretation", ""))
    significance = str(assessment.get("significance_to_cam", ""))
    current = (d.get("interpretive_provenance") or {}).get("current_ai_review") or {}

    if len(sources) <= 1:
        signals.append("single-source evidence spine")
    if not any((s.get("primary_artefact_access") or {}).get("direct_primary_artefact_review") is True for s in sources):
        signals.append("no directly reviewed primary/authoritative artefact")
    if len(clauses) == 0:
        signals.append("no Section 02 clause analysis")
    elif len(clauses) == 1:
        signals.append("single-row Section 02")
    version = str(taxonomy.get("taxonomy_version", ""))
    if version != "0.6.6":
        signals.append(f"taxonomy not current ({version or 'missing'})")
    cap = current.get("capability_profile") or {}
    if cap.get("new_external_source_research") is False:
        signals.append("latest assessment explicitly used no new external research")
    if re.search(r"preserved source records describe the bounded occurrence", summary, re.I):
        signals.append("generic migrated summary")
    if re.search(r"the selected evidence reports", factual, re.I):
        signals.append("generic migrated factual basis")
    if re.search(r"controls should preserve evidence, authority state, escalation and contestability", significance, re.I):
        signals.append("generic migrated CAM conclusion")
    if len(governance.strip()) < 180:
        signals.append("compressed governance interpretation")
    if len(factual.strip()) < 180:
        signals.append("compressed factual basis")
    if sources and all(s.get("source_role") in {"record-cross-reference", "contextual-background"} for s in sources):
        signals.append("no substantive occurrence-evidence source")
    if taxonomy.get("classification_status") in {"classified", "provisionally-classified", "classification-disputed"} and version != "0.6.6":
        signals.append("classification inherited from pre-0.6.6 taxonomy")
    return signals


def main():
    for rid in (1, 65, 113):
        fix_record(rid)

    rows = []
    for path in sorted(INCIDENT_DIR.glob("VIGIL-INC-*.json")):
        d = load(path)
        sig = placeholder_signals(d)
        score = len(sig)
        if score >= 6:
            tier = "A — rebuild first"
        elif score >= 3:
            tier = "B — substantive review"
        elif score >= 1:
            tier = "C — health check"
        else:
            tier = "D — currently healthy"
        rows.append((d.get("id"), tier, score, sig, d.get("record_identity", {}).get("title", "")))

    counts = {}
    for _, tier, *_ in rows:
        counts[tier] = counts.get(tier, 0) + 1

    lines = [
        "# VIGIL placeholder-corpus rewrite census — 2026-09-22",
        "",
        "## Purpose",
        "",
        "This census identifies active Incident records that require an evidence-first rebuild rather than another schema-only or Section-02-only migration. A signal is a triage indicator, not a finding that the occurrence is invalid or that an existing classification is wrong.",
        "",
        "## Completion contract for the rewrite campaign",
        "",
        "A record is complete only after occurrence-specific source research, source-role and evidence-boundary review, rebuilt factual basis, substantive Section 02 reasoning, current VIGIL Failure Taxonomy 0.6.6 adjudication (including material rejected candidates), Harm Impact consistency review, and an evidence-traceable conclusion. Existing completed records are preserved unless the evidence review identifies a substantive reason to reopen them.",
        "",
        "## Corpus triage",
        "",
    ]
    for tier in ("A — rebuild first", "B — substantive review", "C — health check", "D — currently healthy"):
        lines.append(f"- **{tier}: {counts.get(tier, 0)} records**")
    lines += ["", "## Record-level census", "", "| Incident | Tier | Signals | Title |", "|---|---|---:|---|"]
    for rid, tier, score, sig, title in rows:
        detail = "; ".join(sig) if sig else "none"
        lines.append(f"| {rid} | {tier} | {score} | {title} — {detail} |")
    lines += [
        "",
        "## Execution rule",
        "",
        "Work Tier A first in bounded tranches. For each record: search the occurrence afresh; prefer first-party, court/regulator, affected-party and technically authoritative evidence; preserve contradictory accounts; rebuild Section 02 from the evidence rather than the old Failure Mode; re-adjudicate the complete current class set; and record unclassified/taxonomy-gap outcomes where no class boundary is actually evidenced.",
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)} for {len(rows)} Incident records")


if __name__ == "__main__":
    main()
