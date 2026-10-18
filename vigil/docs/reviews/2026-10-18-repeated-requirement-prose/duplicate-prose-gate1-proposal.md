# Gate 1 proposal: repeated external-requirement assessment prose

Date: 18 October 2026. Status: **proposed; no validator, schema or permanent test change implemented**.

## Problem and current behaviour

`external_requirement_assessments[].assessment_basis` explains one occurrence against one canonical external proposition. Current validation checks structure, references, derivation and result. It accepts the identical entire explanation across different requirement IDs. INC-117 used the same two sentences for four different NIST propositions. The bounded, separately requested INC-117 prose repair distinguishes those propositions without changing any result.

## Exact proposed rule

At `assessment_errors()` in `vigil/scripts/occurrence_requirement_validation.py`, compare nonempty string `assessment_basis` values **within each Incident**, across different valid canonical `requirement_id` values. Normalise Unicode NFKC, letter case (`casefold`), and whitespace (collapse runs and trim). If complete normalised values are equal, emit a blocking diagnostic identifying every affected row and requirement ID: **boilerplate: duplicate complete assessment_basis across distinct requirements; provide requirement-specific evidence and decisive missing facts**.

The rule applies independently of Aligned, Not aligned or Boundary. Both canonical and standalone occurrence-requirement validation use this shared helper. It does not alter any canonical field or alignment result. Existing invalid/missing-field checks continue to apply.

Do not use similarity scores, minimum word counts, keyword bans or generic automatic rewriting. Do not block a common factual sentence where the complete explanations differ substantively. Source evidence, source anchors, quotations held as evidence, taxonomy conditions, central requirement text, standard notices and append-only review history are outside this rule's field scope. A duplicate complete authored explanation containing a quotation still needs independent requirement reasoning; adding a row number or synonym is not substantive remediation.

## Pass/fail examples

- **New failure:** two different requirements both say: “The operator replaced the models. Its wider governance protocols are not published.” Whitespace, case-only and NFKC presentation variants also fail.
- **Still passes:** two rows share “The operator replaced the models”, then one identifies the missing halt plan and the other identifies missing regularly reviewed deactivation criteria. Their complete explanations differ and address the respective propositions.
- **Still passes:** the same requirement assessed against distinct source episodes with different evidence reasoning, subject to the existing duplicate-row and reference rules.
- **Still passes:** a legitimate quotation repeated in source evidence, or shared taxonomy recognition conditions. Those fields are not compared.
- **Already fails:** malformed requirement IDs, unresolved evidence references and invalid alignment values remain invalid.

No currently rejected canonical content becomes valid under this rule. A passing syntactic comparison is not certification that prose is specific or substantively correct; paraphrased boilerplate still requires editorial review.

## Measured corpus impact

Read-only full-field equality screen at baseline `81670d9`: **194 Incidents, 1,343 assessment rows; 44 duplicate groups, 263 affected rows in 36 Incidents**. This counts all participating rows, not 263 distinct erroneous requirements or proven false findings.

After the bounded INC-117 repair: **43 groups, 259 rows in 35 Incidents**. Complete row indices, requirement IDs and duplicated text are in `read-only-duplicate-inventory.json`. INC-117's four unchanged Boundary outcomes now have separate explanations; no other record was repaired.

Affected public surface: Section 04, Evidence and assessment basis, including web, print and static projections. There is no website label or schema change. No fields are removed, moved, hidden or truncated.

## Preservation risks and controls

Different requirements may legitimately draw on the same event, overlapping propositions or the same missing document. The diagnostic requires reviewers to explain the distinct proposition, not invent different facts. Review actual canonical requirements before remediation. Preserve source quotations, evidence, episode identity, outcomes, uncertainty and provenance. Do not manufacture specificity or decisive outcomes merely to clear validation. NFKC can equate presentation variants; reviewers must inspect such matches, not alter scientific or quoted meaning mechanically.

The validator is appropriate for this narrow, deterministic authored-text duplication check because existing structural validation cannot detect a repeated full explanation. Documentation alone does not make the failure visible in routine checks. Semantic similarity and adequacy of independent reasoning remain editorial duties.

## Implementation and stop conditions

If approved, add the shared-helper check and isolated fixtures for exact duplicates, case/whitespace/NFKC variants, distinct full explanations sharing facts, different results, and malformed values. Do not freeze live Incident IDs, class counts or current failure totals in permanent tests.

Run the implemented control read-only over all records and report the actual failure set. **Stop under Gate 2 before repairing the remaining 35 Incidents or any newly discovered records.** If any legitimate source meaning would need to be changed, preserved content deleted, or an alignment result inferred solely to satisfy the rule, stop and return that conflict to the maintainer. Approval of this control does not authorise broad corpus repair.

Gate source: `vigil/MAINTAINERS.md`, “Gate 1 — approval before changing the control”: “Before editing any validator, schema rule, permanent test, builder rule or publication guard that can change whether canonical Incident content passes or fails, the agent or maintainer must first present the proposed change to the human maintainer and STOP.”
