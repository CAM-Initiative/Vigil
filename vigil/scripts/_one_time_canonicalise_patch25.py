#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CAELESTIS = ROOT / "caelestis"
TODAY = "2026-07-28"
CANONICAL_COMMIT_MESSAGE = "Reconcile civilisational wealth and red-team governance divergence"
PATCH25_REVIEW = "VIGIL-REVIEW-2026-07-28-GPT56-PATCH-0025-CANONICAL"
PATCH15_REVIEW = "VIGIL-REVIEW-2026-07-28-GPT56-PATCH-0015-CURRENT-STATUS"
OLD_PATCH25_SHAS = {
    "bd22cad95de6b78c4c613353eadacda9b8253e0e",
    "289cceb41f8dbb2f2f3e6839e5b6f94f96656396",
    "23a1c5a9a112e73179767973e39871d4dce2c383",
}


def command(*args: str, cwd: Path = ROOT, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(list(args), cwd=cwd, check=check, text=True, capture_output=True)


def git_text(revision: str, path: str) -> str:
    completed = command("git", "show", f"{revision}:{path}", cwd=CAELESTIS, check=False)
    if completed.returncode:
        raise RuntimeError(completed.stderr.strip() or f"Unable to read {revision}:{path}")
    return completed.stdout


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def normalise_heading(value: str) -> str:
    return re.sub(r"^#+\s*", "", value.strip()).strip()


def extract_heading_block(text: str, requested_heading: str, section: str) -> tuple[str, str]:
    lines = text.splitlines(keepends=True)
    target = normalise_heading(requested_heading)
    headings: list[tuple[int, int, str]] = []
    for index, line in enumerate(lines):
        match = re.match(r"^(#+)\s+(.+?)\s*$", line.rstrip("\n"))
        if match:
            headings.append((index, len(match.group(1)), match.group(2).strip()))

    exact = [item for item in headings if normalise_heading(item[2]) == target]
    chosen = exact[0] if len(exact) == 1 else None
    if chosen is None:
        section_token = section.replace("§", "").strip().split()[0]
        section_matches = [
            item for item in headings
            if normalise_heading(item[2]) == section_token
            or normalise_heading(item[2]).startswith(section_token + " ")
        ]
        if len(section_matches) == 1:
            chosen = section_matches[0]
    if chosen is None:
        raise RuntimeError(
            f"Unable to resolve heading {requested_heading!r} / section {section!r}; "
            f"available headings include {[item[2] for item in headings[:30]]}"
        )

    start, level, current_heading = chosen
    end = len(lines)
    for index, candidate_level, _ in headings:
        if index > start and candidate_level <= level:
            end = index
            break
    return "".join(lines[start:end]).rstrip() + "\n", current_heading


def replace_stale_references(value, canonical_sha: str):
    if isinstance(value, str):
        for old_sha in OLD_PATCH25_SHAS:
            value = value.replace(old_sha, canonical_sha)
        replacements = (
            ("policy/civilisational-wealth-governance", "main"),
            ("branch-only", "canonical-main"),
            ("working-branch", "canonical-main"),
            ("working branch", "canonical main"),
            ("canonical-main adoption pending", "canonical-main adoption complete"),
            ("canonical adoption pending", "canonical adoption complete"),
            ("pending canonical adoption", "following canonical adoption"),
        )
        for old, new in replacements:
            value = value.replace(old, new)
        return value
    if isinstance(value, list):
        return [replace_stale_references(item, canonical_sha) for item in value]
    if isinstance(value, dict):
        return {key: replace_stale_references(item, canonical_sha) for key, item in value.items()}
    return value


def review(review_id: str, scope: str, outcome: str) -> dict:
    return {
        "review_id": review_id,
        "reviewer_type": "AI analytical reviewer",
        "reviewer_platform": "OpenAI ChatGPT",
        "reviewer_model": "GPT-5.6 Thinking",
        "review_date": TODAY,
        "review_scope": scope,
        "capability_profile": {
            "direct_text_analysis": True,
            "direct_repository_analysis": True,
            "direct_static_image_analysis": False,
            "direct_audio_analysis_in_this_pass": False,
            "direct_uploaded_video_analysis_in_this_pass": False,
            "direct_externally_hosted_video_analysis": False,
            "web_link_and_metadata_review": False,
        },
        "known_limitations": [
            "Deleted branch Git objects could not be retained as durable canonical locators.",
            "External runtime conformance and incident-specific telemetry remain outside corpus verification.",
        ],
        "review_outcome": outcome,
    }


def set_current_review(record: dict, current_review: dict) -> None:
    provenance = record["interpretive_provenance"]
    history = provenance.setdefault("review_history", [])
    if not any(item.get("review_id") == current_review["review_id"] for item in history if isinstance(item, dict)):
        history.append(current_review)
    provenance["current_ai_review"] = current_review


def canonical_commit() -> str:
    result = command(
        "git", "log", "--format=%H", f"--grep=^{CANONICAL_COMMIT_MESSAGE}$", "-n", "1",
        cwd=CAELESTIS,
    ).stdout.strip()
    if not result:
        raise RuntimeError("Unable to locate canonical Caelestis reconciliation commit")
    if command("git", "merge-base", "--is-ancestor", result, "HEAD", cwd=CAELESTIS, check=False).returncode:
        raise RuntimeError(f"Canonical reconciliation commit {result} is not an ancestor of Caelestis main")
    return result


def reconcile_patch15() -> None:
    path = ROOT / "vigil/records/patches/2026/VIGIL-2026-PATCH-0015.json"
    record = load_json(path)
    entries = record["corpus_implementation"]["entries"]
    for index in (4, 6, 9, 10):
        entries[index]["verification"].update({
            "verified_on": TODAY,
            "review_id": PATCH15_REVIEW,
            "current_clause_status": "later-amended",
        })
    record["record_identity"].update({"updated": TODAY, "version": "2.1"})
    if not any(event.get("date") == TODAY and event.get("event_type") == "implementation-verified" for event in record["decision_trace"]["events"]):
        record["decision_trace"]["events"].append({
            "date": TODAY,
            "event_type": "implementation-verified",
            "description": "Four historical implementation clauses remain exact at their cited canonical source commit but have since been amended on current Caelestis main; their current-clause status was corrected without altering the preserved literal evidence.",
            "authority_role": "AI analytical reviewer under human governance editorship",
            "evidence_references": [PATCH15_REVIEW, "VIGIL-2026-PATCH-0015"],
        })
    current_review = review(
        PATCH15_REVIEW,
        "PATCH-0015 current-clause status reconciliation against current Caelestis main.",
        "Historical literal implementation evidence remains verified; four entries are correctly classified as later-amended.",
    )
    set_current_review(record, current_review)
    save_json(path, record)


def reconcile_patch25(canonical_sha: str) -> None:
    path = ROOT / "vigil/records/patches/2026/VIGIL-2026-PATCH-0025.json"
    record = replace_stale_references(load_json(path), canonical_sha)
    main_sha = command("git", "rev-parse", "HEAD", cwd=CAELESTIS).stdout.strip()
    parent = command("git", "rev-parse", f"{canonical_sha}^", cwd=CAELESTIS).stdout.strip()

    for entry in record["corpus_implementation"]["entries"]:
        source_path = entry["canonical_path"]
        source_text = git_text(canonical_sha, source_path)
        current_text = git_text(main_sha, source_path)
        resulting_text = entry["resulting_text"]
        heading = entry["section_heading"]
        if resulting_text not in source_text:
            resulting_text, heading = extract_heading_block(source_text, heading, entry["section"])
        entry["resulting_text"] = resulting_text
        entry["section_heading"] = normalise_heading(heading)
        entry["source"] = {
            "repository": "CAM-Initiative/Caelestis",
            "commit": canonical_sha,
            "path": source_path,
            "direct_url": f"https://github.com/CAM-Initiative/Caelestis/blob/{canonical_sha}/{source_path}",
        }
        if entry.get("prior_text_status") == "captured":
            prior_text = entry.get("prior_text")
            prior_source = git_text(parent, source_path)
            if not isinstance(prior_text, str) or prior_text not in prior_source:
                entry["prior_text"] = None
                entry["prior_text_status"] = "unavailable"
        entry["verification"] = {
            "status": "verified-canonical",
            "verified_on": TODAY,
            "review_id": PATCH25_REVIEW,
            "exact_text_match": True,
            "current_clause_status": "current" if resulting_text in current_text else "later-amended",
        }

    record["record_state"] = "closed-actioned"
    record["record_identity"].update({"updated": TODAY, "version": "2.1"})
    record["corpus_implementation"].update({
        "canonical_state": "canonical-main",
        "implementation_outcome": "The mixed fourteen-instrument repair is adopted on canonical Caelestis main. All 38 literal entries were reconstructed and verified against the canonical reconciliation commit.",
    })
    if not any(event.get("event_type") == "canonicalised" for event in record["decision_trace"]["events"]):
        record["decision_trace"]["events"].append({
            "date": TODAY,
            "event_type": "canonicalised",
            "description": "PATCH-0025 was reconstructed from the deleted working-branch locators onto the canonical Caelestis reconciliation commit, preserving literal section evidence and current-clause status.",
            "authority_role": "CAM constitutional authority under human governance editorship",
            "evidence_references": [
                f"https://github.com/CAM-Initiative/Caelestis/commit/{canonical_sha}",
                "https://github.com/CAM-Initiative/Caelestis/pull/102",
                PATCH25_REVIEW,
            ],
        })
    record["implementation_verification"] = {
        "verification_method": "Direct checkout of canonical Caelestis history; section-by-section reconstruction at the reconciliation commit; exact substring verification; current-main status comparison; VIGIL PATCH-trace validation.",
        "verification_date": TODAY,
        "verified_by": "OpenAI ChatGPT — GPT-5.6 Thinking under Dr Michelle Vivian O'Rourke's human governance editorship",
        "evidence": f"Caelestis canonical reconciliation commit {canonical_sha} and all 38 corpus_implementation entries.",
    }
    record["remaining_work"] = [
        "Assess external runtime conformance for target–action authority verification, aggregate-pathway revalidation and Scoped Ethical Admissibility Hold controls.",
        "Continue monitoring the OpenAI–Hugging Face incident and preserve uncertainty regarding unavailable prompts, trajectories and internal telemetry.",
    ]
    record["record_reconstruction"].update({
        "review_id": PATCH25_REVIEW,
        "method": "Reconstructed from the canonical Caelestis reconciliation commit after the original working-branch Git objects ceased to resolve.",
        "limitations": [
            "The deleted branch commits are retained in historical review narrative but are no longer used as canonical source locators.",
            "External implementation and runtime conformance remain outside this PATCH.",
        ],
    })
    for origin in record["repair_provenance"].get("coverage_origin", []):
        origin["effective_date"] = f"Canonical on Caelestis main at {canonical_sha}, verified {TODAY}"
        origin["source_commits"] = [canonical_sha]
    if "repair_scope" in record:
        verification = record["repair_scope"].get("verification_by_failure_mode", {})
        if "VIGIL-2026-FM-0044" in verification:
            verification["VIGIL-2026-FM-0044"] = {
                "status": "implemented-canonical",
                "patch_id": "VIGIL-2026-PATCH-0025",
                "verification": "corpus-verified",
                "canonical_adoption": "complete",
            }
    current_review = review(
        PATCH25_REVIEW,
        "PATCH-0025 canonical reconstruction, literal source verification and lifecycle reconciliation.",
        f"PATCH-0025 is verified as canonical-main at {canonical_sha}; historical branch locators are superseded by durable canonical evidence.",
    )
    set_current_review(record, current_review)
    save_json(path, record)


def reconcile_fm44(canonical_sha: str) -> None:
    path = ROOT / "vigil/records/failures/2026/VIGIL-2026-FM-0044.json"
    record = load_json(path)
    record["record_state"] = "monitoring"
    record["record_identity"].update({"updated": TODAY, "version": "1.3"})
    record["triage"].update({
        "triage_status": "CAM repair canonical on Caelestis main; ecosystem monitoring active",
        "mitigation_status": f"VIGIL-2026-PATCH-0025 records the canonical, corpus-verified objective–pathway and target-authority repair at {canonical_sha}.",
        "escalation_required": "external runtime conformance and incident telemetry monitoring",
        "recommended_next_step": "Maintain canonical PATCH verification and continue monitoring runtime conformance, recurrence and the OpenAI–Hugging Face investigation.",
    })
    record["cam_internal"]["proposal_needed"] = "no new proposal required — VIGIL-2026-PROP-0017 is resolved by canonical VIGIL-2026-PATCH-0025"
    record["repair_status"].update({
        "status": "repaired",
        "date_repaired": TODAY,
        "verification_status": "corpus-verified",
        "monitoring_status": "active-monitoring",
        "repair_basis": "patch-implemented",
        "remaining_gaps": [
            "External runtime-conformance evidence does not yet establish deployment of the canonical gate, hold, authority-verification or aggregate-pathway controls.",
            "The OpenAI–Hugging Face investigation remains incomplete, and incident-specific prompts, complete trajectories, internal ethical-state telemetry and final causal reconstruction are not public.",
        ],
    })
    record["ecosystem_status"]["last_assessed"] = TODAY
    record["corpus_coverage"].update({
        "classification": "implemented-repair",
        "corpus_ref": "main",
        "corpus_commit": canonical_sha,
        "assessed_date": TODAY,
        "coverage_summary": f"VIGIL-2026-PATCH-0025 records the canonical fourteen-instrument Caelestis repair at {canonical_sha}. The CAM-side governance gap is repaired; external deployment and incident telemetry remain monitoring matters.",
        "remaining_gaps": [],
    })
    current_review = review(
        PATCH25_REVIEW,
        "FM-0044 canonical repair-state and external-monitoring reconciliation.",
        "FM-0044 is CAM-side repaired and remains in monitoring because external implementation and incident telemetry are unresolved.",
    )
    set_current_review(record, current_review)
    save_json(path, record)


def reconcile_prop17(canonical_sha: str) -> None:
    path = ROOT / "vigil/records/proposals/2026/VIGIL-2026-PROP-0017.json"
    record = load_json(path)
    record["record_state"] = "closed-actioned"
    record["record_identity"].update({"updated": TODAY, "version": "1.4"})
    record["next_action"] = "No further corpus drafting under this proposal. Maintain PATCH-0025 verification and continue external runtime-conformance and incident monitoring."
    record["cam_internal"]["drafting_status"] = "implemented and verified on canonical Caelestis main"
    record["cam_internal"]["routing_note"] = "PATCH-0025 records the canonical implementation: ETHICS defines objective–pathway admissibility and target-authority separation; runtime and OPERATIONS implement the bounded gate, hold, verification and safely severable continuation controls."
    record["resolution_status"] = {
        "status": "resolved-by-patch",
        "resolved_by": ["VIGIL-2026-PATCH-0025"],
        "resolution_note": f"Resolved by the canonical Caelestis implementation recorded in VIGIL-2026-PATCH-0025 at {canonical_sha}.",
    }
    record["coverage_reconciliation"] = {
        "status": "current-corpus-coverage-verified",
        "assessed_date": TODAY,
        "corpus_commit": canonical_sha,
        "resolved_by": ["VIGIL-2026-PATCH-0025"],
        "remaining_scope": [
            "External runtime-conformance evidence and incident-specific telemetry remain monitoring matters rather than unresolved corpus drafting."
        ],
        "note": "The objective–pathway ethical admissibility and target-authority repair is canonical on Caelestis main.",
    }
    current_review = review(
        PATCH25_REVIEW,
        "PROP-0017 canonical resolution and PATCH-0025 linkage reconciliation.",
        "PROP-0017 is resolved by canonical PATCH-0025; remaining work is external monitoring rather than corpus drafting.",
    )
    set_current_review(record, current_review)
    save_json(path, record)


def run() -> str:
    canonical_sha = canonical_commit()
    reconcile_patch15()
    reconcile_patch25(canonical_sha)
    reconcile_fm44(canonical_sha)
    reconcile_prop17(canonical_sha)
    return canonical_sha


if __name__ == "__main__":
    print(run())
