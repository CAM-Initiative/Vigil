# External requirement occurrence review — INC-000001 through INC-000120

**Review date:** 2026-10-01  
**Branch:** `work/reconcile-taxonomy-external-requirements`  
**Starting commit:** `6d31968` — Normalize taxonomy roles for Incident 002

## Scope and analytical basis

The range contains 113 current Incident records (112 active, one monitoring). Absent/retired allocations were skipped. INC-000121+ records and website source were excluded. Review follows source_records → material source clauses → canonical mapped Fidelity Classes → structured resolvable EXTREQ references → independent applicability → independently supported occurrence finding. Contextual history and source evidence were preserved.

The initial deterministic candidate rebuild was performed before the maintainer instructed this thread to continue without using or updating the matrices. Its two generated snapshots were restored to the starting commit. Subsequent review and coverage checks derive candidates directly from each canonical Incident’s primary/secondary class references and canonical EXTREQ records. Neither matrix is a deliverable or an authoritative count for this review. The large taxonomy adjudication matrix was not used or edited. Candidate-builder regression tests operate on isolated fixtures.

The direct per-Incident derivation identifies **279 unique Incident–requirement pairs**, **43 distinct canonical requirements**, **75 candidate-bearing Incidents**, and **15 pairs with multiple contributing mapped classes**. There are 91 Incidents with canonical class mappings; mapped classes with contextual-only citations legitimately produce no candidate. All contributors are retained in `derived_from_class_ids`.

## Clause/class reconciliation

Every material clause was checked for an explicitly canonical relationship absent from its Incident’s mapped class set. **Zero canonical clause-class omissions** were found. Candidate, adjacent and rejected relationships marked `canonical_taxonomy_mapping: false` were excluded. No shared builder-contract defect was found; builder, methodology, schema, validator and permanent tests remain unchanged. The INC-121+ thread has no shared implementation change to incorporate.

Baseline validation exposed five missing reciprocal admitted ambiguous-boundary exemplars: INC-000006/FC-000046, INC-000007/FC-000046, INC-000012/FC-000049, INC-000062/FC-000052 and INC-000113/FC-000003. These relationships were already independently adjudicated in the September 30 clauses and Incident mappings. Reciprocal taxonomy rows were completed without changing those findings, definitions, reference IDs or candidate provenance.

INC-000099 clause 2 had status `mapped` despite its only relationship explicitly rejecting FC-000063 and being non-canonical. Its status was corrected to `resolved-no-mapping`; no class was promoted. The final material-clause statuses are 228 mapped, 84 resolved-no-mapping, 37 unresolved and one taxonomy-gap (350 total). Existing source interpretations and uncertainties remain.

Four incomplete historical provenance entries (INC-000094, 000095, 000117 and 000119) lacked `review_outcome`. Only that missing key was completed, explicitly dated as an October 1 metadata completion based on the immediately following preserved clause-level review. Historical entries were not removed or replaced; the new external review is appended.

## Requirement sources and limits

All 43 candidate requirements were reviewed for source/version, actor, governed object, lifecycle, jurisdiction, timing, normative force, conditions and exceptions from their canonical records. The source checks included the following primary locations:

