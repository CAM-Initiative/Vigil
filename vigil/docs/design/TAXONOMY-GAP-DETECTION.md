# Taxonomy Gap Detection — design proposal

Status: design proposal only. This document does not amend the canonical Alignment Taxonomy, `vigil/VIGIL.Schema.json`, validators, clause-level adjudication semantics, or canonical Incident classifications.

## Purpose

VIGIL already requires exhaustive testing of the current Alignment Taxonomy and already permits taxonomy escalation when a materially evidenced governance mechanism cannot be represented faithfully. What remains underspecified is the decision rule between:

- an Incident that is simply unclassified because evidence is insufficient;
- an Incident-analysis point that sits near an existing class but does not satisfy it;
- an existing class whose boundary or terminology needs repair; and
- a genuinely missing Fidelity Class.

This proposal defines a repeatable taxonomy-gap test.

The core rule is:

> A taxonomy gap exists when occurrence evidence establishes a governance-relevant invariant, mechanism or boundary that is materially necessary to explain the Incident, but the current taxonomy cannot represent it without omitting the point, stretching an existing class beyond its canonical recognition conditions, or collapsing a distinct governance property into another one.

A taxonomy gap is therefore a **coverage conclusion**, not a synonym for `unclassified`.

## Incident Breakdown as a gap-detection surface

The clause-level Incident Breakdown is an especially useful detection surface because its editorial sequence is:

> Source wording → recovered principle → occurrence-specific incident analysis → formal structured classification.

During the occurrence-specific analysis, a reviewer may recover one or more materially supported governance propositions that do not reconcile cleanly with the current class set.

Those unreconciled propositions are **taxonomy-gap signals**.

Examples include:

- a recovered principle is necessary to explain why a source clause matters, but no current class states that governed integrity property;
- the Incident analysis repeatedly has to describe a mechanism in prose that disappears when reduced to the available structured classification;
- several clauses point to the same distinct governance boundary but all available classes capture only adjacent parts of it;
- a proposed mapping would require adding recognition conditions, exclusions or meaning that are not actually present in the target class;
- the same unreconciled mechanism appears across multiple Incidents; or
- an external assessment identifies a materially relevant dimension that VIGIL can evidence independently but cannot represent faithfully in the current taxonomy.

Discussion richness alone is not evidence of a gap. The signal must correspond to an evidence-supported governance proposition.

## The taxonomy-gap test

For each materially unreconciled Incident-analysis point, apply the following sequence.

### 1. State the recovered governance proposition

Express the point without referring to a provider, product, sector, outcome severity or proposed class name.

Prefer the form:

> When [governed condition], the system/process must preserve [integrity property or required boundary].

or:

> [Authority/control/representation/state] must not be transformed into [different governed state] without [required condition].

The proposition must be sufficiently general to describe a governance property rather than merely restating what happened in one Incident.

If no coherent governance proposition can be recovered, there is not yet a taxonomy-gap candidate.

### 2. Establish occurrence evidence

Identify the source and occurrence evidence that makes the proposition material to this Incident.

Separate:

- evidence that the governed condition existed;
- evidence that the relevant mechanism or boundary was engaged;
- evidence of violation, preservation or boundary ambiguity; and
- evidence that remains unavailable.

A possible new class must not be created merely to classify an adverse outcome whose mechanism is unknown.

### 3. Test the complete current taxonomy at the correct abstraction level

Apply the current minimum-sufficient-evidence and abstraction rules.

For each nearest plausible class:

- identify the canonical invariant;
- test its recognition conditions;
- test exclusions;
- identify what part of the recovered proposition it captures; and
- identify what material part, if any, remains outside the class.

Do not reject an existing class because lower-level implementation telemetry is unavailable when the class does not require that telemetry.

Do not stretch an existing class by silently inventing new recognition conditions simply to avoid a taxonomy gap.

### 4. Diagnose the mismatch

Every gap signal must be assigned one preliminary diagnosis:

#### EVIDENCE-GAP

The existing taxonomy may already cover the mechanism, but a required recognition fact is genuinely unavailable.

