# EXTREQ-03 — External Requirements Provenance, Assurance and CAM Layer 2 Boundary Repair

## Package authority and boundary

- Package date: 2026-08-16
- Human governance role: Dr Michelle Vivian O’Rourke — contract approver
- Substantive human review: not established
- Human source verification: not established
- Working branch: `agent/instrumental-coercive-influence-capability-revalidation`
- Starting working-branch head: `772098742c0e1ee86c2824e45bc8a325c04ea9b0`
- Canonical `main` at preflight: `e0afc3f38c64ebe1318efb4e2c6008bfe014cafc`
- Starting divergence: 43 commits ahead and 0 commits behind `main`

This package repairs the evidentiary and semantic architecture identified in the post-EXTREQ-02 audit. It preserves the frozen Layer 0/Layer 1 maintained baseline, strengthens the effective Layer 1 projection, and introduces a separate empty Layer 2 architecture for later CAM applicability and coverage assessment.

It does not retrospectively claim human review, source verification, CAM applicability, CAM compliance, CAM conformance or CAM coverage.

## 1. Source-document provenance repair

Historical Layer 0 `fingerprint` and Layer 1 `interpretation_provenance.source_fingerprint` values were found to be SHA-256 hashes of VIGIL's material **source metadata projection**, not hashes of the actual PDF, HTML capture or licensed source artefact reviewed.

The frozen v1.1 maintained baseline remains unchanged for reproducibility. Effective Layer 1 v1.2 now distinguishes:

- `source_metadata_fingerprint` — metadata identity/change-detection hash; and
- `reviewed_source_digest` — SHA-256 of the exact reviewed primary-source artefact, when actually recorded.

No historical reviewed-source digest is inferred. Existing direct-source extractions without a preserved artefact digest are explicitly `not-recorded`.

For controlled standards, source digests and non-copyrighted artefact metadata may be retained without committing licensed source text.

## 2. Normative-force and downstream claim semantics

Effective Layer 1 now separates three semantic dimensions:

1. `requirement_posture` — source-internal posture of the represented clause/control;
2. `normative_force` — authority category of the external source; and
3. `alignment_relationship` — appropriate downstream claim family if applicability/adoption is later established.

This prevents a mandatory clause inside a voluntary standard from being misread as a generally binding legal obligation.

The effective vocabulary distinguishes binding law, regulatory/contractual contexts, voluntary consensus standards, voluntary technical specifications, informative technical reports, government voluntary frameworks and industry frameworks. The corresponding downstream claim vocabulary is `compliance`, `conformance`, `alignment` or `reference-only`.

These are external-source semantics. They are not CAM applicability findings.

## 3. Human assurance without authorship inflation

`source-review-assurance.json` is introduced as a maintained Layer 1 sidecar for:

- exact reviewed-source artefact digests; and
- later human review or verification.

The sidecar is intentionally empty at introduction.

A later assurance statement records reviewer/verifier role, scope, method, evidence and limitations. It supplements the original AI authorship provenance and does not rewrite AI-authored material as human-authored.

The repository provenance declaration is extended accordingly. Contract approval, repository acceptance, publication and human presence remain insufficient to establish substantive review or source verification.

## 4. Historical review provenance correction

The historical EXTREQ-01 and EXTREQ-02 review artefacts used `Reviewer: Dr Michelle Vivian O’Rourke`, while the later repository-wide provenance declaration establishes the operational model as AI-authored semi-autonomous production under human contract approval unless contemporaneous evidence establishes a stronger artefact-level exception.

Those historical review headers are therefore corrected separately to record:

- human governance role — contract approver;
- substantive human review — not established; and
- human source verification — not established.

The correction does not alter the technical history of EXTREQ-01 or EXTREQ-02.

## 5. Extension-pack transition hardening

The previous effective builder allowed repeated `source_scope_updates` for one source/version to be resolved by sorted filename order.

