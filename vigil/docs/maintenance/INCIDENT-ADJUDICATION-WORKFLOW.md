# VIGIL Incident Adjudication Workflow

Status: maintainer contract

Applies to: substantive Incident rebuilds, refactors, re-adjudications and taxonomy migrations.

Also applies to the complete ordinary processing of every newly requested Incident.

## New-entry completion — maintainer instruction, 18 October 2026

A request for a new Incident authorises evidence research, source and duplicate/scope review, chronological material-episode analysis, current selectable-taxonomy consideration, all twelve current HIM dimensions, independent external-requirement review, public interpretation and provenance, appropriate authentic media, generated-output rebuilding and required validation. Creating the JSON record is an intermediate step.

Use `vigil/templates/incident-completion-checklist-template.json` as a dated **audit**, alongside the canonical record and any rebuild manifest. It is not a canonical field, schema amendment, validator or publication guard. A checklist is process evidence only when its references and specific decisions permit inspection. Never mark an unperformed pass reviewed.

Complete these passes:

1. Establish source identity/access, duplicate and occurrence boundaries. Search for primary evidence and later corrections. Keep different occurrences distinct.
2. Reconstruct all material source episodes in supported relative order. Retain exact decisive wording where available. Several statements in one passage can need separate adjudication without becoming separate events. Distinguish observed conduct from reported or hypothetical effects. Apply **Temporal Integrity of Adjudication** when later intervention, appeal, correction, recovery or withdrawal may change how an earlier episode is interpreted.
3. Review the current selectable taxonomy, recognition criteria, exclusions and relevant comparators. Preserve supported mappings and independently assess protective responses. Record specific missing recognition facts. A completed review can legitimately leave partial taxonomy coverage, Boundary or unclassified results.
4. Screen all twelve current HIM dimensions and the assessment pathway. Record supported quantities, thresholds and causal limits. Preserve a prior result where the review finds no justified change. Unreported harm is not S1; a research error is not automatically production harm.
5. Resolve class-based requirement leads and independently search the admitted corpus. Read the canonical propositions, actors, objects, lifecycle and qualifications. Independently decide relevance and alignment. Preserve accepted evidence/episode references and dated candidate exclusions. Unknown voluntary adoption does not exclude a requirement. Inspect registered supporting sources before proposing source admission or extraction.
6. Reconcile the public narrative, evidence assessment, mapping explanations, discussion, integrated conclusion and append-only AI provenance. Preserve the four canonical prose roles. Check whether authentic media adds material evidence; record a reason when no media is needed or capture is blocked. Do not substitute synthetic or reconstructed captures.
7. Rebuild generated outputs using their builders. Run applicable canonical/public, provenance, requirement and taxonomy validators and assessment/resolver/projection tests, plus the full suite. Inspect the output for lost details or collapsed mapping roles.
8. Deliver a per-record completion report: material episode coverage, supported mappings, precise decisive evidence gaps, HIM changes or preservation, retained external assessments, no-retained reasons, genuine outstanding work and validation results. Structural success alone is not substantive completion.

For each pass distinguish `not-reviewed`, `reviewed`, `reviewed-evidence-limited` and `blocked` in the audit. The external pass additionally distinguishes `reviewed-with-assessments` and `reviewed-none-retained`. A none-retained outcome needs an inspected candidate inventory, scope and specific reason. A blocked outcome names the missing source or fact and the work it prevents; an empty list or generic complete statement is insufficient. Evidence-limited means the available evidence was actually reviewed and the unavailable decisive fact identified. It does not mean an omitted pass.

Do not invent historical review state or backfill untouched records. Canonical review-status fields or blocking checks require a separate Gate 1 proposal with exact fields, examples, measured impact, preservation risks and stop conditions. Repairs outside the authorised records require Gate 2. Keep performing authorised record adjudications while that proposal is considered.

This workflow exists because an Incident is not a summarisation object. It is a bounded evidence record plus separate factual, taxonomy, harm and governance adjudications. A capable model may assist with the work, but free-form model judgement is not a substitute for the control sequence below.

## Core invariant

A rebuild MUST be non-destructive by default.

Existing source evidence, supported factual detail, taxonomy relationships, mapping roles, confidence, harm findings and interpretive provenance are the starting state. They may change only through explicit re-adjudication. No prior taxonomy mapping or source record may disappear silently.

### Public-record content boundary

The three governed surfaces have deliberately different jobs:

- **Incident = public evidentiary and adjudicative result.** It carries the accepted taxonomy relationships, concise occurrence-specific aggregate and mapping-local bases, material uncertainty, harm reasoning, governance interpretation and substantive comparison with external assessments.
- **Clause-level Incident adjudication = authoritative occurrence results.** `vigil_assessment.source_clause_analysis.clauses[]` records material evidence episodes and their dispositions; `taxonomy_classification` carries the accepted Fidelity Class mappings, roles and coverage. Occurrence findings must not be derived from a separate exhaustive Incident-by-class dataset.
- **Review/audit artefact = temporary notice board.** A dated rebuild manifest or focused campaign packet under `vigil/docs/reviews/` supports source-first comparison, negative-candidate testing, human decisions and cross-thread handoff while work is active. It is **not** a permanent authority. The accepted occurrence findings and material uncertainty belong in the Incident; durable general methods and workflow controls belong in `vigil/docs/maintenance/`. Apply the closeout process in [REVIEW-RECORD-RETENTION.md](REVIEW-RECORD-RETENTION.md) and retire the notice board after its decisions have been promoted.

