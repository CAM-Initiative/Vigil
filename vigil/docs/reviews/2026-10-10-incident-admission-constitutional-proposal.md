# Proposed VIGIL constitutional amendment — incident admission before diagnosis

**Proposal date:** 10 October 2026  
**Proposal reference:** `proposal/incident-admission-constitution-reconciled-20261014`  
**Original basis:** `main` at `257e55354a560db13ded691f0082103ab1e33f5e`; **reconciled to** `main` at `38e72662a0bed19d9f1e0114f8370128445f0bc8`; existing Constitution 0.1.0-beta  
**Proposed draft:** 0.1.1-beta (not adopted)  
**Decision authority:** CAM Initiative, under Constitution Article 13  
**Status:** Pending explicit human approval. No present authority to create, suppress or reclassify an Incident.

## Reconciliation with current main (14 October 2026)

The proposed admission text from commit `7a68ed560af33fe126db6022b97675f084f2f2c8` has been ported to the current Constitution without undoing changes landed in incident-ingestion PR #118. The current clause-level review contract is preserved and **the retired global adjudication matrix is not reintroduced**. Article 2.8 and the additional Article 5 text remain **proposed, not adopted**; this branch does not operationalise the rule in schemas, validators, or existing Incident findings. Maintainer/Agent/Incident Adjudication Workflow subordinate alignment is a distinct gate following express Article 13 approval. Original historical branch remains attributed here for audit, but need not remain open when the present proposal is safeguarded.

## Current subordinate-control reconciliation (14 October 2026)

Read-only reconciliation against the current `main` sources, not an authorisation to implement their changes:

| Current authority | Current control | Follow-on action if Article 2.8 is approved |
| --- | --- | --- |
| `vigil/MAINTAINERS.md` | Canonical new Incident IDs originate solely on `agent/incident-ecosystem-ingestion`; source watch lists do **not** determine admission, and existing incidents take precedence over duplicates. | Define a documented, evidence-led **ADMISSION** decision before ID allocation, including candidates with successful or mixed AI-boundary outcomes, human misuse, incidental security-tool cases, current/withdrawn/deleted-incident identity screening, and under-evidenced disposition. Recreate the dedicated ingestion branch from current main when next needed, as the existing allocation rule requires; do not allocate IDs on this proposal branch. |
| `vigil/AGENTS.md` | Agents must preserve evidence, separate interpretation, and respect maintainer approval and non-destructive rebuild gates. | Give agents candidate-research and recommendation duties only; no unilateral adoption, canonical allocation or reclassification; retain schema/validator Gate 1/Gate 2 approval restrictions. |
| `vigil/docs/maintenance/INCIDENT-ADJUDICATION-WORKFLOW.md` | Existing `BASELINE → EVIDENCE → FACTUAL RECORD → TAXONOMY → HARM → INTERPRETATION → VALIDATION` describes **rebuilding admitted Incidents**. | Add a separate **pre-allocation intake/admission workflow**, not a destructive replacement of the existing rebuild sequence; explicitly preserve the baseline-and-mapping disposition rules for extant records. |
| `vigil/VIGIL.Schema.json` and public projections | Canonical Incident data, harm/taxonomy and current publication are governed separately. | First review whether candidate screening requires any canonical field at all. Do not create mandatory retroactive fields or assign a failure/exemplar/HIM band merely to admit an occurrence; validate candidate data in a noncanonical research surface. |
| External requirements and taxonomy | Source applicability, requirement alignment, class recognition and severity require independent assessments. | An admission decision alone must confer **no** compliance result, fidelity-class status, legally attributable wrongdoing, or severity. |

### Known reconciliation risks and approval gate

- **Constitutional adoption is pending**: Article 13 requires explicit CAM Initiative approval of the proposed text and the governance effect before changing operative authority.
- **Dedicated ingestion branch is no longer among current open branches**: follow the existing Maintainers rule to recreate it at the current `main` head before any new ID allocation; do not allow branch deletion or this proposal to bypass that custody rule.
- **Deleted/withdrawn records**: audit historical identifiers before any new allocation, but this proposal does not itself restore, re-admit or reclassify any prior record.
- **Retired global matrix**: the current corpus uses clause-level adjudication. Do not restore the old adjudication-matrix references from the 10 October proposal's historical baseline.
- **Publication**: reconcile the Knowledge Base's already published explanatory admission principle only after constitutional approval. Public exposition is not constitutional enactment.
- **Validation**: run targeted constitutional-document review, then the applicable tests on an approved implementation PR. A known shared `VIGIL records` generated-textbook-examples mismatch (INC-000032/FC-000035) on unrelated PRs is not evidence of a defect in this two-file proposal.