`extension-transitions.json` now explicitly records every currently intended extension-to-extension state transition. The seven known transitions are the IEEE direct-review promotions completed during EXTREQ-02.

The effective builder rejects:

- an unregistered repeated source/version scope update;
- a transition whose prior state does not match the earlier extension result;
- a transition whose target state does not match the later pack; and
- an unused transition registration.

Filename order remains deterministic processing order, but is no longer sufficient authority for changing a previously established extension scope state.

## 6. Source-family assumption removal

The historical `manage-external-requirements-extended.py` remains as a frozen compatibility implementation because existing extension packs and generated history depend on it.

The authoritative effective path is now `manage-external-requirements-effective.py`.

Its active source-scope and direct-requirement construction:

- derives canonical identifier scheme/value from the registered Layer 0 source;
- derives access language from the actual access state;
- derives review date from the extension pack;
- does not use IEEE as the generic fallback for new source families; and
- preserves source-specific handling only where the represented source itself is specifically IEEE or SDOS.

This allows future reviewed non-IEEE extension packs to enter the effective corpus without receiving false IEEE provenance language.

## 7. Source coverage manifests

`source-coverage-manifests.json` is introduced as a generated per-source/version assurance projection.

It separates:

- source access route;
- source retrieval state;
- analysis state;
- represented requirement and clause/control counts;
- known unreviewed and inaccessible sections;
- bounded completeness criterion;
- reviewed-source digest status; and
- human assurance status.

A historical `complete` extraction is represented as `bounded-complete`, meaning governance-significant material identified by the recorded criterion is represented. It is not a claim that every sentence or informative annex was atomised.

This also prevents `direct-public-primary` from being misread as proof that the primary artefact was actually retrieved and reviewed.

## 8. Separate CAM applicability/conformance Layer 2

A new `vigil/cam_conformance/` directory defines Layer 2.

Layer 2 is the only external-requirements layer permitted to state:

- whether an effective EXTREQ is applicable, conditionally applicable, reference-only, not applicable or unresolved for CAM;
- the assessed CAM corpus commit;
- CAM instrument and evidence references;
- coverage disposition: full, partial, absent, conflicting, indeterminate or not applicable;
- remediation and VIGIL routing state; and
- post-production assurance.

Layer 2 validates source/version, normative-force and relationship fields against the effective Layer 1 requirement and cannot silently redefine the external source.

The maintained `assessments.json` is empty at introduction. No current EXTREQ has been retroactively declared applicable to, satisfied by or implemented in CAM.

## 9. Copyright and inaccessible standards boundary

This package does not reconstruct ISO/IEC or IEEE requirements from metadata, abstracts, titles, tables of contents, third-party summaries or derivative crosswalks.

Critical blocked standards remain access work until lawful primary text can be obtained and reviewed. Licensed source text is not to be committed merely because a digest or analytical abstraction is maintained.

## 10. Validation surface

The external-governance workflow is extended to:

- rebuild frozen Layer 1 for backward-compatibility tests;
- build and validate effective Layer 1 v1.2;
- test metadata/digest separation;
- test explicit extension transitions;
- test normative-force/relationship semantics;
- generate and test source coverage manifests;
- validate the separate empty Layer 2 architecture; and
- preserve repository-wide authorship/human-assurance validation.

Generated outputs remain deterministic and are rebuilt by the existing GitHub Actions publication path.

## Stop boundary

EXTREQ-03 establishes stronger provenance, assurance, semantics and separation. It does not perform the substantive CAM applicability/conformance assessment and it does not claim access to currently blocked primary standards.

The next substantive stages are:

1. lawfully obtain/review critical blocked ISO/IEC and IEEE primary texts and record exact artefact digests where possible;
2. extend Layer 1 from those texts without reproducing controlled source content; and
3. only then perform evidence-backed Layer 2 CAM applicability and coverage assessments against a named CAM corpus commit.
