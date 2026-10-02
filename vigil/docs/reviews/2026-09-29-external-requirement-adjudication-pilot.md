# External Requirement Adjudication Pilot Review

Review date: 2026-09-29

Status: bounded contract and pilot review

Scope: candidate audit of the current Incident corpus, the optional assessment field, validator rules, and a small evidence-bounded pilot. This review does not migrate the full corpus or make organisation-wide compliance determinations.

## Supersession note — 2026-09-29

The candidate snapshot and unresolved Article 12 reference described below are historical pilot findings. The retired aggregate reference was reconciled to Article 12(1) and Article 12(2), the candidate matrix was regenerated, and all 94 EU AI Act candidate pairs were independently adjudicated. The full-tranche results are in [the EU AI Act adjudication review](2026-09-29-eu-ai-act-full-corpus-adjudication.md); use that review and the current Incident assessment fields for the current state.

## Candidate audit snapshot

The audit covered 170 current Incident records: 169 `active` and one `monitoring`. Of these, 148 have a primary or secondary taxonomy mapping. The deterministic matrix contains 447 unique Incident-to-requirement candidates across 51 distinct canonical EXTREQ IDs. Twenty-seven candidate relationships are reached through more than one mapped Fidelity Class.

| External source | Incident–requirement candidates | Unique requirement IDs |
|---|---:|---:|
| NIST-AI-100-1 | 58 | 4 |
| IEEE-7014 | 28 | 5 |
| IEEE-7009 | 85 | 5 |
| IMDA-AGENTIC-AI-MGF | 30 | 6 |
| IEEE-7001 | 28 | 4 |
| AAM-SDOS-RUNTIME-GOVERNANCE | 14 | 2 |
| EU-AI-ACT-2024-1689 | 64 | 4 |
| IEEE-7014.1 | 122 | 12 |
| IEEE-7000 | 10 | 6 |
| NIST-AI-600-1 | 8 | 3 |
| **Total** | **447** | **51** |

The taxonomy contains 139 external-reference rows: 77 with structured IDs and 62 without one (44 distinct unstructured citation tuples by title, publisher, date, URL and reference role). The unstructured references appear in 395 Incident-to-class exposures. They remain contextual or evidentiary taxonomy references and are excluded from candidate generation unless a structured canonical requirement ID is present.

One structured taxonomy citation, `EXTREQ-33898CCD26FBF5D5` (EU AI Act Article 12), does not resolve in the 978-record canonical requirement corpus. It is referenced by FC-000022 and FC-000024 across 15 Incidents, producing 30 mapped-class exposures. It is excluded from the matrix and left unresolved for separate taxonomy/reference maintenance; this pilot does not repair or reinterpret it.

`standards_and_regulatory_references` is populated in five Incidents with 13 entries. Four of those Incidents also have taxonomy-derived candidates. One contextual field (INC-121) contains three textual EXTREQ identifiers, but those strings do not drive candidate generation. The field remains unchanged and continues to carry non-evidentiary context.

## Pilot assessments

### INC-000151 — Swedish synthetic investment advertisements

`EXTREQ-9A63E34FA83EAFA2`, EU AI Act Article 5(1)(a), is derived through FC-000052 and FC-000082. The Incident records AI-generated impersonations and fabricated investment endorsements distributed in Sweden, with TV4 attributing reported estimates of thousands of victims and substantial aggregate losses. The event was reported after the Article 5 prohibitions began applying on 2 February 2025. Article 2(1)(c) also addresses providers or deployers established outside the Union where the system's output is used in the Union. On those bounded facts, the pilot assesses the legal/time/system scope as applicable and records an occurrence-level `failure-occurrence` finding against Article 5(1)(a). It identifies no provider or deployer and makes no actor-level liability or organisation-wide compliance determination.

`EXTREQ-DC7C4F064C590E5A`, Article 5(1)(b), is derived through FC-000052. The same territorial and temporal scope supports assessing the requirement as applicable, but the preserved reporting does not establish whether the practice exploited a person's age, disability, or social or economic vulnerability in the specific manner required by Article 5(1)(b). The pilot therefore records `ambiguous-boundary`, not a copied taxonomy outcome or a presumption from financial loss alone.

The two assessments show why source class roles and external requirement findings must remain independent: the Article 5(1)(a) ID is reached through both an ambiguous taxonomy mapping and a failure mapping, while the separate requirement's occurrence finding is grounded in its own statutory test.

### INC-000145 — DNB executive impersonation attempt

`EXTREQ-233EE01AB85DB0F0` (NIST AI RMF MEASURE 1.2), reached through FC-000083, is a voluntary framework candidate. Although the Incident records successful security reporting and intervention, its sources do not establish that DNB had adopted or was using the NIST AI RMF. The pilot records `insufficient-evidence` for applicability and includes no finding.

`EXTREQ-9A63E34FA83EAFA2` (EU AI Act Article 5(1)(a)), reached through FC-000082, is `not-applicable` to this occurrence because the reported event occurred 21–23 January 2025, before Article 5's prohibitions began applying on 2 February 2025. This is a temporal scope disposition, not an assessment of the conduct under other law.

### INC-000136 — controlled compaction-training occurrence

`EXTREQ-4C18B5A910ECD719` (IEEE 7014.1-2026 clause 6.25.3(a–c)), reached through FC-000001, is `not-applicable`. The Incident describes a controlled reinforcement-learning training task about local library holdings, not a partner-based general-purpose AI system using emulated empathy as specified in the canonical requirement's applicability conditions. The cited 2026 source version is also later than the 18 July 2026 occurrence. The successful downstream taxonomy mappings are not converted into an external-requirement pass.

The FC-000001 citation to OWASP LLM01:2025 has no structured `requirement_id`; it remains an authoritative contextual reference and does not create an EXTREQ candidate. The separate IEEE requirement above is included because its taxonomy reference has a resolvable structured ID.

## Pilot coverage limit

The current evidence review did not identify a real corpus occurrence where an external requirement's scope and adoption are established and the evidence affirmatively demonstrates the requirement holding under relevant pressure. DNB is not a valid substitute because NIST adoption is not evidenced, and the other reviewed successful-invariant candidates concern voluntary standards/frameworks or do not establish the legal system, actor, jurisdiction, or effective-date scope. No applicable-success assessment has been fabricated. The validator and tests include a synthetic applicable-success case solely to verify the schema contract.

## Maintainer decision

The optional Incident contract, deterministic candidate generator, and bounded pilot are ready for review. Existing records are not mechanically backfilled. The candidate matrix is generated from current taxonomy and EXTREQ data and contains no applicability or finding decisions.

Official legal references used for the EU scope examples:

- European Commission, *AI Act: first rules on prohibited AI practices and AI literacy enter into application on 2 February 2025*: <https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai>
- Regulation (EU) 2024/1689, Article 2 (territorial scope): <https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng#art_2>
- Regulation (EU) 2024/1689, Article 5 (prohibited practices): <https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng#art_5>