Do not repeat exhaustive rejected-class inventories in an Incident's classification basis, mapping-local basis or external-assessment comparison. But material negative candidates, unresolved conditions and exclusions necessary to explain the accepted occurrence disposition must have a canonical clause-level rationale. Repository workflow details—including branches, pull requests and validator repair—are not public Incident content. `diagnostic_provenance` is retired and forbidden on active Incidents. `classification_review_provenance` remains compact metadata; any review reference to the notice board is **transitional** and must be reconciled at campaign closeout. Process history belongs in Git/PR history, not a permanent second corpus.

This boundary does not authorise compression of evidence. Preserve factual chronology, uncertainty, occurrence-specific accepted mechanism reasoning, source-clause analysis, Harm Impact findings and valid AI authorship disclosure in `interpretive_provenance`.

Where an Incident also receives an external requirement assessment, use the separate scope, evidence and status rules in `vigil/docs/maintenance/EXTERNAL-REQUIREMENT-ADJUDICATION.md`. A taxonomy-derived candidate is not an occurrence relevance or alignment decision, and the external assessment does not replace or inherit a taxonomy mapping role.

The required control sequence is:

```text
BASELINE → EVIDENCE → FACTUAL RECORD → TAXONOMY → HARM → INTERPRETATION → VALIDATION
```

The sequence is deliberately short. Each gate has a distinct authority boundary and must be completed before the next gate is treated as final.

## 1. BASELINE — establish the record being rebuilt

Before editing:

- read the complete canonical Incident;
- record the baseline Git ref or commit;
- inventory all existing `source_records`;
- inventory the primary and every secondary taxonomy mapping, including mapping-local role, basis and confidence;
- note the current taxonomy version, Harm Impact assessment and current interpretive provenance;
- read `vigil/VIGIL.Schema.json`, `vigil/templates/incident-record-template.json`, the current taxonomy families/classes and comparable Incidents.

Do not begin from a generated index, website projection, handoff summary or an older working branch when a newer canonical record exists.

## 2. EVIDENCE — reconstruct before rewriting

For a full rebuild, existing sources are the floor, not the ceiling.

Search for additional occurrence evidence before rewriting the record. Prefer, in order:

1. originating first-party or primary artefacts;
2. regulator, court, standards-body, research-lab or other authoritative records;
3. independent technical or investigative corroboration;
4. later corrections, updates or consequence reporting;
5. reputable secondary reporting where it contributes material occurrence or harm evidence.

The maintainer must record the search in the adjudication manifest. A full rebuild may not use `new_external_source_research: false` merely because the current record already contains sources.

Evidence search is not permission to inflate the record. Add a source only when it materially supports occurrence facts, evidentiary limits, external assessment, harm or another canonical field. Preserve claim-relative evidence status.

A source may be removed only when the manifest records the source and an explicit reason such as duplication, wrong occurrence, inaccessible/non-verifiable replacement, or demonstrated unreliability.

### Wording-dependent evidence

Apply **Wording-dependent evidence and chronological source clauses** in `vigil/MAINTAINERS.md` whenever the adjudication depends materially on the words used. Preserve the exact decisive passage, its attribution and surrounding task context in the relevant source clause. Preserve the source-supported sequence through the receiver response and later consequences. Several propositions in one passage remain one event; separate responses remain separate events.

Review source fidelity and occurrence order together. A quote-led rewrite that loses the event sequence is incomplete. A chronological paraphrase that removes the words on which the adjudication depends is also incomplete. If the transcript is unavailable, label the available attributed report and bound the conclusion rather than reconstructing dialogue. Each relevant taxonomy rationale must identify the decisive words, explain their significance and state the observed conduct or precise missing recognition fact.

## 3. FACTUAL RECORD — write facts before diagnosis

Rebuild `summary` and `vigil_assessment.factual_basis` from the evidence before performing taxonomy adjudication.

- `summary` is the rich lay occurrence narrative.
- `factual_basis` states what the preserved evidence establishes, corroborates, disputes and leaves unresolved.
- Neither field should be compressed merely to make the record shorter.
- Material chronology, actors, systems, actions, outcomes, quantities and uncertainty must survive the rebuild when supported.
- Governance diagnosis, taxonomy labels and severity reasoning belong in their governed fields.

If a rebuild materially shortens the baseline `summary` or `factual_basis`, the adjudication manifest must explain why the reduction is a fidelity improvement rather than information loss.

### Occurrence-environment adjudication

Adjudicate the four occurrence-environment dimensions independently from the cited occurrence evidence:

1. `deployment_state` asks whether the materially participating model or system was actually in operational or public deployment: `pre-deployment`, `deployed` or `unknown`.
2. `activity_contexts` records evidenced `training`, `evaluation`, `research` and/or `operational-use`; use multiple values only when each is established, and use `unknown` alone when the activity cannot be established.
3. `external_reach` asks whether the activity remained `contained`, materially reached real external systems, services, people or data (`live-external`), or is `unknown`.
4. `activity_actor` records who conducted training, evaluation or research. It replaces the narrower testing-actor concept because non-operational activity is not limited to testing.

Do not infer deployment from external reach. Public-internet access, interaction with a production website, real-world harm, consumer-origin data, provider identity and a deployed sibling product do not prove that the participating model was deployed. A provider-internal training agent may therefore be `pre-deployment`, `training`, `live-external` and `provider-internal`. Conversely, ordinary use of an evidenced released product is `deployed` and `operational-use`, while its external reach is still adjudicated separately. Preserve `unknown` for any unsupported dimension rather than using external consequences as a lifecycle proxy.

## 4. TAXONOMY — retrieve, test and adjudicate

Taxonomy classification is a separate analytical pass.

For a full rebuild the maintainer must:

