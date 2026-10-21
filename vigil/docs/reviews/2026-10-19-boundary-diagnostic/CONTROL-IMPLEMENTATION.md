# Approved canonical Boundary control — implementation and Gate 2 report

Date: 19 October 2026. Maintainer approval: direct instruction, “I approve this exact control change.” Scope: control, templates, governing documentation and tests; not automatic canonical population or reclassification.

Canonical input: `032f8a2087a41e35451466e28161842c63433349`. Prior audit commit: `4a4d2215b109ac4a99cea37cfc8c78570c5a6398`. All canonical Incident bytes remain unchanged.

## Implemented contract

Every primary or secondary `ambiguous-boundary` mapping must contain `boundary_adjudication` with non-empty `taxonomy_version`, `material_engagement`, `unresolved_conditions`, `diagnostic_reasons`, `decisive_blocker` and `resolution_requirements`. Each unresolved condition contains polarity, exact condition text, assessment and source/episode references. Source references must resolve to source_records; episode references must resolve within the same Incident. Duplicate reasons/references are rejected. No new fields are required on decisive findings.

Permitted reasons: insufficient-evidence, conflicting-evidence, recognition-criteria-insufficiency. Unsupported engagement and incomplete review cannot satisfy the diagnosis enum. Multiple contributing reasons are permitted. The validator checks structure and reference integrity, not the truth or adequacy of analytical prose. It does not authenticate source facts or mechanically decide which criteria are relevant.

Updated: root/vigil AGENTS, MAINTAINERS, schema-rules contract, adjudication workflow, pilot protocol supersession note, intake/rebuild guidance, dedicated canonical object template and validator. Website rendering, taxonomy conditions, historical confidence semantics, independent assessments and builders remain unchanged.

## Measured validation delta

- Before: 194 canonical Incidents passed canonical validation.
- After: exactly 96 missing adjudication objects across 56 Incidents; zero additional errors in the canonical validation run.
- Exact fields and class IDs are enumerated in `CONTROL-FAILURES.json`.
- Canonical and generated files have no diff.
- New isolated control suite: 12 tests passed. Covers missing/empty fields, supported diagnoses, multiple diagnoses, malformed conditions, dangling/duplicate references, both mapping positions, decisive-role scope and preservation of historical confidence.
- Existing basis-only unit fixture now uses a decisive synthetic role so its assertions remain about public basis wording rather than the separate Boundary requirement.
- Full unittest discovery: 293 tests, eight failures and one import error. One failure is the intended live-corpus validation failure. Seven arise from legacy/synthetic Boundary fixtures that lack the new object (including occurrence-role independence and historical HIM rule fixtures). The import error is unavailable `jsonschema` in the test process. These results are not reported as a green full suite. No skipped checks, weakened assertions or fabricated historical adjudications were introduced to hide them.

## Gate 2: required substantive completion

The missing fields are semantic defects under the new control, not safe boilerplate repairs. Each Boundary needs independent evidence/criteria review before canonical population. Unsupported membership and changes to role/confidence require separate explicit dispositions. Preserve all source facts, historical confidence and interpretive provenance.

Illustrative proposed addition for INC-003 / FC-002, NOT applied to the Incident and NOT a completed full-record decision:

- Before: `boundary_adjudication` absent; existing Boundary role, medium confidence and basis retained.
- After proposal: taxonomy_version 0.7.0; material engagement identifies protected credential/capability use without established permission; the unresolved failure condition is use of availability as a material basis for permission. Reference E009 and its existing source_records[4], [5], [6]. Assessment distinguishes action despite possible unauthorisation from action because possession confers permission. Successful authorised execution is not established. Diagnostic reason is insufficient-evidence; decisive blocker is the unavailable permission premise. Resolution requires the corresponding complete authority decision/trajectory from provider or investigator material. Do not require latent-state telemetry.
- Preservation risk: copying this into every Boundary would manufacture the same evidentiary deficit, hide criteria insufficiency or retain unsupported engagement. It is an occurrence-specific proposal only. No confidence is added to the new object; historical medium remains untouched.

MAINTAINERS Gate 2 requires: “STOP again for human-maintainer approval before broad, multi-record or corpus-wide edits.” No canonical population performed. Existing audit-only E/pending inventory entries remain audit holds and do not satisfy this canonical control.
