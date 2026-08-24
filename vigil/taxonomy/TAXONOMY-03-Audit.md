# TAXONOMY-03 — Evidence-Derived Failure Family Expansion Audit

Review date: 24 August 2026

## Branch preflight and divergence

Remote heads were resolved before editing:

| Ref | Remote head |
|---|---|
| `main` | `e3d1dcb12875642c71ca3100b43b6d63872bf69a` |
| `agent/failure-taxonomy-prototype` | `f62b99cf1808cb98e94b44cdff89b9a82ba44fcc` |
| `agent/extsrc-ux-01` | `c390c9f2bed36c29981e0cb4f17d00526995dd0f` |

The taxonomy branch was 14 commits ahead of and 0 behind `main`. It was 14 commits ahead of and 4 commits behind `agent/extsrc-ux-01`. The 14 taxonomy commits through `f62b99c` were inspected; no commit had been added since the handoff. Changed-file comparison found no overlap between the taxonomy workstream and the four EXTSRC-only commits. No merge, rebase, reset, cherry-pick, force-push, or cross-branch copying was performed.

TAXONOMY-03 changes only taxonomy files and `vigil/tests/test_failure_taxonomy.py`. The concurrent EXTSRC changes remain untouched. With the recorded remote heads unchanged, the TAXONOMY-03 result is 15 commits ahead of and 0 behind `main`, and 15 commits ahead of and 4 behind `agent/extsrc-ux-01`; the remote comparison is rechecked after publication.

### Post-publication remote verification

At final verification on 24 August 2026, the remote taxonomy branch was at `3b8615bd51809a42c07764a428444ae6b2d8eb72`. Concurrently, EXTSRC-UX-01 had been deliberately merged to `main` through PR #57, advancing `main` to `9fcaf0e498ca5f7ea0db7c925da4f9c10a4a6891`; the remote `agent/extsrc-ux-01` branch had then been deleted.

The taxonomy branch is therefore 15 commits ahead of and 1 commit behind current `main`. Comparison of the taxonomy branch's unique changed files with the 13 files changed by the EXTSRC merge found no overlap. No EXTSRC file or commit was copied, merged, rebased, reset, or cherry-picked into the taxonomy branch. Any future reconciliation remains a separate bounded package through updated `main`.

## Identifier allocation

Before allocation, the catalogue's highest identifiers were `VIGIL-FF-0004` and `VIGIL-FC-000027`; `removed_ids` was empty. The batch allocated families `VIGIL-FF-0005` through `VIGIL-FF-0007` and classes/variants `VIGIL-FC-000028` through `VIGIL-FC-000042` sequentially. No identifier was reused or derived from family membership.

## Admitted families

### `VIGIL-FF-0005` — Access & Session State Integrity Failures

Invariant: effective access and session state remains synchronised, distinguishable, and accurately represented across authentication and access transitions.

Admitted mechanisms:

- `VIGIL-FC-000031` — Authentication-State Continuity Failure
- `VIGIL-FC-000032` — Access-State Collapse
- `VIGIL-FC-000033` — Re-entry Access-State Ambiguity (variant of `VIGIL-FC-000032`)

The boundary excludes authority to act, credential possession or compromise, work-state persistence, enforcement proportionality, and reviewability.

### `VIGIL-FF-0006` — Work-State Continuity Integrity Failures

Invariant: material work state necessary for correct continuation remains durably anchored, recoverable, and usable across interruption or transition.

Admitted mechanisms:

- `VIGIL-FC-000034` — Continuity Anchor Failure
- `VIGIL-FC-000035` — Material Work-State Persistence Failure
- `VIGIL-FC-000036` — Restoration-State Integrity Failure

The boundary excludes relational or persona continuity, access state, provenance evidence, and ordinary task failures that leave resumable state intact.

### `VIGIL-FF-0007` — Governance Control Reach Integrity Failures

Invariant: an applicable governance control or signal is available, activates when required, retains operative authority and state, and traverses the required route to the material point it governs.

Admitted mechanisms:

- `VIGIL-FC-000037` — Control Availability Ambiguity
- `VIGIL-FC-000038` — Required Control Non-Activation
- `VIGIL-FC-000039` — Control Authority Suppression (variant of `VIGIL-FC-000038`)
- `VIGIL-FC-000040` — Control-State Preservation Failure
- `VIGIL-FC-000041` — Required Governance Route Bypass
- `VIGIL-FC-000042` — Governance Signal Delivery Dead-End

This is a bounded decomposition of the former Governance Reach hypothesis, not a recreation of the historical Governance bucket. Runtime or modality locus, responsibility metadata, formation substitution, generic governance weakness, source authority, and post-event observability are excluded.