## 1. Issue and purpose

The current Constitution establishes evidence before conclusion (2.1), separate adjudications (2.2), admissible incompleteness (2.3), no forced taxonomy fit (2.6), successful-invariant recognition (Article 9), and governed correction. It does not explicitly define the **pre-adjudication Incident admission gate**. Without that gate, research intake may inadvertently select only apparent failures, confuse malicious human AI use with model misalignment, or include ordinary security incidents with merely incidental AI.

The new CAM Initiative public Knowledge Base section on Incident Admission has now articulated the principle. This proposal places the narrow epistemic boundary in the higher governance instrument without automatically claiming that the public page itself has amendment authority.

## 2. Exact provisions proposed

- **Add Article 2.8 — Incident admission precedes diagnosis.** Defines evidence, bounded occurrence, material AI role, independent diagnosis, unsuccessful/successful/mixed/incomplete outcomes, relevant security/misuse limits, historical comparisons, and duplication gate.
- **Extend Article 5 — Minimum conditions for authoritative adjudication.** Separates admitting an Incident from finishing its taxonomy, Harm Impact, governance or requirement assessment.
- **Version:** Advance draft from `0.1.0-beta` to `0.1.1-beta (proposed)`; preserve visible `not adopted` status. No claim of constitutional adoption by branch creation.

Full proposed constitutional wording is shown in `vigil/CONSTITUTION.md` on this **proposal branch only**.

## 3. Why this belongs in the Constitution

A pre-adjudication gate prevents upstream selection bias. A protection that an observer can confirm held under attack pressure should not be omitted because no failure occurred; a ransomware case should not establish model intent merely because the operator was malicious; an unlabeled statistical system should not be admitted solely because an external catalogue calls it AI.

Article 2.8 is a scope and epistemic integrity principle, not a new taxonomy class, automated validator verdict, or expansion of unilateral agent authority.

## 4. Consequences for subordinate contracts after approval

Upon explicit CAM Initiative approval, reconcile in a bounded follow-on change:

1. `vigil/MAINTAINERS.md`: introduce intake eligibility, scoped security categories, candidate disposition and current/deleted/superseded crosswalk **before ID allocation**. Preserve the existing requirement that new IDs originate on `agent/incident-ecosystem-ingestion`.
2. `vigil/docs/maintenance/INCIDENT-ADJUDICATION-WORKFLOW.md`: document an admission stage before the current `BASELINE → EVIDENCE → FACTUAL RECORD → TAXONOMY → HARM → INTERPRETATION → VALIDATION` sequence, without erasing the non-destructive rebuild contract.
3. `vigil/AGENTS.md`: cross-reference the admission rule but do not grant agents a new constitutional authority or make source/title heuristics authoritative.
4. Existing schema/validators: examine whether existing fields can preserve distinct system-role, confidence and admission rationale; avoid adding mandatory fields or retroactive corpus invalidations without separate design review.
5. The Observatory private research workflow can record `new candidate`, `existing`, `same mechanism but distinct occurrence`, `out of scope`, `under-evidenced` and `historical reconsideration` without making a candidate automatically canonical.
6. Public Knowledge Base: verify its exposition remains consistent with adopted Article 2.8, and keep publication clear that a public explanation never constitutes legal certification or binding constitutional enactment.

## 5. Practical governance effect

**What changes after adoption:** explicit constitution-level separation between occurrence admission and downstream diagnosis, source-bound handling of malicious AI use and security occurrences, and record-level anti-duplication expectations.

**What does not change:** who has constitutional approval authority; whether an individual incident is actually evidenced; whether a Fidelity Class is met; HIM severity; external governance applicability; the user's existing corpus QAQC work; or the preserved validity of historical Git evidence.

**No retroactive remedy:** The amendment does not silently re-admit deleted cases, reclassify existing records, or approve any of the AIID discovery queue.

## 6. Adoption decision record — deliberately pending

- Human approval: **NOT YET GIVEN for constitutional amendment**.
- Approved text/version: **PENDING**.
- Date of approval: **PENDING**.
- Version actually operative on `main`: **unchanged**.
- Required subordinate reconciliation: **NOT YET IMPLEMENTED**.
- Merge: **DO NOT MERGE as authoritative until explicitly approved and reconciled**.

The user's approval of the general public admission principle, or approval to transfer this branch, does not itself complete Article 13's constitutional amendment process. The exact proposed Article 2.8 and Article 5 text remains subject to a separate explicit human adoption decision.
