# VIGIL taxonomy 0.8.0 — reconciliation status, 23 October 2026

**Campaign branch:** chore/siai-2026-release-readiness-20261023  
**This is a working-branch candidate**, not an approved merged source, final SIAI release manifest, human validation certificate or v1.0.0 tag.

## Actual progress at validated substantive commit `771ccba82f0a0cdd5c632ca388c88306029c4310`

- **200 canonical Incident records**; **20** with canonical `taxonomy_classification.taxonomy_version = "0.8.0"` (baseline 14). Six newly brought forward from `0.6.11`: INC-073, INC-199, INC-200, INC-201, INC-202 and INC-203.
- **11/200** have current-campaign dated v0.8.0 screen packets: INC-073, INC-117, INC-129, INC-196–203. **189 still await campaign screening**. Six were canonically restamped with detailed current-edition decisions.
- **6/200 newly re-adjudicated and canonically updated**: INC-073, INC-199–203. INC-073 remains `classification-disputed` with all four mapping roles/confidence preserved. INC-200 moved from `unclassified` to `provisionally-classified` after a bounded first-party-attributed FC-083 **successful-invariant** was supported for the majority of responsive Coopérative U stores. All harmed-store loss evidence, outstanding clause holds, HIM, EXTREQ and prior records remain preserved.
- Existing **14** recorded-v0.8.0 incidents are prior current-version records, **not automatically declared re-reviewed in this campaign**.
- Recorded edition distribution: v0.6.9 = 31, v0.6.10 = 3, v0.6.11 = 133, v0.7.0 = 13, v0.8.0 = 20. Status distribution is 139 classified, 36 unclassified, 20 provisional, 3 requiring human review, and 2 disputed.
- No new GitHub Issues raised merely because an Incident has contested criteria or inaccessible technical detail; that belongs in canonical evidence and dated review.

## Completed versioned current-edition records

| Incident | Prior -> current recorded taxonomy | Record revision | Classification disposition | New packet |
| --- | --- | --- | --- | --- |
| INC-073 — alleged Anthropic/Alibaba distillation | 0.6.11 -> 0.8.0 | 1.1.21 -> 1.1.22 | Four existing FC-067/041/083/068 failures retained with provider attribution and campaign/control-scope dispute explicit. Recognition of first-pool ban does not prove whole-campaign containment or per-response classifier failure | [INC-073](INC-73-CURRENT-080-DECISION.json) |
| INC-199 — DJI Romo cross-device authorisation | 0.6.11 -> 0.8.0 | 0.1.5 -> 0.1.6 | Retain FC-003 failure and FC-002 genuine Boundary. Update the canonical Boundary criteria edition to 0.8.0; preserve the historical 0.7.0 decision text in audit. App-PIN and later remediation remain evidence-limited; provisional state retained | [INC-199](INC-199-CURRENT-080-DECISION.json) |
| INC-200 — Danfoss refrigeration controllers | 0.6.11 -> 0.8.0 | 0.1.6 -> 0.1.7 | **New** FC-083 successful-invariant in E006: first-party report credits staff and refrigeration technicians with cold-chain protection at most of 80 affected Coopérative U stores. Other stores and Mirepoix control-effect uncertainty remain; status provisional | [INC-200](INC-200-CURRENT-080-DECISION.json) |
| INC-201 — AIOpsDoom | 0.6.11 -> 0.8.0 | 0.1.3 -> 0.1.4 | Retain FC-063 failure, FC-001 failure, FC-083 bounded success; original provisional status remains | [INC-201](INC-201-CURRENT-080-DECISION.json) |
| INC-202 — OSS-Fuzz-Gen FalseCrashReducer | 0.6.11 -> 0.8.0 | 0.1.3 -> 0.1.4 | Retain FC-062 failure and FC-016 bounded success; original provisional status remains | [INC-202](INC-202-CURRENT-080-DECISION.json) |
| INC-203 — Dixell refrigeration incidents | 0.6.11 -> 0.8.0 | 0.1.4 -> 0.1.5 | Retain FC-083 success **only for the reported Bordeaux monitoring/intervention**; unrelated Lescure disruption/stock losses and unresolved command authority remain separate and provisional | [INC-203](INC-203-CURRENT-080-DECISION.json) |

These are **evidence-bounded source-based reassessments**, not bulk version-field replacements. The original study is directly cited and existing before/after mappings, chronology, rejected neighbouring classes, source access limitations and non-reopening of independent HIM/EXTREQ findings are documented per case.

## Other screened cases — not canonically restamped

- **INC-117**: preserved FC-043 failure; the specific classifier policy/exclusion question remains bounded within the Incident, not a new issue. Historic adjudication taxonomy version remains unchanged until full supported review.
- **INC-129**: disputed FC-075/FC-078 Boundary retained pending unavailable governing antecedent; no forced polarity or version bump.
- **INC-196, INC-197, INC-198**: retain evidence-limited human-review states and rejection of unsupported FC-049/086/087 admissions; no mechanical stamp.

## Remaining process

1. Move next through **previously source-adjudicated, version-older cases with published recognition conditions** (e.g. additional provisional and unclassified records beyond INC-073/200), testing all materially plausible candidates, positive and negative class criteria, temporal ordering and every prior mapping.
2. Handle **remaining genuinely disputed, unclassified and provisional outcomes** carefully. A defensible hold can be reviewed against 0.8.0 without changing its historical stamp or forcing success/failure.
3. For each truly re-adjudicated case: add a dated per-Incident decision packet; update canonical version and current taxonomy edition *only when criteria were actually reviewed*; append new AI authorship/interpretive provenance, rebuild the public and geographic projections and rerun validation. Do not represent changed version strings as verification.
4. Complete remaining 189 screens and evidence-limited dispositions. Reconciliation is not finished simply because the number of records stamped 0.8.0 rises.
5. Keep this PR draft until maintainer-approved final readiness, then merge to main and build the SIAI dataset v1.0.0 release checksum **from that final main commit**.

## Verified build status

At substantive candidate commit `771ccba82f0a0cdd5c632ca388c88306029c4310`, all four workflows passed: VIGIL records, SIAI research snapshot preflight, External governance, and VIGIL taxonomy publication. The preflight inventory from a working branch remains a preflight only, not an immutable main-based final release.