- load the current canonical VIGIL Failure Taxonomy, not remembered labels or an older branch copy;
- inspect the complete current class set at least once before selecting candidate classes;
- recover every baseline mapping before considering deletion;
- test candidate classes against their technical definition, recognition criteria and exclusions;
- test nearby/distinguishing classes where the taxonomy itself identifies a boundary;
- adjudicate each mapping independently as `failure-occurrence`, `successful-invariant` or `ambiguous-boundary`;
- keep consequence/severity reasoning out of taxonomy membership;
- allow the Incident to remain unclassified when the mechanism is not evidenced.

### Source-first adjudication sequence (including held Boundary mappings)

Apply this sequence to a substantive re-adjudication, even when the assignment begins with one existing Boundary or proposed removal. A Boundary-population review is not evidence that the complete Incident was adjudicated. Use the **entire affected Incident and material chronology**, not just the preselected mapping and its rationale.

1. **Recover the occurrence:** Re-read source records, chronological episodes, material decisions, corrective actions and consequences. Search for relevant primary artefacts and later reporting where a decisive fact is reasonably recoverable. Record specific searches, what was found, and what remains genuinely inaccessible. The absence of a fact from the preserved packet does not establish its absence from the occurrence. Apply the temporal non-erasure test below wherever a later outcome might be mistaken for evidence that the earlier governed action was correct.
2. **Discover before comparing:** Independently articulate each material governance property demonstrated, preserved or left genuinely indeterminate by the evidence **before using existing VIGIL mappings as a candidate shortlist**. Consider separate properties operating in the same episode, including failed verification, inappropriate reliance, authority promotion and source/lineage distortion where evidenced. Do not assume that these examples apply in every case.
3. **Test the taxonomy:** Inspect the complete version-pinned selectable class set and identify *all* materially plausible classes for those properties, including classes previously omitted. Apply each class's literal necessary conditions and exclusions at its own governed level. A neighbouring class is not an automatic exclusion. Where an exclusion says another mechanism is sufficient, explain why the other class fully accounts for the distinct property rather than merely naming it.
4. **Check negative findings:** Before proposing Boundary, no mapping, or removal, name the specific unestablished necessary condition or satisfied exclusion and seek reasonably accessible evidence that could resolve it. Do not demand model scores, hidden implementation details or root-cause localisation unless the class actually requires them. Separate uncertainty about *whether the governed property failed* from uncertainty about *why or where it failed*. A supported failure is not Boundary simply because the implementation cause is unknown.
5. **Preserve uncovered governance properties:** When the evidence materially establishes a governed integrity property not faithfully represented by any selectable class, retain a reasoned `taxonomy-gap` disposition. It need not name a new class. Reconcile relevant prior gap findings and unadmitted proposals as research history; neither silently discard a material gap nor treat a proposal as selectable.
6. **Reconcile only after independent analysis:** Compare the resulting evidence-to-class assessment with every previous mapping, relevant per-Incident review and materially similar Incident. Record retained, changed and rejected decisions and any newly discovered applicable classes in the decision packet. Reconcile episode relationships and dependencies on external requirements, HIM and the integrated interpretation without modifying those independent results outside the authorised scope.

A reviewer who cannot finish a decisive evidence search or condition assessment must record an **explicit incomplete review or evidence hold**, not present an unsupported negative decision as final. Do not escalate routine interpretive disagreements to the maintainer. Escalate only an irreducible evidentiary hold, a needed change to taxonomy authority, or an edit outside the authorised scope.

The dated per-Incident **working** packet records actual reasoning and research for this adjudication campaign. It is a staging aid, not an answer key, mandatory Incident-by-class matrix, replacement for source-first adjudication or permanent release artefact. At closeout, transfer the material findings/limits to the Incident and reusable methodology to `docs/maintenance`, then retire the packet under the review-notice-board policy. No test, validator, class, schema or publication rule is changed by this instruction.

### Reproducible classification decision packet

For each materially reviewed **existing mapping** and independently plausible new or no-mapping candidate, record a dated, occurrence-specific decision before editing canonical text. Use the per-Incident manifest or dated audit (not a global Incident-by-class dataset), and keep the accepted, concise result in the canonical mapping and clause fields.

The minimum decision packet is:

1. **Pinned inputs:** Incident baseline commit and version; exact taxonomy version and reference; tested class ID; previous mapping role, confidence and basis (or no prior mapping). Never substitute the newest taxonomy wording for the earlier decision without marking the version difference.
2. **Evidence claims:** the precise episode IDs, source refs, decisive observed or attributed facts, source access limits and contrary evidence. Separate the source's report of an event from its theory of why the event happened.
3. **Class test:** literal, version-specific text of every relevant success/failure required condition and exclusion; for each condition state `established`, `contradicted` or `unknown`, with evidence references and missing decisive fact. Current recognition entries do not have immutable condition IDs, so identify them by their quoted text and pinned taxonomy ref; do not treat an unversioned array position as an identifier.
4. **Abstraction and neighbours:** apply minimum sufficient evidence at the class-defined governance level. Test materially adjacent classes and identify the distinct additional condition that each would require. Do not invent hidden implementation requirements.
5. **External interpretation and VIGIL divergence:** separately report relevant external conclusions and the prior VIGIL interpretation. Explicitly decide whether each material difference survives, needs correction or remains unresolved, and explain the **recognition/evidence** reason, never institutional prestige or silence.
6. **Proposed outcome:** `failure-occurrence`, `successful-invariant`, `ambiguous-boundary`, `resolved-no-mapping`, `unresolved` or `taxonomy-gap` as appropriate to the class mapping versus episode layer. State the mapping disposition, confidence, occurrence-specific mapping basis and distinct episode-relationship rationales; keep different record-layer statuses separate.
7. **Preservation:** compare prior/new mappings, evidence, rationales, aggregate explanation and mixed episode outcomes; check independent external assessments, external-requirement derivations, HIM and review history for collateral change. An unchanged mapping can still have a materially rewritten basis; account for that rewrite explicitly.

