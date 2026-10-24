# SIAI corpus facts — 18 October 2026

**Archive note (24 October 2026):** The dated reproduction script and historical metric JSON outputs were retired from the active notice board after this source-specific result was recorded. For exact original reproduction, retrieve [count-corpus.py](https://github.com/CAM-Initiative/Vigil/blob/82ee10e0be062a059fd893c5cff77f1f4ec0ebe5/vigil/docs/reviews/2026-10-18-issue-126-him-reassessments/count-corpus.py), [corpus-counts.json](https://github.com/CAM-Initiative/Vigil/blob/82ee10e0be062a059fd893c5cff77f1f4ec0ebe5/vigil/docs/reviews/2026-10-18-issue-126-him-reassessments/corpus-counts.json) and [baseline-counts.json](https://github.com/CAM-Initiative/Vigil/blob/82ee10e0be062a059fd893c5cff77f1f4ec0ebe5/vigil/docs/reviews/2026-10-18-issue-126-him-reassessments/baseline-counts.json) from the pinned pre-cull Git commit. The commands below reproduce the historical workflow when run from that commit; they are not current-branch commands.


Artefact class: AUDIT. This report describes a reproducible repository snapshot; it is not a manuscript edit or a claim of empirical methodology validation.

**Data commit: `cfeb57a996e29eb08a3d2a928a090ac5e0646fc1`.** Original handoff baseline: `adac7b35b5f8edd3a0f9d666666ff3b6a40dd123`. Publication parent: `cee60da57816ec40345135f1ac5193776b9234ab`, whose concurrent INC-003 change is preserved. The later report-only commit does not change the canonical counting inputs.

## Counting method

Read every Incident JSON in `vigil/records/incidents/` from the explicit Git commit. Count canonical `record_type = incident` objects; separately filter `record_state = active` for the strict active-only subset. Do not count generated navigation entries, historical ledgers or draft candidates. Workflow state is independent of HIM severity.

```bash
python vigil/docs/reviews/2026-10-18-issue-126-him-reassessments/count-corpus.py cfeb57a996e29eb08a3d2a928a090ac5e0646fc1
python vigil/docs/reviews/2026-10-18-issue-126-him-reassessments/count-corpus.py adac7b35b5f8edd3a0f9d666666ff3b6a40dd123
```

Exact JSON outputs are `corpus-counts.json` and `baseline-counts.json`. Every corpus distribution below comes from these outputs and therefore the two exact commits above. Review-work counts come from the 24 before/after audit files and successor hold register in the data commit.

## Corpus and methodology

| Measure | Baseline | Result |
| --- | ---: | ---: |
| Current canonical Incidents | 194 | 194 |
| Workflow state active | 193 | 193 |
| Workflow state monitoring | 1 | 1 |
| HIM 1.1.0, all current canonical records | 170 | 194 |
| HIM 1.0.1, all current canonical records | 24 | 0 |
| HIM 1.1.0, strict active-only records | 169 | 193 |

The full canonical corpus is now uniformly declared HIM 1.1.0. This working methodology includes dated 11 October minimum-harm and 18 October animal-welfare amendments. The 170 earlier 1.1.0 records were not silently reassessed against the new animal criteria; none has a scored environmental row, and all remain byte-identical to the publication parent. Reporting the version distribution does not establish uniform evidence depth, human verification or calibrated measurement.

## Overall severity

| Band | Baseline: all 194 | Result: all 194 | Result: active-only 193 |
| --- | ---: | ---: | ---: |
| S1 | 24 | 23 | 23 |
| S2 | 40 | 38 | 38 |
| S3 | 70 | 67 | 67 |
| S4 | 21 | 20 | 19 |
| S5 | 4 | 4 | 4 |
| SU | 35 | 42 | 42 |

SU is reported explicitly. The 42 current SU records include previously accepted evidence-limited findings; this review does not assert that all 42 received new source research in this tranche.

## Reassessment completion

- 24 completed legacy reassessments: 16 banded, eight completed evidence-limited SU.
- Zero unperformed reviews and zero continuing HIM migration holds in this work package.
- Thirteen overall bands changed; eleven retained their overall band while receiving substantive current-method dimension/pathway decisions.
- The eight completed SU reviews are INC-060, 092, 099, 106, 121, 167, 169 and 170. They name specific missing consequence, authority, clinical or attribution facts. SU is not no harm.
- No release exception or hold disposition is used to manufacture completion.

## Material band changes

| Incident | Baseline → result | Reason |
| --- | --- | --- |
| VIGIL-INC-000051 | S2 → S3 | Police-sourced reporting describes misuse of lost identity-card information and AI-altered portraits in fifteen successful account openings. The sensitivity and actual identity misuse support meaningful bounded confidentiality harm. Final containment and subsequent cardholder consequences remain unknown. |
| VIGIL-INC-000060 | S2 → SU | Actual interrupted evaluation function, material impairment and recovery; resulting protected-information, victim-asset or recipient harm remain unsubstantiated. |
| VIGIL-INC-000083 | S3 → S2 | The reproduced false endorsement and Kohler’s attributable public correction establish a bounded dignitary/attribution consequence. Product reach, recurring removals and annual scam losses do not establish a material lost opportunity or standing consequence for this portrayal. |
| VIGIL-INC-000092 | S2 → SU | Historical permission to process retained copies and the control/notice in force when the user disconnected. |
| VIGIL-INC-000099 | S3 → SU | Feature-specific eligible cohort, representative deployed encounters and credible consequential collective impact; no specific injury is established. |
| VIGIL-INC-000106 | S3 → SU | Actual lost credit/standing or institutional consequence, and occurrence-specific private-data access lineage. |
| VIGIL-INC-000109 | S2 → S3 | The reported withholding removed the entire pre-release evaluation opportunity for Mythos 5.1, materially impairing an important institutional assurance workflow. Later access arrangements do not restore the missed pre-release opportunity. The October parliamentary answer does not confirm a completed Mythos 5.1 evaluation. |
| VIGIL-INC-000116 | S4 → S3 | RubyGems paused new registrations for approximately four days during the campaign. Its operator clarifies that existing users could still install and publish. Material onboarding impairment supports S3; essential package delivery collapse is not established. Researchers attribute the campaign to AI agents, while the operator cannot independently determine AI authorship. |
| VIGIL-INC-000121 | S2 → SU | Actual recipient injury or impaired relational agency, payment, feature-specific eligible cohort and credible collective consequence. |
| VIGIL-INC-000144 | S1 → S2 | Police contacted the remote operator and a maintenance team took control after the lighting fault. The reported correction and local operational intervention support routine local workflow impairment. No ticket or reported injury is not affirmative evidence of no operational harm. |
| VIGIL-INC-000148 | S3 → S2 | Actual unwanted order-state changes and unsuccessful correction attempts occurred during live ordering. They support the S2 transaction-state minimum. More than 100 pilot sites is deployment scale, not a count of impaired sites. Pilot termination and undisclosed success criteria do not establish material S3 impairment across the pilot. Final charges, correction time and affected-order counts remain unknown. |
| VIGIL-INC-000169 | S3 → SU | Executed AI biometric identification and the decision chain materially connecting it to revocation or other reported consequences. |
| VIGIL-INC-000170 | S3 → SU | What non-public target information was actually read, persisted changes, actual impairment and the target-specific basis of Google’s no-harm assessment. |

The complete 24-record table, source links, dimension-specific reasoning, gaps and dispositions are in [README.md](README.md) and each linked before/after JSON audit. INC-082 remains overall S3, controlled by privacy/impersonation; financial harm remains S1 from US$4,820. INC-148 is S2, and the one approved frozen adjudication test was removed. INC-167 remains SU under the now-explicit animal-welfare scope because its clinical outcome and material AI contribution are insufficiently substantiated.

## Remaining limitations and paper dependencies

Evidence includes first-party reconstructions, named testimony and attributed reporting. Private clinical records, operational recovery records, historical processing permissions and some full original articles remain unavailable. Claim-relative source limits, contested causation and independent no-harm claims are preserved; access failure is not disproof. Wider campaign totals, attempted payments, demanded damages, product reach and research experiments are not converted into AI-attributable realised loss.

The animal-welfare bands are an expressly agreed VIGIL policy distinction, not an externally validated clinical scale. No animal S-band was assigned in this tranche. The monetary-threshold interpretation for INC-082 is explicitly recorded rather than erasing arrears. Other taxonomy gaps and external-requirement work are unchanged.

**Issue #130 remains separate and open.** INC-099 and INC-121 use the required generic-deployed Aggregate Harm route but remain SU because scoring evidence is inadequate. This reassessment neither completes calibration nor establishes empirically valid eligible-population thresholds. The paper must not describe Aggregate Harm calibration or methodology validation as completed by this exercise.

## Validation

Independent untouched baseline a94ea8e: 281/281 tests pass after installing the existing pinned jsonschema 4.26.0 dependency. Candidate and the combined state including cee60da: 280/280 tests pass. The one-method decrease is the specifically approved test removal, not skipped or rewritten outcomes. All 24 rebuild guards and required canonical/public/source/interpretive/authorship/component/occurrence-requirement/taxonomy validators pass. Builder and publication eligibility outputs were regenerated and committed. `git diff --check` passes. See validation.json, preservation-and-impact.json and rebuild-guards.json in the data commit.

Hosted CI and PR readiness are reported on PR #137 for its exact final head. Local checks do not substitute for that hosted result. No merge, deployment, email or SIAI manuscript submission is performed.
