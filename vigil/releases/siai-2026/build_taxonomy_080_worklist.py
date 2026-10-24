#!/usr/bin/env python3
"""Construct a deterministic current-taxonomy reconciliation queue; NO adjudication."""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
INCIDENTS = ROOT / "vigil" / "records" / "incidents"
DEST = Path(__file__).resolve().parent / "TAXONOMY-080-WORKLIST.json"
FOCAL = {"VIGIL-INC-000003", "VIGIL-INC-000117", "VIGIL-INC-000129"}
NONFINAL = {"provisionally-classified", "requires-human-review", "classification-disputed"}
# The published v0.8.0 criteria are immutable and remain the scientific basis
# of the dated 080 campaign. This SHA is an ancestor of the release branch,
# not an arbitrary current-branch ref that can silently advance to v0.8.1.
PUBLISHED_080_REF = "6aff1c4d6ff85a94e0892d558a3bfa651d0b557d"
PAPER_081_BASELINE_REF = "bf58646d22c90a86c8333ac9bc7fe83ac856589c"
PAPER_081_DIR = ROOT / "vigil/docs/reviews/2026-10-24-siai-paper-v081"
PAPER_FOCALS = {"VIGIL-INC-000003", "VIGIL-INC-000117", "VIGIL-INC-000129"}
CRITERION_FIELDS = ("failure_recognition", "success_recognition", "exclusions")


def published_080_classes() -> dict[str, dict]:
    """Load exact published v0.8.0 class criteria from pinned Git history.

    Fail closed if the baseline is unavailable, off-history or not v0.8.0.
    A historical review packet never acquires v0.8.1 screening credit.
    """
    subprocess.run(
        ["git", "merge-base", "--is-ancestor", PUBLISHED_080_REF, "HEAD"],
        cwd=ROOT, check=True,
    )

    def git_json(path: str) -> dict:
        raw = subprocess.check_output(
            ["git", "show", f"{PUBLISHED_080_REF}:{path}"], cwd=ROOT, text=True,
        )
        return json.loads(raw)

    index = git_json("vigil/taxonomy/VIGIL.FailureTaxonomy.Index.json")
    if index.get("standard", {}).get("version") != "0.8.0":
        raise SystemExit("Pinned taxonomy baseline is not published v0.8.0")
    paths = subprocess.check_output(
        ["git", "ls-tree", "-r", "--name-only", PUBLISHED_080_REF,
         "--", "vigil/taxonomy/families"],
        cwd=ROOT, text=True,
    ).splitlines()
    if len(paths) != 17 or any(not p.endswith(".json") for p in paths):
        raise SystemExit("Unexpected historical v0.8.0 taxonomy family inventory")
    classes = {}
    for path in paths:
        for klass in git_json(path)["classes"]:
            cid = klass["class_id"]
            if cid in classes:
                raise SystemExit(f"Duplicate class in v0.8.0 baseline: {cid}")
            classes[cid] = klass
    if len(classes) != 80:
        raise SystemExit("Expected 80 classes in the pinned v0.8.0 baseline")
    return classes


def priority(rec: dict) -> tuple[int, str]:
    rid, status, version = rec["incident_id"], rec["classification_status"], rec["recorded_taxonomy_version"]
    if rid in FOCAL:
        return 0, "SIAI case-study crosscheck"
    if status in NONFINAL:
        return 1, "unresolved or provisional status"
    if status == "unclassified":
        return 2, "evidence-bounded no-mapping review"
    if version != "0.8.0":
        return 3, "legacy-classification current-ruleset screen"
    return 4, "current-version integrity screen"

