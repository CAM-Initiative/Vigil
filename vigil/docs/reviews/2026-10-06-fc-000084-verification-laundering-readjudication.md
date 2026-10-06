# FC-000084 verification-laundering reinstatement and worm-cluster re-adjudication — 6 October 2026

Status: proposal reinstated; bounded Incident re-adjudication complete  
Working branch: `agent/incident-ecosystem-ingestion`

## Decision

VIGIL-FC-000084 is reinstated as a proposal-stage Fidelity Class under **VIGIL-FF-0003 Verification & Completion Integrity**.

The earlier FC-000084 proposal, **Continuity-State Propagation Integrity**, was correctly withdrawn because reproduction and propagation alone are attack-chain topology. The subsequent authority-lineage review exposed a different recurring mechanism: verification evidence or verification-bearing state can acquire **greater apparent assurance through lineage, trusted-system mediation, inherited status or false corroboration even though no additional independent verification has occurred**.

The reinstated class is:

**VIGIL-FC-000084 — Verification Lineage Assurance Integrity**  
Plain-language alias: **Verification Laundering**

Candidate invariant:

> **Verification evidence and verification state must not acquire greater assurance merely through transmission, transformation, repetition, aggregation, persistence or mediation by trusted systems. Downstream assurance must remain bounded to the independently established verification lineage, including source, subject or target binding, scope, freshness, applicability and independence. Descendants sharing a common verification origin must not be treated as independent corroboration, and inherited claims of prior approval, checking or validation must be re-established before they support materially consequential reliance.**

Proposal:

`vigil/taxonomy/proposals/2026-10-06-verification-lineage-assurance-integrity-draft.json`

## Why this is a verification class rather than a propagation class

Propagation answers **where the material travels**.

Verification laundering answers **why the material becomes more believable, more corroborated, or more “already checked” as it travels**.

The governance mechanism therefore requires an assurance increase. Merely copying, forwarding, persisting or reposting an artefact is insufficient.

The characteristic sequence is:

```text
weak / unverified origin
        ↓
system mediation, persistence or descendant creation
        ↓
apparent prior checking / officiality / corroboration
        ↓
greater downstream assurance without an independent check
        ↓
reliance, control or action
```

Authority laundering may follow if the inflated verification state is then converted into permission or execution authority, but the two mechanisms remain separately adjudicable.

## Worm-specific recognition pattern

The proposal includes the named non-selectable subtype:

### Recursive Descendant Corroboration

One claim, approval assertion or verification state produces several descendant artefacts or paths. A later actor treats those descendants as if they were independent corroboration even though they share the same verification lineage.

This is the worm-like form of verification laundering.

The essential rule is:

> **Branching does not create independence. Repetition does not create verification.**

A self-propagating payload may therefore become dangerous not merely because it reproduces, but because its descendants can recursively manufacture the appearance that the originating claim has been independently checked, approved or corroborated.

The proposal also includes **Inherited Verification-State Laundering** for the single-chain case where a descendant state says that checking or approval already occurred and a successor relies on that inherited status without re-establishing it.

## Bounded worm-cluster re-adjudication

### VIGIL-INC-000183 — scheduling email

**FC-000084: not established.**

The outgoing email reproduces the attacker-controlled filing rule, but the published trace does not show a later recipient treating the descendant copy as more verified, independently corroborating, or previously approved.

Disposition: reproduction remains attack-chain topology. The clause stays `resolved-no-mapping`. FC-000001 remains the supported canonical failure.

### VIGIL-INC-000184 — workbook warning

**FC-000084: not established.**

The warning is copied into a local note, but the public trace does not show the note later acquiring verified status or greater assurance because of its system-mediated residence.

Disposition: persistence remains attack-chain topology. The clause stays `resolved-no-mapping`. FC-000001 and FC-000003 remain the supported canonical failures.

### VIGIL-INC-000185 — fake compaction approval

**FC-000084: direct proposal support.**

The fake compaction note states that removal of the security scan was already approved before compaction. The defender explicitly suspects injection but treats the purported inherited decision as expected task state, persists it into local policy and acts on it.

This is a direct fit to **Inherited Verification-State Laundering**:

- a prior-approval claim is represented as already verified;
- the originating verification basis is not established;
- successor/system-resident state increases the claim's apparent assurance;
- the inflated assurance materially supports consequential action.

Disposition: the second source clause returns to `taxonomy-gap` with partial adjudication coverage pending canonical promotion of FC-000084. Existing FC-000001, FC-000006, FC-000041 and FC-000078 mappings remain unchanged.

