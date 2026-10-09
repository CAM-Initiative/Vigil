# Phase 3 — ninth source-first reconciliation tranche

Date: 2026-10-09  
Branch: `agent/incident-ecosystem-ingestion`  
Baseline: `4d83f011acf825be235fff4cbd31f7d371fcbc08`

Eleven records repaired; two reviewed and held. **29 clauses → 48 episodes; 24 indexed EXTREQ rows reconciled.** The corpus campaign remains ongoing.

## Case results

| Incident | Clauses → episodes | Indexed EXTREQ | Material repair | Commit |
|---|---:|---:|---|---|
| INC-049 | 3 → 5 | 0 | Restored post-meeting instructions before transfer outcome and separated later identification/investigation from the synthetic meeting. | `4b546c58d3d041d59d7a1eaf16ed53201be2ad90` |
| INC-050 | 2 → 4 | 4 | Separated application, flagged first interview, further assessment and deliberately observed second interview. | `224cd81f08e72ab4e9b645079a5ce5f1087b8052` |
| INC-051 | 3 → 5 | 1 | Reordered portrait alteration before accepted verification; restored intelligence, disputed arrest dating, seizure and institutional advice. | `65cc70d580199367953fb1681f5281b0976a7d37` |
| INC-052 | 2 → 5 | 0 | Placed attack delivery and execution before later analytical control discussion; restored persistence and kept correlated campaigns separate. | `48799544bc5113b0ad87f85d4dc578a73e6a18e7` |
| INC-054 | 2 → 5 | 0 | Separated pre-AI campaign, reported personal effects, repeated reports, identification and agreed civil remedy. | `5f77f0d645df721d7e77479239f8071a17f818ae` |
| INC-058 | 3 → 4 | 6 | Separated real-event correction from synthetic handoff, identity-protective cropping and later disclosure. | `cc621f48e65459db0f6899924f6f23f12f88fe24` |
| INC-079 | 2 → 3 | 0 | Separated creation and contribution omission from uninformed public distribution and later removal/apology. | `235a407450a9c60243e5f7edd131e20de6f435a7` |
| INC-082 | 3 → 4 | 0 | Merged three descriptions of one synthetic advertisement; restored escalating demands, discovery, extortion, reporting and individual consequences. | `49a8ac443ae4592253922fd8d57127472bc98d4d` |
| INC-083 | 3 → 5 | 0 | Merged thematic descriptions of the same campaign mechanism, restored follow-up funnel and separated loss/takedown aggregates and a specific false-article example. | `58fb988b8e2c2fbec654c88d209b91c15f982a97` |
| INC-145 | 3 → 5 | 12 | Separated invitation, security escalation, observed deception, payment-stage cutoff and retrospective technical account. | `75ca36917859dc7a1633644ebf11583662f27455` |
| INC-152 | 3 → 3 | 1 | Consolidated advertisement interpretations and restored public report, removal request and later denial in date order. | `99223273935062f17b46985d256333347d27e5f4` |

## Evidence boundaries

- INC-049: recorded conference, post-meeting instant messages and actual transfers remain separate. Other police cases are not merged.
- INC-050: the company deliberately observed the second interview. That does not resolve the first interview’s later take-home assessment or imply a hire. Shamar is separate.
- INC-051: portrait alteration precedes accepted verification. AI-assisted fifteen openings remain separate from thirty total openings and unallocated later financial activity. First-hand arrest-date reports conflict; that conflict remains explicit.
- INC-052: delivery and execution precede the recovered image. The later investigator refusal/sample discussion is not an attacker transcript. Related technical campaigns and advertised detection capability are not added as victims or proved containment.
- INC-054: pre-AI photographs, later synthetic depictions, personal effects, reporting, identification and civil remedy remain distinct. Agreed undertakings are not criminal convictions or independently verified deletion.
- INC-058/079: police joke image and parks flyer are separate events. Officer protection preceded the newsroom crop. Parks creation, mayoral publication, artist objection and response are distinct actions. Official supply or reuse alone does not establish verification laundering.
- INC-082: one advertisement carries several distinct interpretations. Follow-up document/payment demands, discovery, alleged extortion, reports and consequences are restored. The attorney’s broader totals remain attributed.
- INC-083: aggregate campaign funnel remains distinct from the specific Kohler/Bullock example. Neither aggregate loss nor all takedowns is AI-only. Recurring profiles and Meta’s separate detection claim do not establish eradication.
- INC-145: invitation, operative security report, deliberate observation, payment-stage cutoff and later analysis are separate. The accessible bank report clarifies adapted CEO footage, CFO voice and silent looped external participants.
- INC-152: the public alert and removal request preceded the Premier’s denial. A request is not a confirmed removal or prevention outcome.

All canonical mappings, class/role rationales, HIM dimensions and overall severity, independent external results/bases and coverage are preserved. New source records retain attribution and access limits. Original evidence is archived in manifests. No taxonomy or schema change.

## Held cases

INC-053 and INC-164 remain awaiting. See `PHASE3-TRANCHE-09-HELD-EVIDENCE.md` for issuer-access limitations and the real-clinician versus fictional-doctor discrepancy. Holds are not completed source-first repairs.

## Audit and validation

Eleven `INC-000NNN-phase3-tranche09-repair-manifest.json` files include baseline blobs, original clauses/sources, all evidence crosswalks, every external row and preservation checks. All eleven rebuild guards passed. Local canonical/public, source/interpretive/authorship/component and occurrence-requirement validators passed. Taxonomy integrity passed for 76 classes. 79 unit tests passed; pipeline-state and source-origin checks passed. Generated index parity is 179 entries. The record-test suite’s rejected negative fixtures are expected, not corpus failures.

Published commit identities and GitHub Actions results will be recorded after branch publication. Tranche 08’s report now records its published commits and three passed checks. No schema, validator, permanent test, builder or workflow was changed.

## Census

| Review state | Count |
|---|---:|
| Bounded source-first repaired | 80 |
| Pilot-only | 4 |
| Preliminary spotcheck | 1 |
| Awaiting source-first review, including two fresh holds | 94 |
| Total | 179 |

Cumulative indexed EXTREQ reconciliations: **434**. These are reference reconciliations, not new failure counts. Current corpus: 641 clauses/episodes, 596 sources and 1,315 external assessment rows. **99 cases remain without completed source-first repair.** This is bounded AI-authored review, not human certification or source exhaustiveness. Continue the campaign; branch remains unmerged.

## Artefact disposition

- LIVE: eleven canonical records.
- GENERATED: public Incident index.
- REVIEW/AUDIT: eleven manifests, held-evidence note, inventories, summary, campaign and reports.
- RETIRE: none. Temporary orchestration is outside the repository.
