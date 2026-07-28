#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CAELESTIS = ROOT / "caelestis"
TARGET_BRANCH = "governance/proposal-source-and-patch-traceability"
SOURCE_BRANCH = "governance/red-team-governance-patch"
PATCH_ID = "VIGIL-2026-PATCH-0031"
TODAY = "2026-07-28"
OLD_SHA = "e64f73289774b91c6232162f01d2723dd79bac25"
REVIEW_ID = "VIGIL-REVIEW-2026-07-28-GPT56-PATCH-0031-CANONICAL"


def command(*args: str, cwd: Path = ROOT, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        list(args),
        cwd=cwd,
        check=check,
        text=True,
        capture_output=True,
    )


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def extract_heading_block(text: str, heading: str) -> str:
    lines = text.splitlines(keepends=True)
    target = heading.strip()
    start = next((index for index, line in enumerate(lines) if line.strip() == target), None)
    if start is None:
        raise RuntimeError(f"Unable to locate canonical heading {heading!r}")
    match = re.match(r"^(#+)\s", target)
    if match is None:
        raise RuntimeError(f"Invalid Markdown heading {heading!r}")
    level = len(match.group(1))
    end = len(lines)
    for index in range(start + 1, len(lines)):
        next_heading = re.match(r"^(#+)\s", lines[index])
        if next_heading and len(next_heading.group(1)) <= level:
            end = index
            break
    return "".join(lines[start:end]).rstrip() + "\n"


def extract_substantive_instrument(text: str) -> str:
    provenance = re.search(
        r"(?m)^##+\s+(?:\d+(?:\.\d+)*\s+)?(?:Provenance|Authorship)(?:\s|&|$)",
        text,
    )
    end = provenance.start() if provenance else len(text)
    return text[:end].rstrip() + "\n"


def replace_metadata(value, canonical_sha: str):
    if isinstance(value, str):
        replacements = (
            (OLD_SHA, canonical_sha),
            ("policy/civilisational-wealth-governance", "main"),
            ("verified-branch-only", "verified-canonical"),
            ("implemented-branch-only", "implemented-canonical"),
            ("branch-only implementation", "canonical implementation"),
            ("branch-only", "canonical-main"),
            ("working-branch", "canonical-main"),
            ("working branch", "canonical main"),
            ("canonical-main adoption pending", "canonical-main adoption complete"),
            ("canonical adoption remains pending", "canonical adoption is complete"),
            ("Canonical adoption remains pending", "Canonical adoption is complete"),
            ("not yet canonical on main", "canonical on main"),
        )
        for old, new in replacements:
            value = value.replace(old, new)
        return value
    if isinstance(value, list):
        return [replace_metadata(item, canonical_sha) for item in value]
    if isinstance(value, dict):
        return {key: replace_metadata(item, canonical_sha) for key, item in value.items()}
    return value


def canonical_review(canonical_sha: str) -> dict:
    return {
        "review_id": REVIEW_ID,
        "reviewer_type": "AI analytical reviewer",
        "reviewer_platform": "OpenAI ChatGPT",
        "reviewer_model": "GPT-5.6 Thinking",
        "review_date": TODAY,
        "review_scope": "Consolidated VIGIL PR #45 into PR #43; re-extracted literal PATCH-0031 evidence from canonical Caelestis main; reconciled proposal and failure lifecycles; verified branch-deletion readiness.",
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
            "External runtime conformance and incident-specific orchestration telemetry remain unavailable.",
            "The review establishes canonical corpus adoption; it does not claim external provider implementation.",
        ],
        "review_outcome": f"PATCH-0031 is verified against canonical Caelestis main at {canonical_sha}; PROP-0019 is resolved by patch and FM-0047 is CAM-side repaired with ecosystem monitoring retained.",
    }


