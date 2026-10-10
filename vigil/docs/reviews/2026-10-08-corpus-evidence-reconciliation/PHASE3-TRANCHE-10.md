# Phase 3 — tenth source-first reconciliation tranche

Date: 2026-10-09  
Branch: `agent/incident-ecosystem-ingestion`  
Baseline: `a7b07d825db94af93f3d854a41f7bc821fc16ffa`

Ten repaired, two held: **31 clauses → 45 episodes; 26 indexed EXTREQ rows reconciled.** The corpus campaign remains ongoing.

| Incident | Clauses → episodes | Indexed EXTREQ | Material repair | Commit |
|---|---:|---:|---|---|
| INC-013 | 3 → 5 | 0 | Restore legal disruption, retaliation and later civil proceedings after the distinct credential, intermediary and guardrail activities. | `479a84195a20742e8c696e8ad053b2a80d73f124` |
| INC-045 | 2 → 5 | 0 | Separate model-turn transmission, independent repository snapshots, settings tests, corrected measurement and tested-account recovery. | `b2d206bc69dc53264ff755dbdc985f35bca31958` |
| INC-094 | 2 → 4 | 5 | Distinguish existing foothold and staged tools from the operator’s deliberate approval removal, logged agent actions and later investigation. | `97cb34114a376b6863e146ba419b282a2808cd85` |
| INC-117 | 4 → 4 | 5 | Put pre-incident policy before the forensic task; consolidate the two accounts of the same refusal, then retain fallback and its results. | `57a3d9aa4ad68edfce69c5a01f966fdfd8e25cc1` |
| INC-118 | 3 → 4 | 3 | Consolidate three thematic descriptions of one agentic campaign and restore access preparation, persistence, separate victims and data aggregation. | `ad062328883488f84ef842a06f71ac769c727ca0` |
| INC-123 | 3 → 4 | 7 | Separate benchmark assignment and scoring, specific monitor misses, independent reasoning-visibility variants and dated corrections. | `68c4c19e97c7781a1d8de21c86fae41118b76e55` |
| INC-124 | 4 → 4 | 0 | Restore the simulated context and execution sequence; merge two class interpretations of the same cache substitution. | `bbcaa5638e70886604c7142fcd2aeb03f6f7227f` |
| INC-125 | 3 → 5 | 0 | Distinguish experimental variants, token-limit investigation and permitted abstention; qualify the report’s ground-truth exceptions. | `6381e4665d91afb7422153df0537a3abffb456f4` |
| INC-126 | 4 → 5 | 6 | Restore initial internal escalation and eventual human posting; preserve the source authors’ concern about proxy coaching alongside bounded human review findings. | `e5025ccb878ed45450a060387c82d906fb127141` |
| INC-127 | 3 → 5 | 0 | Restore patch-before-campaign chronology, laboratory preparation, timed campaign stages, uneven escalation, specific blocking and later maintenance releases. | `e8dbce87ac54f20e8b6d159e5cbb7df841412052` |

Follow-up fixture/source-type/rubric clarification commit: `438341c9f4e5c219a2d463ec98c5021c1273f76e`. Source type uses the existing canonical vocabulary. No validator or schema rule changed.

INC-013 separates provider allegations, legal seizure, retaliation, entry of default, magistrate recommendation and metadata-only later grant. Final-order text is unavailable; no criminal conviction or damages award is inferred. INC-045 preserves the researcher’s corrected measurement and limits the size finding to captured bytes. INC-094 separates deliberate unattended mode, logs, staged tools and unverified mitigation. INC-117 places policy before the response and consolidates two reports of one refusal. INC-118 keeps victim paths and reused historical data distinct. INC-123 incorporates dated errata. INC-124 merges interpretations of one substitution and restores its setup. INC-125 separates variants and token-limit effects and retains defensible label exceptions. INC-126 restores eventual posting and the source authors’ concern about proxy coaching without reversing the independent-human-review finding. INC-127 separates the patch timeline, lab preparation, wider campaign, uneven escalation, one WAF block and maintenance releases. PaperCut explicitly did not independently verify GreyNoise’s indicators.

All canonical mappings, class roles/rationales, HIM dimensions/severity, external decisions/bases and adjudication coverage preserved. Two additional sources for court proceedings preserve access limits. No classification-completeness claim is converted into source exhaustiveness.

## Audit and validation

Ten repair manifests contain original blobs/clauses/sources, old-to-new semantic crosswalks, every external row, preservation checks and retrieval limits. All ten rebuild guards passed. Canonical/public, source/interpretive/authorship/component and occurrence-requirement validators passed for 179 records and 598 sources. Taxonomy integrity passed for 76 classes in 15 families. 79 unit tests and the pipeline-state check passed. Initial rule-test failures were a live-fixture assumption about INC-126’s first clause; four existing rule tests now exercise the same expectations with an isolated taxonomy fixture and unchanged rules. This is an execution repair under MAINTAINERS.md, not a semantic validator change. No new tests or corpus acceptance rule were added.

Published checkpoint: [`0b1f3e0fa164a250a17488ad4b2cd75dd3f0d87f`](https://github.com/CAM-Initiative/Vigil/commit/0b1f3e0fa164a250a17488ad4b2cd75dd3f0d87f). All three associated checks passed: [push records](https://github.com/CAM-Initiative/Vigil/actions/runs/37885010713), [PR records](https://github.com/CAM-Initiative/Vigil/actions/runs/37885015431), and [taxonomy publications](https://github.com/CAM-Initiative/Vigil/actions/runs/37885015421). Tranche 09’s published commits and all three passed checks are recorded in its report.

## Remaining workload

| Review state | Count |
|---|---:|
| Bounded source-first repaired | 90 |
| Pilot-only | 4 |
| Preliminary spotcheck | 1 |
| Awaiting, including held cases | 84 |
| Total | 179 |

**89 cases remain without completed source-first repair.** Cumulative indexed EXTREQ reconciliations: **460**; these are evidence-reference repairs, not new compliance-failure counts. Live corpus: 655 clauses/episodes, 598 sources, 1,315 external rows. AI-authored bounded review, not human verification or exhaustiveness certification.

INC-120 and INC-139 remain awaiting with reasons and next evidence in `PHASE3-TRANCHE-10-HELD-EVIDENCE.md`. No held case is counted as repaired. Branch remains unmerged; continue remaining records.

## Artefact disposition

- LIVE: ten canonical records.
- GENERATED: public Incident index.
- REVIEW/AUDIT: ten manifests, held notes, inventories, campaign and reports.
- TEST FIXTURE: execution-only isolation of four existing taxonomy rule tests.
- RETIRE: none. Temporary orchestration remains outside the repository.


Publication-reference reconciliation, 9 October 2026: the table and fixture-follow-up reference now use the actual GitHub commit identities from this branch's published history. Earlier provisional identities were superseded at publication. No canonical episode, mapping or assessment changed in this documentation reconciliation.
