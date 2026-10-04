# VIGIL Public Output Style

Status: maintainer contract for public VIGIL-authored prose.

## Purpose

VIGIL public output uses an ASD-STE100-informed controlled-language profile.

The purpose is to make Case Files easier to read, compare and translate while preserving the full analytical meaning of the canonical record.

This profile applies to VIGIL-authored public prose. It does not rewrite or simplify quoted source text, legislation, standards text, source anchors, preserved evidence, titles or other material that must remain faithful to its source.

VIGIL does not claim formal ASD-STE100 conformity unless a publication has been checked against the applicable ASD-STE100 issue and its controlled vocabulary. The current reference issue is ASD-STE100 Simplified Technical English, Issue 9 (15 January 2025). See https://www.asd-ste100.org/.

## Core writing rules

For VIGIL-authored public prose:

1. Put the analytical result before the explanation when a result is present.
2. Use short sentences.
3. Prefer one proposition in each sentence.
4. Prefer active voice when the actor is known and active voice improves clarity.
5. Use one term for one concept. Do not rotate synonyms for style.
6. Use direct verbs instead of abstract noun phrases where possible.
7. Avoid long noun clusters, stacked qualifiers and maintenance jargon.
8. State the evidence and the analytical consequence separately.
9. State uncertainty directly. Do not add generic caution language when a specific boundary can be named.
10. Keep source fidelity. Do not simplify quoted or preserved source language.
11. Define an abbreviation before first public use unless the abbreviation is itself the canonical public name.
12. Do not expose repository workflow, validator language or internal maintenance terminology in public explanations.

VIGIL uses Australian English spelling in VIGIL-authored prose. This is the project spelling directive for the STE profile. Use forms such as `organisation`, `behaviour` and `materialised` consistently.

## Controlled VIGIL terminology

Use the following public terms consistently.

| Concept | Required public term | Do not use as an equivalent public label |
| --- | --- | --- |
| Positive alignment result | **Aligned** | successful, success, passed, met, compliant, invariant held |
| Negative alignment result | **Not aligned** | failed, failure, misaligned, not met, non-compliant, breached |
| Unresolved relevant proposition | **Boundary** | ambiguous boundary, unresolved, applicability unresolved, insufficient evidence, not assessable |
| VIGIL taxonomy | **Alignment Taxonomy** | failure taxonomy, failure-only taxonomy |
| Taxonomy unit | **Fidelity Class** | failure class |
| External proposition | **external requirement** | standard finding, compliance item, control finding |
| Authority of an external source | **normative force** | applicability status |
| Evidence explanation | **assessment basis** | finding basis, applicability basis |
| Candidate-stage decision | **relevant / not relevant** | applicable / not applicable, unless describing the source's own legal or technical scope |
| Public occurrence record | **Case File** | report, dossier, failure record |

Canonical machine values can remain lower-case or hyphenated where required by schema. Public rendering uses the labels above.

Structured taxonomy relationship roles such as `successful-invariant`, `failure-occurrence` and `ambiguous-boundary` remain valid canonical data. They are not alternate public result labels.

## Result language

When a public component already displays an Aligned / Not aligned / Boundary chip, do not repeat the chip mechanically in every sentence. The adjacent prose explains why the result applies.

Preferred pattern:

> The requirement says that the system must preserve the authorised state. The incident shows that the system replaced that state.

Avoid:

> This is a failure occurrence and therefore the requirement was not met and the system was non-compliant.

For Boundary:

> The requirement is relevant to this incident. The available evidence does not show whether the control operated.

Name the missing decisive fact when it is known.

Avoid generic phrases such as:

- evidence is insufficient;
- applicability is unresolved;
- cannot be determined;
- there is not enough information;

unless the next sentence states exactly what evidence or fact is missing.

## Field-specific rules

### Stage 01 — What happened

`summary` describes the occurrence.

Use chronological, concrete language. Name the actor, system, action and consequence when the evidence supports them. Do not insert taxonomy, Harm Impact or external-requirement results.

### Evidence and factual basis

`vigil_assessment.factual_basis` states what the preserved evidence establishes and what it does not establish.

Separate established facts from unresolved facts. Attribute disputed claims to their sources.

### Taxonomy assessment

Public taxonomy rationale explains what the occurrence demonstrates against the Fidelity Class.

Use the public result label supplied by the renderer. Explain the relevant invariant and the occurrence evidence in direct language.

Do not substitute a class ID, relationship role or class name for the explanation.

### External requirements

For each canonical external requirement, public output uses:

- Assessment result;
- External requirement;
- Normative force;
- Evidence and assessment basis.

The result is Aligned / Not aligned / Boundary.

Normative force is separate metadata. Do not weaken or hedge a result because the source is voluntary.

Candidate exclusions are audit material. They are not public assessment rows.

### Harm Impact

State materialised harm directly. Do not imply unreported harm. Do not use severity language as a synonym for taxonomy or standards alignment.

### Discussion

Discussion can explain competing interpretations, dependencies and limitations. Keep the same controlled terminology and short-sentence structure.

A complex analysis can use multiple simple sentences. Do not compress several analytical steps into one sentence.

### Conclusion

State the bounded VIGIL conclusion first. Then state the most important evidence boundary.

Do not introduce new evidence or new taxonomy/standards findings in the conclusion.

## Consistency across surfaces

The same concept must use the same public term in:

- canonical VIGIL-authored public prose;
- generated Case File projections;
- website labels and tables;
- PDFs and print views;
- public taxonomy explanations;
- public external-requirement assessments;
- tooltips, banners and explanatory notes.

Historical audits are historical evidence. Do not rewrite them solely to update terminology. New audits use the current controlled vocabulary and may describe retired terms when necessary to explain a migration.

Source quotations and source titles remain unchanged.

## Review checklist

Before publication, check:

- Does each sentence communicate one main proposition?
- Is the actor clear where the evidence identifies one?
- Does each technical term have one consistent meaning?
- Are Aligned, Not aligned and Boundary used consistently?
- Is normative force separate from the alignment result?
- Does the prose name the evidence rather than rely on generic hedging?
- Are internal IDs and maintainer workflow terms absent from the public explanation unless they are intentionally rendered metadata?
- Are quotations and source text preserved faithfully?
- Does the wording preserve the analytical meaning of the canonical record?

If a simpler sentence changes the meaning, keep the necessary technical term and explain it. Simplicity must not reduce evidentiary fidelity.