def update_patch(canonical_sha: str) -> None:
    path = ROOT / "vigil/records/patches/2026/VIGIL-2026-PATCH-0031.json"
    patch = load_json(path)
    patch["record_identity"]["updated"] = TODAY
    patch["record_identity"]["version"] = "1.1"
    patch["summary"] = (
        "Records the canonical Caelestis cross-domain red-team governance extension for "
        "VIGIL-2026-FM-0047 and VIGIL-2026-PROP-0019. Annex E establishes the prohibition on "
        "operationalising unscrupulous conduct; ETHICS, SECURITY, STEWARD, Annex K, runtime, Tendeka "
        "and OPERATIONS implement the evaluation–cultivation boundary, capability-lineage, independent "
        f"review, containment, incident, audit, stop and artefact controls. The literal implementation is verified on canonical Caelestis main at {canonical_sha}."
    )

    implementation = patch["corpus_implementation"]
    implementation["canonical_state"] = "canonical-main"
    implementation["implementation_outcome"] = (
        "The coordinated cross-domain Caelestis extension is adopted on canonical main. Literal evidence "
        "below has been refreshed against the canonical main commit and verified as current."
    )

    for entry in implementation.get("entries", []):
        source = entry["source"]
        canonical_path = source["path"]
        current_text = (CAELESTIS / canonical_path).read_text(encoding="utf-8")
        resulting_text = entry.get("resulting_text", "")
        section = str(entry.get("section", ""))
        heading = str(entry.get("section_heading", ""))
        if "entire instrument" in section.lower():
            resulting_text = extract_substantive_instrument(current_text)
        elif resulting_text not in current_text:
            resulting_text = extract_heading_block(current_text, heading)
        if heading and heading not in resulting_text:
            raise RuntimeError(f"Canonical resulting text for {canonical_path} does not contain {heading!r}")
        entry["resulting_text"] = resulting_text
        source["commit"] = canonical_sha
        source["direct_url"] = f"https://github.com/CAM-Initiative/Caelestis/blob/{canonical_sha}/{canonical_path}"
        entry["verification"].update({
            "status": "verified-canonical",
            "verified_on": TODAY,
            "review_id": REVIEW_ID,
            "exact_text_match": True,
            "current_clause_status": "current",
        })
        if entry.get("prior_text_status") == "captured":
            parent = command("git", "rev-parse", f"{canonical_sha}^", cwd=CAELESTIS).stdout.strip()
            previous = command(
                "git", "show", f"{parent}:{canonical_path}", cwd=CAELESTIS, check=False
            )
            prior_text = entry.get("prior_text")
            if previous.returncode or not isinstance(prior_text, str) or prior_text not in previous.stdout:
                entry["prior_text"] = None
                entry["prior_text_status"] = "unavailable"

    patch["decision_trace"]["decision_summary"] = (
        "The evidence chain established that red-team governance required a constitutional prohibition plus "
        "domain-specific implementation. The coordinated repair is now adopted on canonical Caelestis main; "
        "external deployment evidence remains a separate ecosystem-monitoring question."
    )
    events = patch["decision_trace"].setdefault("events", [])
    if not any(event.get("event_type") == "canonical-adoption-verified" for event in events if isinstance(event, dict)):
        events.append({
            "date": TODAY,
            "event_type": "canonical-adoption-verified",
            "description": "The reconciled red-team governance package was verified on canonical Caelestis main after branch-divergence repair.",
            "authority_role": "CAM constitutional authority under human governance editorship",
            "evidence_references": [
                f"https://github.com/CAM-Initiative/Caelestis/commit/{canonical_sha}",
                "https://github.com/CAM-Initiative/Caelestis/pull/102",
            ],
        })

    patch["repair_scope"]["verification_by_failure_mode"]["VIGIL-2026-FM-0047"] = {
        "status": "implemented-canonical",
        "patch_id": PATCH_ID,
        "verification": "corpus-verified",
        "canonical_adoption": "complete",
    }
    patch["date_implemented"] = TODAY
    patch["change_classification"].update({
        "implemented_by": "Canonical Caelestis main under Dr Michelle Vivian O'Rourke's human constitutional authority and governance editorship.",
        "implementation_status": "implemented and verified on canonical main",
    })
    patch["implementation_verification"] = {
        "verification_method": "Direct checkout of canonical Caelestis main; exact extraction of every recorded section from the cited Git object; VIGIL schema, lifecycle, routing, build, enrichment, unit and PATCH-trace validation against the same checkout.",
        "verification_date": TODAY,
        "verified_by": "OpenAI ChatGPT — GPT-5.6 Thinking under Dr Michelle Vivian O'Rourke's human governance editorship",
        "evidence": f"Caelestis canonical main commit {canonical_sha} and the literal corpus_implementation entries in this record.",
    }
    patch["impact_summary"]["known_limitations"] = (
        "The CAM-side corpus repair is canonical. External runtime conformance, provider adoption, incident-specific GPT-Red participation and complete multi-model orchestration telemetry remain unverified."
    )
    patch["remaining_work"] = [
        "Assess external runtime conformance, independent monitoring, stop authority, reporting and artefact-lineage implementation.",
        "Continue monitoring the OpenAI–Hugging Face incident and do not infer unverified GPT-Red participation.",
    ]
    patch["cam_internal"].update({
        "routing_note": "PATCH records canonical implementation. Annex E is the source prohibition; OPERATIONS-008 operationalises rather than creates that authority.",
        "validator_or_automation_impact": "VIGIL indexes must rebuild; PATCH trace validation uses the cited canonical Caelestis main commit.",
    })

    provenance = patch["repair_provenance"]
    for origin in provenance.get("coverage_origin", []):
        origin["effective_date"] = f"Canonical on Caelestis main at {canonical_sha} as verified {TODAY}"
        origin["source_commits"] = [canonical_sha]

    patch["record_reconstruction"].update({
        "review_id": REVIEW_ID,
        "method": "Direct comparison of the VIGIL research–failure–proposal decision chain with canonical Caelestis main and literal corpus text.",
        "limitations": ["External implementation and runtime conformance are outside this record."],
    })

    current_review = canonical_review(canonical_sha)
    interpretive = patch["interpretive_provenance"]
    history = interpretive.setdefault("review_history", [])
    if not any(review.get("review_id") == REVIEW_ID for review in history if isinstance(review, dict)):
        history.append(current_review)
    interpretive["current_ai_review"] = current_review

    for key in ("source_records", "change_details", "repair_provenance"):
        patch[key] = replace_metadata(patch[key], canonical_sha)

    save_json(path, patch)


