# EU AI Act Article 12 Reconciliation and Full-Corpus Adjudication

Review date: 2026-09-29

Status: completed for the current EU AI Act candidate tranche

## Reconciliation qualification — 30 September 2026

After consolidating the later source-clause corpus, the candidate matrix was regenerated: it now contains 479 Incident–requirement pairs across 53 canonical requirement IDs and 149 taxonomy-mapped Incidents. The EU AI Act subset remains 94 pairs across six requirements. The matrix and assessments below are preserved branch work, but are not a final post-taxonomy snapshot: complete the two P1A full-corpus Fidelity Class reviews and P1B review of the 23 partial Incidents first, then regenerate the matrix and revisit any assessments whose candidate or finding could be affected.

Scope: reconciliation of the retired Article 12 taxonomy citation, regeneration of the taxonomy-derived candidate matrix, and independent occurrence-level adjudication of every EU AI Act candidate pair in the current Incident corpus. These are occurrence-level research assessments, not determinations of any organisation's general compliance or an actor's legal liability.

## Article 12 taxonomy reconciliation

The former aggregate Article 12 reference `EXTREQ-33898CCD26FBF5D5` did not resolve in the canonical 978-requirement corpus. The taxonomy's two distinct Article 12 duties now point to their atomic successor records:

| Fidelity Class | Atomic provision | Canonical requirement ID | Requirement scope |
|---|---|---|---|
| FC-000022 | Article 12(1) | `EXTREQ-42D3F017A9786AE8` | Provider design duty: a high-risk AI system must technically allow automatic recording of events over its lifetime. |
| FC-000024 | Article 12(2) | `EXTREQ-90A317D512B165D5` | Logging must provide traceability appropriate to the high-risk system's intended purpose. |

The Article 12 taxonomy notes and governance placements now identify the relevant paragraph and the proper provider/high-risk-system scope. Existing non-Article 12 citations were retained. The retired identifier no longer appears in the active taxonomy.

## Regenerated candidate matrix

The deterministic matrix now covers 170 Incident records (169 active, one monitoring), including 149 taxonomy-mapped Incidents. It contains 479 unique Incident–requirement pairs across 53 canonical requirement IDs; 27 pairs are reached through more than one Fidelity Class. Taxonomy reference reconciliation found 139 external-reference rows: 77 with structured IDs and 62 without one. All structured IDs resolve; none are malformed. The 62 unstructured rows remain outside candidate generation.

The EU AI Act tranche contains 94 pairs across six atomic requirements. The Article 12 repair adds 30 pairs that the earlier pilot excluded with the unresolved aggregate reference; the EU tranche therefore moves from 64 pairs/four IDs to 94 pairs/six IDs. The matrix remains a candidate list and carries no applicability or finding decision.

## Independent adjudication results

Every candidate pair was reviewed against the occurrence record, the atomic requirement, and the applicable scope and timing rules. The taxonomy class IDs remain in `derived_from_class_ids` as candidate provenance only; taxonomy roles and findings were not copied into the external requirement assessment. Each of the 94 pairs has an assessment on its Incident record. The 59 Incidents with one or more EU AI Act candidates now carry those assessments.

| Requirement | Candidate pairs | Not applicable | Insufficient evidence | Applicable | Occurrence-level finding |
|---|---:|---:|---:|---:|---|
| Article 5(1)(a) — prohibited manipulative/deceptive practices | 33 | 16 | 16 | 1 | `INC-000151`: `failure-occurrence` |
| Article 5(1)(b) — exploitation of vulnerability | 11 | 8 | 2 | 1 | `INC-000151`: `ambiguous-boundary` |
| Article 12(1) — automatic event recording | 15 | 15 | 0 | 0 | None |
| Article 12(2) — traceability from logs | 15 | 15 | 0 | 0 | None |
| Article 14(4)(e) — human oversight capability | 12 | 12 | 0 | 0 | None |
| Article 73 — serious-incident reporting | 8 | 8 | 0 | 0 | None |
| **Total** | **94** | **74** | **18** | **2** | **One failure-occurrence; one ambiguous-boundary** |

Only the two applicable Article 5 assessments carry findings. The Swedish synthetic investment-advertisement occurrence (`INC-000151`) is applicable to Article 5(1)(a): evidence reports AI-generated false endorsements directed at Swedish investors after that prohibition began applying, and attributed estimates of thousands of victims and approximately SEK 500 million in losses. The provider/deployer is not identified; this is not an actor-liability finding. The Article 5(1)(b) assessment for the same occurrence is `ambiguous-boundary`: the record does not establish that a person was selected or exploited because of age, disability, or a specific social or economic situation. Financial loss alone does not establish that statutory vulnerability element.

The `insufficient-evidence` assessments preserve unresolved scope or material facts, especially where reporting identifies potentially relevant conduct outside the Union but does not establish the Article 2 Union-market, Union-established-deployer, or Union-use connection. They are not treated as negative findings. The other Article 5 `not-applicable` assessments turn on timing or on the absence of a required practice, material distortion, significant harm, or protected-vulnerability element on the bounded occurrence evidence.

## Application-date treatment for Articles 12, 14, and 73

Regulation (EU) 2026/1744 entered into force on 27 July 2026 and amended Article 113. Chapter III, Sections 1–3 now apply from 2 December 2027 for systems classified as high-risk under Article 6(2)/Annex III, and from 2 August 2028 for systems classified under Article 6(1)/Annex I. Articles 12 and 14 are in Chapter III, Section 2. Every preserved occurrence window in these two candidate sets is before the earliest of those application dates, including the August 2026 reports and the May–August 2026 activity window. Each is therefore not applicable to that historical occurrence; no logging or oversight finding is inferred from the taxonomy mapping.

Article 73 remains under the Regulation's general 2 August 2026 application date; the 2026 amendment's delay is specific to Chapter III, Sections 1–3. Six Article 73 candidate records are dated before 2 August 2026. The undated health-search record documents potentially harmful guidance but no identified serious incident within Article 73's reporting categories. The 20 September 2026 internal-training occurrence postdates the general application date, but the preserved record establishes neither a high-risk AI system/provider nor a serious incident triggering Article 73. All eight Article 73 candidates are not applicable on their occurrence evidence and timing; none receives an occurrence finding.

## Validation

- Candidate matrix regenerated after branch reconciliation: 479 unique Incident–requirement pairs, 53 requirement IDs, zero unresolved structured taxonomy references. These are provisional pending the P1A/P1B taxonomy sequence above.
- External-requirement assessment, candidate-matrix, and public-projection unit tests passed.
- Canonical Incident record validation passed for all 170 records.
- Taxonomy validation passed for 15 family files and 76 classes.
- Public Incident index and registry-manifest validation passed after adding `external_requirement_assessments` to the validator's permitted, source-matched projection.

## Authoritative law

- [Regulation (EU) 2026/1744, Digital Omnibus on AI, Official Journal text](https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng), including the amended Article 113 application dates.
- [Regulation (EU) 2024/1689, consolidated text as of 27 July 2026](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02024R1689-20260727), including Articles 2, 5, 12, 14, and 73.
