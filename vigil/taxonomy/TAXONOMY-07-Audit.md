# TAXONOMY-07 — Compound Failure Classification and Native Taxonomy Expansion Audit

## Scope and branch preflight

- Repository: `CAM-Initiative/Vigil`
- Existing branch: `agent/failure-taxonomy-prototype`
- Live-verified pre-work remote head: `7e23d0632b65aca4c16763d3d82aafe24d19e231`
- Pre-work latest commit: `Review NIST SP 800-218A metadata fidelity`
- Live-verified `main`: `9fcaf0e498ca5f7ea0db7c925da4f9c10a4a6891`
- Merge base: `e3d1dcb12875642c71ca3100b43b6d63872bf69a`
- Pre-work comparison: 76 commits ahead of and 1 commit behind `main`
- Intervening remote commits after the supplied handoff head: none
- Taxonomy version retained: `0.2.0-draft`

The taxonomy commits from `f5a8350 — Classify failure modes under native taxonomy` through `bab4fed — Add evidence access classes and close validators` were inspected. The post-`bab4fed` range was also inspected. It contains the concurrent EXTREQ source-fidelity, EU AI Act staged re-extraction, metadata-review, IMDA review, NIST review, and FM-0071 evidence work. TAXONOMY-07 does not modify or revert any EXTREQ source, requirement, fidelity, metadata-review, re-extraction, provenance, or assurance content.

No merge, rebase, reset, cherry-pick, force-push, new branch, pull request, or `main` reconciliation was performed.

## Pre-work catalogue and identifier allocation

The live catalogue contained 8 families and 45 classes. The highest allocated class ID was `VIGIL-FC-000045`; the highest allocated family ID was `VIGIL-FF-0008`; `removed_ids` was empty. The bounded review was completed before allocation.

The surviving concepts were then allocated sequentially:

| ID | Family | Class |
| --- | --- | --- |
| `VIGIL-FC-000046` | `VIGIL-FF-0001` | Inferential Evidence–Authority Conflation |
| `VIGIL-FC-000047` | `VIGIL-FF-0002` | Unsupported Mechanism Attribution |
| `VIGIL-FC-000048` | `VIGIL-FF-0005` | Verification-Dependency Access Failure |
| `VIGIL-FC-000049` | `VIGIL-FF-0009` | Dependency-Cultivation Optimisation |
| `VIGIL-FC-000050` | `VIGIL-FF-0009` | Protected-Signal Influence Repurposing |
| `VIGIL-FC-000051` | `VIGIL-FF-0009` | Relationally Conditioned Epistemic Steering |
| `VIGIL-FC-000052` | `VIGIL-FF-0009` | Instrumental Choice Manipulation |

`VIGIL-FF-0009 — Agency-Preserving Influence Integrity Failures` was allocated only after its family invariant and four distinct native mechanisms passed review. No IDs were removed, reused, renumbered, or preallocated.

## Compound classification architecture

The existing primary classification remains canonical and backward compatible:

- `classification_status` continues to describe the primary outcome;
- `primary_family` and `primary_class` remain the one principal structural mechanism for an exactly classified FM;
- existing generated index fields `family_id` and `class_id` remain the primary projection;
- legacy single-class records without a `secondary_classifications` field remain valid.

An optional `secondary_classifications` array now records zero or more additional independently evidenced mechanisms. Every secondary item carries:

- a canonical family reference;
- a canonical class reference;
- an independent classification basis;
- an independent classification confidence.

Validation rejects unresolved IDs, family/class mismatch, reuse of the primary class as a secondary, duplicate secondary classes, a non-array collection, incomplete secondary entries, and any attempt to use a secondary class in place of a missing primary. The model does not encode harms, consequences, manifestations, sectors, loci, unsupported hypotheses, or merely conceivable causes as secondary classes.

Generated registry summaries preserve the original primary fields and add a secondary summary only when one exists. The Case File reverse mapping and generated HTML label every example as `Primary` or `Secondary`, so secondary membership cannot silently replace or visually outrank the principal mechanism.

## Nine-FM decision table