def build() -> dict:
    commit = subprocess.check_output(["git","rev-parse","HEAD^{commit}"], cwd=ROOT, text=True).strip()
    baseline_080 = published_080_classes()
    current_index = json.loads(
        (ROOT / "vigil/taxonomy/VIGIL.FailureTaxonomy.Index.json").read_text(encoding="utf-8")
    )
    if current_index.get("standard", {}).get("version") != "0.8.1":
        raise SystemExit("Expected v0.8.1 as the presently published taxonomy")
    taxonomy_classes = {
        c["class_id"]: c
        for path in sorted((ROOT / "vigil/taxonomy/families").glob("*.json"))
        for c in json.loads(path.read_text(encoding="utf-8"))["classes"]
    }
    if len(taxonomy_classes) != 80 or set(taxonomy_classes) != set(baseline_080):
        raise SystemExit("Unexpected v0.8.1 class count or identity change")
    # A criteria change is an impact signal, never evidence that a historical
    # source/criterion review was re-executed. Non-criterion class changes
    # do not mechanically invalidate existing clause-level reasoning.
    changed_081 = {
        cid: [key for key in CRITERION_FIELDS
              if taxonomy_classes[cid][key] != baseline_080[cid][key]]
        for cid in sorted(taxonomy_classes)
    }
    changed_081 = {cid: keys for cid, keys in changed_081.items() if keys}
    class_fingerprints = {
        cid: hashlib.sha256(json.dumps(c, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
        for cid, c in sorted(taxonomy_classes.items())
    }
    rows = []
    for path in sorted(INCIDENTS.glob("VIGIL-INC-*.json")):
        raw = path.read_bytes()
        data = json.loads(raw)
        identity = data.get("record_identity") or {}
        cl = data.get("taxonomy_classification") or {}
        record_id = data.get("id") or identity.get("record_id") or path.stem
        record = {
            "incident_id": record_id,
            "canonical_path": str(path.relative_to(ROOT)).replace("\\", "/"),
            "canonical_sha256": hashlib.sha256(raw).hexdigest(),
            "record_version": identity.get("version"),
            "title": identity.get("title") or (data.get("summary") or {}).get("title"),
            "classification_status": cl.get("classification_status") or "unspecified",
            "recorded_taxonomy_version": cl.get("taxonomy_version") or "unspecified",
            "primary_fidelity_class": (cl.get("primary_classification") or {}).get("class_id"),
            "secondary_class_ids": [x.get("class_id") for x in (cl.get("secondary_classifications") or [])],
            "source_record_count": len(data.get("source_records") or []),
            "current_080_screen_result": "NOT-REVIEWED",
            "human_assurance_not_inferred": True,
        }
        rank, reason = priority(record)
        record["priority"] = rank
        record["priority_reason"] = reason
        # Discovery inputs are evidence pointers, never inferred adjudications.
        # Preserve all source episodes and pre-existing candidates for the next
        # semantic reviewer; a candidate's presence confers no screening credit.
        clauses = (data.get("vigil_assessment", {}).get("source_clause_analysis") or {}).get("clauses", [])
        candidates = sorted({
            rel["class_id"] for clause in clauses
            for rel in clause.get("taxonomy_relationships", []) if rel.get("class_id")
        } | {cid for cid in [record["primary_fidelity_class"], *record["secondary_class_ids"]] if cid})
        record["review_inputs"] = {
            "discovery_state": "EXISTING-RECORD-LEADS-NOT-ADJUDICATION",
            "candidate_class_ids_from_record": candidates,
            "candidate_class_sha256": {cid: class_fingerprints.get(cid) for cid in candidates},
            "additional_current_classes_require_semantic_discovery": True,
            "sources": [{"ref": f"source_records[{i}]", "url": source.get("source_url")}
                        for i, source in enumerate(data.get("source_records", []))],
            "episodes": [{"episode_id": c.get("episode_id"),
                          "source_record_refs": c.get("source_record_refs", []),
                          "source_paraphrase": c.get("source_paraphrase"),
                          "adjudication_status": c.get("adjudication_status"),
                          "taxonomy_relationships": c.get("taxonomy_relationships", [])}
                         for c in clauses],
            "prior_taxonomy_review": cl.get("classification_review_provenance"),
        }
        rows.append(record)
    if len(rows) != 200:
        raise SystemExit(f"Unexpected corpus size {len(rows)}; update count only through governed intake")
    if len({r["incident_id"] for r in rows}) != len(rows):
        raise SystemExit("Duplicate canonical incident IDs")
    # Three named paper cases received separately governed 0.8.1 promotions.
    # Their 0.8.0 review is verified against the exact pre-promotion commit.
    promoted_081 = {}
    for rid in sorted(PAPER_FOCALS):
        case_number = rid.rsplit("-", 1)[-1]
        path = PAPER_081_DIR / f"INC-{case_number}-081-REVIEW.json"
        packet = json.loads(path.read_text(encoding="utf-8"))
        row = next((r for r in rows if r["incident_id"] == rid), None)
        if row is None or packet.get("incident_id") != rid:
            raise SystemExit(f"Missing focal Incident or v0.8.1 packet: {rid}")
        if (packet.get("published_taxonomy_version") != "0.8.1"
            or packet.get("baseline", {}).get("ref") != PAPER_081_BASELINE_REF
            or packet.get("canonical_promotion", {}).get("status") != "approved-bounded-canonical-update"
            or row["record_version"] != packet["canonical_promotion"].get("target_record_version")
            or row["recorded_taxonomy_version"] != "0.8.1"):
            raise SystemExit(f"Invalid promoted focal packet or current version: {rid}")
        current = json.loads((ROOT / row["canonical_path"]).read_text(encoding="utf-8"))
        if (current["taxonomy_classification"]["classification_review_provenance"].get("review_reference")
            != str(path.relative_to(ROOT))):
            raise SystemExit(f"Focal review provenance does not point to packet: {rid}")
        promoted_081[rid] = (path, packet)
    # Historical v0.8.0 screening results remain valid only against their
    # original canonical fingerprint and original criteria.
    # Explicit replacement packets preserve the earlier audit and bind the complete
    # canonical record plus exact reviewed class content. This is a campaign
    # credit check, not a new canonical validity or classification rule.
    packet_dir = ROOT / "vigil/docs/reviews/2026-10-23-taxonomy-080-reconciliation"
    current_packets = {}
    for packet_path in sorted([*packet_dir.glob("FOCAL-*-080.json"), *packet_dir.glob("BATCH-*-080.json")]):
        packet = json.loads(packet_path.read_text(encoding="utf-8"))
        rid = packet.get("incident_id")
        if rid in current_packets:
            raise SystemExit(f"Duplicate replacement packet: {rid}")
        current_packets[rid] = (packet_path, packet)
    # Overlay only a dated, explicitly reviewed decision packet, not AI-inferred
    # completion from a matching taxonomy version or changed status label.
    review_path = ROOT / "vigil/docs/reviews/2026-10-23-taxonomy-080-reconciliation/TRANCHE-01-DECISIONS.json"
    if review_path.exists():
        review = json.loads(review_path.read_text(encoding="utf-8"))
        if review.get("screening_taxonomy") not in (None, "0.8.0") or review.get("state") != "SOURCE_AND_CRITERION_SCREEN_COMPLETE_CANONICAL_FINDINGS_UNCHANGED":
            raise SystemExit("Malformed campaign review packet authority or current taxonomy scope")
        index = {r["incident_id"]: r for r in rows}
        seen = set()
        for decision in review.get("checked_records", []):
            rid = decision.get("incident_id")
            if rid in seen or rid not in index:
                raise SystemExit(f"Unknown or duplicate screened Incident: {rid}")
            seen.add(rid)
            row = index[rid]
            if rid in current_packets:
                replacement = current_packets[rid][1]
                if (replacement.get("supersedes_screen_packet") != str(review_path.relative_to(ROOT))
                    or replacement["baseline"]["record_version"] != decision["baseline_record_revision"]):
                    raise SystemExit(f"Unaccounted screen supersession: {rid}")
                continue
            if row["record_version"] != decision.get("baseline_record_revision"):
                raise SystemExit(f"Review stale for {rid}: record version changed; update substantive disposition")
            if row["recorded_taxonomy_version"] != decision.get("baseline_taxonomy_edition"):
                raise SystemExit(f"Review stale for {rid}: adjudication taxonomy edition changed")
            if row["classification_status"] != decision.get("current_status"):
                raise SystemExit(f"Review stale for {rid}: classification state changed")
            if decision.get("has_canonical_record_been_modified") is not False:
                raise SystemExit(f"Review packet improperly claims no canonical change for {rid}")
            row["current_080_screen_result"] = decision["screening_outcome"]
            row["current_080_screen_date"] = decision["screening_date"]
            row["screening_decision_packet"] = str(review_path.relative_to(ROOT))
            row["screening_assurance"] = "AI-assessed; no independent human verification implied"
    # Separate genuinely restamped current-edition adjudications from screening
    # only. Never accept a packet merely because a version string happens to match.
    by_id = {r["incident_id"]: r for r in rows}
    packet_dir = ROOT / "vigil/docs/reviews/2026-10-23-taxonomy-080-reconciliation"
    for packet_path in sorted(packet_dir.glob("INC-*-CURRENT-080-DECISION.json")):
        packet = json.loads(packet_path.read_text(encoding="utf-8"))
        rid = packet.get("incident_id")
        if rid not in by_id:
            raise SystemExit(f"Unknown Incident in reviewed packet {packet_path}")
        row = by_id[rid]
        canonical = json.loads((ROOT / row["canonical_path"]).read_text(encoding="utf-8"))
        rev = canonical.get("taxonomy_classification") or {}
        source_mappings = [rev.get("primary_classification"), *(rev.get("secondary_classifications") or [])]
        source_mappings = [x for x in source_mappings if isinstance(x, dict)]
        decisions = (packet.get("baseline_mapping_dispositions")
                     or packet.get("previous_mapping_dispositions") or [])
        recorded_pairs = [(x.get("class_id"), x.get("classification_role")) for x in source_mappings]
        audited_pairs = [(x.get("class_id"), x.get("previous_role") or x.get("role"))
                         for x in decisions]
        new_mappings = packet.get("new_taxonomy_mappings") or []
        for added in new_mappings:
            if added.get("disposition") != "new-admission":
                raise SystemExit(f"Non-admitted new mapping listed in {packet_path}")
            audited_pairs.append((added.get("class_id"), added.get("classification_role")))
        if len(set(audited_pairs)) != len(audited_pairs):
            raise SystemExit(f"Duplicate adjudicated mapping in {packet_path}")
        criteria = packet.get("adjudicated_taxonomy") or packet.get("current_criteria") or {}
        candidate_version = criteria.get("published_version") or criteria.get("version")
        outcome = packet.get("current_decision") or packet.get("adjudicated_outcome") or {}
        previous_version = packet["baseline"]["record_version"]
        current_version = row["record_version"]
        oldparts, newparts = previous_version.split("."), current_version.split(".")
        expected_revision = (oldparts[:-1] == newparts[:-1]
                             and int(newparts[-1]) == int(oldparts[-1]) + 1)
        if (candidate_version != "0.8.0"
            or row["recorded_taxonomy_version"] != "0.8.0"
            or packet.get("status") != "completed-evidence-limited"
               and packet.get("adjudicated_taxonomy") is None
            or packet.get("incident_id") != rid
            or not expected_revision
            or packet["baseline"].get("taxonomy_version") not in (None, "0.6.11")
            or outcome.get("classification_status") != row["classification_status"]
            or audited_pairs != recorded_pairs
            or rev.get("classification_review_provenance", {}).get("review_reference")
               != str(packet_path.relative_to(ROOT))):
            raise SystemExit(f"Substantive current-taxonomy decision stale or invalid for {rid}")
        if row["current_080_screen_result"] != "NOT-REVIEWED":
            raise SystemExit(f"Duplicate case review overlay for {rid}")
        row["current_080_screen_result"] = (
            "CANONICAL-080-RECONCILED-DISPUTED-RETAINED"
            if row["classification_status"] == "classification-disputed"
            else "CANONICAL-080-RECONCILED-PROVISIONAL-NEW-SUCCESS"
            if new_mappings else "CANONICAL-080-RECONCILED-PROVISIONAL-RETAINED"
        )
        row["current_080_screen_date"] = packet["review_date"]
        row["screening_decision_packet"] = str(packet_path.relative_to(ROOT))
        row["screening_assurance"] = "AI source/criterion review; original evidence limits preserved"
    # Reuse the completed source-first 23 October intake adjudications without
    # inventing another canonical revision or treating an edition stamp as review.
    # Every counted case must still have EXACTLY the evidence-bounded mappings,
    # provenance, current edition and review completion recorded in its packet.
    prior_intake_dir = ROOT / "vigil/docs/reviews/2026-10-23-intake-readjudication"
    for incident_number in range(204, 210):
        rid = f"VIGIL-INC-{incident_number:06d}"
        packet_path = prior_intake_dir / f"{rid}-adjudication.json"
        if not packet_path.is_file():
            raise SystemExit(f"Missing required v0.8.0 intake adjudication: {packet_path}")
        packet = json.loads(packet_path.read_text(encoding="utf-8"))
        row = by_id[rid]
        canonical = json.loads((ROOT / row["canonical_path"]).read_text(encoding="utf-8"))
        cl = canonical.get("taxonomy_classification") or {}
        provenance = cl.get("classification_review_provenance") or {}
        taxonomy_review = packet.get("taxonomy_review") or {}
        completion = packet.get("decision_completion") or {}
        prior_mappings = [
            cl.get("primary_classification"), *(cl.get("secondary_classifications") or [])
        ]
        prior_mappings = [x for x in prior_mappings if isinstance(x, dict)]
        reviewed_mappings = [
            decision.get("proposed_mapping")
            for decision in (packet.get("independent_adjudication") or {}).get("mapping_decisions", [])
        ]
        # Compare complete mapping objects, including basis, role, confidence
        # and Boundary conditions; never only the class ID or version string.
        if (
            packet.get("incident_id") != rid
            or row["current_080_screen_result"] != "NOT-REVIEWED"
            or row["recorded_taxonomy_version"] != "0.8.0"
            or provenance.get("review_reference") != str(packet_path.relative_to(ROOT))
            or provenance.get("review_date") != packet.get("reviewed_on")
            or taxonomy_review.get("taxonomy_version") != "0.8.0"
            or taxonomy_review.get("complete_class_set_review") is not True
            or not taxonomy_review.get("candidate_classes_tested")
            or not (packet.get("source_first_discovery") or {}).get("episode_inventory")
            or completion.get("status") != "reviewed-evidence-limited"
            or completion.get("recognition_and_exclusion_tests") != "reviewed"
            or (packet.get("validation") or {}).get("status") != "passed"
            or prior_mappings != reviewed_mappings
        ):
            raise SystemExit(f"Stale/incomplete prior 0.8.0 review for {rid}; rescreen explicitly")
        row["current_080_screen_result"] = "PRIOR-080-INTAKE-REVIEW-CROSSCHECKED"
        row["current_080_screen_date"] = packet["reviewed_on"]
        row["screening_decision_packet"] = str(packet_path.relative_to(ROOT))
        row["screening_assurance"] = (
            "Prior dated AI source/criterion full-rebuild crosschecked against "
            "current canonical mapping; no new independent source or human assurance"
        )
    # Replacement packets are dated v0.8.0 work. Validate their literal
    # conditions against the pinned v0.8.0 publication rather than conflating
    # this integrity check with a new v0.8.1 assessment.
    for rid, (packet_path, packet) in current_packets.items():
        if rid not in by_id:
            raise SystemExit(f"Unknown reviewed Incident: {rid}")
        row = by_id[rid]
        if rid in promoted_081:
            raw = subprocess.check_output(
                ["git", "show", f"{PAPER_081_BASELINE_REF}:{row['canonical_path']}"],
                cwd=ROOT,
            )
            canonical = json.loads(raw)
            historical_sha = hashlib.sha256(raw).hexdigest()
            if canonical["record_identity"]["version"] != promoted_081[rid][1]["baseline"]["record_version"]:
                raise SystemExit(f"Incorrect v0.8.0 canonical version before promotion: {rid}")
        else:
            canonical = json.loads((ROOT / row["canonical_path"]).read_text(encoding="utf-8"))
            historical_sha = row["canonical_sha256"]
        if (row["current_080_screen_result"] != "NOT-REVIEWED"
            or historical_sha != packet.get("canonical_sha256")
            or packet.get("status") != "completed-evidence-limited"
            or packet.get("validation", {}).get("status") != "passed"
            or packet.get("taxonomy_review", {}).get("taxonomy_version") != "0.8.0"
            or canonical["taxonomy_classification"] != packet.get("after_taxonomy")
            or not packet.get("mapping_tests")):
            raise SystemExit(f"Stale or incomplete replacement packet: {rid}")
        for test in packet["mapping_tests"]:
            cid = test["class_id"]
            if cid not in baseline_080:
                raise SystemExit(f"Unknown historical v0.8.0 class: {rid} {cid}")
            historical = baseline_080[cid]
            for key in CRITERION_FIELDS:
                literal = (historical[key] if key == "exclusions"
                           else historical[key]["required_conditions"])
                if [x["condition"] for x in test[key]] != literal:
                    raise SystemExit(f"Changed criteria require rescreen: {rid} {test['class_id']} {key}")
                if any(not x.get("assessment") or not x.get("source_record_refs") for x in test[key]):
                    raise SystemExit(f"Missing criterion reasoning: {rid}")
        row["current_080_screen_result"] = packet["screen_outcome"]
        row["current_080_screen_date"] = packet["review_date"]
        row["screening_decision_packet"] = str(packet_path.relative_to(ROOT))
        row["screening_assurance"] = "AI source/criterion review; complete historical-record fingerprint checked; no human assurance"
    # The 080 worklist stays an 080 worklist. A new edition requires a
    # separate source-first review; candidate IDs only rank its work.
    for row in rows:
        candidate_ids = row["review_inputs"]["candidate_class_ids_from_record"]
        row["v081_changed_candidate_class_criteria"] = {
            cid: changed_081[cid] for cid in candidate_ids if cid in changed_081
        }
        rid = row["incident_id"]
        if rid in promoted_081:
            row["v081_screen_status"] = "PAPER-FOCAL-081-REVIEW-PROMOTED-NOT-HUMAN-CERTIFIED"
            row["v081_review_packet"] = str(promoted_081[rid][0].relative_to(ROOT))
            row["v081_review_note"] = (
                "Focused v0.8.1 adjudication promoted to canonical record with prior "
                "mapping roles and evidence limitations preserved. 0.8.0 packet "
                "above remains a historically verified screening receipt."
            )
        else:
            row["v081_screen_status"] = "NOT-ASSESSED-UNDER-081"
            row["v081_review_note"] = (
                "Recorded candidates are discovery leads, not a complete 0.8.1 "
                "semantic re-screen. Previous 0.8.0 review does not certify 0.8.1."
            )
    rows.sort(key=lambda x: (x["priority"], x["incident_id"]))
    return {
        "worklist_schema": "vigil-taxonomy-080-reconciliation/1",
        "project": "VIGIL Observatory",
        "branch_scientific_commit": commit,
        "current_published_taxonomy": "0.8.1",
        "historical_screening_campaign_taxonomy": "0.8.0",
        "historical_criteria_git_commit": PUBLISHED_080_REF,
        "historical_screening_not_081_certification": True,
        "changed_081_criterion_fields_by_class": changed_081,
        "current_class_sha256": class_fingerprints,
        "state": "HISTORICAL-080-SCREENING-VALIDATION--081-REVIEW-OUTSTANDING",
        "roles": "Dated decision packet overlays only; approved canonical edits must independently pass rebuild and derived-output validation",
        "counts": {
            "incidents": len(rows),
            "priority": dict(sorted(Counter(str(x["priority"]) for x in rows).items())),
            "status": dict(sorted(Counter(x["classification_status"] for x in rows).items())),
            "recorded_taxonomy": dict(sorted(Counter(x["recorded_taxonomy_version"] for x in rows).items())),
            "screened_with_dated_packet": sum(r["current_080_screen_result"] != "NOT-REVIEWED" for r in rows),
            "not_screened": sum(r["current_080_screen_result"] == "NOT-REVIEWED" for r in rows),
            "screen_outcomes": dict(sorted(Counter(r["current_080_screen_result"] for r in rows).items())),
            "v081_criterion_changed_class_count": len(changed_081),
            "v081_rows_with_changed_recorded_candidates": sum(
                bool(r["v081_changed_candidate_class_criteria"]) for r in rows
            ),
            "v081_focal_reviews_promoted": len(promoted_081),
            "v081_unreviewed_records": len(rows) - len(promoted_081),
            "v081_independently_readjudicated": 0,
        },
        "incident_worklist": rows,
    }

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = (json.dumps(build(), indent=2, ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8")
    if args.write:
        DEST.write_bytes(payload)
        summary = json.loads(payload)["counts"]
        print("TAXONOMY_080_RECONCILIATION_QUEUE " + json.dumps(summary, sort_keys=True))
        print("No statuses or evidence were adjudicated or altered.")
        return 0
    if DEST.read_bytes() != payload:
        print("ERROR: reconciliation roster differs from exact checkout", file=sys.stderr)
        return 1
    print("PASS: reconciliation roster reproduces current checkout")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
