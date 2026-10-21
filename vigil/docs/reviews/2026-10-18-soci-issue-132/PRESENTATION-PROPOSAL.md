# Coverage presentation — verified branch behaviour and bounded proposal

Date: 18 October 2026. Classification: REVIEW. Website PR #158 branch `fix/conclusion-reading-paragraphs-20261018`, inspected HEAD `708baf98d81e023cdb3fe3f7e6ee0d821e24ec86`. No website changes, new canonical fields, blocking controls or deployment are authorised by this review.

## Verified current behaviour

`src/pages/vigil-case-file.tsx` delegates Section 04 to `CaseTaxonomyCompliance`; `src/components/vigil/CaseTaxonomyClassification.tsx` delegates that component to `CaseRequirementAssessments.tsx`. `src/lib/vigilOccurrenceRequirements.mjs` constructs rows only from canonical `external_requirement_assessments` and resolves descriptions/force through the central requirement dataset. Static pages reuse the same row function. This correctly separates taxonomy polarity, occurrence result and instrument force.

The four columns are Assessment result / External requirement / Normative force / Evidence and assessment basis. The exact Aligned / Not aligned / Boundary labels, assessment dates and Incident-local source references are preserved. The introduction disclaims organisation-wide compliance/certification. An empty array produces “No occurrence-specific external requirement assessment is published for this Case File.” It does not explicitly say that no legal duties exist.

However, the row function returns an empty result for both a missing assessment property and an empty array. The component has no review-coverage input. It therefore cannot distinguish not reviewed, reviewed-none-retained, or blocked review from those inputs. Forty voluntary rows also do not establish that binding-instrument review occurred. This is a process-coverage gap, not a reason to invent a fourth alignment result.

The force-label map supports government-voluntary-framework, voluntary-consensus-standard, binding-law, voluntary-technical-specification and industry-framework. Other permitted corpus force values, including regulatory-requirement, fall back to “Not recorded.” A focused execution probe verifies that fallback. This is an incomplete force-vocabulary display, not evidence that the source lacks force metadata. No SOCI force label is manufactured from a source title.

## Test evidence

The existing occurrence-requirements suite passes **13/13**, including interactive row semantics, all three results and static rendering. Missing and empty arrays are deliberately tested as producing no rows. Additional read-only probes confirm the missing/empty equivalence and regulatory-requirement fallback. This validates source/module behaviour, not a deployed browser or every export surface.

The initial test could not import React. Installing only the four exact relevant versions from the branch's lockfile into the external temporary review directory resolved it: React 18.3.1, react-dom 18.3.1, TypeScript 5.9.3 and lucide-react 0.462.0. The initial npm cache path was unwritable; a task-local cache fixed that environment issue. Installation scripts were disabled; repository manifests and lockfiles were unchanged. The reviewed website checkout remains clean.

## Bounded proposal

1. On the existing website branch, separately authorise additive explanation that rows show only assessed requirements; normative force does not itself establish legal applicability to the occurrence, and absent binding rows are not proof of absent legal duties. Preserve existing three result labels and canonical row authority.
2. Make the force-label map cover the full already-governed vocabulary, with generic fixtures for each value. Do not introduce a new canonical force category just to display SOCI.
3. Do not infer review coverage from empty lists, nonempty lists, timestamps or counts. Where no explicit declaration exists, present review coverage as not recorded in this view, rather than falsely labelling the pass not performed or completed.
4. Coordinate explicit review-coverage presentation with PR #137's existing pending `processing_review` proposal at `vigil/docs/reviews/2026-10-18-inc-199-203-completion/completion-control-gate1.md`. That proposal already defines `processing_review.external_requirements.status`, reason, blockers, record version and an audit reference. Do not add a competing field or retrospectively backfill it. Its Gate 1 decision and implementation remain separate prerequisites.
5. If that contract is approved, display Not reviewed / Reviewed with assessments / Reviewed with none retained / Blocked as **review status**, independently of Aligned / Not aligned / Boundary. Resolve the versioned audit evidence and display the recorded scope and missing source/fact. A reviewed pass can still have evidence-limited Boundary results. Unknown legal applicability should be explained in reviewed scope/audit metadata; do not revive retired applicability_status fields as alternate alignment outcomes.
6. Apply the same truthful coverage message to static, print and PDF views. A source registration, contextual reference or candidate never generates assessment rows. Record exact source/version/commencement conditions in the requirement/source view rather than deriving them from a force chip.

No new schema or test semantic change is implemented by this proposal. A later implementation request should state the exact accepted/rejected declaration set, prospective versus historical scope, consumer fields, affected counts, preservation risks and Gate 2 stop. The existing proposal must be reconciled rather than bypassed.