| FM | Primary mechanism | Primary family/class | Secondary mechanism(s) | Secondary class(es) | Confidence | Action |
| --- | --- | --- | --- | --- | --- | --- |
| `VIGIL-2026-FM-0023` | Material image-prompt transformation stages and the evaluated representation cannot be reliably reconstructed | `VIGIL-FF-0002` / `VIGIL-FC-000013` | Specific refusal/policy cause is attributed although the available lineage does not establish it | `VIGIL-FF-0002` / `VIGIL-FC-000047` | primary high; secondary high | existing class primary; new class in existing family secondary |
| `VIGIL-2026-FM-0026` | Deception or scheming mechanism is attributed without traceable objective/pathway evidence | `VIGIL-FF-0002` / `VIGIL-FC-000047` | none | none | high | new class in existing family |
| `VIGIL-2026-FM-0030` | Purposeful runtime cause is narrated without telemetry or traceable evidentiary lineage | `VIGIL-FF-0002` / `VIGIL-FC-000047` | Actual material runtime state is unavailable or not surfaced for reliance | `VIGIL-FF-0004` / `VIGIL-FC-000029` | primary high; secondary medium | new class primary; existing class secondary |
| `VIGIL-2026-FM-0032` | Affective-governance authority/applicability for one functional role or relationship scope is transposed into another | `VIGIL-FF-0001` / `VIGIL-FC-000003` | none | none | high | existing class |
| `VIGIL-2026-FM-0038` | Probabilistic identity evidence is promoted into practically determinative coercive authority | `VIGIL-FF-0001` / `VIGIL-FC-000046` | no separately established control or assessment mechanism | none | high | new class in existing family; compound evidence insufficient for secondary |
| `VIGIL-2026-FM-0039` | Population-derived prediction is promoted into binding or presumptive individual care-entitlement authority | `VIGIL-FF-0001` / `VIGIL-FC-000046` | no separately established control or assessment mechanism | none | high | new class in existing family; compound evidence insufficient for secondary |
| `VIGIL-2026-FM-0043` | User belief and relational posture condition the evidence channel toward agreement and confidence amplification | `VIGIL-FF-0009` / `VIGIL-FC-000051` | Shared antecedent claims or inference pathways are presented as apparently independent evidence | `VIGIL-FF-0002` / `VIGIL-FC-000011` | primary high; secondary high | new-family class primary; existing class secondary |
| `VIGIL-2026-FM-0058` | Another decision-maker is instrumentally manipulated to obtain an objective-directed state transition | `VIGIL-FF-0009` / `VIGIL-FC-000052` | no single identity, provenance, authority, or control mechanism is required across all qualifying tactics | none | high | new-family class; compound evidence insufficient for secondary |
| `VIGIL-2026-FM-0062` | Biometric non-verification is promoted into authority to change essential-benefit entitlement/access | `VIGIL-FF-0001` / `VIGIL-FC-000046` | Unresolved verification blocks practical access without a proportionate alternative verification route | `VIGIL-FF-0005` / `VIGIL-FC-000048` | primary high; secondary high | new class in existing family primary and secondary |

The substantive FM definitions, thresholds, source evidence, event evidence confidence, triage state, corpus coverage, and diagnostic provenance were not rewritten to fit these outcomes.

## Existing-family decisions

### Inferential Evidence–Authority Conflation

FM-0038, FM-0039, and FM-0062 satisfy the `VIGIL-FF-0001` invariant. In each case, an evidentiary or unresolved verification state is promoted beyond its legitimate meaning into consequential authority:

| Input state | Legitimate meaning | Improper conversion |
| --- | --- | --- |
| probabilistic identity match | investigative evidence | arrest or detention authority |
| predictive care estimate | decision support | individual care-denial authority |
| biometric non-verification | unresolved verification state | benefit-suspension authority |

The mechanism is therefore a new class in Authority Boundary Integrity, not a new inference, evidence, classification, ethics, human-rights, or harm family.

### Unsupported Mechanism Attribution

FM-0026 and adjacent native FM-0027 establish a recurring Provenance & Lineage mechanism: a causal, operational, behavioural, or intentional account is assigned without traceable evidence showing that the mechanism generated the event. FM-0030 provides a distinct runtime instance, and FM-0023 provides a secondary refusal-rationale instance.

This class is narrower than Untraceable Synthesis and remains distinguishable from event non-capture, audit-trail non-reconstructability, and execution-state non-disclosure. Those mechanisms may co-occur without supplying the unsupported attribution itself.

### Verification-Dependency Access Failure

FM-0050 supplies the primary native case: a facially valid entitlement becomes unusable because remote verification cannot complete and no proportionate fallback preserves access. FM-0062 supplies a secondary essential-benefit instance. This is an Access & Session State mechanism rather than Work-State Continuity. FM-0062 separately contains the authority conversion represented by FC-000046.

## Control, verification, and harm boundaries

- FM-0023 is not mapped to `VIGIL-FC-000043 — Unwarranted Control Activation`. A refusal occurred, but the evidence does not establish that a defined safeguard's valid activation conditions were unsatisfied. The record instead preserves unresolved classifier, transformation, routing, tool, load, and fallback possibilities.
- FM-0038 and FM-0039 do not receive speculative human-assurance or impact-assessment secondary classes. Their records establish absent or ineffective review/corroboration in general terms, but do not establish one defined, applicable control trigger or one required pre-deployment assessment obligation with sufficient precision for an additional taxonomy assignment.
- Arrest, detention, care denial, and benefit suspension remain harms or consequences. They are not taxonomy classes.
- Required Control Non-Activation, Governance Control Reach, Verification & Completion, and Authority Boundary remain separate questions.

## New-family examination

The admitted family is `VIGIL-FF-0009 — Agency-Preserving Influence Integrity Failures`.

