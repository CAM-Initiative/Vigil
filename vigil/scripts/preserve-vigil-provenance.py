#!/usr/bin/env python3
"""Preserve record-specific provenance against the legacy registry migration.

The July 14 provenance migration is append-only historical metadata. It must not
replace a newer record-specific current review or overwrite source-access facts
that were established during direct review.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
RECORDS = VIGIL / "records"
GENERIC_REVIEW_ID = "VIGIL-REVIEW-2026-07-14-GPT-5.6-THINKING"


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain one JSON object")
    return value


def write(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def access(status: str, method: str, direct: bool, limitations: list[str]) -> dict[str, Any]:
    return {
        "access_status": status,
        "reviewing_system": "GPT-5.6 Thinking",
        "access_method": method,
        "direct_primary_artefact_review": direct,
        "limitations": limitations,
    }


RESTORATIONS: dict[str, dict[str, tuple[dict[str, Any], str]]] = {
    "VIGIL-2026-FM-0034": {
        "https://www.blackhc.net/essays/trust_is_not_governance/": (
            access(
                "direct text review",
                "public web retrieval and user-supplied source context",
                True,
                [
                    "Historical acquisition conditions and internal oversight arrangements are partly dependent on public reporting rather than a complete published contractual record.",
                    "The source represents the author's analysis and should not be treated as an adjudicated finding against Google or DeepMind.",
                ],
            ),
            "Direct review of the public essay, bounded by the availability and quality of the historical sources on which it relies.",
        ),
        "https://x.com/blackhc?s=11": (
            access(
                "user-supplied quotation and account URL; post-level artefact not independently retrieved",
                "user quotation, account link, and related public essay",
                False,
                [
                    "The exact post URL was not available in the review package.",
                    "Wording and date rely on the human governance editor's supplied quotation and contemporaneous discussion.",
                ],
            ),
            "Human-supplied quotation corroborated by the author's related public essay; no claim of direct post-level retrieval is made.",
        ),
        "https://x.com/demishassabis/status/2076957440109625718": (
            access(
                "link and public reporting reviewed; X rendering may be access-limited",
                "user-supplied post URL and public reporting describing the proposal",
                False,
                [
                    "The reviewing system did not rely on an authenticated native X session.",
                    "Assessment concerns omitted governance primitives and does not assert that the proposal has been implemented.",
                ],
            ),
            "Public post metadata, user-supplied context, and corroborating public reporting.",
        ),
        "https://theintercept.com/2024/01/12/open-ai-military-ban-chatgpt/": (
            access(
                "public text report reviewed through web retrieval",
                "public web retrieval",
                True,
                [
                    "The report establishes a policy-text change, not the full internal rationale or every operational safeguard applied after the change.",
                    "Removal of a blanket prohibition does not by itself prove absence of narrower safety controls.",
                ],
            ),
            "Direct review of public reporting, with claims limited to the documented policy change.",
        ),
        "https://apnews.com/article/8a7ba341e06a66e9a7935bb06214edcb": (
            access(
                "public text report reviewed through web retrieval",
                "public web retrieval",
                True,
                [
                    "The source reports the judgement of a departing safety leader and OpenAI's response; it does not independently audit all internal safety processes.",
                    "Organisational integration of a team is not automatically equivalent to removal of its functions.",
                ],
            ),
            "Direct review of authoritative news reporting and attributed public statements.",
        ),
        "https://arxiv.org/abs/2509.24394": (
            access(
                "abstract and public research record reviewed",
                "public web retrieval",
                True,
                [
                    "The paper analyses policy affordances and does not prove that every discretion identified has been exercised unsafely.",
                    "The record adopts the paper as independent expert analysis, not as final legal or technical adjudication.",
                ],
            ),
            "Direct review of the public research abstract and reported methodology and conclusions.",
        ),
    },
    "VIGIL-2026-FM-0035": {
        "https://www.chinatalk.media/p/how-to-buy-cheap-claude-tokens-in": (
            access(
                "directly reviewed",
                "Public web-text review on 2026-07-16",
                True,
                [
                    "Some allegations were not independently verified.",
                    "The report does not establish that all Chinese intermediaries are abusive.",
                ],
            ),
            "Used only for the source-qualified claim stated above.",
        ),
        "https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks": (
            access(
                "directly reviewed",
                "Public web-text review on 2026-07-16",
                True,
                [
                    "Provider telemetry and attribution were not independently reproduced.",
                    "Named-company claims remain allegations.",
                ],
            ),
            "Used only for the source-qualified claim stated above.",
        ),
        "https://arxiv.org/abs/2603.01919": (
            access(
                "directly reviewed",
                "Public web-text review on 2026-07-16",
                True,
                ["Preprint; may be revised.", "The sample does not establish market-wide prevalence."],
            ),
            "Used only for the source-qualified claim stated above.",
        ),
        "https://arxiv.org/abs/2604.08407": (
            access(
                "directly reviewed",
                "Public web-text review on 2026-07-16",
                True,
                ["Preprint; may be revised.", "Observed conduct cannot be generalised to every router."],
            ),
            "Used only for the source-qualified claim stated above.",
        ),
    },
    "VIGIL-2026-PATCH-0022": {
        "https://turntrout.com/red-line-framework": (
            access(
                "directly reviewed",
                "Direct web-text retrieval and analysis on 2026-07-16",
                True,
                [
                    "The review assessed the published text and did not independently verify private correspondence granting courtesy permission.",
                    "Legal claims and jurisdiction-specific assertions in the external framework were not adopted as CAM findings through this patch.",
                ],
            ),
            "The external framework is treated as a conceptual and provenance source. CAM adopted only the concepts expressly identified in this patch after corpus-adjacency and constitutional-authority review.",
        ),
        "https://github.com/CAM-Initiative/Caelestis/commit/207538cc0a2e4e38a39809455694ffc5ef61c2b5": (
            access(
                "directly reviewed",
                "Direct GitHub repository and commit review",
                True,
                [
                    "The implementation is present on the Caelestis working branch and draft PR at record creation; squash merge to main has not yet occurred.",
                    "External runtime or institutional adoption is not established.",
                ],
            ),
            "The repository commit is the authoritative implementation artefact for the changes described in this record.",
        ),
        "https://chatgpt.com/g/g-p-6823b831b67c8191a9415269aaec338f/c/6a583699-2684-83ec-9712-57f9f821f607": (
            access(
                "directly reviewed",
                "Current governed conversation context",
                True,
                [
                    "The conversation URL may require authorised account access.",
                    "The source is an internal governance artefact rather than independent external corroboration.",
                ],
            ),
            "Used to preserve human governance decisions, rejected formulations, final clause placement, and the boundary between external inspiration and CAM adoption.",
        ),
    },
}


def review_sort_key(review: dict[str, Any]) -> tuple[str, int]:
    date = str(review.get("review_date", ""))
    non_generic = int(review.get("review_id") != GENERIC_REVIEW_ID)
    return date, non_generic


def restore_record(path: Path) -> bool:
    record = load(path)
    before = json.dumps(record, ensure_ascii=False, sort_keys=True)
    record_id = str(record.get("id", ""))

    provenance = record.get("interpretive_provenance")
    if isinstance(provenance, dict):
        history = provenance.get("review_history")
        if isinstance(history, list):
            candidates = [item for item in history if isinstance(item, dict)]
            if candidates:
                provenance["current_ai_review"] = max(candidates, key=review_sort_key)

    source_map = RESTORATIONS.get(record_id, {})
    sources = record.get("source_records")
    if isinstance(sources, list):
        for source in sources:
            if not isinstance(source, dict):
                continue
            restored = source_map.get(str(source.get("source_url", "")))
            if restored is None:
                continue
            access_value, reliance = restored
            source["primary_artefact_access"] = access_value
            source["interpretive_reliance"] = reliance

    after = json.dumps(record, ensure_ascii=False, sort_keys=True)
    if after != before:
        write(path, record)
        return True
    return False


def patch_legacy_migration() -> bool:
    path = VIGIL / "scripts" / "migrate-vigil-interpretive-provenance.py"
    text = path.read_text(encoding="utf-8")
    revised = text.replace(
        '    block["current_ai_review"] = review_entry()\n',
        '    if not isinstance(block.get("current_ai_review"), dict):\n        block["current_ai_review"] = review_entry()\n',
    )
    revised = revised.replace(
        '        source["evidence_modality"] = modality(source)\n        source["primary_artefact_access"] = artefact_access(source)\n        source["interpretive_reliance"] = (\n',
        '        source.setdefault("evidence_modality", modality(source))\n        source.setdefault("primary_artefact_access", artefact_access(source))\n        source.setdefault("interpretive_reliance", (\n',
    )
    revised = revised.replace(
        '            "Assessment is limited to the evidence actually accessible to the named reviewer and must not be read as direct audiovisual verification unless primary_artefact_access states otherwise."\n        )\n',
        '            "Assessment is limited to the evidence actually accessible to the named reviewer and must not be read as direct audiovisual verification unless primary_artefact_access states otherwise."\n        ))\n',
        1,
    )
    if revised != text:
        path.write_text(revised, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed = 0
    for record_id, folder in (
        ("VIGIL-2026-FM-0034", "failures"),
        ("VIGIL-2026-FM-0035", "failures"),
        ("VIGIL-2026-PATCH-0022", "patches"),
    ):
        path = RECORDS / folder / "2026" / f"{record_id}.json"
        if restore_record(path):
            changed += 1
    patched = patch_legacy_migration()
    print(f"VIGIL provenance preservation completed: {changed} record(s) restored; legacy migration patched={patched}.")


if __name__ == "__main__":
    main()