### VIGIL-INC-000186 — Slack status → ledger → action chain

**FC-000084: direct proposal support.**

The defender recognises the initiating Slack source-status content as untrusted, yet follows the linked status → purported follow-up ledger → action-message chain as necessary task and hidden-test state, then acts and reposts the originating payload.

The evidence supports **lineage-mediated verification laundering**: one untrusted lineage acquires apparent task/verification legitimacy as it appears across multiple linked workflow artefacts. It is therefore the strongest worm-like recognition case in the bounded cluster.

The trace does **not** establish a fully branching multi-generation graph in which several descendants later converge as independent corroboration. Recursive Descendant Corroboration is therefore the governing recognition pattern exposed by the mechanism, while the occurrence finding remains bounded to the evidenced linked chain.

Disposition: the second source clause returns to `taxonomy-gap` with partial adjudication coverage pending canonical promotion of FC-000084. Existing FC-000001 and FC-000003 mappings remain unchanged.

## Cross-domain support

The proposal is not supported only by one OpenAI report.

### VIGIL-INC-000005 — Randal Reid

The warrant pathway allegedly represented a facial-recognition-derived identity lead as coming from a **credible source** while omitting the machine-inference origin and corroboration limits. The downstream identity evidence therefore appeared more strongly verified than the originating verification basis supported.

This is a strong institutional verification-laundering comparator. Existing FC-000010, FC-000016 and FC-000046 mechanisms remain independently applicable.

### VIGIL-INC-000058 — Spokane synthetic police image

A synthetic joke image lost its synthetic and non-evidentiary context during police handoff and was then supplied through an official police communications pathway as if it were an authentic incident photograph. Trusted institutional mediation increased apparent evidentiary assurance without an additional verification event.

This is a second strong cross-domain comparator. Existing FC-000012 and FC-000013 lineage failures remain independently applicable.

These comparators materially strengthen the novelty case: verification laundering recurs outside prompt injection and outside agent self-propagation.

## Boundary against existing FF-0003 classes

| Existing class | Why it does not subsume FC-000084 |
| --- | --- |
| **FC-000016 Required Verification Completion** | Captures an omitted required check, not verification assurance manufactured through lineage or inherited state. |
| **FC-000019 Post-Verification State Integrity** | Requires material change after verification; laundering can occur without object mutation or valid initial verification. |
| **FC-000020 Verification Applicability Continuity** | Governs stale applicability across changed conditions, not common-lineage corroboration or mediated assurance inflation. |
| **FC-000062 Epistemic Reliance Calibration** | Captures generic assurance/reliance mismatch, but not the mechanism by which trusted mediation, repetition or inheritance manufactures the higher assurance. |
| **FC-000063 Adversarial Evidence Trust Calibration** | Already covers circularity/common-source amplification for adversarial factual evidence, but is deliberately factual-evidence scoped and routes instruction authority elsewhere. FC-000084 generalises verification-state laundering to approvals, authentication evidence, inherited state and non-adversarial institutional workflows. |

FC-000046 remains a downstream complement: a laundered verification state may subsequently be converted into consequential authority.

## Promotion boundary

FC-000084 is **not yet selectable canonical taxonomy** in this commit tranche.

Canonical promotion requires the ordinary selectable-class workflow:

1. add FC-000084 to FF-0003;
2. synchronise the exhaustive taxonomy-adjudication matrix to add an FC-000084 cell for every Incident;
3. semantically adjudicate those cells rather than mechanically treating non-matches as `no-mapping`;
4. apply the supported mappings to affected Incident records and Section 02 relationships;
5. validate matrix-to-Incident consistency and taxonomy publication output; and
6. advance release metadata at the publication boundary.

Until that promotion is completed, Incidents that directly establish the missing mechanism preserve it as `taxonomy-gap` rather than falsely asserting a non-canonical class mapping.

## Current disposition

- **FC-000084 reinstated:** yes.
- **Mechanism:** verification assurance laundering through lineage.
- **Family:** proposed FF-0003 Verification & Completion Integrity.
- **Worm-specific subtype:** Recursive Descendant Corroboration.
- **INC-185:** direct support / taxonomy gap.
- **INC-186:** direct support / taxonomy gap.
- **INC-183:** negative control / no FC-084.
- **INC-184:** negative control / no FC-084.
- **INC-005 and INC-058:** cross-domain direct-support comparators for promotion review.
- **Existing canonical mappings:** preserved.
