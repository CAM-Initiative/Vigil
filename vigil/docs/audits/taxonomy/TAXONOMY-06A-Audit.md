# TAXONOMY-06A — Native-Evidence Admission of Unwarranted Control Activation Audit

## Preflight and scope

- Existing branch: `agent/failure-taxonomy-prototype`
- Pre-work remote head: `f5a835014b2856398c8bab345a2c5657c67a12fc`
- Pre-work `main`: `9fcaf0e498ca5f7ea0db7c925da4f9c10a4a6891`
- No commits had been added to the taxonomy branch after the handoff.
- The local TAXONOMY-05 tree matched the remote branch tree exactly.
- The pre-work catalogue contained 8 families and 42 classes. Its highest allocated class ID was `VIGIL-FC-000042`; `removed_ids` was empty and no intervening allocation existed.
- No merge, rebase, reset, cherry-pick, force-push, branch creation, PR or reconciliation was performed.

## Admission decision

`VIGIL-FC-000043 — Unwarranted Control Activation` is admitted as a peer class within `VIGIL-FF-0008 — Control Activation Integrity Failures`.

The native VIGIL evidence establishes the bounded mechanism that the legacy evidence reviewed in TAXONOMY-04A did not: a defined control has identifiable activation conditions, those conditions are absent in the material context, and the control nevertheless becomes operative with a material effect. The class remains portable; its definition does not depend on a vendor, defensive-analysis domain or relational application.

The class is not a variant of `VIGIL-FC-000038 — Required Control Non-Activation`. The two are opposite peer activation-state failures and are connected by reciprocal `distinguish_from` relationships.

## Native Failure Mode review

| Failure Mode | Confidence | Finding | Reconciled result |
| --- | --- | --- | --- |
| `VIGIL-2026-FM-0019` | high | Hostile content inside an inspected artefact makes a restriction operative even though the bounded defensive-analysis trigger conditions are absent. | `classified` → `VIGIL-FC-000043` |
| `VIGIL-2026-FM-0020` | medium | A safety control becomes operative in a permissible adult reassurance context; the record also preserves boundaries around upstream misclassification and disproportionate intervention. | `classified` → `VIGIL-FC-000043` |
| `VIGIL-2026-FM-0048` | high | A restriction becomes operative against authorised defensive telemetry interpretation although the conditions justifying that restriction are absent. | `classified` → `VIGIL-FC-000043` |

The three records' definitions, thresholds, source evidence, diagnostic provenance and substantive content were not rewritten. Their TAXONOMY-05 confidence values remain high, medium and high. Human substantive review remains `not-reviewed`; this package does not upgrade unrelated classifications or claim human approval.

## Recognition and boundary result

The admitted class requires all five conditions: a defined control; identifiable activation conditions; absence of those conditions in the material context; activation nevertheless occurring; and a material governance, execution, restriction, routing, refusal, escalation or access effect.

| Event | Structural classification |
| --- | --- |
| Trigger satisfied; safeguard does not activate | Required Control Non-Activation |
| Trigger not satisfied; safeguard nevertheless activates | Unwarranted Control Activation |
| Safeguard correctly activates but is much too broad | Protective Scope / Proportionality — unresolved |
| Correct activation destroys unrelated account or work continuity | Access/Session or Work-State Continuity, possibly co-occurring with proportionality |
| Correct signal is generated but never reaches enforcement | Governance Control Reach Integrity |
| Technical ability to restrict is mistaken for permission | Authority Boundary Integrity |

The class exclusions also preserve upstream evidence/classification error, excessive scope or intensity after valid activation, stale post-trigger persistence, authority misuse and downstream control-reach failure as distinct mechanisms.

## Reconciliation and generated artefacts

- The Failure Mode classification outcome changed from 34 to 37 exact classifications; `candidate-new-class` changed from 3 to 0. Family-only (5), unmapped (23) and deferred (6) outcomes are unchanged.
- The canonical FM-to-taxonomy ledger was reconciled for the three records.
- The TAXONOMY-05 migration decision table was updated so a future deterministic classification rebuild cannot restore the retired candidate state. The historical TAXONOMY-05 audit remains unchanged as the record of that earlier review.
- `VIGIL.FailureTaxonomy.Index.json` now records four classes in FF-0008.
- The FF-0008 standalone HTML and complete eight-family reference manual were regenerated.
- The non-normative Case File examples projection now maps all three native Failure Modes to `VIGIL-FC-000043`.
- `VIGIL.Failures.Index.json` and `VIGIL.Registry.Index.json` were deterministically rebuilt from the canonical records.

## Validation

- Taxonomy validation passed: 8 families and 43 classes; catalogue integrity OK.
- 15 failure-taxonomy tests passed.
- 10 taxonomy-classification tests passed.
- The full `vigil/tests` suite passed: 143 tests.
- The full `vigil/scripts` suite passed: 34 tests.
- Pipeline-state validation passed.
- Observatory-boundary, interpretive-provenance, lifecycle and corpus-coverage validation passed for 101 records.
- Python bytecode compilation passed.
- All 9 generated taxonomy HTML files parsed successfully.
- Deterministic taxonomy, index and reverse-mapping rebuilds were byte-identical.
- `git diff --check` passed.
- Repository-wide record validation retained the exact TAXONOMY-05 comparison result: 111 warnings and 16 unresolved research-link errors. TAXONOMY-06A introduced no repository-wide regression and did not repair unrelated records.

## Hold point

No additional family or class was created, and no unmapped or deferred Failure Mode was reclassified. Evidence-accessibility and Evidence / Uncertainty / Classification work remains outside this package and requires a separate bounded review.
