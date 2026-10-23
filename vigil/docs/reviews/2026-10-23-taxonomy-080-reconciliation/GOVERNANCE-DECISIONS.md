# Maintainer-only decision — role scope of exclusions

Review date: 2026-10-23. Baseline: `6aff1c4d6ff85a94e0892d558a3bfa651d0b557d`.

## G01 — universal exclusions conflict with positive recognition

The workflow and MAINTAINERS explicitly state that an established exclusion defeats failure, success **and** Boundary admission. Some published exclusions describe the very protective outcome required by the same class's success criteria:

| Class | Literal exclusion | Positive recognition conflict |
| --- | --- | --- |
| FC-024 Audit-Trail Reconstructability | “The pathway can be reconstructed adequately from the available evidence.” | Success requires a bounded reconstruction establishing the pathway with appropriate confidence and explicit limits. |
| FC-072 Oversight Independence | “The review function remains practically independent and adequately capable, even though it reaches an adverse or contested conclusion.” | Success requires actual independent, capable review and challenge. |
| FC-022 Material Event Capture | “Equivalent evidence is captured through another reliable mechanism.” | Success recognises proportionate captured and retained event evidence, without restricting it to one capture mechanism. This exclusion can defeat alternative-channel successful capture. |

INC-003 currently has positive mappings for all three classes. Its evidence and existing mappings are preserved; this review does not silently reinterpret the published exclusions, remove protective findings or certify whole-case completion. FC-018 and FC-066 retain evidence-limited Boundary findings; their source-specific missing facts are not resolved merely by a current-edition stamp.

**Recommendation:** explicitly scope failure-mechanism exclusions to failure recognition, while retaining genuinely role-neutral engagement/scope exclusions for every role. Inventory the affected classes before applying a governed taxonomy/documentation correction. Do not use an Incident edit to change the published taxonomy's meaning. This is a governance-rule decision requiring maintainer authority, not a request to approve routine case findings.

**Interim treatment:** preserve existing positive mappings and their history; mark the current-edition screen incomplete for affected cases. Continue unaffected cases. Do not open a GitHub Issue for this in-PR decision. No released taxonomy version, class text, schema, permanent validator or canonical role has been changed.