A Boundary requires positive evidence engaging the class invariant with unresolved outcome polarity; mere topical similarity or failure to prove either polarity does not qualify. All required failure or success conditions must be established for the corresponding role. External disagreement or inaccessible vendor internals are not automatically missing required conditions. Conversely, demonstrably missing recognition evidence must not be filled by VIGIL's prior preference.

**Order:** adjudicate from the source packet and canonical criteria first, then compare the proposed answer with the prior VIGIL record and relevant external interpretations, then write an evidence-grounded revision. This reduces anchoring on either a prestigious external conclusion or the previous VIGIL answer. If source context or taxonomy version is insufficient to decide a required condition, hold that candidate without rewriting it as a stronger or weaker proven finding.

This is a review protocol, **not** an automated semantic verdict. The manifest template offers a machine-readable expression of these decisions for future API use, but the current rebuild guard does not yet require its new fields. No new permanent validator or canonical schema requirement arises from this documentation alone.

### Decision integrity: exclusion, recognition and completion

These are adjudication **reasoning steps**, not code-based classifications or new taxonomy conditions. Apply them before proposing **any** canonical mapping role, including a retained Boundary or success.

**Exclusion before role:** Evaluate each literal version-pinned exclusion as a proposition about this occurrence, with its own source/episode support and one of `established`, `contradicted` or `unknown`. If an exclusion is established, it defeats the corresponding class mapping (including Boundary); do not preserve the class as Boundary just because a related invariant is salient. In particular, an exclusion explicitly defined in terms of an *unresolved condition* must be evaluated against the actual unresolved evidence state, rather than misread as a reason to admit Boundary. An unknown potentially decisive exclusion remains a pending candidate review, not an assumed clean pass. Do not use a different class as an exclusion unless the literal exclusion applies and its stated sufficiency or scope is demonstrated.

**Condition-specific proof:** For every proposed failure or success, assess *each* necessary recognition condition independently: quote its exact text; give its individual `established`, `contradicted` or `unknown` finding; identify the specific fact and source/episode proving or limiting **that particular condition**, and address contrary evidence. One repeated aggregate classification basis across all conditions is **not** evidence that each condition was tested. One source may support several conditions, but the inferential explanation for each must be distinguishable. For success, show the full required protective pathway and effects, not simply a favourable ending. For failure, distinguish the observed breached governance property from speculation about internal causes. Reassess exclusions after gathering relevant evidence, before deciding the role.

**Disposition logic:** A failure or success requires its respective necessary conditions established and no operative exclusion. A canonical Boundary requires positive class engagement, unresolved polarity and **no operative exclusion**; it cannot be used to store a class defeated by its exclusion. Where the governance property is plausible but a required admission fact is unavailable, preserve the candidate and precise missing fact in the working packet **and in the material canonical clause disposition**; use clause-level `unresolved` where appropriate, rather than inventing a canonical mapping. If no selectable class faithfully captures an evidenced material property, preserve a `taxonomy-gap`. Do not equate outcome harm alone with a particular class or require root-cause localisation where the class does not.

**Completion reconciliation:** Check Temporal Integrity of Adjudication for every materially corrected or remediated episode, preserving original conduct, later decision, proven implementation and consequences separately. At the end, separately state (a) whether the *listed* clauses have completed dispositions (the meaning of the canonical `adjudication_coverage.status`), and (b) whether the **substantive Incident adjudication** finished source research, episode coverage, independent candidate discovery, condition-specific tests, exclusion resolution, comparators, prior-findings reconciliation and affected downstream dependency review. These are not equivalent. Resolve contradictory packet statuses before presenting a final adjudication. A packet labelled `pending`, `initial`, `not-reviewed` or with an outstanding decisive step cannot simultaneously claim substantive completion. Record outstanding work and its actual effect; an evidence-limited review can finish with explicitly bounded conclusions, but cannot claim to have completed research or checks it did not do.

### Temporal Integrity of Adjudication — maintainer-approved, 20 October 2026

**Normative reasoning rule (all Fidelity Classes):** A later appeal, correction, reversal, intervention, safeguard activation, recovery, restoration, withdrawal or successful remedy **MUST NOT** retrospectively erase, neutralise or relabel an independently supported earlier failure. Conversely, the existence of a later reversal, complaint or repair does not *automatically prove* an earlier failure. Test the original governed act against the **version-pinned recognition conditions and exclusions applicable to that episode**, using all legitimate evidence available to the reviewer, including later evidence that clarifies the original act. **Do not substitute the eventual trajectory's favourable or unfavourable ending for the recognition test at the relevant decision point.**

When a material intervention or correction is evidenced, explicitly separate and independently adjudicate:

1. **Original governed conduct or decision:** who acted, when, under which independent authority, obligation and context; what was materially done, withheld or omitted; and which success/failure conditions and exclusions were established **for that decision**.
2. **Challenge, appeal, intervention or recognition of error:** what a later decision actually established about the earlier conduct. A later authoritative finding may supply evidence of the original entitlement or impropriety; do not turn external legal conclusions automatically into VIGIL's taxonomy outcome.
3. **Remedy ordered or attempted versus remedy completed:** distinguish a direction to produce, rollback, restore, notify, compensate or correct from verified implementation. Test a later `successful-invariant` **separately**, only where its own necessary conditions and relevant effects are affirmatively evidenced.
4. **Residual and materialised consequences:** review delay, lost access or work, costs, rights and other effects on their own evidence and under VIGIL-HIM. A later successful remedy does not cancel already materialised harm. Do not infer costs or harm simply because there was litigation or a dispute.
5. **Cross-episode non-erasure:** preserve earlier and later findings in source order; an aggregate mapping or explanation must not convert an earlier failure into success solely because correction succeeded, nor claim later success solely because the original problem was recognised. Where evidence does not decide a stage, name the **specific** unknown rather than collapsing the stages into one Boundary.

