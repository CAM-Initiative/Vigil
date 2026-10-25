#!/usr/bin/env python3
"""Apply five approved SIAI v0.8.1 taxonomy-edition promotions.

Run once on branch chore/siai-2026-release-readiness-20261023.
Uses existing v0.8.0 criterion packets, not a new adjudication.
The script removes itself from the resulting commit.
"""
from __future__ import annotations

import copy
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRANCH = "chore/siai-2026-release-readiness-20261023"
PACKET = "vigil/docs/reviews/2026-10-25-siai-taxonomy-081-delta/TARGETED-6-FOCUSED-REVIEW-20261025.json"
FACTS = "vigil/releases/siai-2026/PAPER-RECONCILIATION-FACTS.md"
CASES = {
    34: ("1.1.23", "1.1.24", "0.6.11",
         "Retain five independent Boundaries. A reported companion relational cue is not merely observed user attachment; original warning validity, effectiveness, retention objective and decision transition are not established."),
    62: ("1.1.21", "1.1.22", "0.6.11",
         "Preserve attributed FC-062 and independently evidenced pre-event medical-care duty FC-087 failures, with FC-052/082/086 Boundaries. No medical causation or liability conclusion."),
    101: ("0.1.24", "0.1.25", "0.6.9",
          "FC-066 deployment-wide assent failure stands. FC-051 relational evidence-channel conditioning remains unestablished in a particular interaction; FC-065/082 retain separate uncertainty."),
    145: ("0.1.16", "0.1.17", "0.6.9",
          "FC-038 observed reporting activation, FC-042 accountable security escalation and FC-083 effective pre-transfer containment are three distinct success findings; none is inferred merely from absence of payment."),
    195: ("0.1.4", "0.1.5", "0.6.11",
          "Preserve FC-049/086 Boundaries and reported successful user reset as counterevidence, not proof of product-level positive control. The original model dialogue is not authenticated."),
}
KEEP = ("source_records", "vigil_assessment", "harm_impact_assessment",
        "external_requirement_assessments", "external_assessments",
        "incident_identity", "affected_party_context", "jurisdictional_context")

def run(*args):
    subprocess.run(args, cwd=ROOT, check=True)

