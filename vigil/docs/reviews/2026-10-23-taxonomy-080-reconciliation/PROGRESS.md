# VIGIL taxonomy 0.8.0 — reconciliation status, 23 October 2026

**Campaign branch:** chore/siai-2026-release-readiness-20261023  
**This is a working-branch candidate**, not an approved merged source, final SIAI release manifest, human validation certificate or v1.0.0 tag.

## Actual progress at validated candidate commit `ef2140edcc9d481e671e175cb8fc9cc68fe4dfaf`

- **200 canonical Incident records**; **18** with canonical `taxonomy_classification.taxonomy_version = "0.8.0"` (baseline 14). Four newly brought forward from `0.6.11`: INC-199, INC-201, INC-202 and INC-203.
- **9/200** have current-campaign dated v0.8.0 screen packets: INC-117, INC-129, INC-196–199 and INC-201–203. **191 still await campaign screening**. Only **four** were substantively canonically restamped during the present campaign.
- **4/200 newly re-adjudicated and canonically updated on this branch**: INC-199, INC-201, INC-202 and INC-203. Their `classification_status` remains `provisionally-classified` due to original evidence limits. All previously admitted mapping roles/confidence, valid Boundaries, independently evidenced successes, HIM and external requirements are preserved.
- Existing **14** recorded-v0.8.0 incidents are prior current-version records, **not automatically declared re-reviewed in this campaign**.
- Recorded edition distribution: v0.6.9 = 31, v0.6.10 = 3, v0.6.11 = 135, v0.7.0 = 13, v0.8.0 = 18. Status distribution remains 139 classified, 37 unclassified, 19 provisional, 3 requiring human review, and 2 disputed.
- No new GitHub Issues raised merely because an Incident has contested criteria or inaccessible technical detail; that belongs in canonical evidence and dated review.

## Completed versioned current-edition records

| Incident | Prior -> current recorded taxonomy | Record revision | Classification disposition | New packet |
| --- | --- | --- | --- | --- |
| INC-199 — DJI Romo cross-device authorisation | 0.6.11 -> 0.8.0 | 0.1.5 -> 0.1.6 | Retain FC-003 failure and FC-002 genuine Boundary. Update the canonical Boundary criteria edition to 0.8.0; preserve the historical 0.7.0 decision text in audit. App-PIN and later remediation remain evidence-limited; provisional state retained | [INC-199](INC-199-CURRENT-080-DECISION.json) |
| INC-201 — AIOpsDoom | 0.6.11 -> 0.8.0 | 0.1.3 -> 0.1.4 | Retain FC-063 failure, FC-001 failure, FC-083 bounded success; original provisional status remains | [INC-201](INC-201-CURRENT-080-DECISION.json) |
| INC-202 — OSS-Fuzz-Gen FalseCrashReducer | 0.6.11 -> 0.8.0 | 0.1.3 -> 0.1.4 | Retain FC-062 failure and FC-016 bounded success; original provisional status remains | [INC-202](INC-202-CURRENT-080-DECISION.json) |
| INC-203 — Dixell refrigeration incidents | 0.6.11 -> 0.8.0 | 0.1.4 -> 0.1.5 | Retain FC-083 success **only for the reported Bordeaux monitoring/intervention**; unrelated Lescure disruption/stock losses and unresolved command authority remain separate and provisional | [INC-203](INC-203-CURRENT-080-DECISION.json) |

These are **evidence-bounded source-based reassessments**, not bulk version-field replacements. The original study is directly cited and existing before/after mappings, chronology, rejected neighbouring classes, source access limitations and non-reopening of independent HIM/EXTREQ findings are documented per case.

## Other screened cases — not canonically restamped

- **INC-117**: preserved FC-043 failure; the specific classifier policy/exclusion question remains bounded within the Incident, not a new issue. Historic adjudication taxonomy version remains unchanged until full supported review.
- **INC-129**: disputed FC-075/FC-078 Boundary retained pending unavailable governing antecedent; no forced polarity or version bump.
- **INC-196, INC-197, INC-198**: retain evidence-limited human-review states and rejection of unsupported FC-049/086/087 admissions; no mechanical stamp.

## Remaining process

1. Move next through **previously source-adjudicated, version-older cases with published recognition conditions** (e.g. INC-200 and other older records with independently supported mappings), testing all materially plausible candidates, positive and negative class criteria, temporal ordering and every prior mapping.
2. Handle **INC-073 plus genuinely disputed, unclassified and other provisional outcomes** carefully. A defensible hold can be reviewed against 0.8.0 without changing its historical stamp or forcing success/failure.
3. For each truly re-adjudicated case: add a dated per-Incident decision packet; update canonical version and current taxonomy edition *only when criteria were actually reviewed*; append new AI authorship/interpretive provenance, rebuild the public and geographic projections and rerun validation. Do not represent changed version strings as verification.
4. Complete remaining 191 screens and evidence-limited dispositions. Reconciliation is not finished simply because the number of records stamped 0.8.0 rises.
5. Keep this PR draft until maintainer-approved final readiness, then merge to main and build the SIAI dataset v1.0.0 release checksum **from that final main commit**.

## Verified build status

On the last fully validated substantive checkpoint `738506715544dfd7c1cc9e683928d42ccc8fa780`, four workflows passed. For this current candidate `ef2140edcc9d481e671e175cb8fc9cc68fe4dfaf`, VIGIL records, External governance and taxonomy publication workflows passed; the final SIAI preflight should be checked independently before declaring the entire current change fully green. The preflight inventory from a working branch remains a preflight only, not an immutable main-based final release.