**Result:** do not propose a new class. Preserve the unresolved evidence condition.

#### EXISTING-CLASS-FIT

A current class faithfully represents the recovered governance proposition once applied at its actual canonical abstraction level.

**Result:** use the existing class. No taxonomy change.

#### BOUNDARY-REPAIR

The intended governed property already belongs to an existing class, but the class definition, recognition criteria or exclusions are demonstrably too broad, too narrow or internally inconsistent.

**Result:** propose a class-boundary amendment rather than a new class.

#### TERMINOLOGY-REPAIR

The class substantively covers the proposition but its name or explanatory terminology obscures the actual invariant.

**Result:** propose terminology repair without changing the recognition boundary.

#### DECOMPOSITION-REVIEW

The unreconciled point appears to combine two or more independently governable properties that should not be represented as one class.

**Result:** conduct family/class decomposition review before proposing a class.

#### FAMILY-PLACEMENT-REVIEW

The proposition appears genuinely distinct, but its relationship to existing Fidelity Families is unclear or indicates that a family boundary itself may be wrong.

**Result:** review family architecture before class admission.

#### TAXONOMY-COVERAGE-GAP

The proposition is evidenced, materially governance-relevant, independently describable, and cannot be faithfully represented by any current class without semantic distortion.

**Result:** create a new-class candidate for taxonomy review.

These diagnoses are mutually useful, not merely labels: they identify the next governance action.

## New Fidelity Class candidate test

A taxonomy-coverage gap becomes a **new Fidelity Class candidate** only when all of the following are true:

1. **Evidenced mechanism or invariant** — the candidate describes something established at the governance-mechanism level, not merely an outcome, harm, policy concern or speculative root cause.
2. **Independent integrity property** — the candidate protects or describes a governance property that can be stated independently of the Incident that revealed it.
3. **Non-duplication** — no current class captures the same invariant and recognition boundary.
4. **Non-stretch** — representing the candidate through an existing class would require changing that class's meaning, recognition criteria or exclusions.
5. **Operational recognisability** — it is possible to state observable recognition conditions by which future Incidents could be adjudicated.
6. **Excludability** — it is possible to state what superficially similar situations do *not* belong in the class.
7. **Polarity independence** — the proposed class can support failure-occurrence, successful-invariant and, where appropriate, ambiguous-boundary relationships. The class is not merely a label for a bad outcome.
8. **Generalisability** — the class is not provider-specific, product-specific, sector-specific or incident-specific unless that scope is itself an unavoidable governance boundary.
9. **Analytical value** — creating the class preserves a distinction that would otherwise be lost and that matters to governance analysis or cross-Incident comparison.

Failure of one of these tests does not prove the underlying Incident analysis is wrong. It means the appropriate representation may be evidence uncertainty, a boundary amendment, subtype/recognition pattern, family repair, or prose-level governance interpretation rather than a new selectable class.

## Recurrence rule

Recurrence is a strong taxonomy-gap signal but is **not an absolute prerequisite** for a new class.

A single Incident may justify a new-class proposal where:

- the invariant is unusually clear;
- the occurrence evidence establishes the recognition boundary strongly;
- the property is independently generalisable; and
- no existing class can represent it without distortion.

However, before admission of a new class, the reviewer should search the corpus for:

- previously unclassified Incidents;
- `unresolved` clause-level adjudication statuses;
- ambiguous-boundary mappings;
- repeated governance-interpretation language;
- source-clause analysis with similar unreconciled propositions; and
- existing classes whose rationales may already be carrying the same concept implicitly.

Repeated independent occurrences materially strengthen the case that the problem is taxonomy coverage rather than one-off description.

## Discussion-point accumulation

A single Incident may produce several taxonomy-gap signals.

Do not automatically create one candidate class per discussion point.

First group the points by the **governed invariant**, not by source clause or wording. Several clauses may be evidence of one missing invariant. Conversely, one clause may expose more than one independently governable property.

The reviewer should therefore produce a temporary gap ledger of the form:

