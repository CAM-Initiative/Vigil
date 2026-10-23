#!/usr/bin/env python3
"""Read-only research-release curation inventory; no automatic deletion."""
from __future__ import annotations
from collections import Counter
from pathlib import Path
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[3]
BASELINE = "f031c4421f772e1af5b945bc388363aa81e1a179"
OUT = Path(__file__).resolve().parent / "REPOSITORY-RETENTION-AUDIT.json"

def git(*args: str) -> bytes:
    return subprocess.check_output(["git", *args], cwd=ROOT)

def collect_values(obj, label="", refs=None):
    if refs is None:
        refs = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, str) and (
                v.startswith("vigil/docs/reviews/") or
                (k in {"review_reference", "review_manifest", "decision_packet"} and v.strip())
            ):
                refs.append({"field": k, "value": v})
            collect_values(v, k, refs)
    elif isinstance(obj, list):
        for item in obj:
            collect_values(item, label, refs)
    return refs

def main() -> None:
    changed = git("diff", "--name-only", BASELINE, "HEAD", "--", "vigil/records",
                  "vigil/taxonomy", "vigil/docs/reviews", "vigil/cam_assessment")
    if changed.strip():
        raise SystemExit("Research baseline changed; refuse curation inventory")
    paths = [x.decode("utf-8") for x in git("ls-files", "-z").split(b"\0") if x]
    subdirs = ["vigil/cam_assessment/", "vigil/tests/", "vigil/docs/reviews/"]
    folder_counts = {}
    for prefix in subdirs:
        found = [p for p in paths if p.startswith(prefix)]
        folder_counts[prefix] = {
            "tracked_files": len(found),
            "size_bytes": sum((ROOT / p).stat().st_size for p in found),
            "file_paths": found if prefix == "vigil/cam_assessment/" else None,
        }
    record_data = []
    all_ref_items = []
    for p in sorted(x for x in paths if re.fullmatch(r"vigil/records/incidents/VIGIL-INC-[0-9]{6}\.json", x)):
        r = json.loads((ROOT / p).read_text(encoding="utf-8"))
        identity = r.get("record_identity") or {}
        cl = r.get("taxonomy_classification") or {}
        item = {
            "id": r.get("id") or identity.get("record_id"),
            "title": identity.get("title") or r.get("summary", {}).get("title"),
            "record_version": identity.get("version"),
            "recorded_taxonomy_version": cl.get("taxonomy_version"),
            "classification_status": cl.get("classification_status") or "unspecified",
            "primary_class_id": (cl.get("primary_classification") or {}).get("class_id"),
            "classification_review_provenance": (cl.get("classification_review_provenance") or {}).get("review_reference"),
        }
        record_data.append(item)
        for ref in collect_values(r):
            all_ref_items.append({"incident": item["id"], **ref})
    by_status = Counter(x["classification_status"] for x in record_data)
    by_version = Counter(str(x["recorded_taxonomy_version"]) for x in record_data)
    awaiting = [x for x in record_data if x["classification_status"] in
                {"provisionally-classified", "human-review-required", "classification-disputed"}]
    # Some historical enums are spelled differently; retain exact current values.
    pending = [x for x in record_data if x["classification_status"] not in {"classified", "unclassified"}]
    current_version = [x for x in record_data if x["recorded_taxonomy_version"] == "0.8.0"]
    review_prefix = "vigil/docs/reviews/"
    review_files = {p for p in paths if p.startswith(review_prefix)}
    referenced = set()
    missing = set()
    for ref in all_ref_items:
        value = ref["value"].split("#", 1)[0].strip()
        if value.startswith(review_prefix):
            (referenced if value in review_files else missing).add(value)
    # Non-review source references include tests, maintenance scripts, docs and workflows.
    code_ref = {}
    needle = re.compile(r"vigil/docs/reviews/[A-Za-z0-9_./-]+")
    for p in paths:
        if p.startswith(review_prefix) or p.startswith("vigil/records/incidents/"):
            continue
        path = ROOT / p
        if path.stat().st_size > 2000000:
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for raw in needle.findall(content):
            target = raw.rstrip(".,:)]}")
            if target in review_files:
                code_ref.setdefault(target, []).append(p)
    cam_refs = []
    for p in paths:
        if p.startswith("vigil/docs/reviews/") or p.startswith("vigil/records/incidents/"):
            continue
        q = ROOT / p
        if q.stat().st_size > 2000000:
            continue
        try:
            text = q.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        if any(n in text for n in ("cam_assessment", "cam-assessments", "CAM applicability/coverage")):
            cam_refs.append(p)
    payload = {
        "pinned_scientific_base": BASELINE,
        "status": "audit-only; no curation, adjudication or release authorised",
        "folder_inventory": folder_counts,
        "incident_counts": {
            "total": len(record_data),
            "classification_statuses": dict(sorted(by_status.items())),
            "recorded_taxonomy_versions": dict(sorted(by_version.items())),
            "using_0_8_0": len(current_version),
        },
        "taxonomy_0_8_0_records": current_version,
        "nonfinal_status_records": pending,
        "unclassified_records": [x for x in record_data if x["classification_status"] == "unclassified"],
        "all_records": record_data,
        "cam_assessment_code_dependencies": cam_refs,
        "canonical_review_reference_entries": all_ref_items,
        "referenced_review_files_from_incidents": sorted(referenced),
        "missing_review_reference_paths": sorted(missing),
        "review_files_referenced_from_other_code": code_ref,
    }
    if len(record_data) != 200:
        raise SystemExit(f"Expected 200 incidents, found {len(record_data)}")
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    print("FOLDER_COUNTS " + json.dumps({k: {"files": v["tracked_files"], "bytes":v["size_bytes"]}
            for k, v in folder_counts.items()}))
    print("CLASSIFICATION_STATUSES " + json.dumps(payload["incident_counts"]))
    print("TAXONOMY_080 " + json.dumps([x["id"] for x in current_version]))
    print("NONFINAL_STATUSES " + json.dumps(
        {s: [x["id"] for x in pending if x["classification_status"] == s] for s in sorted(by_status)}))
    print("REVIEW_REFERENCES " + json.dumps({"source_entries":len(all_ref_items),
        "resolved_files":len(referenced),"missing_paths":len(missing),
        "test_or_code_referenced_files":len(code_ref)}))
    print("CAM_DEPENDENCIES " + json.dumps(cam_refs))

if __name__ == "__main__":
    main()
