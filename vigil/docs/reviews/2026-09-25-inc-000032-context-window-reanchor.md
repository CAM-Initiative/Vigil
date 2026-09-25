# INC-000032 — 2026-09-25 context-window re-anchor

## Decision

VIGIL-INC-000032 is re-anchored in version 2.0.0 to the directly preserved 24 September 2026 ChatGPT Work occurrence in which a role-aware VIGIL taxonomy adjudication thread reached its context limit before all material adjudication state had been durably published to GitHub.

This is an explicit evidence-boundary correction, not an assertion that the September occurrence is the same historical event as the superseded June 2026 Codex occurrence previously represented by INC-000032.

## Why the record was re-anchored

The maintainer reported that the original conversational context supporting the earlier June occurrence is no longer available. Continuing to present that occurrence as though its original evidence remained inspectable would overstate the current evidentiary position.

The September occurrence has stronger directly preserved evidence and fits the same current structural mechanism, VIGIL-FC-000035 Material Work-State Persistence.

Earlier versions remain recoverable in Git history and are not reused as evidence for the re-anchored occurrence.

## Preserved evidence

1. Registry artefact `VIGIL/VIGIL-INC-000032.png` at merged Registry commit `d4b3da4623475c8dcc6155144b1ca7e5a1045f84` preserves the visible Work-thread termination, including the context-length message.
2. Registry artefact `VIGIL/VIGIL-INC-000032-02.png` at the same immutable merged commit preserves the recovery assessment identifying the durable GitHub boundary: architecture at `d808f4d2`, role-aware INC-000001–000002 at `500700e8`, and INC-000003 onward not published in the new role-aware form.
3. Vigil commit `500700e8a3748f8d3bada080a9ec63b1aba6e381`, committed on 24 September 2026, independently verifies the durable repository checkpoint described by the recovery evidence.

The original screenshots were supplied by the maintainer through authenticated email. The Registry copies are legibility-preserving derivatives used for durable public evidence storage.

## Recovered thread context

The recovered surrounding conversation identifies the interrupted workflow more precisely than the screenshots alone. The active work concerned role-aware VIGIL adjudication and final-state consolidation from `fix/inc-001-050-adjudication-matrix` into `integration/consolidate-divergent-branches`; the maintainer had explicitly directed the agent to commit material work as it progressed.

Later reconstruction of the broader workflow records corpus-scale consolidation and identification of 49 improved Incident blobs for transplant. That later reconstruction is used only to establish the material scope and continuity requirements of the workflow. It is **not** treated as evidence that exactly 49 records, or every later corpus decision, were lost at the context interruption.

The canonical Incident now exposes both Registry screenshots through `incident_artefacts[]`, so the case-file renderer can display them in Stage 01 / **What happened** rather than leaving them only as source URLs.

## Classification

The occurrence remains classified to:

- family: `VIGIL-FF-0006` Continuity-State Integrity
- class: `VIGIL-FC-000035` Material Work-State Persistence
- role: `failure-occurrence`
- confidence: high
- taxonomy version: 0.6.7

The classification is bounded to persistence. The record does not infer whether the proximate implementation cause was model-side, client-side, orchestration-side or storage-side.

## Harm

VIGIL-HIM 1.0.1 remains S3 on property and asset damage because material digital governance work was unavailable from the durable checkpoint and required recovery/re-execution. The exact number of lost decisions, elapsed recovery time and monetary value are not established and are not inferred.

## Adjudication-matrix consequence

Because the represented occurrence changed, prior class-by-class negative or unresolved decisions about INC-000032 must not be assumed to remain evidentially current merely because the primary FC-000035 mapping is unchanged. The role-aware matrix should be re-adjudicated against the re-anchored September evidence before any claim of exhaustive current-class coverage for INC-000032.
