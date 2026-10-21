# Gate 1 amendment — supporting external governance requirement extraction

Classification: REVIEW. Revised: 11 October 2026. Status: **implementation approval pending**.
Amendment baseline: `f0baf24b3d05a972705995986c82e1b64770ae34` on `work/infrastructure-governance-instruments`.
This supersedes the initial category-limited proposal; its earlier text remains in Git history. AI-authored research. No human verification is claimed.

## Decision requested

Approve a separate implementation pass in which eligibility depends on an authoritative normative provision and a reviewed material relationship to an existing Alignment Taxonomy invariant, rather than on whether the instrument is AI-specific or a treaty.

International and national technical standards, infrastructure and telecommunications instruments, sector-specific laws and regulations, responsible-business and human-rights principles, established voluntary frameworks, treaties, resolutions and other authoritative instruments can qualify. This is an eligibility rule, not an approved clause list or a general infrastructure compliance database.

Read the [assessment matrix](FC-058-059-SOURCE-ASSESSMENT.md), [registration gaps](SOURCE-REGISTRATION-GAPS.md), [INC-090 note](INC-090-APPLICABILITY.md) and [implementation plan](IMPLEMENTATION-PLAN.md) with this proposal.

## Current behaviour

`vigil/scripts/manage-external-requirements.py` accepts requirements only from `primary-ai-governance`. Its scope validator requires `supporting-external-authority` to use `supporting-only`, which permits zero requirements. The schema lists a supporting role but combined controls prevent its extraction. Fidelity methodology also excludes supporting sources from first-class extraction review.

The Data Act is registered but unextracted. FC-058/059 references remain pending from an earlier review. The admitted FC-059 NIST relationship is contextual and excluded by the candidate resolver. INC-090 retains unresolved, non-canonical FC-058/059 candidate boundaries and no external requirement assessments. These facts supply no occurrence compliance result.

## Proposed behaviour and minimum controls

1. **Role and provision eligibility.** Keep `primary-ai-governance` unchanged. Permit `supporting-external-authority` extraction for a bounded reviewed normative provision, with authoritative access, faithful metadata and a demonstrable invariant relationship. Keep `context-or-discovery` and `excluded-from-current-scope` ineligible. Research, abstracts, institutional interpretation, commentary and examples remain reference-only. Registration and issuer prestige cannot turn commentary into a duty. A source-defined recommendation may be represented as a recommendation after review; explanatory commentary must not be upgraded into it.
2. **Scope compatibility.** Retain `supporting-only` as a zero-requirement state. Permit eligible supporting sources to use existing `in-progress`, `partial` and `complete` states with their review restrictions. Complete means complete for the declared bounded scope. Preserve blocked access, unreviewed sections, next actions and maintainer-action fields. No automatic promotion of registered sources.
3. **Force and applicability.** Reuse `binding-law` or `regulatory-requirement` for laws as appropriate, `voluntary-consensus-standard` for voluntary consensus standards, `government-voluntary-framework` for UNGP/OECD principles and `industry-framework` for GNI, with its multi-stakeholder character explicit. Use posture, expectation type, actor, governed object, applicability and qualifications to distinguish duties, recommendations, permissions and guidance. A mandatory clause within a voluntary standard is not thereby binding law. Contractual incorporation needs evidence. Voluntary alignment assessment does not require adoption or certification under the existing occurrence contract. Enforceability, territorial reach, commencement, party status, designation, contract and delegation remain independent questions.
4. **Vocabulary restraint.** Withdraw the initial proposal's three new force categories from the minimum change. Existing vocabulary can represent the immediate EU, UNGP, OECD, GNI and ISO queue. Mixed resolutions remain held where existing metadata cannot faithfully represent clause force. Present a separate clause-specific vocabulary decision before extraction in such cases. An `international-resolution` category would describe instrument form, not determine binding effect. Do not flatten exhortation and demand into uniform duties.
5. **Validation and fidelity.** Change role and scope guards together. Require bounded extraction review, sufficient access to the actual provision and all canonical fields. Extend fidelity review to extracted supporting sources. Preserve review and assurance distinctions. Official metadata or abstracts cannot support reconstruction of inaccessible copyrighted clauses. Official extracts support only their visible scope. Review artifacts are not canonical requirements.
6. **Relationship admission.** Review the provision and its invariant relationship as distinct decisions. Use existing strengths `direct`, `strong-supporting` and `contextual`. Rejection is a review disposition, not a new canonical strength. Record supported component, actor/object/condition correspondence, limitations and review evidence. A narrow component match is not whole-class equivalence. Extraction can start in a review workspace; promotion must preserve traceability to the reviewed invariant. Do not invent proposal EXTREQ IDs. Preserve source-defined compound structures where appropriate.
7. **Projection and occurrence independence.** Coverage must reflect actual source role, review state and normative force. Keep the resolver's strength and mapped-clause guards. Its output remains disposable candidates. Section 04 consumes only independently justified, materially relevant occurrence assessments, with Aligned / Not aligned / Boundary and canonical force metadata. Irrelevant candidates stay audit-only. Mapping strength cannot select polarity, legal liability or applicability.

