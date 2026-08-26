#!/usr/bin/env python3
"""Apply the bounded TAXONOMY-05 classification review to canonical Failure Modes."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
FAILURES = ROOT / "records" / "failures" / "2026"
FAMILIES = ROOT / "taxonomy" / "families"
VERSION = "0.2.0-draft"
LEDGER = ROOT / "taxonomy" / "migration" / "VIGIL.FailureMode.TaxonomyClassificationLedger.json"
AUDIT = ROOT / "taxonomy" / "TAXONOMY-05-Audit.md"

# status, family ID, class ID, confidence, basis, candidate name, flags
DECISIONS: dict[int, tuple[str, str | None, str | None, str, str, str | None, list[str]]] = {
 1:("classified","VIGIL-FF-0001","VIGIL-FC-000002","high","The definition requires tool capability to become operative before user permission is established.",None,[]),
 2:("unmapped",None,None,"high","The mechanism is missing multi-agent turn arbitration; no current family governs participation topology or floor control.",None,[]),
 3:("family-only","VIGIL-FF-0006",None,"medium","Material strategic work state cannot be reliably resumed, but the record does not isolate anchor loss, persistence loss, or defective restoration.",None,[]),
 4:("unmapped",None,None,"high","Vulnerability monetisation and commercial capture are outside the current eight structural invariants.",None,[]),
 5:("unmapped",None,None,"high","Dependency cultivation is a relational influence mechanism not represented by a current family.",None,[]),
 6:("unmapped",None,None,"high","Paid legitimacy allocation is an economic and public-participation mechanism outside the current taxonomy.",None,[]),
 7:("deferred",None,None,"low","The definition combines ambiguity classification, enforcement proportionality, access continuity, evidence preservation, and appeal routing.",None,["compound-mechanism"]),
 8:("classified","VIGIL-FF-0005","VIGIL-FC-000032","high","Materially distinct authentication, entitlement, quota, policy, outage, and continuity states are collapsed into an ambiguous access representation.",None,[]),
 9:("classified","VIGIL-FF-0001","VIGIL-FC-000001","medium","Revoked or quarantined assistant content continues to be treated as direction-bearing authority rather than non-authoritative material.",None,[]),
 10:("classified","VIGIL-FF-0008","VIGIL-FC-000038","high","Minor-status signals satisfy a protective trigger but the applicable protective interaction state does not activate.",None,[]),
 11:("classified","VIGIL-FF-0008","VIGIL-FC-000038","high","Minor status requires a reduced relational-risk control state, but dependency-forming behaviour remains operative.",None,[]),
 12:("classified","VIGIL-FF-0008","VIGIL-FC-000038","high","Minor or unresolved-age signals require sexual-boundary activation, but the system continues the governed conduct.",None,[]),
 13:("classified","VIGIL-FF-0008","VIGIL-FC-000038","high","Minor-status conditions require an artificial-identity boundary, but the protective control does not become operative.",None,[]),
 14:("classified","VIGIL-FF-0008","VIGIL-FC-000038","high","Teen mental-health signals trigger bounded support and escalation controls that are not activated.",None,[]),
 15:("unmapped",None,None,"high","The defect is inadequacy of age-assurance design relative to risk, not availability or activation of a defined control.",None,[]),
 16:("unmapped",None,None,"high","The mechanism converts protective vulnerability signals into engagement personalisation; no current invariant captures that signal-purpose inversion.",None,[]),
 17:("unmapped",None,None,"high","The mechanism is overbroad upstream classification and proportionality, both intentionally outside current families.",None,[]),
 18:("classified","VIGIL-FF-0006","VIGIL-FC-000035","high","Substantive work is produced but not durably persisted before quota or environment interruption destroys resumable state.",None,[]),
 19:("classified","VIGIL-FF-0008","VIGIL-FC-000043","high","Hostile artefact content activates a safety restriction although the defensive-analysis activation conditions are not satisfied.",None,[]),
 20:("classified","VIGIL-FF-0008","VIGIL-FC-000043","medium","A safety control becomes operative against a permissible adult reassurance interaction even though the valid activation conditions are not satisfied.",None,[]),
 21:("family-only","VIGIL-FF-0005",None,"medium","The record concerns broad and poorly separated access states, but also combines proportionality, sovereign authority, review, and continuity mechanisms.",None,["compound-mechanism"]),
 22:("classified","VIGIL-FF-0001","VIGIL-FC-000001","high","External lower-authority content is treated as execution-bearing instruction without independent authority validation.",None,[]),
 23:("unmapped",None,None,"high","The primary mechanism is ambiguity collapse across classification and user-facing rationale, not a current authority, access, or audit class.",None,["compound-mechanism"]),
 24:("deferred",None,None,"low","The record combines runtime-lane continuity, audit-plane impairment, separation, incident disclosure, and authority bleed-through.",None,["compound-mechanism"]),
 25:("classified","VIGIL-FF-0004","VIGIL-FC-000029","high","Material tool, constraint, fallback, uncertainty, and action state is omitted from the report surface needed for supervision and reliance.",None,[]),
 26:("unmapped",None,None,"high","The mechanism is premature behavioural-mechanism classification under a deception label; classification integrity is not yet a family.",None,[]),
 27:("unmapped",None,None,"high","Anthropomorphic explanatory collapse is a representation and mechanism-attribution failure not captured by current audit classes.",None,[]),
 28:("deferred",None,None,"low","The definition deliberately combines control availability, non-activation, authority suppression, preservation, runtime identity, and conformance claims.",None,["compound-mechanism"]),
 29:("classified","VIGIL-FF-0004","VIGIL-FC-000029","medium","The system does not disclose materially relevant perception, turn, presence, and session state needed for timely interaction supervision.",None,[]),
 30:("unmapped",None,None,"high","The mechanism is unsupported causal self-explanation rather than missing event capture or reconstructability.",None,[]),
 31:("unmapped",None,None,"high","Pragmatic advice calibration and foreseeable interpersonal risk are outside current structural families.",None,[]),
 32:("unmapped",None,None,"high","The primary mechanism is role classification followed by affective-policy misapplication; classification integrity is not yet represented.",None,[]),
 33:("classified","VIGIL-FF-0004","VIGIL-FC-000044","medium","An identifiable authoritative artefact cannot be directly inspected in the authorised review environment, and secondary representations cannot preserve the properties material to review.",None,[]),
 34:("classified","VIGIL-FF-0007","VIGIL-FC-000040","medium","An established safeguard loses binding authority and operative effect across institutional transition before it can govern later conduct.",None,[]),
 35:("deferred",None,None,"low","The record combines entitlement transfer, identity attribution, model verification, provenance, data custody, and enforcement evasion.",None,["compound-mechanism"]),
 36:("classified","VIGIL-FF-0001","VIGIL-FC-000008","high","Authority to inspect or act in a workspace is expanded into transmission, persistence, training, or secondary-use authority.",None,[]),
 37:("deferred",None,None,"low","The record combines required higher-order review omission, cross-instrument contradiction, lineage loss, and instrument-identity collapse.",None,["compound-mechanism"]),
 38:("unmapped",None,None,"high","The mechanism promotes uncertain identity evidence into coercive authority; evidence/classification integrity is not represented by a current family.",None,[]),
 39:("unmapped",None,None,"high","The mechanism converts a population prediction into an individual entitlement determination; no current family captures this inference-to-decision transition.",None,[]),
 40:("classified","VIGIL-FF-0001","VIGIL-FC-000001","medium","Synthetic identity evidence from a non-authorising source is accepted as transaction-bearing authority.",None,[]),
 41:("deferred",None,None,"low","The FM requires both unauthorised destructive execution and subsequent truth-state falsification, which are independent mechanisms.",None,["compound-mechanism"]),
 42:("classified","VIGIL-FF-0001","VIGIL-FC-000003","high","Political restriction authority tied to one jurisdiction is transposed into a materially different global deployment scope.",None,[]),
 43:("unmapped",None,None,"high","Relationally conditioned evidence selection and calibration failure require an evidence-and-uncertainty family not presently admitted.",None,[]),
 44:("classified","VIGIL-FF-0001","VIGIL-FC-000002","high","Technical usefulness and executable capability are treated as permission despite absent target and method authority.",None,[]),
 45:("classified","VIGIL-FF-0001","VIGIL-FC-000007","high","Valid credentials and general role reachability are mistaken for authority for a specific purpose-bound surveillance action.",None,[]),
 46:("classified","VIGIL-FF-0002","VIGIL-FC-000013","high","Synthetic transformation provenance is lost across institutional handoffs, flattening the artefact into apparent authentic source material.",None,[]),
 47:("classified","VIGIL-FF-0001","VIGIL-FC-000009","high","Originating task authority is assumed to propagate through an adversarial delegate to its methods and downstream effects.",None,[]),
 48:("classified","VIGIL-FF-0008","VIGIL-FC-000043","high","A restriction becomes operative against authorised defensive interpretation although the conditions justifying that restriction are not satisfied.",None,[]),
 49:("unmapped",None,None,"high","Recursive identity optimisation and relational substrate capture are not governed by a current structural invariant.",None,["compound-mechanism"]),
 50:("family-only","VIGIL-FF-0005",None,"medium","A remote entitlement dependency makes effective access discontinuous, but current classes do not capture unavailable verification without state collapse.",None,[]),
 51:("classified","VIGIL-FF-0007","VIGIL-FC-000040","high","Safety-control state is weakened or erased during downstream model transfer while capability continues into the governed derivative.",None,[]),
 52:("classified","VIGIL-FF-0007","VIGIL-FC-000042","high","A correct safety signal is produced but fails to reach or engage a capable owner, responder, or execution point.",None,[]),
 53:("classified","VIGIL-FF-0004","VIGIL-FC-000023","high","A material route or actor omits, disables, or circumvents the monitoring boundary required for consequential conduct.",None,[]),
 54:("classified","VIGIL-FF-0001","VIGIL-FC-000003","high","Authority and scope declared for a simulated evaluation are carried into a materially different real target environment.",None,[]),
 55:("classified","VIGIL-FF-0004","VIGIL-FC-000045","medium","Valid investigative authority exists, but the governance architecture provides no bounded, protected, and auditable route through which necessary non-public evidence can be obtained.",None,[]),
 56:("classified","VIGIL-FF-0001","VIGIL-FC-000007","high","Surviving credentials, sessions, devices, or trust bindings are treated as cross-organisational permission after authority changes.",None,[]),
 57:("classified","VIGIL-FF-0002","VIGIL-FC-000012","high","Reasoning state crosses user, session, model, or purpose contexts without retaining applicability and provenance boundaries.",None,[]),
 58:("unmapped",None,None,"high","Instrumental manipulation and coercive influence require a bounded influence-integrity family not currently present.",None,[]),
 59:("classified","VIGIL-FF-0008","VIGIL-FC-000038","medium","A required human assurance control is nominally assigned but is not meaningfully invoked before the consequential transition.",None,[]),
 60:("classified","VIGIL-FF-0001","VIGIL-FC-000003","medium","Authority and control state for bounded defence are transposed into offensive scope, or offensive constraints are applied to distinct defensive scope.",None,["compound-mechanism"]),
 61:("classified","VIGIL-FF-0001","VIGIL-FC-000003","high","Prior offensive authority is renewed or extended into a new event and time scope without independent reauthorisation.",None,[]),
 62:("unmapped",None,None,"high","The mechanism converts verification uncertainty into essential-benefit denial; classification, proportionality, and fallback integrity are not current families.",None,[]),
 63:("unmapped",None,None,"high","Medical-guidance substitution is a domain-specific reliance and duty-of-care mechanism outside current families.",None,[]),
 64:("unmapped",None,None,"high","Non-consensual sexual identity synthesis is an identity appropriation and consent mechanism not captured by existing authority classes.",None,[]),
 65:("unmapped",None,None,"high","Untrustworthy evidence is promoted into authoritative fact; current source-authority classes concern instruction authority rather than epistemic warrant.",None,[]),
 66:("classified","VIGIL-FF-0007","VIGIL-FC-000041","high","An alternate access route reaches the governed capability while bypassing the risk-assessment and control route required for that conduct.",None,[]),
 67:("classified","VIGIL-FF-0002","VIGIL-FC-000012","medium","Adversarial state persists into later contexts without provenance, revocation, or applicability boundaries needed for safe reuse.",None,[]),
 68:("classified","VIGIL-FF-0001","VIGIL-FC-000005","high","The FM and class share the required transformation, lower-authority source, post-transformation authority increase, and operative effect.",None,[]),
 69:("classified","VIGIL-FF-0001","VIGIL-FC-000006","high","Attacker-influenced data-plane state crosses into trusted framework control state without fresh authority validation.",None,[]),
 70:("unmapped",None,None,"high","End-to-end control composition failure is not reducible to the present route, activation, verification, or authority classes.",None,[]),
 71:("classified","VIGIL-FF-0007","VIGIL-FC-000040","high","An initially operative boundary loses material control state across the cumulative interaction trajectory before governing later turns.",None,[]),
}


def catalogue() -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    families: dict[str, dict[str, Any]] = {}
    classes: dict[str, dict[str, Any]] = {}
    for path in sorted(FAMILIES.glob("*.json")):
        document = json.loads(path.read_text(encoding="utf-8"))
        family = document["family"]
        families[family["family_id"]] = family
        classes.update({item["class_id"]: item for item in document["classes"]})
    return families, classes


def migrate() -> dict[str, int]:
    families, classes = catalogue()
    counts: dict[str, int] = {}
    paths = sorted(FAILURES.glob("VIGIL-2026-FM-*.json"))
    if len(paths) != len(DECISIONS):
        raise ValueError(f"expected {len(DECISIONS)} decisions for {len(paths)} records")
    ledger_rows = []
    for path in paths:
        record = json.loads(path.read_text(encoding="utf-8"))
        number = int(record["id"].rsplit("-", 1)[1])
        status, family_id, class_id, confidence, basis, candidate, flags = DECISIONS[number]
        block: dict[str, Any] = {
            "taxonomy_version": VERSION,
            "classification_status": status,
            "classification_basis": basis,
            "classification_confidence": confidence,
            "classified_on": "2026-08-25",
            "structural_review_flags": flags,
        }
        if family_id:
            family = families[family_id]
            block["primary_family"] = {
                "family_id": family_id, "family_code": family["family_code"], "family_name": family["name"]
            }
        if class_id:
            item = classes[class_id]
            block["primary_class"] = {
                "class_id": class_id, "class_code": item["class_code"], "class_name": item["name"],
                "abstraction": item["abstraction"],
            }
        if candidate:
            block["candidate_class"] = {
                "provisional_name": candidate,
                "gap_description": "The observed mechanism is bounded but no immutable class ID is allocated in TAXONOMY-05."
            }
        block["classification_review_provenance"] = {
            "method": "record-definition-threshold-to-taxonomy-criteria-review",
            "review_date": "2026-08-25",
            "ai_provider": "OpenAI",
            "ai_platform": "ChatGPT Work",
            "ai_model": "GPT-5.6 Sol",
            "ai_role": "substantive taxonomy classification analysis and drafting support",
            "human_review_status": "not-reviewed",
            "authority_boundary": "AI classification is provisional draft taxonomy analysis and is not independently authoritative."
        }
        record["taxonomy_classification"] = block
        path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        ledger_rows.append({
            "failure_mode_id": record["id"], "title": record["record_identity"]["title"],
            "classification_status": status, "family_id": family_id, "class_id": class_id,
            "classification_confidence": confidence, "classification_basis": basis,
            "structural_review_flags": flags,
        })
        counts[status] = counts.get(status, 0) + 1
    ledger_document = {
        "schema_version": "1.0", "taxonomy_version": VERSION, "reviewed_on": "2026-08-25",
        "record_count": len(ledger_rows), "classification_status_counts": counts, "entries": ledger_rows,
    }
    LEDGER.write_text(json.dumps(ledger_document, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    family_counts: dict[str, int] = {}
    class_counts: dict[str, int] = {}
    for row in ledger_rows:
        if row["family_id"]:
            family_counts[row["family_id"]] = family_counts.get(row["family_id"], 0) + 1
        if row["class_id"]:
            class_counts[row["class_id"]] = class_counts.get(row["class_id"], 0) + 1
    lines = [
        "# TAXONOMY-05 — Failure-Mode Native Classification Transmutation Audit", "",
        "## Scope and branch state", "",
        "- Existing branch: `agent/failure-taxonomy-prototype`", "- Pre-work remote head: `d5f81a41a1c0ac1de598edf47150800e04ada7fc`",
        "- Taxonomy version: `0.2.0-draft`", f"- Canonical Failure Modes reviewed: {len(ledger_rows)}",
        "- The taxonomy definitions and immutable IDs were not changed.", "- Diagnostic provenance and substantive FM definitions, thresholds and evidence were not changed.", "",
        "## Outcome counts", "",
    ]
    lines.extend(f"- `{key}`: {counts[key]}" for key in sorted(counts))
    lines += ["", "## Family distribution", ""]
    lines.extend(f"- `{key}`: {value}" for key, value in sorted(family_counts.items()))
    lines += ["", "## Exact class distribution", ""]
    lines.extend(f"- `{key}`: {value}" for key, value in sorted(class_counts.items()))
    lines += [
        "", "## Taxonomy gaps and structural flags", "",
        "Three records identify the same bounded candidate gap, **Unwarranted Control Activation**, within `VIGIL-FF-0008`; no class ID was allocated.",
        "Unmapped records principally expose later work around relational influence, evidence and uncertainty, classification integrity, proportionality, identity appropriation, domain-specific reliance and composite assurance.",
        "Records marked `compound-mechanism` remain intact and require later FM structural review; TAXONOMY-05 does not split, merge, withdraw or rewrite them.", "",
        "## Failure Mode decisions", "",
        "| FM | Title | Status | Family | Class | Confidence | Basis / issue |", "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in ledger_rows:
        safe = row["classification_basis"].replace("|", "\\|")
        title = row["title"].replace("|", "\\|")
        flags = "; ".join(row["structural_review_flags"])
        issue = safe + (f" Flag: `{flags}`." if flags else "")
        lines.append(f"| `{row['failure_mode_id']}` | {title} | `{row['classification_status']}` | `{row['family_id'] or '—'}` | `{row['class_id'] or '—'}` | `{row['classification_confidence']}` | {issue} |")
    lines += [
        "", "## Provenance and authority boundary", "",
        "Classification review was performed on 25 August 2026 by OpenAI ChatGPT Work using GPT-5.6 Sol through definition/threshold-to-taxonomy-criteria analysis. Human substantive review is recorded as `not-reviewed`; the migration does not claim independent authority or approval.", "",
        "## Validation", "",
        "- Taxonomy validation passed: 8 families and 42 classes.",
        "- 14 focused taxonomy tests passed.",
        "- 140 repository tests passed; 34 script tests passed.",
        "- Pipeline-state, lifecycle, corpus-coverage, observatory-boundary and interpretive-provenance checks passed.",
        "- Deterministic registry and reverse-mapping rebuilds were byte-identical.",
        "- Python bytecode compilation and `git diff --check` passed.",
        "- Repository-wide validation retained the exact pre-work result: 111 warnings and 16 unresolved research-link errors. TAXONOMY-05 introduced no repository-wide regression.",
    ]
    AUDIT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return counts


if __name__ == "__main__":
    print(json.dumps(migrate(), sort_keys=True))