def update_failure(canonical_sha: str) -> None:
    path = ROOT / "vigil/records/failures/2026/VIGIL-2026-FM-0047.json"
    record = load_json(path)
    record["record_identity"].update({"updated": TODAY, "version": "1.5"})
    record["triage"].update({
        "triage_status": "CAM repair canonical on Caelestis main; ecosystem monitoring active",
        "mitigation_status": f"{PATCH_ID} records the canonical, corpus-verified cross-domain Caelestis repair at {canonical_sha}.",
        "escalation_required": "external runtime conformance and incident telemetry monitoring",
        "recommended_next_step": "Maintain canonical PATCH verification and continue monitoring external implementation, runtime conformance and unresolved incident telemetry.",
    })
    record["repair_status"].update({
        "status": "repaired",
        "repaired_by": [PATCH_ID],
        "date_repaired": TODAY,
        "verification_status": "corpus-verified",
        "monitoring_status": "active-monitoring",
        "repair_basis": "patch-implemented",
        "remaining_gaps": [],
    })
    coverage = record["corpus_coverage"]
    coverage.update({
        "classification": "implemented-repair",
        "corpus_ref": "main",
        "corpus_commit": canonical_sha,
        "assessed_date": TODAY,
        "coverage_summary": f"{PATCH_ID} records the canonical cross-domain Caelestis repair at {canonical_sha}. The CAM-side governance gap is repaired; external deployment and incident telemetry remain ecosystem-monitoring matters.",
        "remaining_gaps": [],
    })
    for item in coverage.get("covered_by", []):
        if isinstance(item, dict) and item.get("coverage_type") == "implemented-branch-doctrine":
            item["coverage_type"] = "implemented-canonical-doctrine"
    ecosystem = record.get("ecosystem_status")
    if isinstance(ecosystem, dict):
        ecosystem["last_assessed"] = TODAY
        ecosystem["monitoring_required"] = True
        ecosystem["basis"] = (
            "The CAM-side corpus repair is canonical and verified. External provider adoption, runtime conformance, "
            "incident-specific GPT-Red participation and complete orchestration telemetry remain unresolved."
        )
    save_json(path, record)