- [NIST AI RMF 1.0 primary PDF](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf): GOVERN 1.7, MANAGE 4.1, MEASURE 1.2 and MEASURE 2.5.
- [NIST Generative AI Profile primary PDF](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf): MP-2.1-002 and MS-2.10-001.
- [AAM SDOS public v1 reference](https://aamcyber.com/sdos/reference/v1): agentic/tool-invocation scope, static-chat exclusion and SDOS-EN-01 pre-egress policy enforcement.
- [IMDA primary framework PDF](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf): blocked by anti-bot verification on this session’s re-access. Canonical records document the earlier complete primary-text v1.5 review and digest.
- IEEE publisher catalogue scope/version information and the documented licensed primary-text reviews `EXTREQ-05`, `EXTREQ-06`, `EXTREQ-07`, `EXTREQ-08` and `EXTREQ-09` in this directory. Fresh licensed IEEE full text was unavailable in this session. This review relies on those documented reviews and canonical clause conditions; it does not claim fresh full-text access or human assurance.

Publisher dates used for historical scope exclusions were IEEE 7014.1-2026 (12 June 2026), IEEE 7009-2024 (5 July 2024), NIST AI RMF 1.0 (January 2023), and the cited IMDA 2026-05 revision (20 May 2026). The historical publication exclusion concerns the cited published version, not a declaration that earlier conduct was acceptable.

For the EU AI Act, current primary-source checks used [the consolidated Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02024R1689-20260727), [Regulation (EU) 2026/1744](https://eur-lex.europa.eu/eli/reg/2026/1744/oj), [the Commission’s current application timeline](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai), and [the Commission AI Act Explorer](https://ai-act-service-desk.ec.europa.eu/en/ai-act). EUR-Lex full-document opening was blocked in this session; official indexed text and the Commission timeline corroborated the July amendment. The Explorer warns that some displayed provisions remain based on the earlier text, so it was not used as the sole source for amended application dates.

Articles 12 and 14 are Chapter III Section 2 duties: the amended earliest high-risk application date is 2 December 2027 (Annex III), with Annex I application on 2 August 2028. Article 73 is a separate Chapter IX duty with 2 August 2026 application. Article 5 applies from 2 February 2025. Chapter V applies from 2 August 2025, with Article 111(3)’s pre-existing GPAI-model transition to 2 August 2027. The two new INC-000073 Article 53(c)/(d) assessments preserve unresolved model placement/transition facts; the open-source exception for 53(a)/(b) is not extended to (c)/(d).

Underlying occurrence review used the preserved source_records, factual basis and material clauses, with attempted public-source re-access across the candidate-bearing Incidents. Some URLs were unavailable, some exposed only limited text, and complete internal logs, medical records, interaction histories and framework undertakings were not available. These access limits are disclosed in appended review provenance. No new source evidence, hidden control state, adoption fact, territorial nexus or successful invariant was invented.

## Reviewable tranches

| Incident range | Candidate assessments | Insufficient evidence | Not applicable | Existing retained | Existing revised | Existing withdrawn | New entries |
|---|---:|---:|---:|---:|---:|---:|---:|
| 001–030 | 65 | 43 | 22 | 8 | 1 | 3 | 56 |
| 031–060 | 60 | 43 | 17 | 9 | 4 | 1 | 47 |
| 061–090 | 75 | 59 | 16 | 14 | 6 | 1 | 55 |

Completed tranches currently contain **200 assessments**: **145 insufficient-evidence**, **55 not-applicable**, **zero applicable**. Consequently there are zero external failure-occurrence, successful-invariant or ambiguous-boundary findings. Applicability is assessed; the missing evidence remains a substantive blocker.

## Earlier assessment audit

Each previously present assessment is accounted for below. Retained entries preserve their original assessment date and independently supported basis. Revised entries carry the current date; withdrawals preserve the earlier value through Git history and give an explicit provenance explanation.

- `VIGIL-INC-000001` / `EXTREQ-DEA2B22466A64818` — **retained**. Independent applicability reasoning retained; exact contributing class set remains valid.
- `VIGIL-INC-000002` / `EXTREQ-9A63E34FA83EAFA2` — **revised**. Replaced unsupported affirmative exclusion with the identified missing scope facts.
- `VIGIL-INC-000003` / `EXTREQ-42D3F017A9786AE8` — **retained**. Independent applicability reasoning retained; exact contributing class set remains valid.
- `VIGIL-INC-000003` / `EXTREQ-90A317D512B165D5` — **retained**. Independent applicability reasoning retained; exact contributing class set remains valid.
- `VIGIL-INC-000003` / `EXTREQ-C0D92D72BD0672E1` — **retained**. Independent applicability reasoning retained; exact contributing class set remains valid.
- `VIGIL-INC-000003` / `EXTREQ-DEA2B22466A64818` — **retained**. Independent applicability reasoning retained; exact contributing class set remains valid.
- `VIGIL-INC-000004` / `EXTREQ-DEA2B22466A64818` — **retained**. Independent applicability reasoning retained; exact contributing class set remains valid.
- `VIGIL-INC-000012` / `EXTREQ-9A63E34FA83EAFA2` — **retained**. Independent applicability reasoning retained; exact contributing class set remains valid.
- `VIGIL-INC-000014` / `EXTREQ-C0D92D72BD0672E1` — **retained**. Independent applicability reasoning retained; exact contributing class set remains valid.
- `VIGIL-INC-000023` / `EXTREQ-9A63E34FA83EAFA2` — **withdrawn**. The final clause/class state no longer canonically maps the formerly contributing VIGIL-FC-000082. No remaining mapped class has a structured reference to this requirement; the prior assessment is withdrawn for loss of candidate provenance, not a new factual or legal determination. Prior value remains in Git history.
- `VIGIL-INC-000024` / `EXTREQ-9A63E34FA83EAFA2` — **withdrawn**. The final clause/class state no longer canonically maps the formerly contributing VIGIL-FC-000082. No remaining mapped class has a structured reference to this requirement; the prior assessment is withdrawn for loss of candidate provenance, not a new factual or legal determination. Prior value remains in Git history.
- `VIGIL-INC-000029` / `EXTREQ-9A63E34FA83EAFA2` — **withdrawn**. The final clause/class state no longer canonically maps the formerly contributing VIGIL-FC-000082. No remaining mapped class has a structured reference to this requirement; the prior assessment is withdrawn for loss of candidate provenance, not a new factual or legal determination. Prior value remains in Git history.
- `VIGIL-INC-000034` / `EXTREQ-9A63E34FA83EAFA2` — **retained**. Independent applicability reasoning retained; exact contributing class set remains valid.
- `VIGIL-INC-000034` / `EXTREQ-DC7C4F064C590E5A` — **retained**. Independent applicability reasoning retained; exact contributing class set remains valid.
- `VIGIL-INC-000047` / `EXTREQ-DEA2B22466A64818` — **retained**. Independent applicability reasoning retained; exact contributing class set remains valid.
- `VIGIL-INC-000049` / `EXTREQ-9A63E34FA83EAFA2` — **retained**. Independent applicability reasoning retained; exact contributing class set remains valid.
- `VIGIL-INC-000050` / `EXTREQ-9A63E34FA83EAFA2` — **revised**. Replaced unsupported affirmative exclusion with the identified missing scope facts.
- `VIGIL-INC-000051` / `EXTREQ-9A63E34FA83EAFA2` — **withdrawn**. The final clause/class state no longer canonically maps the formerly contributing VIGIL-FC-000082. No remaining mapped class has a structured reference to this requirement; the prior assessment is withdrawn for loss of candidate provenance, not a new factual or legal determination. Prior value remains in Git history.
- `VIGIL-INC-000052` / `EXTREQ-9A63E34FA83EAFA2` — **retained**. Independent applicability reasoning retained; exact contributing class set remains valid.
- `VIGIL-INC-000052` / `EXTREQ-DC7C4F064C590E5A` — **revised**. Replaced unsupported affirmative exclusion with the identified missing scope facts.
- `VIGIL-INC-000053` / `EXTREQ-9A63E34FA83EAFA2` — **retained**. Independent applicability reasoning retained; exact contributing class set remains valid.
- `VIGIL-INC-000054` / `EXTREQ-9A63E34FA83EAFA2` — **retained**. Independent applicability reasoning retained; exact contributing class set remains valid.
- `VIGIL-INC-000056` / `EXTREQ-DEA2B22466A64818` — **retained**. Independent applicability reasoning retained; exact contributing class set remains valid.
- `VIGIL-INC-000058` / `EXTREQ-9A63E34FA83EAFA2` — **revised**. Replaced unsupported affirmative exclusion with the identified missing scope facts.
- `VIGIL-INC-000060` / `EXTREQ-9A63E34FA83EAFA2` — **retained**. Independent applicability reasoning retained; exact contributing class set remains valid.
- `VIGIL-INC-000060` / `EXTREQ-DC7C4F064C590E5A` — **revised**. Replaced unsupported affirmative exclusion with the identified missing scope facts.
- `VIGIL-INC-000062` / `EXTREQ-9A63E34FA83EAFA2` — **retained**. Independent applicability reasoning retained; exact contributing class set remains valid.
- `VIGIL-INC-000062` / `EXTREQ-DC7C4F064C590E5A` — **revised**. Replaced unsupported affirmative exclusion with the identified missing scope facts.
- `VIGIL-INC-000063` / `EXTREQ-C0D92D72BD0672E1` — **revised**. Replaced missing-trigger exclusion with positive January–February 2026 temporal exclusion.
- `VIGIL-INC-000066` / `EXTREQ-9A63E34FA83EAFA2` — **revised**. Replaced unsupported affirmative exclusion with the identified missing scope facts.
- `VIGIL-INC-000073` / `EXTREQ-DEA2B22466A64818` — **retained**. Independent applicability reasoning retained; exact contributing class set remains valid.
- `VIGIL-INC-000075` / `EXTREQ-DEA2B22466A64818` — **retained**. Independent applicability reasoning retained; exact contributing class set remains valid.
- `VIGIL-INC-000080` / `EXTREQ-9A63E34FA83EAFA2` — **withdrawn**. The final clause/class state no longer canonically maps the formerly contributing VIGIL-FC-000082. No remaining mapped class has a structured reference to this requirement; the prior assessment is withdrawn for loss of candidate provenance, not a new factual or legal determination. Prior value remains in Git history.
- `VIGIL-INC-000081` / `EXTREQ-9A63E34FA83EAFA2` — **revised**. Replaced unsupported affirmative exclusion with the identified missing scope facts.
- `VIGIL-INC-000081` / `EXTREQ-DC7C4F064C590E5A` — **revised**. Replaced unsupported affirmative exclusion with the identified missing scope facts.
- `VIGIL-INC-000082` / `EXTREQ-9A63E34FA83EAFA2` — **retained**. Independent applicability reasoning retained; exact contributing class set remains valid.
- `VIGIL-INC-000082` / `EXTREQ-DC7C4F064C590E5A` — **retained**. Independent applicability reasoning retained; exact contributing class set remains valid.
- `VIGIL-INC-000083` / `EXTREQ-9A63E34FA83EAFA2` — **retained**. Independent applicability reasoning retained; exact contributing class set remains valid.
- `VIGIL-INC-000083` / `EXTREQ-DC7C4F064C590E5A` — **revised**. Replaced unsupported affirmative exclusion with the identified missing scope facts.
- `VIGIL-INC-000084` / `EXTREQ-42D3F017A9786AE8` — **retained**. Independent applicability reasoning retained; exact contributing class set remains valid.
- `VIGIL-INC-000084` / `EXTREQ-90A317D512B165D5` — **retained**. Independent applicability reasoning retained; exact contributing class set remains valid.
- `VIGIL-INC-000085` / `EXTREQ-42D3F017A9786AE8` — **retained**. Independent applicability reasoning retained; exact contributing class set remains valid.
- `VIGIL-INC-000085` / `EXTREQ-90A317D512B165D5` — **retained**. Independent applicability reasoning retained; exact contributing class set remains valid.
- `VIGIL-INC-000086` / `EXTREQ-42D3F017A9786AE8` — **retained**. Independent applicability reasoning retained; exact contributing class set remains valid.
- `VIGIL-INC-000086` / `EXTREQ-90A317D512B165D5` — **retained**. Independent applicability reasoning retained; exact contributing class set remains valid.
- `VIGIL-INC-000088` / `EXTREQ-42D3F017A9786AE8` — **retained**. Independent applicability reasoning retained; exact contributing class set remains valid.
- `VIGIL-INC-000088` / `EXTREQ-90A317D512B165D5` — **retained**. Independent applicability reasoning retained; exact contributing class set remains valid.

## Remaining evidence blockers and taxonomy signal

The principal blockers are evidence of voluntary adoption/conformance undertaking; selected stakeholder transparency levels; specified fail-safe and Annex A.3 function scope; emulated-empathy partnering and affective-data processing; design-stage ethical-value artefacts; model placement/transition dates; the relevant Union provider/deployer/output nexus; protected vulnerability; and Article 5’s practice, behavioural-distortion and actual/likely significant-harm conditions. These are requirement-specific applicability facts, not missing taxonomy labels. Records identify the relevant missing fact for every insufficient-evidence pair. Temporally excluded requirements and affirmative lifecycle/trigger exclusions omit findings as required.

INC-000064’s existing taxonomy-gap clause remains: a standalone Grok privacy impact assessment did not cover the materially different automatic public @Grok posting pathway. FC-000016’s represented-verification-completion condition and FC-000041’s defined mandatory-route-bypass condition were not established. The runtime pathway-specific assessment issue remains a separate taxonomy review signal; no external finding was issued by bypassing the taxonomy. No additional taxonomy gap was established, and broad organisational-governance topics were not added.

## Validation

Validation results will be completed after all tranches and deterministic public projection regeneration. Candidate matrix snapshots remain untouched by the maintainer’s later instruction.
