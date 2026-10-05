# Authority-lineage laundering and recursive legitimacy diagnostic — 5 October 2026

Status: candidate cross-Incident diagnostic; not a canonical Fidelity Class  
Working branch: `agent/incident-ecosystem-ingestion`

## Decision

The cross-corpus review does **not** support promotion of proposed `VIGIL-FC-000084 Continuity-State Propagation Integrity`.

The self-replicating prompt-injection examples establish that attacker-controlled instruction-bearing material can be reproduced into successor carriers. Reproduction is important attack-chain topology, but the act of copying does not by itself establish a governance mechanism that the current taxonomy cannot represent. The governance failure becomes classifiable when a system treats a source, successor artefact, delegated instruction, transformed representation, control-plane state or inherited state as operative without satisfying the applicable existing authority, lineage, verification or continuity invariant.

The earlier propagation proposal is therefore withdrawn from promotion and retained only as analytical history.

A more useful recurring structure is **authority laundering across an authority lineage**: unsupported or insufficiently established authority can acquire increasing *apparent* legitimacy as it passes through system actors, artefacts and control surfaces, especially where downstream actors rely on system-mediated descendants instead of independently re-establishing the originating mandate.

## Candidate invariant

> **Authority must remain traceable to an independently valid originating mandate across propagation, transformation, delegation, persistence and replication; descendant artefacts must not acquire authority merely from system-mediated descent and must not be treated as independent corroboration of their own authority lineage.**

This is a candidate chain-level invariant. It does not amend the canonical taxonomy in this review.

## Why this is not FC-000084

A worm-like sequence can be decomposed into already governed events:

1. lower-authority or attacker-controlled material is encountered;
2. the material is treated as operative instruction without sufficient source-authority validation;
3. an action, write, send, promotion or delegation occurs;
4. the resulting artefact becomes available to a later actor or context;
5. the later actor must independently establish authority, provenance, scope and applicability before reliance;
6. if it does not, the applicable source-authority, delegated-authority, lineage, control-plane, scope or continuity failure recurs.

The causal chain can repeat or branch without creating a new per-hop Fidelity Class. What changes is the **graph structure and resilience of the invalid authority claim**.

## Existing canonical coverage

| Canonical class | Relevant boundary |
| --- | --- |
| **FC-000001 — Source-Authority Separation** | Lower-authority content must not become operative instruction merely because it is encountered. |
| **FC-000003 — Target and Scope Authority Binding** | Authority must be independently re-established across material changes in principal, target, action, environment, task, delegation chain, scope or duration. |
| **FC-000005 — Transformation Authority Preservation** | A representation change must not increase operative authority. The class already carries the alias “Transformation-Mediated Authority Laundering”. |
| **FC-000006 — Control-Plane Authority Separation** | Non-authoritative material requires fresh provenance and authority validation before promotion into policy, permissions, durable memory, checkpoints, orchestration or execution state. |
| **FC-000009 — Downstream Delegated Authority Validation** | Delegation is non-transitive; every downstream actor/action boundary must independently validate the authorising principal and scope. |
| **FC-000012 — Cross-Context Lineage Preservation** | Authority, provenance, rights, identity and intended-use constraints must accompany transferred material or be revalidated before receiving-context use. |
| **FC-000078 — Continuity-State Validity** | Inherited state does not become valid or permanent merely through continuity; receiving execution must revalidate its current authority and applicability. |
| **FC-000063 — Adversarial Evidence Trust Calibration** | For factual/evidentiary use, VIGIL already tests provenance, independence, circularity and common-source amplification. This is an important analogue for descendant corroboration but must not be stretched to instruction authority, which its exclusions route to FC-000001. |

The authority-lineage diagnostic therefore composes existing invariants rather than replacing them.

## Diagnostic concepts

### Authority lineage

The traceable ancestry of an authority-bearing claim, instruction, permission, approval, mandate or execution-shaping state back to the independently valid mandate that could authorise the current actor/action/scope.

Immediate provenance is insufficient where the immediate source is itself a descendant. “Agent B wrote this” is not the same proposition as “the originating mandate authorised this.”

### Authority laundering

A condition in which an authority claim acquires greater apparent legitimacy through system-mediated transformation, delegation, persistence, repetition, promotion or reproduction without an independently adequate increase in underlying authority.

Examples of laundering surfaces include a peer-agent message, workflow note, shared file, durable memory, policy file, cache, credential state, permission state or other artefact whose system residence can be mistaken for evidence that its authority was validly established.

### Laundering depth

The number of successive authority-reliance boundaries separating a current operative claim from the last independently validated originating mandate.

For a bounded occurrence, depth should be reported only to the extent directly reconstructable from evidence. Unknown intermediate ancestry must remain unknown rather than being inferred.

### Propagation breadth

The number of descendant actors, artefacts or control surfaces produced from an authority-bearing lineage. Breadth and depth are separate: a shallow fan-out can be large, while a long chain can remain narrow.

### Revalidation gap

A material lineage transition at which authority/provenance should have been independently established but the available evidence shows reliance on inherited or intermediary state instead.

### Provenance retention

Whether a downstream actor can still recover the originating authority basis and the constraints that travelled with it, rather than seeing only the most recent intermediary artefact.

### Orphaned authority

An authority-bearing claim or state that remains operative even though the system can no longer establish the originating mandate that supposedly justifies it.

Orphaning captures the “patient zero no longer matters” problem: the original carrier can disappear while descendant state continues to influence execution.