## Invariants and pass/fail delta

FC-058 requires an independent authority-basis assessment. Ownership, reliance, shutdown capability and consequences do not prove that dependency was treated as authority or that no legitimate basis existed. FC-059 additionally requires access leverage towards a governance-relevant concession or outcome. Interruption alone does not satisfy it. Class definitions, success/failure recognition and exclusions remain unchanged.

| Content | Current control | Proposed control |
| --- | --- | --- |
| Reviewed Data Act clause, supporting role, partial bounded extraction and reviewed component relationship | Fails role/status guards | Eligible structurally; applicability remains independent |
| Reviewed UNGP or GNI recommendation with accurate voluntary force | Fails role/status guards | Eligible if material invariant relationship established; no legal-duty conversion |
| Licensed national standard clause materially related to authority or choice | Fails role/status guards | Same admission controls; no assumed adoption |
| ISO abstract used to invent clause wording | Inadmissible | Still inadmissible |
| Commentary promoted to enforceable law | Inadmissible in supporting-only state | Still inadmissible; substantive review required |
| Supporting-only source carrying requirements | Fails | Still fails |
| Valid primary AI requirement | Passes | Continues to pass; no role migration |
| Supporting requirement without demonstrable reviewed invariant relationship | Fails role guard | Remains held from promotion |
| INC-090 interruption used to infer a concession or source breach | Unsupported | Remains unsupported |

No currently valid canonical requirement is expected to become invalid. Confirm with a read-only corpus comparison before repair. New review gates must not retroactively rewrite existing requirements.

## Surfaces, impact and repair implications

[The plan](IMPLEMENTATION-PLAN.md) identifies manager/schema dependencies, scope guidance, fidelity controls, review surfaces, generated coverage and downstream Section 04. Some surfaces need documentation or verification only. Change controls only where current behaviour blocks the approved contract.

This amendment changes review documents only. The branch retains 98 registered source versions, 1,102 requirements and 189 canonical Incidents. No new registration, requirement, relationship or Incident assessment is made in this amendment. Future extraction count is unmeasured because atomicity and admission remain unapproved. Audit the full supporting-role inventory before implementation to measure the generic guard's reach. The matrix is not a count target.

No migration, deletion, reidentification, source-version replacement, taxonomy rewrite or Incident repair is authorised. Risks include flattening conditions, confusing State/company actors, inventing adoption, hiding exceptions, forcing class fit and publishing candidates as findings. Preserve qualifications and version identity. Managers own generated-output rebuilds.

The manager is the correct structural enforcement point because it checks source-role/status compatibility and canonical requirement metadata corpus-wide. Schema checks vocabulary and shape; fidelity and substantive review establish meaning. The renderer must not decide admissibility or alignment. A rationale string cannot prove a real normative relationship.

## Approval boundary and stop condition

Under [MAINTAINERS.md](../../../MAINTAINERS.md), Gate 1: “No semantic validator/schema/test change may be implemented until the human maintainer explicitly approves that described behaviour.” The handoff includes builders and publication guards.

Approval of the revised eligibility, scope compatibility, fidelity and traceability behaviour is required before implementation. This matrix does not approve extraction, relationship admission or occurrence findings. After approved controls, validate read-only, report exact failing records and fields, and stop under Gate 2 before broad semantic repairs. No control changes are implemented in this pass.
