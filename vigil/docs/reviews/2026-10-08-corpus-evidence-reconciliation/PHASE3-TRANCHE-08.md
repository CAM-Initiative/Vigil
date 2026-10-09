# Phase 3 — eighth source-first reconciliation tranche

Date: 2026-10-09  
Branch: `agent/incident-ecosystem-ingestion`  
Baseline: `1bb12ccfbd4cd006f1f96769775f7d476e4bd008`

Thirteen previously awaiting records were reconciled. **34 clauses became 62 source-backed episodes**, with **14 indexed EXTREQ rows** reconciled individually. The campaign remains ongoing.

## Case results

| Incident | Clauses → episodes | Indexed EXTREQ | Material repair | Commit |
|---|---:|---:|---|---|
| INC-015 | 4 → 6 | 1 | Restored the premature resolved update, return to monitoring, further affected users and email sequence; separated an unconfirmed later individual ban. | `9c76d680272b381059b37c3918d3ac17ba3ec691` |
| INC-016 | 2 → 4 | 1 | Merged symptom and route-labelling interpretations of the same initial state; separated gradual recovery, applied mitigation and final resolution. | `432dd7c8015314093476af5a6cc3b747c246be35` |
| INC-018 | 4 → 5 | 1 | Merged duplicated Classic fallback, restored the required app update and separated first fix, recurrence and final recovery. | `77cd4a6ce4b23c3b956c0554cd9c484e1f75b9a4` |
| INC-019 | 2 → 3 | 0 | Separated onset notice, mitigation and resolution; bounded the 105-minute figure to the public update window. | `c5b508a1b830ee72f3e00f6793d70cd8c9d29b1b` |
| INC-020 | 2 → 3 | 0 | Separated scope, recovery and occurrence identity; corrected the current component list from twelve to eleven while auditing the historical discrepancy. | `f674d592cecb111dfe53532de8c05546ace6ed59` |
| INC-021 | 3 → 5 | 1 | Merged duplicate route-identification descriptions; retained heterogeneous fallbacks and later attributed account complaints without conflating them with the separate suspension incident. | `5f7cc3b278c76a74ed3b41d9667148aa46eca931` |
| INC-022 | 2 → 5 | 1 | Restored mitigation actions and three recovery stages; corrected authentication recovery from 82 to 62 minutes and kept 82 minutes for edge availability. | `b93af06d9b56b0cb1b7508cb82d24269d8fd36a6` |
| INC-027 | 3 → 5 | 0 | Restored identification and three separate function-recovery transitions; preserved the unresolved meaning of the initial 403 response. | `fe5285b6beb6fee2d7fd26738044cf935477315f` |
| INC-038 | 2 → 3 | 0 | Separated initial identification, continued investigation and final recovery without equating the eleven-day public interval with a continuous total outage. | `eae1f48c64bdacf3c506ffe80024a047f30dd3b9` |
| INC-039 | 2 → 3 | 1 | Merged two interpretations of the same partial-restoration state; restored the later broad resolution while preserving missing feature-specific recovery and log-loss evidence. | `d5be84f1cc9e1ab2ce4805adb40d08c28d0a89ba` |
| INC-095 | 3 → 6 | 7 | Separated upstream compromise, publication, working Linux PyPI payload, nonfunctional npm payload, external detection/removal and investigation closure. | `0b5371b21f4adf231de7a8e057619934252fe007` |
| INC-107 | 3 → 8 | 0 | Merged duplicate log/reconstruction clauses and restored access, download, patch-before-discovery, containment, notification and corrected disclosure stages. | `e9524eaeec0100a35c71ad242a1c051030c31ab5` |
| INC-108 | 2 → 6 | 1 | Restored infrastructure test, instruction seeding, hidden task, concealment and decommissioning-before-disclosure chronology; distinguished the demonstrated proof of concept from possible delivery routes. | `d093baac4c8fb738f31399429c1ab5f21169d232` |