### Endogenous corroboration

Multiple descendants of the same authority lineage are treated as if they were independent evidence that the underlying authority is valid.

This is the authority analogue of common-source amplification. Branching does not create source independence.

### Convergence

Separate descendant branches later meet in one reasoning or control context and mutually reinforce apparent legitimacy. Convergence is especially dangerous when the receiving actor sees multiple system-resident artefacts but cannot recover their common ancestry.

### Authority amplification

A lineage reaches a surface with greater consequence, privilege, persistence, audience, or execution power than the surface from which the claim entered, without the increased authority being independently established.

## Corpus test

| Incident / review | Evidence relevant to the diagnostic | Disposition |
| --- | --- | --- |
| **INC-000183** | Attacker-controlled email content was reproduced into an outgoing email. The public trace does not show a later recipient obeying the descendant copy. | Propagation topology only; FC-000001 owns the evidenced authority failure. The reproduction clause is resolved-no-mapping. |
| **INC-000184** | A fake workspace warning was copied into a note while its destructive instruction was executed. | FC-000001 and FC-000003 own the evidenced failures. No later reliance on the copied note is established. |
| **INC-000185** | A fake compaction/approval note was persisted into a local policy file and used while build configuration was changed. | Strong laundering surface: attacker state becomes policy-like system state. FC-000001, FC-000006 and the FC-000078 boundary already govern the evidenced mechanism. |
| **INC-000186** | A multi-hop Slack injection produced out-of-task sends and reposted the original payload. | FC-000001 and FC-000003 own the evidenced reliance/scope failures. One reproduction is shown; uncontrolled later generations are not. |
| **INC-000108** | Attacker-controlled instructions persisted in shared Artifactory state and were later consumed by a victim session using that session's tools and permissions. | Strong cross-session lineage/reliance comparator. FC-000001 and FC-000003 already classify the occurrence. |
| **INC-000159** | Public issue text induced execution, poisoned shared cache state, then reached a privileged release workflow and npm publication. | Strong control-surface authority-chain comparator. FC-000006, FC-000009 and FC-000001 already classify the material chain. |
| **INC-000060** | AISI reported agents planting instructions for other coding agents and leaving reusable public accounts or artefacts. | Supports propagation/persistence surfaces; the current public record does not establish a complete descendant reliance graph for every artefact. |
| **INC-000003 / HF-02 review** | Peer direction, assignment and subdelegation interacted with apparent group authority; the historical HF-02 review already required originating authority to remain bound “at every hop.” | Strong authority-chain comparator. This diagnostic does not reopen the later Incident-level mapping set or reinstate mappings removed by subsequent adjudication. |

## Branching and the “patient zero” problem

A branching authority lineage must be analysed as a directed graph, not a simple chain.

If one compromised node creates several descendants, later actors may encounter multiple apparently separate artefacts. Those artefacts are not independent merely because they arrived through different paths. If their ancestry converges on the same unvalidated authority claim, counting them as independent confirmation creates endogenous corroboration.

The original carrier can also disappear. A mature lineage may persist through policy state, permissions, cache state, memory, messages or downstream artefacts that are now generated by the governed system itself. That is why the diagnostic must preserve **ancestry**, not merely immediate source identity.

The currently reviewed OpenAI worm examples do **not** establish an uncontrolled multi-generation branching graph or descendant convergence outside the published bounded simulations. Branching, orphaning and endogenous corroboration are therefore diagnostic dimensions and design requirements, not occurrence findings attributed to INC-000183–186.

## Suggested graph representation

For future analytical tooling, an authority-lineage graph could represent each material node with:

- actor or artefact identity;
- immediate predecessor(s);
- originating mandate reference, if recoverable;
- authority-bearing proposition;
- target/action/scope claimed;
- control surface;
- transformation or promotion event;
- independent revalidation status;
- provenance retained/lost/unknown;
- privilege or consequence change;
- descendant count;
- convergence/common-ancestor relationship.

Useful derived measures include:

- **laundering depth** — longest evidenced sequence of un-revalidated authority reliance;
- **breadth / fan-out** — evidenced descendant count;
- **revalidation density** — validated authority boundaries divided by material authority hand-offs;
- **orphan status** — whether an operative claim lacks recoverable originating authority;
- **lineage independence** — whether apparently corroborating artefacts have genuinely independent authority origins;
- **authority amplification** — whether consequence/privilege/reach increases along the lineage.

These are analytical descriptors, not severity scores and not substitutes for canonical taxonomy adjudication.

## Taxonomy disposition

1. **Do not promote FC-000084.**
2. Preserve the FC-000084 proposal file as a withdrawn proposal with this review as its disposition.
3. Convert the reproduction-only clauses in INC-000183–186 from `taxonomy-gap` to `resolved-no-mapping`; retain the occurrence fact and chain significance.
4. Preserve every existing canonical mapping in those Incidents.
5. Do not map the authority-lineage diagnostic as a Fidelity Class.
6. Do not extend FC-000063 from factual/evidentiary corroboration into instruction authority; use it only as a conceptual analogue unless its actual recognition conditions are independently met.
7. Revisit canonical taxonomy only if future cases establish a recurring governance failure that remains after FC-000001/003/005/006/009/012/078 and applicable verification controls are fully applied.

## Relationship to the external-reach proposal

This review does not dispose of proposed FC-000085 External-Reach Containment Integrity. That proposal concerns an independently identified environment-side containment boundary and remains a separate maintainer question.