**Mandatory adjudication check:** Before finalising any candidate success, failure, Boundary or mapping removal where later corrective action exists, answer: *Am I using evidence of an appeal, eventual outcome, remediation or restoration as a shortcut for testing the earlier decision? Have I confused an order/offer/attempt with verified delivery? Have I preserved any independently supported earlier failure and any distinct later success without conflating them?* Record the relevant episode and source references and the answer in the dated per-Incident decision packet or manifest; the canonical Incident keeps the concise accepted episode-specific reasoning, not this process transcript.

**INC-008 — concrete regression example (State v Arteaga, facial-recognition discovery):**

- **Earlier decision (E004):** the defendant sought 13 categories of non-public facial-recognition material; two were provided and the trial court did not compel the other eleven. The later appellate decision establishes a bounded discovery entitlement and reverses the original denial. Under revised **FC-045 Authorised Investigative Evidence Access** (v0.8.1), the earlier operative withholding is separately supported as a **failure-occurrence** within an existing discovery pathway. The availability of appellate review is *not* itself success at the original access decision.
- **Appellate correction (E005):** the appellate court reversed/remanded for production, potentially subject to protective orders or in-camera review. This is evidence of a corrective **order**, not evidence that the ordered materials were actually produced, inspected, preserved or placed under completed custody safeguards. Do **not** assign a later FC-045 success merely from the order.
- **Consequences:** whether, and to what extent, additional costs, delay or other harm materialised must be independently supported by source evidence and the applicable HIM method; neither court involvement nor eventual correction proves a particular financial or psychological harm band.

This is a **general reasoning regression example**, not a permanent incident-specific test assertion or an automatic permission to rewrite INC-008. The v0.8.1 dated [FC-045 occurrence-level reassessment](../reviews/2026-10-20-fc045-fc079-followup/FC-045-INC-008-INC-109-REASSESSMENT.json) recommends changing the earlier canonical FC-045 Boundary to a supported failure for E004, preserving its previous mapping and keeping the E005 completion question unresolved. That mapping change requires its own authorised canonical edit and validation. If newer evidence materially changes the source/criterion assessment, re-adjudicate rather than preserving this illustrative outcome as immutable doctrine.

**Contrast cases (not automatic verdicts):** a truly justified original withholding may remain valid even when reviewed on appeal; a verified later repair may independently satisfy a success test while an earlier failure remains; a nominal or merely ordered repair is not verified completion. Apply the relevant class-specific criteria in each case.

### Finite evidence-limited review and cross-case candidate closure

When several Incidents leave plausible candidates unadmitted, **review the shared recognition question together**, using the current class abstraction, version-pinned exclusions and comparable successful/failure cases. Do not infer one Incident's answer from a neighbour's outcome: apply the agreed distinction independently to each episode. This is a completion step under existing authority, not a request for a new taxonomy class or a blanket mapping outcome.

Distinguish **research completion** from **recognition certainty**. After a targeted search of reasonably accessible decisive sources, a candidate may have a *completed, evidence-limited non-admission* because a required condition is not established. That does **not** establish the opposite historical fact and does not erase other proven governance findings. Retain searched-source process detail in the temporary review packet while working; put the material missing fact, source limitations and any meaningful reopening condition in the canonical Incident before packet retirement. Reserve an *actionable pending task* for a specifically identified source, permissible investigation or precise recognition-scope decision that could materially change admission; state who or what can resolve it. Do not carry an indefinitely pending research task merely because unpublished internal details might theoretically exist. An inaccessible fact can remain substantively uncertain in the canonical clause relationship without falsely marking the research pass unperformed.

Do not misstate **lack of evidence for a positive link** as affirmative evidence that the opposite mechanism occurred. Where an exclusion is expressly written as an evidence-state threshold (for example, an observed effect *without an established mechanism link*), apply that threshold to the inspected record but name the evidentiary limit; do not claim that the mechanism is proven absent. If a class's literal conditions or exclusions actually cannot express a materially evidenced governance property, retain the correct independently supported classes and flag the exact taxonomy-scope question through the existing Gate process. Neither overrule literal recognition requirements for a desirable outcome nor fabricate additional requirements to reject an uncomfortable one.

Before reporting a batch as complete, reconcile the count of **final supported mappings**, **completed evidence-limited non-admissions**, **actionable pending investigations**, and **taxonomy-scope referrals**. Preserve their separate meanings rather than reporting all non-admitted candidates as unfinished adjudications. Human maintainers decide genuine taxonomy-authority amendments, not ordinary case-by-case evidence interpretations.

### Prior-mapping disposition rule

Every taxonomy mapping present in the baseline must appear in the adjudication manifest with exactly one disposition:

- `retained`;
- `role-changed`;
- `confidence-changed`;
- `role-confidence-changed`;
- `superseded`; or
- `removed-unsupported`.

`superseded` and `removed-unsupported` require a substantive reason. `superseded` must identify the replacement class or classes.

Any class newly added to the candidate record must appear in `new_taxonomy_mappings` with its evidence-bounded rationale.

A missing baseline mapping with no disposition is a rebuild failure.