| Gap signal | Recovered proposition | Nearest classes tested | Mismatch diagnosis | Cross-Incident recurrence | Proposed next action |
| --- | --- | --- | --- | --- | --- |
| source-clause / Incident-analysis reference | general governance proposition | class IDs | one diagnosis above | IDs or none found | no change / evidence follow-up / boundary repair / terminology repair / family review / new-class candidate |

This ledger is maintenance evidence and is not public Incident content.

## External classifications and assessments as gap signals

External assessors may use concepts, categories or distinctions that VIGIL does not currently represent.

Those classifications are useful as **searchlights, not authority**.

An external label can trigger the question:

> Does the occurrence evidence independently establish a governance property that our taxonomy currently cannot express?

The answer must be reached through VIGIL's own evidence and taxonomy rules.

Do not:

- translate an external category directly into a VIGIL Fidelity Class;
- create a VIGIL class merely because another framework contains one;
- assume agreement with a provider's causal or normative framing; or
- treat terminology mismatch alone as taxonomy incompleteness.

Where an external classification exposes a genuinely evidenced distinction that VIGIL currently collapses, it should enter the same taxonomy-gap test as any Incident Breakdown signal.

## Escalation and authority

An ingestion or adjudication agent may autonomously:

- identify taxonomy-gap signals;
- build the temporary gap ledger;
- test all current classes;
- assign the preliminary mismatch diagnosis;
- search the corpus for recurrence and comparators;
- draft a proposed invariant, recognition conditions and exclusions for a new-class candidate; and
- stage a taxonomy action with the existing Gmail QA protocol when unresolved work remains.

The agent must **not autonomously admit a new Fidelity Class into the canonical taxonomy**.

Canonical class creation changes VIGIL's analytical constitution and remains a human-governance decision.

A new-class escalation should provide:

- affected Incident ID(s);
- the recovered governance proposition;
- occurrence evidence establishing it;
- each nearest class tested;
- the exact semantic remainder that each class fails to represent;
- mismatch diagnosis;
- recurrence/comparator search results;
- proposed invariant;
- draft recognition conditions;
- draft exclusions;
- likely Fidelity Family or reason family placement is unresolved; and
- whether a boundary amendment, terminology repair, subtype, family review or genuinely new selectable class remains the preferred action.

## Relationship to `unclassified`

`unclassified` and `taxonomy gap` answer different questions.

**Unclassified** asks:

> Can the current evidence establish a canonical taxonomy relationship?

**Taxonomy gap** asks:

> Does the evidence establish a governance property that the current taxonomy itself cannot faithfully represent?

An Incident may therefore be:

- unclassified with **no** taxonomy gap because evidence is insufficient;
- classified with an existing class **and still** expose a separate taxonomy gap;
- classified under several current classes while one material Incident-analysis point remains uncovered; or
- unclassified **because** a genuine taxonomy-coverage gap exists.

This distinction should be preserved explicitly.

## Proposed lifecycle

The resulting analytical sequence is:

```text
INCIDENT EVIDENCE
  ↓
INCIDENT BREAKDOWN / GOVERNANCE PROPOSITIONS
  ↓
CURRENT TAXONOMY TEST
  ↓
UNRECONCILED POINT
  ↓
MISMATCH DIAGNOSIS
  ├─ evidence-gap → preserve unresolved evidence
  ├─ existing-class-fit → classify
  ├─ boundary-repair → taxonomy amendment review
  ├─ terminology-repair → terminology review
  ├─ decomposition-review → architecture review
  ├─ family-placement-review → family review
  └─ taxonomy-coverage-gap
         ↓
     corpus recurrence search
         ↓
     new-class candidate
         ↓
     human taxonomy governance
         ↓
     if admitted: taxonomy sync + affected-corpus re-adjudication
```

This deliberately prevents both failure modes:

- **under-generation** — forcing genuinely distinct governance mechanisms into the nearest available class; and
- **over-generation** — creating a new class every time an Incident contains interesting prose that does not map cleanly.

The decisive question is not whether an Incident contains an unmatched discussion point. It is whether that point represents a **material, evidenced, independently governable invariant that the present taxonomy cannot express faithfully**.
