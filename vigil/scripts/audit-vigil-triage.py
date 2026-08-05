#!/usr/bin/env python3
"""Generate the deterministic VIGIL triage migration inventory."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_JSON = ROOT / "vigil" / "docs" / "2026-triage-model-inventory.json"
DEFAULT_MARKDOWN = ROOT / "vigil" / "docs" / "2026-triage-model-inventory.md"

ALLOWED_PRIORITIES = ("P0", "P1", "P2", "P3", "P4", "none")
ALLOWED_STATUSES = (
    "needs-review",
    "active-investigation",
    "awaiting-evidence",
    "ready-for-routing",
    "routed",
    "repair-in-progress",
    "verification-required",
    "monitoring",
    "deferred",
    "closed",
)
ACTIVE_PRIORITIES = {"P0", "P1", "P2", "P3"}
ACTIVE_NONE_FORBIDDEN = {"active-investigation", "repair-in-progress", "verification-required"}
PREFERRED_SEVERITIES = (
    "critical",
    "high",
    "moderate",
    "low",
    "negligible",
    "to-be-assessed",
    "not-applicable",
)


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise TypeError(f"{path} must contain one JSON object")
    return value


def record_files(root: Path, record_class: str) -> list[Path]:
    return sorted((root / "vigil" / "records" / record_class).rglob("*.json"))


def count(values: Iterable[Any]) -> dict[str, int]:
    counts = Counter("<missing>" if value is None or value == "" else str(value) for value in values)
    return dict(sorted(counts.items(), key=lambda item: (-item[1], item[0])))


def grouped_count(rows: list[dict[str, Any]], *keys: str) -> list[dict[str, Any]]:
    counts: Counter[tuple[str, ...]] = Counter()
    for row in rows:
        values = tuple("<missing>" if row.get(key) in (None, "") else str(row[key]) for key in keys)
        counts[values] += 1
    return [
        {**dict(zip(keys, values)), "count": total}
        for values, total in sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    ]


def text_present(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def monitoring_like(row: dict[str, Any]) -> bool:
    status = str(row.get("triage_status") or "").lower()
    return row.get("record_state") == "monitoring" or "monitor" in status or "watch" in status


def linked_patch_ids(record: dict[str, Any]) -> list[str]:
    linked = record.get("linked_records") if isinstance(record.get("linked_records"), dict) else {}
    repair = record.get("repair_status") if isinstance(record.get("repair_status"), dict) else {}
    candidates = []
    for values in (linked.get("related_patch_notes", []), repair.get("repaired_by", [])):
        if isinstance(values, list):
            candidates.extend(value for value in values if isinstance(value, str) and "-PATCH-" in value)
    return sorted(set(candidates))


def learn_by_failure(root: Path) -> dict[str, dict[str, Any]]:
    mapping: dict[str, dict[str, Any]] = {}
    for path in record_files(root, "learn"):
        learn = load_json(path)
        ids = []
        primary = learn.get("primary_failure_mode")
        if isinstance(primary, str):
            ids.append(primary)
        related = learn.get("related_failure_modes")
        if isinstance(related, list):
            ids.extend(value for value in related if isinstance(value, str))
        for failure_id in ids:
            mapping.setdefault(failure_id, learn)
    return mapping


def review_flags(row: dict[str, Any]) -> list[str]:
    flags: list[str] = []
    priority = row.get("triage_priority")
    status = row.get("triage_status")
    state = str(row.get("record_state") or "")
    next_step = row.get("recommended_next_step")

    if priority not in ALLOWED_PRIORITIES:
        flags.append("invalid-priority")
    if status not in ALLOWED_STATUSES:
        flags.append("invalid-status")
    if priority in (None, ""):
        flags.append("missing-priority")
    if status in (None, ""):
        flags.append("missing-status")
    if state.startswith("closed") and priority != "none":
        flags.append("closed-state-active-priority")
    if monitoring_like(row) and priority in {"P0", "P1"}:
        flags.append("monitoring-p0-p1")
    if priority in ACTIVE_PRIORITIES and not text_present(next_step):
        flags.append("active-priority-without-next-step")
    if priority == "none" and status in ACTIVE_NONE_FORBIDDEN:
        flags.append("none-with-active-status")
    if priority in {"High", "Medium", "Low", "Critical", "Urgent", "high", "medium", "low"}:
        flags.append("priority-may-contain-severity")
    if priority in {"closed", "monitoring"}:
        flags.append("priority-contains-workflow-status")
    if row.get("repair_status") == "repaired" and priority in ACTIVE_PRIORITIES:
        flags.append("repaired-with-active-priority-review")
    if row.get("severity") not in PREFERRED_SEVERITIES:
        flags.append("legacy-severity-mapping-required")
    return flags


def build_inventory(root: Path = ROOT) -> dict[str, Any]:
    patches = {load_json(path).get("id") for path in record_files(root, "patches")}
    learns = learn_by_failure(root)
    rows: list[dict[str, Any]] = []

    for path in record_files(root, "failures"):
        record = load_json(path)
        triage = record.get("triage") if isinstance(record.get("triage"), dict) else {}
        classification = (
            record.get("failure_classification")
            if isinstance(record.get("failure_classification"), dict)
            else {}
        )
        repair = record.get("repair_status") if isinstance(record.get("repair_status"), dict) else {}
        ecosystem = (
            record.get("ecosystem_status") if isinstance(record.get("ecosystem_status"), dict) else {}
        )
        patch_ids = linked_patch_ids(record)
        learn = learns.get(str(record.get("id")))
        linked_patches_exist = bool(patch_ids) and all(patch_id in patches for patch_id in patch_ids)
        learn_complete = bool(learn and learn.get("chain_state") == "complete")
        row = {
            "record_id": record.get("id"),
            "record_type": record.get("record_type"),
            "record_state": record.get("record_state"),
            "triage_priority": triage.get("triage_priority"),
            "triage_status": triage.get("triage_status"),
            "severity": classification.get("severity"),
            "repair_status": repair.get("status"),
            "ecosystem_status": ecosystem.get("status"),
            "monitoring_required": ecosystem.get("monitoring_required"),
            "recommended_next_step": triage.get("recommended_next_step"),
            "linked_patch_ids": patch_ids,
            "linked_patch_records_exist": linked_patches_exist,
            "learn_record_id": learn.get("id") if learn else None,
            "learn_record_exists": bool(learn),
            "evidence_chain_appears_complete": linked_patches_exist and learn_complete,
            "source_path": path.relative_to(root).as_posix(),
        }
        row["review_flags"] = review_flags(row)
        rows.append(row)

    rows.sort(key=lambda row: str(row.get("record_id") or ""))
    flag_counts = count(flag for row in rows for flag in row["review_flags"])
    return {
        "inventory_contract": "VIGIL triage semantic migration — Pass 1 model and inventory",
        "governing_rule": (
            "Current triage priority is mutable operational state. Historical urgency is provenance. "
            "Failure severity is classification. Triage status is workflow. Ecosystem monitoring is "
            "continuing external observation."
        ),
        "scope": {
            "record_class": "failure_mode",
            "record_count": len(rows),
            "note": (
                "VIGIL's record-boundary contract forbids failure-mode triage in OBS and PROP/PATCH "
                "records. This inventory therefore audits every current failure mode."
            ),
        },
        "target_vocabularies": {
            "triage_priority": list(ALLOWED_PRIORITIES),
            "triage_status": list(ALLOWED_STATUSES),
            "severity": list(PREFERRED_SEVERITIES),
        },
        "migration_safety": {
            "phase": "pass-1-inventory-only",
            "records_reconciled": False,
            "historical_transitions_fabricated": False,
            "note": "Flags identify review candidates; they do not decide replacement values.",
        },
        "grouped_counts": {
            "priority": count(row.get("triage_priority") for row in rows),
            "status": count(row.get("triage_status") for row in rows),
            "severity": count(row.get("severity") for row in rows),
            "priority_status": grouped_count(rows, "triage_priority", "triage_status"),
            "priority_by_record_state": grouped_count(rows, "record_state", "triage_priority"),
            "priority_by_repair_status": grouped_count(rows, "repair_status", "triage_priority"),
            "priority_by_monitoring_state": grouped_count(rows, "monitoring_required", "triage_priority"),
            "review_flags": flag_counts,
        },
        "records": rows,
    }


def escape(value: Any) -> str:
    if value is None:
        return "—"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, list):
        value = ", ".join(str(item) for item in value) if value else "—"
    return str(value).replace("|", "\\|").replace("\n", " ")


def markdown_table(headers: list[str], rows: Iterable[Iterable[Any]]) -> list[str]:
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    lines.extend("| " + " | ".join(escape(value) for value in row) + " |" for row in rows)
    return lines


def render_markdown(inventory: dict[str, Any]) -> str:
    counts = inventory["grouped_counts"]
    records = inventory["records"]
    lines = [
        "# VIGIL Triage Model Inventory — Pass 1",
        "",
        "> " + inventory["governing_rule"],
        "",
        "This is a deterministic pre-migration inventory. It records the current branch state and review flags; it does not assign replacement priority, status, or severity values.",
        "",
        "## Scope and boundary",
        "",
        f"All {len(records)} current failure-mode records are included. VIGIL's record-boundary contract forbids failure-mode triage in OBS and PROP/PATCH records, so those classes are not given synthetic triage state.",
        "",
        "## Headline findings",
        "",
        f"* Invalid current priority values: {counts['review_flags'].get('invalid-priority', 0)}.",
        f"* Status values outside the target workflow vocabulary: {counts['review_flags'].get('invalid-status', 0)}.",
        f"* Monitoring/watch records retaining P0 or P1: {counts['review_flags'].get('monitoring-p0-p1', 0)}.",
        f"* Repaired records retaining an active priority and requiring reconciliation review: {counts['review_flags'].get('repaired-with-active-priority-review', 0)}.",
        f"* Active P0–P3 records without a recommended next step: {counts['review_flags'].get('active-priority-without-next-step', 0)}.",
        f"* Records requiring a reviewed severity mapping: {counts['review_flags'].get('legacy-severity-mapping-required', 0)}.",
        "",
        "## Priority counts",
        "",
        *markdown_table(["Priority", "Count"], counts["priority"].items()),
        "",
        "## Status counts",
        "",
        *markdown_table(["Status", "Count"], counts["status"].items()),
        "",
        "## Severity counts and migration boundary",
        "",
        *markdown_table(["Severity", "Count"], counts["severity"].items()),
        "",
        "The target severity vocabulary is `critical`, `high`, `moderate`, `low`, `negligible`, `to-be-assessed`, and `not-applicable`. Existing `medium`, `medium-high`, `low-to-medium`, conditional prose ratings, and `to be assessed` are not rewritten in Pass 1. `medium-high`, `low-to-medium`, and conditional prose ratings require record-level judgment rather than blind mapping.",
        "",
        "## Priority by record state",
        "",
        *markdown_table(
            ["Record state", "Priority", "Count"],
            ([row["record_state"], row["triage_priority"], row["count"]] for row in counts["priority_by_record_state"]),
        ),
        "",
        "## Priority by repair status",
        "",
        *markdown_table(
            ["Repair status", "Priority", "Count"],
            ([row["repair_status"], row["triage_priority"], row["count"]] for row in counts["priority_by_repair_status"]),
        ),
        "",
        "## Priority by monitoring state",
        "",
        *markdown_table(
            ["Monitoring required", "Priority", "Count"],
            ([row["monitoring_required"], row["triage_priority"], row["count"]] for row in counts["priority_by_monitoring_state"]),
        ),
        "",
        "## Review-flag definitions",
        "",
        "Flags are diagnostic only. `repaired-with-active-priority-review` does not assume that `none` is correct; a concrete verification or routing task may justify an active priority. `monitoring-p0-p1` includes both lifecycle monitoring and legacy watch/monitor status phrases. `legacy-severity-mapping-required` preserves severity until the migration mapping is reviewed.",
        "",
        "## Record inventory",
        "",
        *markdown_table(
            [
                "Record", "State", "Priority", "Triage status", "Severity", "Repair", "Ecosystem", "Monitoring", "Next step", "PATCH", "LEARN", "Chain appears complete", "Review flags"
            ],
            (
                [
                    row["record_id"], row["record_state"], row["triage_priority"], row["triage_status"], row["severity"], row["repair_status"], row["ecosystem_status"], row["monitoring_required"], row["recommended_next_step"], row["linked_patch_ids"], row["learn_record_id"], row["evidence_chain_appears_complete"], row["review_flags"]
                ]
                for row in records
            ),
        ),
        "",
        "## Pass 2 and Pass 3 boundary",
        "",
        "Pass 2 may enforce the target vocabularies and cross-field invariants in schemas, templates, validators, tests, and registry projection. Pass 3 must reconcile each flagged record according to its actual outstanding CAM/VIGIL work. No historical transition may be invented from this inventory.",
        "",
    ]
    return "\n".join(lines)


def render_json(inventory: dict[str, Any]) -> str:
    return json.dumps(inventory, indent=2, ensure_ascii=False) + "\n"


def write_or_check(path: Path, content: str, check: bool) -> bool:
    if check:
        return path.exists() and path.read_text(encoding="utf-8") == content
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--json-output", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--markdown-output", type=Path, default=DEFAULT_MARKDOWN)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    inventory = build_inventory(args.root.resolve())
    outputs = (
        (args.json_output, render_json(inventory)),
        (args.markdown_output, render_markdown(inventory)),
    )
    stale = [str(path) for path, content in outputs if not write_or_check(path, content, args.check)]
    if stale:
        print("Triage inventory is stale: " + ", ".join(stale))
        return 1
    print(f"VIGIL triage inventory {'verified' if args.check else 'generated'}: {len(inventory['records'])} records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