### Mixed relationships are valid

An Incident may simultaneously contain failure occurrences, successful invariants and ambiguous boundaries. Do not collapse a mixed Incident into a single “good” or “bad” label. A class-level failure mapping may coexist with a later bounded success for that same class at a distinct episode. Preserve both episode outcomes and their source-local rationales; do not force all episode roles to match the Incident-level class role. Apply **Temporal Integrity of Adjudication**: subsequent remedy, appeal or restoration does not retrospectively erase a prior supported failure, and remedial success must be affirmatively evidenced rather than inferred from an order or attempt. Verify that the aggregate explanation does not silently lose either materially supported finding.

`VIGIL-INC-000129` is the design exemplar for this property: its value is that different taxonomy boundaries can have different roles in the same bounded occurrence. It is not a permanent answer key, and its current class set may itself be re-adjudicated through this workflow.

### Clause-level taxonomy adjudication

Review every materially relevant event against the current selectable Fidelity Classes, using their invariants and success/failure recognition conditions. Do not infer a successful invariant merely because failure was not observed. Preserve full literal-condition tests and broad rejected-class comparisons in the temporary adjudication manifest while screening. Carry materially relevant negative-candidate reasons into the canonical clause decision before retiring that manifest; never create a global Incident × class table.

For each material source clause, record `mapped`, `resolved-no-mapping`, `unresolved` or `taxonomy-gap`. Record the evidence and the exact missing recognition fact for unresolved candidates. The derived `taxonomy_classification.adjudication_coverage.status` is `partial` when any material clause remains `unresolved` or `taxonomy-gap`; otherwise it is `complete`.

Only canonical relationships belong in `taxonomy_classification.primary_classification` and `secondary_classifications[]`. `taxonomy_relationships[].canonical_taxonomy_mapping` distinguishes these from noncanonical candidates. A canonical mapping uses one of `failure-occurrence`, `successful-invariant` or `ambiguous-boundary`. The three roles have different evidentiary recognition tests.

For canonical Stage 02 role parsing, `failure-occurrence` and `failure-occurrence contribution` indicate the failure role, `successful-invariant` indicates the successful role, and `ambiguous-boundary` or the compatible label `ambiguous-boundary exemplar` indicate the ambiguous role. Legacy free text such as `canonical failure mapping` must not be guessed into a role.

Map each material event once in activity order, allowing several independently justified Fidelity Class relationships to analyse the same event. Review recorded omissions and attempts as well as realised outcomes. Reconcile all position-based clause references if clauses are reordered or split. A candidate taxonomy role may remain unresolved without blocking unrelated, supported mappings.


### Named-control requirement for FC-000038 and FC-000083

A substantive ethical, relational, agency or vulnerability-protection failure is not evidence that an operational safety control was deployed or failed. Assess the applicable substantive fidelity invariant separately from any concomitant governance-control mechanism. Use the current canonical Fidelity Classes only; draft proposals are not selectable.

For **FC-000038 Required Control Activation**, an admitted failure occurrence must identify and substantiate:

- the **particular evidenced operational control or sufficiently identified applicable protective-control posture** and its protective purpose (for example, a deployed gate, operational restriction or escalation route), not merely the external standard or an abstract duty calling for protection; the exact hidden classifier or code component is not required unless the class itself requires it;
- the control's **defined activation condition**, contemporaneous deployment/applicability, and the occurrence evidence establishing that the condition arose before the governed effect;
- the **observed nonactivation** of that control before the relevant output, action or transition, independently of later harm; and
- the specific governed effect that proceeded without activation.

For **FC-000083 Control Effectiveness Integrity**, establish that the particular applicable control **validly activated**, identify its protective purpose and required effect, and provide evidence that the observed effect was materially inadequate in the relevant hazard and evidenced protection context. Nonactivation, unknown control existence, and missing protective design are not FC-000083 failures.

If the evidence does not sufficiently establish the applicable control or protective-control posture, existence, availability, applicability, valid trigger, activation or effect required by the class, record the precise missing fact as an unresolved candidate in the dated rebuild manifest. Do not infer it from severe harm, source prestige, a later standard, a model-policy assertion, or an observed unsafe answer. If evidence supports a substantive duty but **no operational control was implemented**, preserve that as a distinct protection-coverage/taxonomy-gap question rather than forcing FC-000038/000083.

Multiple independently substantiated mappings may analyse the same evidence episode. Never duplicate that episode to express multiple interpretations. A new candidate class becomes available for canonical Incident mapping only after its governed taxonomy admission and versioned release. The superseded 10 October relational/vulnerability design proposal is recoverable in Git history; its now-admitted class recognition conditions are governed by the canonical FF-0009 definitions for FC-086 Relational Boundary Fidelity and FC-087 Vulnerability-Responsive Protection Fidelity. No earlier speculative IEEE relationships are admitted by that historical proposal.

## 5. HARM — determine pathway before assessing severity

Re-open VIGIL-HIM only after the factual record is stable. Review all **twelve** dimensions for current HIM 1.1.0 (use the applicable eleven for an unchanged historical HIM version). Search for later consequence evidence in a full rebuild. Do not derive severity from taxonomy, notoriety, capability, source prestige or hypothetical worst-case outcomes.

For every **new or substantively reopened HIM 1.1.0** assessment, perform the mandatory Aggregate Harm route-first screen, and record `harm_impact_assessment.aggregate_harm_screening` with deployment, potentially generalisable mechanism, bounded actual harmed case, applicable dimensions, source references and reasoning. The test is **not** whether the source contains one user's screenshot or whether model-wide prevalence has already been proved. A user-observed output may establish a potentially generalisable feature/system mechanism. If deployment and such a mechanism are supported and **no actual particular harmed person/group/asset/institution case is being assessed**, select `generic_deployed_evaluation` even if the eligible cohort, reproducibility or collective consequence are not yet sufficient to assign an Aggregate Harm band. Record SU and the precise missing scoring facts when appropriate. A particular actual harmed case instead requires `specific_consequence`. Do not aggregate user reports into assumed victims or bypass specific-consequence adjudication to obtain a higher score.