## Existing-family additions

| Immutable class ID | Primary family | Admission basis |
|---|---|---|
| `VIGIL-FC-000028` | `VIGIL-FF-0003` | Deterministic decomposition omission is a bounded variant of required verification omission. |
| `VIGIL-FC-000029` | `VIGIL-FF-0004` | Live execution-state non-disclosure is an observability mechanism, not a continuity family. |
| `VIGIL-FC-000030` | `VIGIL-FF-0004` | Fragmented material signals prevent combined oversight even where individual signals exist. |

## Migration-ledger decisions

The 159-entry ledger remains non-normative and complete. TAXONOMY-03 materially updated 36 source entries. It records admitted immutable IDs, overlap decisions, decomposition rationale, and unresolved constituents.

Eight compound entries received specific decomposition:

- `CAEL-0029` — restoration and persistence separated from provenance, target binding, and relational continuity;
- `CAEL-0045` and `CAEL-0046` — access-state collapse separated from protective enforcement, scope, proportionality, and reviewability;
- `CAEL-0053` — age assurance, correction, review, and guardian-remediation components retained for later safeguard analysis, with no TAXONOMY-03 admission;
- `CAEL-0063` — restoration integrity separated from persistence, availability, relational coherence, and migration locus;
- `CAEL-0088` — continuity representation and source attribution separated from runtime locus and control reach;
- `CAEL-0136` — signal fragmentation and delivery dead-end separated from capacity, congestion, and suppression;
- `CAEL-0159` — routing bypass separated from logging, audit-evidence, continuity, and binding-eligibility components.

The ledger now contains 45 `SPLIT_REQUIRED` entries. The TAXONOMY-02 baseline contained 44; `CAEL-0063` was correctly reclassified from a single-class candidate to `SPLIT_REQUIRED` after its bundled mechanisms were examined. None of the unresolved constituents was silently dropped.

## Rejected or deferred candidate families

- **Relational Continuity Integrity — deferred.** One portable rupture mechanism is visible, but playful-frame or persona-mood continuity is currently a domain-specific manifestation rather than a second independent mechanism.
- **Governance Authority Topology Integrity — deferred.** Source-authority ambiguity and structural locality may express different invariants, and their non-overlap with Authority Boundary Integrity is unresolved.
- **Constraint Propagation Integrity — deferred.** The records combine propagation, freshness, binding authority, safeguard removal, auditability, and topology.
- **Governance Reach Integrity — rejected as a broad cluster.** It mixed control reach with cross-runtime and modality manifestations, formation provenance, and responsibility metadata. Only the narrower Governance Control Reach invariant was admitted.

No legacy `OPS.FF` heading was recreated as a portable family.

## Remaining evidence for a later batch

The unresolved ledger, rather than a pre-committed TAXONOMY-04 scope, remains authoritative for further investigation. Material still requiring decomposition includes claim and evidence handling, inference and classification, protective enforcement and safeguard activation, governance metadata and state transitions, information/runtime boundary separation, authority topology, constraint propagation, polyadic floor control, identity and credential boundaries, and economic/automation-governance compounds.

## Validator hardening

The catalogue validator now rejects cross-kind supersession: a family cannot be superseded by a class, and a class cannot be superseded by a family. Two regression tests cover those cases. The existing supersession model is otherwise unchanged.

The migration validator also checks that TAXONOMY-03 admitted-family and existing-family decision IDs resolve, that evidence-entry lists are present, and that deferred decision values are controlled.

## Generated references

All seven standalone family HTML pages and `VIGIL.FailureTaxonomy.FullReference.html` were regenerated. The combined reference contains all 7 families and all 42 classes/variants. The renderer does not add implementation or canonical-source commentary to the published technical reference.

## Validation results

| Check | Result |
|---|---|
| `python -m unittest vigil.tests.test_failure_taxonomy` | PASS — 10 tests |
| `python vigil/taxonomy/validate_taxonomy.py` | PASS — 7 family files / 42 classes; schema and catalogue integrity OK |
| Python bytecode compilation of taxonomy tooling and tests | PASS |
| HTML parser check of all standalone pages and combined reference | PASS — 8 files |
| `git diff --check` | PASS |
| `python vigil/scripts/validate-vigil-records.py` | Expected pre-existing failure — 111 unresolved-link warnings and 16 research-link errors |

The repository-wide validator output was compared byte-for-byte, after normalising checkout paths, with a detached worktree at the pre-work branch head `f62b99c`. The outputs are identical. TAXONOMY-03 causes no new repository-wide validation warning or error.

No failure-mode records were migrated to taxonomy IDs, and no unrelated VIGIL records were changed to mask historical validation results.
