# Evidence Accessibility Review + VIGIL Validator Closure

## Preflight

- Existing branch: `agent/failure-taxonomy-prototype`
- Pre-work remote head: `5df69690e4d0b47433e5ae280f6d27715df38000`
- Pre-work `main`: `9fcaf0e498ca5f7ea0db7c925da4f9c10a4a6891`
- Pre-work comparison: 24 commits ahead and 1 commit behind `main`; merge base `e3d1dcb12875642c71ca3100b43b6d63872bf69a`.
- No later taxonomy-branch commit existed at preflight. No merge, rebase, reset, cherry-pick, force-push, new branch, PR, or reconciliation was performed.

## Evidence-accessibility decision

The native Failure Mode evidence supports two structurally distinct peer classes within `VIGIL-FF-0004 — Observability & Audit Integrity Failures`.

### `VIGIL-FC-000044 — Primary Evidence Accessibility Failure`

FM-0033 establishes a practical evidence-access mechanism: an authoritative artefact exists or is identifiable and is required by an authorised reviewer, but the review environment cannot provide direct inspection and secondary representations cannot preserve the material properties. This differs from Material Event Non-Capture, where the evidence was never adequately captured, and Audit-Trail Non-Reconstructability, where available evidence is substantively insufficient to reconstruct the event.

### `VIGIL-FC-000045 — Authorised Investigative Evidence-Access Pathway Failure`

FM-0055 establishes a governance-route mechanism: independently valid investigative authority exists, but the architecture supplies no bounded, authority-verified, confidentiality-protected, proportionate, and auditable route for obtaining necessary non-public evidence. The class does not create or enlarge investigative authority. It differs from practical artefact accessibility and from Authority Boundary failures.

The pre-work highest class ID was `VIGIL-FC-000043`, `removed_ids` was empty, and no intervening allocation existed. IDs `000044` and `000045` were therefore allocated sequentially.

| Failure Mode | Previous outcome | Current outcome | Confidence |
| --- | --- | --- | --- |
| `VIGIL-2026-FM-0033` | family-only FF-0004 | classified → `VIGIL-FC-000044` | medium, unchanged |
| `VIGIL-2026-FM-0055` | family-only FF-0004 | classified → `VIGIL-FC-000045` | medium, unchanged |

Definitions, thresholds, evidence and diagnostic provenance were not rewritten. Human substantive review remains `not-reviewed`.

## Validator baseline

The untouched repository-wide record validator reproduced exactly:

- 111 warnings;
- 16 errors; and
- exit status 1.

The standalone Failure Mode facet validator reproduced 16 FM-0071 controlled-vocabulary errors.

### Warning root causes

| Root cause | Count | Finding | Repair |
| --- | ---: | --- | --- |
| References to withdrawn PATCH records | 80 | Legitimate typed historical provenance tokens; draft artefacts are intentionally non-public and non-resolvable. | Base and public validators now acknowledge only well-formed withdrawn IDs already present in canonical metadata, without loading drafts or making them public. |
| References to withdrawn PROP records | 29 | Same architecture and semantics as PATCH references. | Same narrow validator correction. |
| References to deleted `VIGIL-2026-OBS-0008` | 2 | Genuine stale adjacency links. OBS-0008 was deliberately deleted when its evidence was consolidated rather than retained as a distinct observation. | Removed from OBS-0021 and OBS-0022; OBS-0021/OBS-0022 remain directly related to each other. |

The validator continues to reject malformed IDs and unresolved public OBS/FM/RESEARCH targets. It does not scan or validate `vigil/drafts`, and acknowledgement does not establish publication, adoption, implementation authority, or target resolvability.

### Research-link errors

Eight withdrawn PROP/PATCH provenance links were each reported twice: once as unresolved and once as lacking public reciprocity.

| Originating research record | Withdrawn target | Target type | Before | After |
| --- | --- | --- | --- | --- |
| RESEARCH-0001 | PROP-0001 | proposal | unresolved + reciprocity error | retained non-resolvable provenance token |
| RESEARCH-0001 | PATCH-0023 | patch | unresolved + reciprocity error | retained non-resolvable provenance token |
| RESEARCH-0002 | PROP-0019 | proposal | unresolved + reciprocity error | retained non-resolvable provenance token |
| RESEARCH-0002 | PATCH-0031 | patch | unresolved + reciprocity error | retained non-resolvable provenance token |
| RESEARCH-0003 | PROP-0024 | proposal | unresolved + reciprocity error | retained non-resolvable provenance token |
| RESEARCH-0004 | PROP-0024 | proposal | unresolved + reciprocity error | retained non-resolvable provenance token |
| RESEARCH-0006 | PROP-0032 | proposal | unresolved + reciprocity error | retained non-resolvable provenance token |
| RESEARCH-0006 | PATCH-0037 | patch | unresolved + reciprocity error | retained non-resolvable provenance token |

Public reciprocity remains mandatory for research links to canonical observations and Failure Modes. It is not fabricated against withdrawn records that are deliberately outside the public resolution graph.

## FM-0071 facet closure

FM-0071's prose-like facet values were reconciled to the existing controlled vocabulary rather than broadening the vocabulary for one record. The authoritative substantive definition and threshold were unchanged. Controlled values now express a confirmed/reproduced failure, externally detected evidence, local within-session propagation, completed bypass, passed source verification and looping execution; detailed trajectory and cross-interface qualifications remain in the narrative facet fields and reporting note.

The standalone facet validator now passes all 71 Failure Modes and the one faceted record.

## Generated artefacts

- Updated FF-0004 canonical JSON and taxonomy index.
- Reconciled FM-0033 and FM-0055 canonical classifications and the FM classification ledger.
- Regenerated all family HTML pages and the full taxonomy reference.
- Regenerated the Case File examples projection.
- Rebuilt Failure, Observation and master registry indexes deterministically.

## Validation results

- Taxonomy validation: PASS — 8 families / 45 classes.
- Focused failure-taxonomy tests: PASS.
- Focused taxonomy-classification tests: PASS.
- Full `vigil/tests`: PASS — 148 tests.
- Full `vigil/scripts`: PASS — 34 tests.
- Repository-wide record validator: PASS — 101 JSON records, 6 research records, 107 public IDs, 57 distinct withdrawn provenance IDs, 0 warnings, 0 errors.
- Public-record validator: PASS with the same public/withdrawn boundary.
- Failure Mode facet validator: PASS — 71 Failure Modes / 1 faceted record.
- Pipeline-state, lifecycle, corpus-coverage, observatory-boundary, interpretive-provenance, authorship-provenance and source-provenance validation: PASS.
- Python bytecode compilation: PASS.
- Generated HTML parser validation: PASS — 9 files.
- Deterministic generation and `git diff --check`: PASS.

No warnings or errors are intentionally retained on the canonical repository-wide validation surface.