The validator checks the screening-to-pathway relationship **when the structured screen is present**. Historical accepted records without it are not automatically rewritten or made invalid; report routing candidates and obtain MAINTAINERS Gate 2 authorisation before modifying their HIM, taxonomy or interpretive provenance. For the decision tree and calibration gates, use `vigil/docs/incident-severity-standard.md` and the governing `vigil/methodologies/VIGIL.HarmImpactMatrix.v1.1.0.json`.

If the rebuild is taxonomy-only, record that Harm Impact was deliberately not reopened and preserve the prior assessment unchanged.

## 6. INTERPRETATION + VALIDATION — integrate only after the governed passes

Write `vigil_assessment.significance_to_cam` and `vigil_assessment.governance_interpretation` after evidence, taxonomy and harm adjudication are stable.

The conclusion should integrate the bounded occurrence, evidentiary limits, taxonomy relationships and materialised consequences without turning uncertainty into fact.

Before accepting a rebuilt Incident:

1. complete an adjudication manifest based on `vigil/templates/incident-rebuild-adjudication-template.json`;
2. run the rebuild guard against the baseline and candidate;
3. run the ordinary VIGIL builders and validators;
4. inspect the generated/public projection for information loss or role collapse;
5. check each affected mapping's original and revised rationale against the source episode, criteria, exclusions and any documented independent VIGIL interpretation, including mixed-role findings and the aggregate explanation;
6. confirm unchanged HIM, external assessment results, source history and review history unless separate evidence and scope justify their modification.

Example:

```bash
python vigil/scripts/validate-vigil-incident-rebuild.py \
  --baseline-ref main \
  --candidate-file vigil/records/incidents/VIGIL-INC-000129.json \
  --manifest /tmp/VIGIL-INC-000129-adjudication.json

python vigil/scripts/build-vigil-public-records.py
python vigil/scripts/validate-vigil-records.py
python vigil/scripts/validate-vigil-public-records.py
python vigil/scripts/validate-vigil-source-provenance.py
python vigil/scripts/validate-vigil-interpretive-provenance.py
python vigil/scripts/validate-vigil-system-components.py
python vigil/scripts/validate-authorship-provenance.py
```


## GitHub Issues for unresolved actionable follow-up

GitHub Issues in `CAM-Initiative/Vigil` are the sole durable queue for **new** VIGIL follow-up tasks. The Incident is the evidentiary/adjudicative record; a dated review is temporary working history retained through Git when retired; an Issue identifies the next concrete action. Do not send Gmail queue emails for new actions.

### When an Issue is justified

A positive or negative classification, a defensible Boundary, `resolved-no-mapping`, `unresolved`, `taxonomy-gap`, partial coverage, or a recorded evidence limitation does **not** automatically require an Issue. GitHub Issues are **not an extension of VIGIL adjudication**. The canonical Incident and its dated decision packet are the appropriate home for uncertainty, evidence limits, confidence disputes and irresolvable unknown internal state.

**Open an Issue only if all conditions are true:** (1) there is a concrete task distinct from ordinary adjudication and its authorised review; (2) a realistic route exists to execute it with available people, scope, information and access; (3) completion can be verified objectively; and (4) it is genuinely a separate backlog task rather than a necessary step or discussion within the current PR. Where the task is part of the authorised PR, record and track it **in that PR**. If its decisive information is inherently private or inaccessible, record the bounded unknown and stop: do not manufacture an issue whose closure requires vendor-internal classifier logs, prompt traces, model weights, undisclosed authorisations or allowlist membership.

Use one primary category: `taxonomy-gap` (a independently actionable, generalisable boundary/design repair rather than merely an unresolved candidate); `evidence-required` (a **known reasonably recoverable** decisive public/authorised source outside the current review scope); `record-maintenance` (a distinct fixable source, episode, record, requirement or cross-record defect); `system-improvement` (a separately scoped workflow, schema, validation or website change). Taxonomy issues must explain the evidenced invariant, nearest classes and their recognition/exclusion limits. Do not opportunistically amend taxonomy to close an Issue.

**Negative example — INC-117:** private Hugging Face/Anthropic per-request cyber-classifier decisions and July allowlist status may remain unknown. The first-party account and pre-incident provider policy support the bounded event analysis. Because there is no reasonable independent route to recover those internals, they are recorded as Incident-level limitations, **not** a permanent GitHub Issue. Issue #163 was closed as `not planned` because its creation improperly turned these facts into a work queue entry; that closure does not resolve or negate the Incident's classification.

A genuinely novel, actionable and separate issue may arise later if a specific public artefact becomes retrievable or a reusable system defect is evidenced. Do not reopen an Issue simply because a recorded uncertainty persists.

### Mandatory deduplicated staging protocol

