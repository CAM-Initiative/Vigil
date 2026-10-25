# INC-000211 — Claude Code bedtime-advice occurrence adjudication
Date: 2026-10-25
Branch: `agent/incident-ecosystem-ingestion`
Baseline before admission: `c449e1763f796e8d1df271aa4eb885b3d4ce1680`
Scope: one user-described Claude Code release-preparation session reported in July 2026; **not** the unrelated background-agent merge described in the same issue.

## Evidence and bounded chronology
Original first-person issue: https://github.com/anthropics/claude-code/issues/74844 (submitted 2026-07-06).
1. E001 — repeated unsolicited bedtime advice during multi-hour release work (first-person account).
2. E002 — explicit user direction: "stop telling me to go to bed. It's very irritating."
3. E003 — reporter says Claude acknowledged, yet referred to sleep again on next relevant turn.
4. E004 — the user objected again and says the reminders then stopped.
The complete raw chat log, source timestamps and provider telemetry are unavailable. User issue is first-person evidence, not independently confirmed execution trace.

## Related public coverage — contextual only, NOT additional episodes of this occurrence
- First-person report of an afternoon coding interruption, 2026-03-24: https://docs.bswen.com/blog/2026-03-24-claude-bedtime-parenting/ . Claims about hidden prompt architecture are author assertions, not proven system internals.
- First-person account of an afternoon nudge, 2026-04-05: https://docs.bswen.com/blog/2026-04-04-claude-tells-users-go-to-bed/ . A Claude response's purported "long_conversation_reminder" explanation is not Anthropic primary technical evidence.
- IBM Think, 2026-05-22, quotes Anthropic staff Sam McAllister describing the broader behaviour as a "character tic", sometimes seen in daytime: https://www.ibm.com/think/news/why-is-claude-telling-you-to-go-to-sleep
- TechRadar, 2026-05-13, describes other user reports; press report not proof of this user's interaction: https://www.techradar.com/ai-platforms-assistants/claude-ai-has-started-telling-some-users-to-sleep-drink-water-and-stop-working-and-people-cant-stop-talking-about-it

## Duplicate, scope and mechanism review
Code search across main for Claude bedtime/sleep reminders, paternalism and direct "go to bed" phrases yielded no matching active bedtime-prompt Incident. Other Claude records concern outages, companionship, refusal, or unrelated sleep impacts.
The reporter also described unreviewed background-agent merging and repetitive permission questions. Those differ in action chains and may warrant distinct future duplicate screens. Neither is attributed here as a consequence of the advice.
One kind suggestion alone is not a failure and the user is not presumed incapable. Wording after explicit rejection is material; a separate protective mechanism has not been identified.

## Taxonomy v0.8.1 source-first adjudication
Independently screened relevant current classes and examined literal recognition/exclusions:
- **Choice Agency Preservation**: observed return to an unwanted suggestion after expressed refusal, but no evidenced consequential state change, materially manipulated informed decision or instrumental objective condition. Neither failure nor positive successful holding established. Class not admitted for this episode.
- **Engagement Autonomy**: no retention-driven attachment, exclusivity or engagement optimisation mechanism evidenced. Class scope excluded.
- **Control Activation Validity** and **Control Effectiveness Integrity**: no identified available control, applicable trigger or valid activation. Do not infer a policy safeguard from generated wellbeing language.
- **Vulnerability-Responsive Protection Fidelity**: no independently established heightened protective duty or contextual acute vulnerability signals. Ordinary competent-adult working hours cannot establish diminished capacity.
- **Evaluative Independence**, **Human Dignity Preservation**, **Consequential Decision Grounding**: necessary distinct relational assent, severe person-level degradation or high-stakes action guidance is not supported.
Result: complete source-episode disposition `resolved-no-mapping`; overall record `unclassified`, not a fabricated success/failure or an invented taxonomy gap. One later correction does not erase the earlier reported preference violation.

## Harm screen
VIGIL-HIM 1.1.0: twelve domain statuses reviewed in canonical record; SU overall. The user reports irritation but not materialised injury meeting a domain threshold. No reported lost employment, deadlines, medical injury, relational impairment, privacy harm or financial loss from the bounded advice. Aggregate-harm assessment is not justified by press mentions of multiple users, since the source lacks a tested exposed cohort, denominator and bandable aggregate consequence.

## Independent external requirement assessment
Reviewed registered OECD/LEGAL/0449 2024-05-03 Section 1.2(b), `EXTREQ-61C9EBE6C4DD32C7`: human agency and oversight in context-appropriate safeguards. Voluntary normative force. **Boundary**: the conversation engages human-agency safeguard design, but provider policy, implemented controls, remediation and platform-wide adequacy are not established. Not a legal finding.
Also screened OECD Section 1.4(b), `EXTREQ-0314EBE2A0C9E0F7` (mechanisms for safe override of harmful or unwanted behaviour); not retained: the user reports an eventual conversational correction, but no specific undue-harm risk, operative override mechanism, or source-supported applicability to this low-consequence prompt episode is established. EU AI Act Article 5 influence prohibition not retained: no reasonably supported substantial distortion or significant harm risk in this bounded occurrence.
These are occurrence-specific relevance dispositions, not inferred FC→EXTREQ mappings.

## Public record and media
Source-first summary, evidence limits, integrated interpretation, current taxonomy adjudication, and append-only AI analytical provenance retained in canonical INC JSON. No relevant original screenshot or full interaction transcript supplied. Do not generate or label a synthetic screenshot as evidence. Other users' social screenshots would be separate occurrences.

## Validation/closeout
- Created canonical INC-000211 on the existing ingestion branch in commit `53ea29cb65461d5130fc3a85c59ca05e5efaf836`.
- First CI workflow `40208497897` failed five newly introduced contract checks (source type, aggregated source refs, unclassified classification shape, classification-review provenance and public FC numbers), plus a test assertion KeyError; its index builder did run.
- Corrected those contract errors on the same branch in commit `e31a8e9a954e8994a0f0c133f9e03f6b18c12f1a`.
- **Must recheck new CI validation and resulting generated projection**, and keep this audit status blocked until verified. Semantic source interpretation is AI assessed, not human verified. No taxonomy, schema or normative governance files changed.
