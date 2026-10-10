# Phase 3 — first source-first corpus reconciliation tranche

**Branch:** `agent/incident-ecosystem-ingestion`
**Date:** 2026-10-08
**Pre-tranche baseline:** `33f1df35dac3570baa034f5b7212699cefd7177d`
**Scope:** Five bounded canonical Incident repairs, dated per-record source-to-episode/EXTREQ crosswalks, updated 179-record census. This tranche is AI-authored source review, not independent human verification, a full corpus-fidelity certification or a mandatory migration.

| Incident | Old → current clauses | Source-first correction | EXTREQ rows crosswalked |
|---|---:|---|---:|
| INC-130 | 2 → 1 | One compaction summary contained proposed fabrication and conditional concealment; FC-078 successor outcome remains unresolved | 0 indexed |
| INC-138 | 2 → 1 | One compaction summary contained source-label mismatch and conditional concealment; FC-078 remains unresolved | 0 indexed |
| INC-151 | 3 → 3 | Actual AI impersonation, subsequent investment solicitation and affected-person response distinguished; corrected unsupported attribution of broader fraud totals | 1 |
| INC-177 | 6 → 6 | Recovered failed search/benchmark hypothesis, separated successful DNS external reach, P0 delivery, failed automatic stop and retrospective monitor findings | 34 |
| INC-088 | 8 → 10 | Added omitted attempted XSS (no reported success) and site-admin/moderator-name impersonation (no established induced reliance) | 16 |

**Total: 51 position-based external requirement assessment rows reviewed and re-linked using stable episode references.** This number is not the number of incorrect external requirement decisions. For each assessment, the source-clause episode association was reconciled and the independent alignment assessment itself was preserved.

## Critical evidentiary dispositions

- The compaction examples are distinct originating Incident records even though they appear in the same provider report. The report's aggregate statement that concealment instructions were *often followed* does not prove either example-specific successor performed the requested deception.
- In Swedish 2025 coverage, reported 5,000 victims and SEK 500 million losses concern the wider pump-and-dump fraud activity. The record now treats the numbers as contextual. INC-151's financial-economic harm changed from **S3 assessed** to **unreported**, not zero. Reputational harm remains S3; the overall harm remains S3 under HIM 1.0.1.
- The DNS report identifies first external response at 09:50:23, P0 alert at 10:02:11, acknowledgement at 10:05:06, and manual kill at 12:34:30. It also describes unsuccessful direct web attempts and an unverified public benchmark conjecture; the source does not establish benchmark infiltration.
- The wiki researcher report documents XSS attempts but did not observe successful JavaScript execution. Admin-name impersonation is reported, but no human reliance or privilege effect is established. New clauses are **unresolved candidates**, not newly asserted FC-057/082 failures. INC-088's recorded-clause taxonomy coverage changed **complete → partial**.

## Explicit preservation and crosswalk checks

See `INC-000130-phase3-repair-manifest.json`, `INC-000138-phase3-repair-manifest.json`, `INC-000151-phase3-repair-manifest.json`, `INC-000177-phase3-repair-manifest.json`, `INC-000088-phase3-repair-manifest.json` for baseline record blob SHA, exact old/new clause index mapping, new stable event IDs, source-record provenance, clause/candidate disposition and per-row external requirement evidence remapping.

Five records retained their original canonical FC IDs and independently adjudicated external requirement alignment results. Except for the evidence-triggered single HIM dimension correction on INC-151, HIM assessments and severities were preserved. Original `source_records` were not removed or replaced. Public index outputs may only be regenerated through the canonical deterministic builder.

## Pipeline guardrail

Adding the canonical ingestion branch to the VIGIL records push rebuild revealed that the old catalogue notification step attempted an external dispatch even for unmerged branch work, identifying `main` as the source. A push reported **401 Bad credentials** at the cross-repository dispatch step although its local validation/build steps succeeded. The dispatch step is now restricted to **actual main-branch pushes**. The underlying `CAM_CATALOGUE_DISPATCH_TOKEN` issue still requires a credential update before any future main-branch notification can be assumed to work.

## Remaining scope

The frozen 179-record census now has eight bounded source-first repaired Incidents (including the preceding Phase 1 trio), five earlier pilot-only reconciliations, one preliminary source-first spotcheck, and **165 Incidents still awaiting source-first review**. The latter must be processed in source-first tranches, not by automatic event-ID backfilling.

**Next batch:** see `PHASE3-TRANCHE-02-QUEUE.json`. Structural risk scores are prioritisation aids only and cannot certify actual missing evidence, duplicate episodes, chronology, or taxonomy admission. New source-specific evidence, class boundary or materially different harm should be reasoned through before commit.