1. Check current `main`, the authorised branch, relevant PRs, and open **and closed** Issues for changed or already-resolved state.
2. Search by Incident/episode IDs, Fidelity Class/requirement IDs and synonyms for the mechanism. A different title is not evidence of a new task.
3. If a relevant Issue is open, update it with the new evidence and context without deleting other subtasks. If a matching Issue is closed, examine its resolution and only propose reopening for genuinely new outstanding evidence.
4. If and **only if** the four issue-admission tests above pass and no matching active Issue exists, create one using `.github/ISSUE_TEMPLATE/vigil-follow-up.md`: specify category, affected IDs, public evidence, exact independently actionable repair, realistic access/owner, relevant taxonomy/standards version, branch/ref, required approval and verifiable closure condition. Do not paste private mailbox contents or sensitive sources into public Issues. If the tests fail, document that this is an **Incident evidence hold, not an Issue**, without staging a ready-to-file payload.
5. Only for an admitted, independent Issue, link its number/URL from the dated review manifest's `escalation` or new-entry completion audit's `outstanding_actions`, and give its status in the per-record completion report. Otherwise retain the real evidentiary limit in the Incident/review without inventing an escalation. Do not put issue-tracking data in canonical Incident interpretations.
6. If GitHub is unavailable, retain the ready-to-file Issue text in the dated audit and report `GITHUB ISSUE STAGING NOT COMPLETED`. Do not claim it was created and do not fall back to Gmail.
7. No Issue is a maintainer approval. Preserve all existing Gate 1/Gate 2 limits, branch holds, human decisions and publication restrictions.

Describe outcomes in the completion report as `record_ready`, `record_ready_with_follow_up` or `record_blocked` (reporting terms, not new canonical schema values). Only validated, authorised records may be prepared for publication.

### Historical Gmail transition — **exactly once**

The former labelled `[CURRENT VIGIL QA ACTION]` Gmail snapshot is a legacy migration source, **not** an ongoing feed. Perform **one** separately tracked reconciliation per historical queue against current canonical records, working branches, existing Issues and recorded supersessions; create or link only distinct outstanding tasks. Document each item as migrated, already tracked, resolved, superseded or excluded, with reasons, in a dated migration audit. Do not copy old emails verbatim to public GitHub.

After the migration audit is marked complete, **never re-scan or re-migrate Gmail as part of normal Incident processing**, and never keep Gmail and GitHub Issues as parallel queues. Later corrections to a migrated item are made on its linked GitHub Issue. The remaining evidence-of-completion check is tracked in GitHub issue #147. Until a dated item-by-item migration audit is located or completed, do not claim the legacy backlog has been transferred.

## Review modes

Use `full-rebuild` for the current corpus refactor/rebuild and for any work that reopens factual evidence, taxonomy or harm.

Use `bounded-edit` only where the work scope is explicitly narrow, such as prose separation, metadata normalisation or a single-source correction. A bounded edit must preserve governed fields outside scope and still account for any taxonomy or source change it makes.

A maintainer must not describe a full re-adjudication as a bounded edit merely to avoid evidence or taxonomy review.

## Stop conditions

Stop the rebuild and escalate rather than guessing when:

- the current taxonomy cannot be loaded;
- primary evidence is inaccessible and the classification depends on it;
- two candidate classes remain materially indistinguishable after recognition/exclusion review;
- the record appears to combine multiple distinct occurrences that require re-bounding;
- a source or mapping would need to be removed without a defensible reason;
- the candidate record becomes materially less informative than the baseline without a fidelity justification; or
- the evidence supports harm but not the mechanism needed for taxonomy classification.

The correct result may be a richer unclassified Incident. Classification is not a completeness metric.

## Canonical Boundary adjudication — approved 19 October 2026

Every admitted `ambiguous-boundary` primary or secondary taxonomy mapping MUST contain a completed `boundary_adjudication` object in the Incident itself. A dated audit packet is supporting review history, never a substitute for the canonical explanation. Use `vigil/templates/boundary-adjudication-template.json`; the authoritative shape is `boundary_adjudication_contract` in `vigil/VIGIL.Schema.json`.

The object records `taxonomy_version`, positive `material_engagement`, non-empty `unresolved_conditions`, `diagnostic_reasons`, `decisive_blocker` and `resolution_requirements`. Each unresolved condition records its `polarity` (failure-occurrence or successful-invariant), literal `condition`, occurrence-specific `assessment`, and resolvable `source_record_refs` and `episode_refs`. Explain why neither outcome is established; do not assume a failure-side unknown proves success or vice versa. Historical taxonomy metadata remains separate from the version applied in this adjudication.

Permitted diagnostic reasons are `insufficient-evidence`, `conflicting-evidence` and `recognition-criteria-insufficiency`, including multiple contributing reasons. Identify the precise missing fact and potential resolving source, incompatible evidence and needed reconciliation, or criteria deficiency and separate taxonomy review. Unsupported class engagement is a candidate for removal or alternative disposition, not a completed Boundary. Review not performed is an audit hold, not a completed adjudication. These reasons explain the existing role; they are not additional canonical classification roles.

The validator rejects absent/incomplete objects, invalid reasons and unresolved source/episode references. It cannot certify that prose is substantively correct or that all relevant criteria have been examined. Boundary mappings require completed boundary_adjudication and must omit classification_confidence. Failure-occurrence and successful-invariant mappings require classification_confidence (low, medium or high) and must omit boundary_adjudication. On a role change, preserve the previous mapping and superseded values in dated review history before removing role-inapplicable fields from the current mapping. Historical confidence is provenance, never a current Boundary rating. Keep complete criterion matrices, rejected candidates and review process history in audit packets. The canonical object contains accepted occurrence-specific reasoning only.

Approval covers this control, documentation, templates and isolated tests. After implementation run the corpus read-only and report exact failures. Do not mechanically fill objects, reclassify findings, change recognition conditions or amend independent assessments. Substantive corpus repair remains subject to explicit maintainer authorisation. This requirement supersedes earlier audit-only placement of Boundary diagnostic reasons. Website display is separate renderer work; no presentation or builder change is authorised here.