## Evidence and interpretation

First-party status notices, post-incident write-ups and originating technical disclosures were directly read. Current source searches checked later updates. User allegations, support replies and researcher statements mediated by a written interview retain attribution. No attack was rerun.

- INC-015: an initial resolved notice preceded renewed monitoring, further affected users and continued credit work. The 9 June ban and later appeal-delay allegations do not establish a provider-confirmed common cause. A later thread was added; prior source context claiming confirmed linkage was corrected explicitly.
- INC-016/021/039: duplicate interpretations of the same access state were merged while preserving canonical and unresolved relationships together. Partial status accuracy does not establish every fallback or every feature’s restoration.
- INC-018/027: first fix, required app update, recurrence and distinct function restoration stages remain explicit. A 403 alone does not establish a misleading authority state.
- INC-019/020/038: published notice windows remain separate from true onset and total unavailability. Same-day incidents retain distinct identity. INC-020’s current provider page lists eleven components, omitting Atlas from the prior twelve-item account. The prior statement is archived in the manifest; no historical capture establishes when it changed.
- INC-022: authentication recovery is approximately 62 minutes, edge availability 82 and overall metrics 102. Several mitigation measures are listed without inventing their exact internal order.
- INC-095: working Linux PyPI import malware is separate from nonfunctional compromised npm paths. External detection and provider removal are not assumed to form one proved control chain. Investigation closure does not prove all customer cleanup.
- INC-107: advisory miss precedes access and download; patching precedes retrospective detection. Containment, preservation, school/regulator notification, individual notices, corrected data-field disclosure and unfinished recovery are restored. Log capture and reconstruction analyse one review episode.
- INC-108: precursor shared-state test and shared-conversation proof of concept remain distinct. Hidden email retrieval and normal visible output are concurrent aspects of the demonstrated turn. The later attributed interview places a failed early-July retest before disclosure; no disclosure-caused-removal claim or wider victim exploitation is introduced.

All canonical mappings, roles, confidence and distinct relationship rationales remain. All harm bands and independent external results/bases remain. INC-020’s source-context and HIM evidence text were corrected for the current component count without changing severity. Two later sources were added. Exact old/new metadata and findings are preserved in the manifests. Existing unresolved conditions remain partial; no new class or taxonomy promotion occurred.

INC-091’s later provider routing write-up was located during selection. It requires a separate full follow-up against monitoring/escalation criteria and provider-specific timelines. It remains awaiting review and is not counted as a repair or completed hold.

## Audit and validation

Each case has an `INC-000NNN-phase3-tranche08-repair-manifest.json` in this directory. Manifests include baseline/blobs, original clauses and source arrays, episode crosswalks, every EXTREQ row, explicit evidence corrections and source retrieval limits.

All thirteen rebuild guards passed against the exact baseline. The deterministic builder and canonical/public validators passed for 179 records. Source, interpretation, authorship and component checks passed. All 84 regression tests passed; pipeline-state and source-origin checks passed. Published commit identities and GitHub Actions results are recorded after publication. No schema, validator, permanent test, builder or workflow rule changed.

## Census

| Review state | Count |
|---|---:|
| Bounded source-first repaired | 69 |
| Pilot-only | 4 |
| Preliminary spotcheck | 1 |
| Awaiting source-first review | 105 |
| Total | 179 |

Cumulative indexed EXTREQ reconciliations: **410**. Current live corpus: 622 episodes/clauses, 594 sources and 1,315 external assessment rows. Remaining source-first workload: **110** cases. These counts do not certify source exhaustiveness or human verification. The branch remains unmerged.

## Artefact disposition

- LIVE: thirteen canonical records.
- GENERATED: rebuilt public Incident index.
- REVIEW/AUDIT: thirteen manifests, inventories, summary, campaign and reports.
- RETIRE: none. Temporary orchestration remains outside the repository.
