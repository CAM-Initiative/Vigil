#!/usr/bin/env python3
"""Read-only, baseline-pinned VIGIL taxonomy coverage and linkage inventory.

This is an AUDIT HELPER, not a validator, a semantic adjudicator, a test or a
publication gate. Output rows describe current records; warning flags are
research queues, NOT permission to amend canonicals or infer failure.
Run inside a Git checkout:
    python vigil/docs/reviews/2026-10-18-incident-taxonomy-reasoning-readjudication/audit-reasoning-inventory.py --out-dir /tmp/vigil-reasoning-inventory

The corpus is ALWAYS read from --ref with 'git show', not working-tree edits.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path

PINNED_REF = "290b8d82c5e238e8ccdea82aa018e491e6d229fb"
INC_PREFIX = "vigil/records/incidents/"
FAMILY_PREFIX = "vigil/taxonomy/families/"
EPISODE_RE = re.compile(r"^E\d{3,}$")
SOURCE_RE = re.compile(r"^source_records\[(\d+)\]$")
ROLE_ALIASES = {
    "ambiguous-boundary exemplar": "ambiguous-boundary",
    "failure-occurrence contribution": "failure-occurrence",
}


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True)


def contents(ref: str, path: str) -> dict:
    return json.loads(git("show", f"{ref}:{path}"))


def filenames(ref: str, prefix: str) -> list[str]:
    return [
        line for line in git("ls-tree", "-r", "--name-only", ref, "--", prefix).splitlines()
        if line.endswith(".json")
    ]


def mapping_rows(record: dict) -> list[tuple[str, dict]]:
    block = record.get("taxonomy_classification") or {}
    primary = block.get("primary_classification")
    secondary = block.get("secondary_classifications") or []
    result = []
    if isinstance(primary, dict) and primary.get("class_id"):
        result.append(("primary", primary))
    result.extend((f"secondary[{i}]", m) for i, m in enumerate(secondary)
                  if isinstance(m, dict) and m.get("class_id"))
    return result


def norm_role(role: str) -> str:
    return ROLE_ALIASES.get(role, role)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--ref", default=PINNED_REF, help="Explicit Git commit containing source data")
    p.add_argument("--out-dir", type=Path, required=True, help="Audit output folder outside canonical records")
    opts = p.parse_args()
    resolved = git("rev-parse", opts.ref).strip()
    incident_paths = filenames(resolved, INC_PREFIX)
    class_paths = filenames(resolved, FAMILY_PREFIX)
    incident_rows, mapping_inventory, episode_inventory = [], [], []
    status_counts, role_counts, version_counts, class_counts = Counter(), Counter(), Counter(), Counter()
    warning_counts = Counter()
    classes = {}
    for path in class_paths:
        family = contents(resolved, path)
        for item in family.get("classes") or []:
            if item.get("class_id"):
                classes[item["class_id"]] = {
                    "class_name": item.get("name"),
                    "family_file": path,
                }

    for path in incident_paths:
        rec = contents(resolved, path)
        rid = rec.get("id") or Path(path).stem
        source_count = len(rec.get("source_records") or [])
        block = rec.get("taxonomy_classification") or {}
        episode_block = (rec.get("vigil_assessment") or {}).get("source_clause_analysis") or {}
        episodes = episode_block.get("clauses") or []
        mappings = mapping_rows(rec)
        version = block.get("taxonomy_version") or "(missing)"
        version_counts[version] += 1
        coverage = (block.get("adjudication_coverage") or {}).get("status") or "(missing)"
        links = defaultdict(list)
        present_episode_ids = set()

        for index, ep in enumerate(episodes):
            eid = ep.get("episode_id") or f"index:{index}"
            if eid in present_episode_ids:
                warning_counts["duplicate_episode_id"] += 1
            present_episode_ids.add(eid)
            adjudication_status = ep.get("adjudication_status") or "(missing)"
            status_counts[adjudication_status] += 1
            relations = ep.get("taxonomy_relationships") or []
            canon = [rel for rel in relations if rel.get("canonical_taxonomy_mapping") is True]
            noncanon = [rel for rel in relations if rel.get("canonical_taxonomy_mapping") is not True]
            if adjudication_status == "mapped" and not canon:
                warning_counts["mapped_episode_without_canonical_relationship"] += 1
            if adjudication_status == "resolved-no-mapping" and canon:
                warning_counts["resolved_no_mapping_with_canonical_relationship"] += 1
            if adjudication_status == "resolved-no-mapping" and any(
                str(rel.get("relationship") or "").startswith("failure-occurrence")
                for rel in noncanon
            ):
                warning_counts["no_mapping_with_failure_contribution_label"] += 1
            srefs = ep.get("source_record_refs") or []
            bad_refs = [
                sr for sr in srefs
                if SOURCE_RE.fullmatch(str(sr)) is None or
                int(SOURCE_RE.fullmatch(str(sr)).group(1)) >= source_count
            ]
            if bad_refs:
                warning_counts["unresolved_episode_source_reference"] += 1
            for rel in canon:
                links[rel.get("class_id")].append((eid, rel))
            episode_inventory.append({
                "incident_id": rid,
                "episode_id": eid,
                "episode_order": index,
                "adjudication_status": adjudication_status,
                "source_record_refs": "|".join(srefs),
                "canonical_class_ids": "|".join(str(c.get("class_id") or "") for c in canon),
                "candidate_class_ids": "|".join(str(c.get("class_id") or "") for c in noncanon),
                "relationship_count": len(relations),
                "has_source_anchor": bool(ep.get("source_anchor")),
                "has_source_paraphrase": bool(ep.get("source_paraphrase")),
                "has_invariant_interpretation": bool(ep.get("recovered_invariant_interpretation")),
                "has_adjudication_note": bool(ep.get("adjudication_note")),
            })
        mapped_ids = {m.get("class_id") for _, m in mappings}
        for mtype, m in mappings:
            cid = m.get("class_id") or ""
            role = m.get("classification_role") or "(missing)"
            role_counts[role] += 1
            class_counts[cid] += 1
            matched = links.get(cid, [])
            warnings = []
            if cid not in classes:
                warnings.append("not_current_selectable_class")
            if not str(m.get("classification_basis") or "").strip():
                warnings.append("empty_mapping_basis")
            if not matched:
                warnings.append("no_canonical_episode_relationship")
            if matched and all(
                norm_role(r.get("relationship") or "") != role for _, r in matched
            ):
                warnings.append("relationship_role_mismatch")
            if not m.get("classification_confidence"):
                warnings.append("missing_confidence")
            for flag in warnings:
                warning_counts[flag] += 1
            mapping_inventory.append({
                "incident_id": rid,
                "record_path": path,
                "mapping_position": mtype,
                "taxonomy_version": version,
                "classification_status": block.get("classification_status"),
                "coverage_status": coverage,
                "class_id": cid,
                "class_name_current": classes.get(cid, {}).get("class_name") or "",
                "role": role,
                "confidence": m.get("classification_confidence") or "",
                "mapping_basis": m.get("classification_basis") or "",
                "episode_ids": "|".join(eid for eid, _ in matched),
                "source_refs_from_episodes": "|".join(sorted({
                    sr for eid, _ in matched
                    for ep in episodes if ep.get("episode_id") == eid
                    for sr in ep.get("source_record_refs", [])
                })),
                "audit_warnings": "|".join(warnings),
                "SEMANTIC_REVIEW_STATUS": "NOT ADJUDICATED BY THIS SCRIPT",
            })
        orphan_links = set(links) - mapped_ids
        if orphan_links:
            warning_counts["episode_links_without_canonical_mapping"] += len(orphan_links)
        incident_rows.append({
            "incident_id": rid,
            "record_path": path,
            "taxonomy_version": version,
            "classification_status": block.get("classification_status"),
            "coverage": coverage,
            "episode_count": len(episodes),
            "mapping_count": len(mappings),
            "source_count": source_count,
            "episode_statuses": dict(Counter(ep.get("adjudication_status") or "(missing)" for ep in episodes)),
            "canonical_episode_classes_missing_from_mappings": sorted(x for x in orphan_links if x),
        })

    summary = {
        "artefact": "READ-ONLY STRUCTURAL INVENTORY — NOT SEMANTIC ADJUDICATION",
        "baseline_commit": resolved,
        "counts": {
            "incident_files": len(incident_paths),
            "taxonomy_families": len(class_paths),
            "current_selectable_classes": len(classes),
            "mapping_rows": len(mapping_inventory),
            "material_source_episodes": len(episode_inventory),
            "adjudication_statuses": dict(status_counts),
            "mapping_roles": dict(role_counts),
            "incident_taxonomy_versions": dict(version_counts),
            "structural_warning_counts": dict(warning_counts),
        },
        "incident_rows": incident_rows,
        "notes": [
            "No role, class, confidence, polarity, fidelity or evidence quality is inferred by this script.",
            "Mapping and episode warning counts are research queues, not validator failures.",
            "Each entry still needs source-first examination against current recognition and exclusions.",
            "No canonical file or public website output has been changed.",
        ],
    }
    opts.out_dir.mkdir(parents=True, exist_ok=True)
    (opts.out_dir / "summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    for name, rows in [
        ("mapping-inventory.csv", mapping_inventory),
        ("episode-inventory.csv", episode_inventory),
    ]:
        dest = opts.out_dir / name
        if rows:
            with dest.open("w", encoding="utf-8", newline="") as fd:
                wr = csv.DictWriter(fd, fieldnames=list(rows[0]))
                wr.writeheader()
                wr.writerows(rows)
        else:
            dest.write_text("", encoding="utf-8")
    print(json.dumps(summary["counts"], indent=2))


if __name__ == "__main__":
    main()