def read(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def write(path, obj):
    (ROOT / path).write_text(
        json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def mappings(t):
    return [m for m in [t.get("primary_classification"),
                        *t.get("secondary_classifications", [])]
            if isinstance(m, dict)]

def mapping_signature(t):
    return [(m.get("class_id"), m.get("classification_role"),
             m.get("classification_confidence"), m.get("classification_basis"))
            for m in mappings(t)]

def main():
    active_branch = subprocess.check_output(
        ["git", "branch", "--show-current"], cwd=ROOT, text=True).strip()
    assert active_branch == BRANCH, f"Switch to {BRANCH} first"
    status = subprocess.check_output(
        ["git", "status", "--porcelain"], cwd=ROOT, text=True).strip()
    assert not status, "Clean working tree required"
    packet = read(PACKET)
    assert packet["canonical_promotion_state"].startswith("pending;")
    paths = []
    for n, (oldv, newv, oldt, reason) in CASES.items():
        path = f"vigil/records/incidents/VIGIL-INC-{n:06}.json"
        data = read(path)
        original = copy.deepcopy(data)
        t = data["taxonomy_classification"]
        assert data["record_identity"]["version"] == oldv, (n, "version")
        assert t["taxonomy_version"] == oldt, (n, "taxonomy")
        sig = mapping_signature(t)
        data["record_identity"]["version"] = newv
        data["record_identity"]["updated"] = "2026-10-25"
        t["taxonomy_version"] = "0.8.1"
        t["classification_review_provenance"] = {
            "review_date": "2026-10-25",
            "reviewer": "OpenAI ChatGPT GPT-6 — AI analytical reviewer",
            "review_status": "Focused current published edition role/exclusion crosswalk against dated v0.8.0 criterion packet; prior findings retained.",
            "review_reference": PACKET,
        }
        for m in mappings(t):
            b = m.get("boundary_adjudication")
            if isinstance(b, dict) and "taxonomy_version" in b:
                b["taxonomy_version"] = "0.8.1"
        review = {
            "review_id": f"VIGIL-REVIEW-2026-10-25-081-FOCUSED-{n:06}",
            "reviewer_type": "AI analytical reviewer",
            "reviewer_platform": "OpenAI ChatGPT / GitHub connector",
            "reviewer_model": "GPT-6",
            "review_date": "2026-10-25",
            "review_scope": "Bounded published 0.8.1 exclusion/role delta against prior source-first 0.8.0 packet; no fresh primary-source research.",
            "capability_profile": {
                "direct_repository_analysis": True, "direct_text_analysis": True,
                "taxonomy_review": True, "web_research": False,
                "harm_impact_review": False, "external_requirement_review": False,
            },
            "known_limitations": [
                "No independent original-source authentication or human verification.",
                reason,
            ],
            "review_outcome": "Prior class roles/confidences and evidence limits retained; canonical taxonomy version updated to 0.8.1.",
        }
        data["interpretive_provenance"]["current_ai_review"] = review
        data["interpretive_provenance"]["review_history"].append(review)
        assert mapping_signature(t) == sig, (n, "mapping changed")
        for key in KEEP:
            assert data.get(key) == original.get(key), (n, key)
        assert data["interpretive_provenance"]["review_history"][:-1] == original["interpretive_provenance"]["review_history"]
        write(path, data)
        paths.append(path)
    assert read("vigil/records/incidents/VIGIL-INC-000118.json")["taxonomy_classification"]["taxonomy_version"] == "0.6.11"
    records = [read(str(p.relative_to(ROOT)))
               for p in sorted((ROOT / "vigil/records/incidents").glob("VIGIL-INC-*.json"))]
    assert len(records) == 200
    assert sum(x["taxonomy_classification"]["taxonomy_version"] == "0.8.1"
               for x in records) == 169

    run("python", "vigil/scripts/build-vigil-public-records.py")
    run("python", "vigil/scripts/build-vigil-jurisdiction-index.py")
    run("python", "vigil/scripts/build-vigil-jurisdiction-index.py", "--check")

    fact_path = ROOT / FACTS
    facts = fact_path.read_text(encoding="utf-8")
    old = "**164 of 200 active canonical Incident records currently stamp published Alignment Taxonomy v0.8.1**; **36 retain older editions** (8 at 0.8.0, 5 at 0.7.0, 14 at 0.6.11 and 9 at 0.6.9)."
    new = "**169 of 200 active canonical Incident records currently stamp published Alignment Taxonomy v0.8.1**; **31 retain older editions** (8 at 0.8.0, 5 at 0.7.0, 11 at 0.6.11 and 7 at 0.6.9)."
    assert facts.count(old) == 1
    facts = facts.replace(old, new, 1)
    old_remaining = "**INC-100+ remaining (19):** five evidence/mapping targeted reviews (**100, 106, 109, 199, 209**); six legacy-edition crosswalks (**101, 103, 118, 145, 194, 195**);"
    new_remaining = "**INC-100+ remaining (16):** five evidence/mapping targeted reviews (**100, 106, 109, 199, 209**); three legacy-edition crosswalks (**103, 118, 194**);"
    assert facts.count(old_remaining) == 1
    facts = facts.replace(old_remaining, new_remaining, 1)
    anchor = "\n**Release limitation:**"
    assert facts.count(anchor) == 1
    facts = facts.replace(anchor,
        "\n**Five focused canonical promotions (25 October):** INC-034, 062, 101, 145 and 195 are canonically reconciled to v0.8.1, retaining their mappings, evidence limitations, harm and external-governance assessments. INC-118 remains held at its historical taxonomy edition. This was a bounded AI-authored criterion crosswalk, not new primary-source authentication or human certification. See the [dated six-case decision](../../docs/reviews/2026-10-25-siai-taxonomy-081-delta/TARGETED-6-FOCUSED-REVIEW-20261025.json).\n" + anchor, 1)
    fact_path.write_text(facts, encoding="utf-8")
    packet["canonical_promotion_state"] = "completed: five canonical incident promotions with three public projections regenerated"
    packet["promotion_integrity"] = {
        "promoted_record_versions": {str(n): data[1] for n, data in CASES.items()},
        "canonical_081_count": 169,
        "prior_class_roles_and_confidence_preserved": True,
        "incident_118_held": True,
        "human_verification_claimed": False,
    }
    packet["limits"] = [
        s.replace("This records taxonomy criterion conclusions only, not five completed canonical promotions.",
                  "Five bounded edition promotions completed; not new original-source authentication.")
         .replace("Earlier 164/200 canonical 0.8.1 coverage remains unchanged until valid record edits and deterministic indexes are committed.",
                  "Canonical coverage is 169/200 after the version updates and regenerated public indexes.")
        for s in packet["limits"]
    ]
    write(PACKET, packet)
    # Remove this one-time operator script from the final reviewed commit.
    (ROOT / "vigil/releases/siai-2026/apply_approved_five.py").unlink()
    allowed = set(paths + [
        "vigil/VIGIL.Incidents.Index.json",
        "vigil/VIGIL.Harm.Dimensions.Index.json",
        "vigil/VIGIL.Incidents.Jurisdictions.Index.json",
        FACTS, PACKET, "vigil/releases/siai-2026/apply_approved_five.py",
    ])
    status_lines = subprocess.check_output(
        ["git", "status", "--porcelain", "--untracked-files=all"],
        cwd=ROOT, text=True).splitlines()
    for line in status_lines:
        assert line[3:] in allowed, ("unexpected changed file", line)
    run("git", "add", "-A", "--", *sorted(allowed))
    run("git", "diff", "--cached", "--check")
    run("git", "commit", "-m", "adjudication(siai): promote approved five to 0.8.1 with retained findings")
    run("git", "push", "origin", f"HEAD:refs/heads/{BRANCH}")
    print("Complete: 169/200 canonical v0.8.1; INC-118 retained on hold.")

if __name__ == "__main__":
    main()
