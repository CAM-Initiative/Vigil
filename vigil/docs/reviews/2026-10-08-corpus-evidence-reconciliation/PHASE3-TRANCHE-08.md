# Phase 3 — eighth source-first reconciliation tranche

Date: 2026-10-09  
Branch: `agent/incident-ecosystem-ingestion`  
Baseline: `1bb12ccfbd4cd006f1f96769775f7d476e4bd008`

Thirteen previously awaiting records were reconciled. **34 clauses became 62 source-backed episodes**, with **14 indexed EXTREQ rows** reconciled individually. The campaign remains ongoing.

## Case results

| Incident | Clauses → episodes | Indexed EXTREQ | Material repair | Commit |
|---|---:|---:|---|---|
| INC-015 | 4 → 6 | 1 | Restored the premature resolved update, return to monitoring, further affected users and email sequence; separated an unconfirmed later individual ban. | `4ae94d4b321c46cce6c4ff9f45013cb6e13e5223` |
| INC-016 | 2 → 4 | 1 | Merged symptom and route-labelling interpretations of the same initial state; separated gradual recovery, applied mitigation and final resolution. | `17ccfaf96a8693733601f9e11086710ec5d0909d` |
| INC-018 | 4 → 5 | 1 | Merged duplicated Classic fallback, restored the required app update and separated first fix, recurrence and final recovery. | `7b9a479ed47e69cd7f6a645bf4765e7fa7cbf89c` |
| INC-019 | 2 → 3 | 0 | Separated onset notice, mitigation and resolution; bounded the 105-minute figure to the public update window. | `21fa20b1c73fc8007434c341a145af25ef9ce2b0` |
| INC-020 | 2 → 3 | 0 | Separated scope, recovery and occurrence identity; corrected the current component list from twelve to eleven while auditing the historical discrepancy. | `6e5f44b7c76c4e03326b5b6b04327e4d536a543f` |
| INC-021 | 3 → 5 | 1 | Merged duplicate route-identification descriptions; retained heterogeneous fallbacks and later attributed account complaints without conflating them with the separate suspension incident. | `2ccabf482bb31fae7b10e41ce191f1bffe77695c` |
| INC-022 | 2 → 5 | 1 | Restored mitigation actions and three recovery stages; corrected authentication recovery from 82 to 62 minutes and kept 82 minutes for edge availability. | `d2c464b5fe1df238539160b3b0a720a7c8c1f300` |
| INC-027 | 3 → 5 | 0 | Restored identification and three separate function-recovery transitions; preserved the unresolved meaning of the initial 403 response. | `109776508fa108d5c77cd6207fe955a037f00942` |
| INC-038 | 2 → 3 | 0 | Separated initial identification, continued investigation and final recovery without equating the eleven-day public interval with a continuous total outage. | `39353121bce4a26f28e593c720c3fc8fa6d8f986` |
| INC-039 | 2 → 3 | 1 | Merged two interpretations of the same partial-restoration state; restored the later broad resolution while preserving missing feature-specific recovery and log-loss evidence. | `7104e5a7a4e9276ba2025b2af223e4789add666f` |
| INC-095 | 3 → 6 | 7 | Separated upstream compromise, publication, working Linux PyPI payload, nonfunctional npm payload, external detection/removal and investigation closure. | `ccf3db09183023d981cbfe4746e63238c6952fa1` |
| INC-107 | 3 → 8 | 0 | Merged duplicate log/reconstruction clauses and restored access, download, patch-before-discovery, containment, notification and corrected disclosure stages. | `c37d4b5d658bbbcd787195a7e8dd26a490381638` |
| INC-108 | 2 → 6 | 1 | Restored infrastructure test, instruction seeding, hidden task, concealment and decommissioning-before-disclosure chronology; distinguished the demonstrated proof of concept from possible delivery routes. | `b74046b181ffaf2e0d13099c240c2bf434dfa76d` |

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
