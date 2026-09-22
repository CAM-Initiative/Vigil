# VIGIL full-corpus record-by-record re-adjudication — 2026-09-22

## Purpose

This campaign replaces the earlier assumption that schema migration, Section 02 population, Harm Impact migration, or deterministic review of the unclassified subset constituted a complete corpus re-adjudication.

Every active Incident record is to be reviewed individually from occurrence evidence through final classification and conclusion. Bulk version normalization is prohibited as a substitute for adjudication.

## Mandatory start-to-finish workflow for each Incident

1. Re-open the canonical Incident record and its review history.
2. Search the occurrence afresh using occurrence-specific terms.
3. Prefer first-party/provider material, court/regulator material, affected-party evidence, technical artefacts, and high-quality independent reporting as appropriate.
4. Rebuild or confirm the evidence spine, including source roles, evidence status, contradictions, and material limitations.
5. Rebuild or confirm `summary` and `vigil_assessment.factual_basis` from the admitted evidence.
6. Build or confirm substantive Section 02 `source_clause_analysis`, resolving source wording/propositions into governance principles rather than merely restating the event.
7. Re-adjudicate against the complete current VIGIL Failure Taxonomy 0.6.6 class set. Record material candidate rejections where they explain the decision. Do not inherit a legacy class merely because it already exists.
8. Re-check VIGIL-HIM against the strengthened occurrence evidence where the evidence review changes or materially strengthens consequence facts.
9. Prepare or confirm the final governance interpretation and CAM significance/conclusion so that every substantive claim is traceable to admitted evidence.
10. Run canonical validation before closing the Incident.

## Allowed dispositions

- **REBUILT** — substantive record changes were required.
- **REVIEWED — NO CHANGE (SUBSTANTIAL)** — the full workflow was completed and the existing record already met the current evidentiary and analytical standard.
- **OPEN** — full record workflow has not yet been completed in this campaign.

A record must not be treated as complete merely because it has `source_clause_analysis`, taxonomy version 0.6.6, or a recent review timestamp.

## Progress ledger

| Incident | Disposition | Review note |
|---|---|---|
| VIGIL-INC-000001 | REVIEWED — NO CHANGE (SUBSTANTIAL) | Fresh source check reconfirmed Replit first-party remediation, dev/prod separation, rollback availability and contemporaneous code-freeze / fabricated-data evidence. Existing FC-000002 primary and FC-000017 secondary mappings, Section 02 analysis and S3 consequence treatment remain evidence-aligned. |
| VIGIL-INC-000002 | OPEN | |
| VIGIL-INC-000003 | OPEN | |
| VIGIL-INC-000004 | OPEN | |
| VIGIL-INC-000005 | OPEN | |
| VIGIL-INC-000006 | OPEN | |
| VIGIL-INC-000007 | OPEN | |
| VIGIL-INC-000008 | OPEN | |
| VIGIL-INC-000009 | OPEN | |
| VIGIL-INC-000010 | OPEN | |
| VIGIL-INC-000011 | OPEN | |
| VIGIL-INC-000012 | OPEN | |
| VIGIL-INC-000013 | OPEN | |
| VIGIL-INC-000014 | OPEN | |
| VIGIL-INC-000015 | OPEN | |
| VIGIL-INC-000016 | OPEN | |
| VIGIL-INC-000017 | OPEN | |
| VIGIL-INC-000018 | OPEN | |
| VIGIL-INC-000019 | OPEN | |
| VIGIL-INC-000020 | OPEN | |
| VIGIL-INC-000021 | OPEN | Fresh occurrence research started; OpenAI status confirms Microsoft personal-account login failure, and contemporaneous community reports preserve `token_exchange_failed` and unaffected alternative OAuth routes. Full adjudication remains open. |
| VIGIL-INC-000022..VIGIL-INC-000144 | OPEN | Expand into individual rows as each record enters review; range notation is administrative only and is not a completion state. |

## Historical-scope finding

The 2026-09-21 deterministic campaign recorded in repository history was repeatedly scoped as an **unclassified Incident re-adjudication** campaign. It therefore did not establish that every previously classified legacy Incident had been migrated to or re-adjudicated under taxonomy 0.6.6. Later metadata/governance-assessment passes also did not reopen every existing taxonomy mapping. This campaign supersedes any contrary completion assumption.
