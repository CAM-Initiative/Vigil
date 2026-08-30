# TAXONOMY-04A — Control Activation Integrity + Control-Reach Boundary Repair

## Scope and preflight

Work began on 24 August 2026 from the exact remote taxonomy head `6f6e9dbda83cd76bbc30b1b55ac501fe801bed3b`. Current `main` was `9fcaf0e498ca5f7ea0db7c925da4f9c10a4a6891`; the taxonomy branch was 16 commits ahead and 1 behind, with merge base `e3d1dcb12875642c71ca3100b43b6d63872bf69a`. The single behind commit was merged EXTSRC-UX-01 work. Its changed files did not overlap the taxonomy work. The late post-TAXONOMY-03 commit changed only `TAXONOMY-03-Audit.md`.

No merge, rebase, reset, cherry-pick, force-push, branch creation, PR, or reconciliation was performed.

## Identifier allocation

The catalogue contained family IDs through `VIGIL-FF-0007`, class IDs through `VIGIL-FC-000042`, and no `removed_ids`. `VIGIL-FF-0008` was allocated to Control Activation Integrity. Classes `VIGIL-FC-000037` through `VIGIL-FC-000039` moved to the new family without changing immutable IDs or semantic codes. No new class ID was allocated.

## Architectural decision

`VIGIL-FF-0008 — Control Activation Integrity Failures` now answers whether the right control became operative at the right time and remained inactive when valid activation conditions were absent. It contains:

- `VIGIL-FC-000037` — Control Availability Ambiguity;
- `VIGIL-FC-000038` — Required Control Non-Activation;
- `VIGIL-FC-000039` — Control Authority Suppression, preserved as a child variant of `000038`.

`VIGIL-FF-0007 — Governance Control Reach Integrity Failures` now begins only after a control or governance signal has become operative. It contains `VIGIL-FC-000040` through `VIGIL-FC-000042` for state preservation, required-route traversal, and delivery to a capable endpoint.

## Unwarranted Control Activation decision

`UNWARRANTED_CONTROL_ACTIVATION` remains an explicit unallocated candidate. The reviewed material supports protective overreach and disproportionate scope (`CAEL-0045`, `CAEL-0048`), stale contextual state (`CAEL-0031`), and upstream evidence/classification collapse (`CAEL-0066`). Those mechanisms can cause or accompany an activation, but they do not directly establish all four required propositions: a defined control, identifiable activation conditions, those conditions being unsatisfied, and the control nevertheless becoming operative. Allocating `VIGIL-FC-000043` would therefore overstate the evidence.

`CAEL-0051` directly supports `VIGIL-FC-000038`: the relevant protective handling fails to activate when the described triggering signals are present. `CAEL-0053` remains `SPLIT_REQUIRED`; age assurance is not converted into a family, and its classification, correction, review, and activation constituents remain unresolved.

## Diagnostic boundary

| Event | Structural classification |
|---|---|
| Trigger satisfied; safeguard does not activate | Control Activation Integrity |
| Trigger unsatisfied; safeguard activates | Control Activation Integrity candidate; canonical class deferred pending evidence |
| Correct activation; excessive scope or intensity | Protective Scope / Proportionality — unresolved |
| Correct activation; unrelated access or work continuity collapses | Access/Session or Work-State Continuity, potentially co-occurring with proportionality |
| Correct signal produced; signal never reaches enforcement | Governance Control Reach Integrity |
| Technical ability to restrict treated as permission | Authority Boundary Integrity |

## Regression coverage

The regression suite now proves that moved immutable IDs remain unchanged, family membership and index alignment remain mandatory, a variant cannot be separated from its parent, and relationships remain resolvable after reclassification. No general migration framework was introduced.

## Validation

| Check | Result |
|---|---|
| `python -m unittest vigil.tests.test_failure_taxonomy` | PASS — 14 tests |
| `python vigil/taxonomy/validate_taxonomy.py` | PASS — 8 families / 42 classes; schema and catalogue integrity OK |
| Python bytecode compilation | PASS |
| HTML parser validation | PASS — 8 standalone family pages and combined reference |
| `git diff --check` | PASS |
| Repository-wide VIGIL validator | Expected non-zero — 111 warnings and 16 research-link errors |

The repository-wide output was rerun at the untouched pre-work head and after TAXONOMY-04A. After normalising checkout paths, the outputs were byte-identical: 111 warnings and 16 errors in both runs. TAXONOMY-04A introduced no repository-wide regression and did not modify the unrelated records.

## Final comparison

Immediately before publication the remote taxonomy head must still equal the verified pre-work head. The intended post-commit state remains deliberately divergent from `main`: the EXTSRC commit is not imported, and no reconciliation is performed.