It passes the family sentence:

> Every class in this family is a way in which influence over another actor fails to preserve meaningful independent deliberation, choice, or disengagement, or repurposes protected relational, emotional, developmental, vulnerability, or cognitive signals toward an incompatible influence objective.

Native support is not a single generic manipulation bucket:

| Native FM | Distinct reusable mechanism |
| --- | --- |
| FM-0005 | dependency-cultivation optimisation |
| FM-0016 | protected-signal influence repurposing |
| FM-0043 | relationally conditioned epistemic steering |
| FM-0058 | instrumental choice manipulation |

FM-0043 and FM-0058 share the bounded agency-preservation invariant but remain distinct peer classes. FM-0043 conditions an epistemic channel on the actor's prior belief or relational posture. FM-0058 uses an objective-directed manipulative or coercive tactic to obtain another actor's decision or behaviour.

Warmth, empathy, emotional expression, consensual relational depth, transparent personalisation, truthful persuasion, ordinary negotiation, effective explanation, disagreement, refusal, and emotional discomfort are explicitly excluded absent a qualifying agency-impairing mechanism.

FM-0049 was examined but remains unmapped. Its record combines identity optimisation, relational substrate capture, intervention resistance, possible authority expansion, and hypothesised strategic self-preservation; direct strategic self-preservation remains unverified. TAXONOMY-07 does not use that compound, evidence-limited record to enlarge the family boundary or assign speculative secondary classes.

## Outcome counts

- Families: 9
- Classes and variants: 52
- Classified Failure Modes: 52
- Family-only Failure Modes: 2
- Unmapped Failure Modes: 11
- Deferred Failure Modes: 6
- Failure Modes carrying secondary classifications: 4
- Total secondary classifications: 4
- `removed_ids`: `[]`

The family-count sum remains 52: FF-0001 10; FF-0002 7; FF-0003 7; FF-0004 10; FF-0005 4; FF-0006 3; FF-0007 3; FF-0008 4; FF-0009 4.

## Generated surfaces

The pass regenerated:

- all affected and unaffected standalone family HTML pages through deterministic catalogue generation;
- `VIGIL.FailureTaxonomy.FullReference.html` as the complete technical reference;
- `VIGIL.FailureTaxonomy.CaseFileExamples.json` with explicit primary/secondary roles;
- the Failure Mode classification ledger, including primary and secondary distributions;
- `VIGIL.Failures.Index.json` and `VIGIL.Registry.Index.json` primary-compatible classification summaries;
- all ordinary VIGIL type indexes through the canonical build workflow.

## Validation

- Taxonomy validator: PASS — 9 family files, 52 classes, catalogue integrity OK.
- Focused taxonomy tests: PASS — 36 tests.
- Full `vigil/tests` suite: PASS — 157 tests.
- Full `vigil/scripts` suite: PASS — 37 tests.
- Repository-wide record validator: PASS — 101 JSON files, 6 research files, 107 unique public records.
- Public-record validator: PASS.
- Failure Mode facet validator: PASS — 71 FM records.
- Pipeline-state validator: PASS.
- Lifecycle and corpus-coverage validator: PASS.
- Observatory-boundary validator: PASS.
- Interpretive-provenance validator: PASS.
- Authorship-provenance validator: PASS.
- Source-provenance validator: PASS — 317 source records.
- External-source registry validator: PASS — 81 source versions, 0 review-required or review-due.
- External-requirement validator: PASS — 81 source versions, 845 requirements.
- External-requirement source-fidelity validator: PASS.
- External-requirement metadata-review validator: PASS.
- EU AI Act staged re-extraction regression: PASS — 8 coarse records to 102 deterministic candidates; 18 source-explicit normalisations.
- Deterministic registry, index, reverse-map, and HTML regeneration: PASS, byte-stable across two complete runs.
- Generated HTML parsing: PASS — 10 generated taxonomy HTML files.
- Python bytecode compilation: PASS.
- `git diff --check`: PASS.

The EXTREQ source-fidelity validator continues to report 16 effective downgrades for historically complete but not yet fidelity-assured sources, and the metadata report continues to identify 527 records requiring metadata review. These are the current concurrent EXTREQ review state, not taxonomy validation failures; the validators exit successfully, and TAXONOMY-07 did not modify the underlying EXTREQ content.

## Provenance and authority boundary

The TAXONOMY-07 classification review was performed on 26 August 2026 by OpenAI ChatGPT Work using GPT-5.6 Sol through record-definition/threshold comparison, neighbouring-class review, family-invariant testing, and compound-mechanism separation. Human substantive review is recorded as `not-reviewed`. The taxonomy remains a draft technical classification and does not establish external factual truth, legal liability, CAM/Caelestis doctrine, or human approval.

The historical TAXONOMY-05, TAXONOMY-06A, and Evidence Accessibility Review + Validator Closure audits remain unchanged as historical records.