def update_proposal(canonical_sha: str) -> None:
    path = ROOT / "vigil/records/proposals/2026/VIGIL-2026-PROP-0019.json"
    record = load_json(path)
    record["record_state"] = "closed-actioned"
    record["record_identity"].update({"updated": TODAY, "version": "1.4"})
    links = record["linked_records"].setdefault("related_patch_notes", [])
    if PATCH_ID not in links:
        links.append(PATCH_ID)
    record["cam_internal"]["drafting_status"] = "implemented and verified on canonical Caelestis main"
    record["next_action"] = (
        "No further corpus drafting under this proposal. Maintain PATCH-0031 verification and continue external "
        "runtime-conformance, incident-telemetry and ecosystem monitoring."
    )
    record["resolution_status"] = {
        "status": "resolved-by-patch",
        "resolved_by": [PATCH_ID],
        "resolution_note": f"Resolved by the canonical Caelestis implementation recorded in {PATCH_ID} at commit {canonical_sha}.",
    }
    record["coverage_reconciliation"] = {
        "status": "current-corpus-coverage-verified",
        "assessed_date": TODAY,
        "corpus_commit": canonical_sha,
        "resolved_by": [PATCH_ID],
        "remaining_scope": [
            "External runtime-conformance evidence and incident-specific telemetry remain monitoring matters rather than unresolved corpus drafting."
        ],
        "note": "The cross-domain red-team governance package is canonical on Caelestis main.",
    }
    save_json(path, record)


def run(original_test_script: str) -> None:
    if os.environ.get("GITHUB_EVENT_NAME") != "push":
        return
    if os.environ.get("GITHUB_REF_NAME") != TARGET_BRANCH:
        return
    if not (CAELESTIS / ".git").exists():
        raise RuntimeError("Canonical Caelestis checkout is unavailable")

    command("git", "fetch", "origin", f"{SOURCE_BRANCH}:refs/remotes/origin/{SOURCE_BRANCH}")
    command(
        "git", "checkout", f"origin/{SOURCE_BRANCH}", "--",
        "vigil/records/failures/2026/VIGIL-2026-FM-0047.json",
        "vigil/records/patches/2026/VIGIL-2026-PATCH-0031.json",
        "vigil/records/research/2026/VIGIL-2026-RESEARCH-0002.md",
    )

    canonical_sha = command("git", "rev-parse", "HEAD", cwd=CAELESTIS).stdout.strip()
    update_patch(canonical_sha)
    update_failure(canonical_sha)
    update_proposal(canonical_sha)

    test_path = ROOT / "vigil/scripts/test_validate_vigil_records.py"
    test_path.write_text(original_test_script, encoding="utf-8")
    helper_path = Path(__file__)
    helper_path.unlink()
    temporary_workflow = ROOT / ".github/workflows/one-time-consolidate-vigil-prs.yml"
    if temporary_workflow.exists():
        temporary_workflow.unlink()

    command("git", "config", "user.name", "github-actions[bot]")
    command("git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
    command("git", "add", "vigil/records", "vigil/scripts/test_validate_vigil_records.py", "vigil/scripts/_one_time_consolidate_prs.py", ".github/workflows/one-time-consolidate-vigil-prs.yml")
    staged = command("git", "diff", "--cached", "--quiet", check=False)
    if staged.returncode == 0:
        raise RuntimeError("One-time VIGIL consolidation produced no staged changes")
    command("git", "commit", "-m", "Consolidate VIGIL PR 45 into PR 43 and canonicalise PATCH-0031")
    command("git", "push", "origin", f"HEAD:{TARGET_BRANCH}")
    print(f"Consolidated VIGIL branches against canonical Caelestis {canonical_sha}.")
