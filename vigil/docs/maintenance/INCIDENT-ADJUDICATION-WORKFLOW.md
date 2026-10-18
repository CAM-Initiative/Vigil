# VIGIL Incident Adjudication Workflow

Status: maintainer contract

Applies to: substantive Incident rebuilds, refactors, re-adjudications and taxonomy migrations.

Also applies to the complete ordinary processing of every newly requested Incident.

## New-entry completion — maintainer instruction, 18 October 2026

A request for a new Incident authorises evidence research, source and duplicate/scope review, chronological material-episode analysis, current selectable-taxonomy consideration, all twelve current HIM dimensions, independent external-requirement review, public interpretation and provenance, appropriate authentic media, generated-output rebuilding and required validation. Creating the JSON record is an intermediate step.

Use `vigil/templates/incident-completion-checklist-template.json` as a dated **audit**, alongside the canonical record and any rebuild manifest. It is not a canonical field, schema amendment, validator or publication guard. A checklist is process evidence only when its references and specific decisions permit inspection. Never mark an unperformed pass reviewed.

Complete these passes:

1. Establish source identity/access, duplicate and occurrence boundaries. Search for primary evidence and later corrections. Keep different occurrences distinct.
2. Reconstruct all material source episodes in supported relative order. Retain exact decisive wording where available. Several statements in one passage can need separate adjudication without becoming separate events. Distinguish observed conduct from reported or hypothetical effects.
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
- **Review/audit artefact = process history.** Baselines, source and mapping dispositions, migration rationale, comparator work, repository repairs and validator history belong in the rebuild manifest or `vigil/docs/reviews/` and `vigil/docs/audits/`.

Do not repeat rejected-class or no-mapping inventories in an Incident's classification basis, mapping-local basis or external-assessment comparison. Repository workflow details—including branches, pull requests, validator repair and whether new research was performed—are not public Incident content. `diagnostic_provenance` is retired and forbidden on active Incidents. `classification_review_provenance` is compact metadata only: review date, reviewer, review status and, when one exists, a stable review reference. Detailed review history must remain outside that block.

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

An Incident may simultaneously contain failure occurrences, successful invariants and ambiguous boundaries. Do not collapse a mixed Incident into a single “good” or “bad” label. A class-level failure mapping may coexist with a later bounded success for that same class at a distinct episode. Preserve both episode outcomes and their source-local rationales; do not force all episode roles to match the Incident-level class role. Verify that the aggregate explanation does not silently lose either materially supported finding.

`VIGIL-INC-000129` is the design exemplar for this property: its value is that different taxonomy boundaries can have different roles in the same bounded occurrence. It is not a permanent answer key, and its current class set may itself be re-adjudicated through this workflow.

### Clause-level taxonomy adjudication

Review every materially relevant event against the current selectable Fidelity Classes, using their invariants and success/failure recognition conditions. Do not infer a successful invariant merely because failure was not observed. Preserve the reasons for rejected candidates and any broader class review in the dated adjudication manifest or audit, not a global Incident × class table.

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

Multiple independently substantiated mappings may analyse the same evidence episode. Never duplicate that episode to express multiple interpretations. A new candidate class becomes available for canonical Incident mapping only after its governed taxonomy admission and versioned release. The 2026-10-10 bounded design proposals and IEEE correspondence review are in `vigil/docs/reviews/2026-10-10-relational-protection-fidelity-class-review.md`.

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


## Gmail staging for unresolved action

The adjudication workflow has an explicit maintainer-output channel. When a rebuild establishes that unresolved work must occur outside the current Incident edit, the reviewing agent must stage that next action in Gmail rather than leaving it only in chat, a branch note or an ephemeral handoff.

**Do not use Gmail as a success, progress or no-change report.** A completed clean adjudication, an unchanged taxonomy, or consistency between canonical Incident classification and source-clause assessment requires no notification. Gmail is reserved for a genuine unresolved next action.

Two escalation classes use this channel:

### Taxonomy action required

Stage a taxonomy action when the occurrence contains a materially evidenced governance mechanism or invariant that cannot be represented faithfully by the current taxonomy without stretching an existing class beyond its definition, recognition criteria or exclusions.

Typical triggers include:

- no current class fits despite a well-evidenced mechanism;
- the same uncaptured mechanism recurs across more than one Incident;
- an existing class boundary is demonstrably too broad, too narrow or internally conflates distinct mechanisms;
- a recovered invariant has no corresponding current taxonomy boundary; or
- correct classification would require redefining an existing class rather than merely applying it.

Do **not** create or amend the taxonomy opportunistically inside the Incident rebuild. Finish the Incident as far as the current taxonomy permits, preserve the gap explicitly, and stage a taxonomy instruction containing:

- affected Incident ID(s);
- concise mechanism/invariant description;
- evidence supporting the gap;
- nearest current classes tested;
- why each current class is insufficient;
- whether the likely action is a new class, class-boundary amendment, family review or terminology repair;
- any cross-Incident comparators; and
- the exact branch/ref from which the instruction was generated.

### Maintainer action required

Stage a maintainer action when the rebuild cannot be completed safely without another task, including:

- a canonical Incident or Section 02 update that the adjudication shows is required but the current task is not authorised to perform;
- manual recovery of a source or artefact;
- occurrence re-bounding or possible retirement;
- unresolved branch-state conflict;
- inaccessible primary evidence that materially affects adjudication;
- a material cross-record consistency issue;
- a taxonomy ambiguity requiring separate taxonomy work;
- a source-provenance repair outside the current record; or
- another stop condition that should survive beyond the current chat.

If the required repair is completed within the authorised task and no unresolved follow-up remains, do not stage a Gmail action merely to report that it was fixed.

### Gmail queue protocol

The Gmail staging queue is the authenticated maintainer Gmail account emailing itself.

The authoritative action queue uses:

- subject prefix: `[CURRENT VIGIL QA ACTION]`;
- Gmail label: `VIGIL/CURRENT QA ACTION`.

When Gmail access is available, the reviewing agent must:

1. search Gmail for the latest message with the exact subject prefix and label;
2. read that current authoritative queue before writing a replacement;
3. merge the new action into the existing unresolved queue, removing an older item only when the record/branch state shows it has already been resolved;
4. send a new self-email with the same exact subject prefix and a current date;
5. apply the `VIGIL/CURRENT QA ACTION` label to the new message; and
6. state in the body that the new note supersedes earlier queue notes.

Do not send a one-item replacement that accidentally erases unresolved staged work. The newest labelled message is a complete queue snapshot, not an append-only fragment.

Do not create or replace a queue message merely because an adjudication batch completed or because the validator passed. A new Gmail queue message is warranted only when the unresolved queue materially changes: a genuine action is added, materially revised, or an existing queued action is resolved and therefore removed. An empty/no-op adjudication result is not a Gmail event.

Use explicit headings such as `TAXONOMY ACTION REQUIRED`, `MANUAL ACTION REQUIRED`, and `NO LONGER ACTIONABLE / RESOLVED` where useful. Each item must contain enough repository and evidence context for a later agent to act without reconstructing the originating conversation.

Do not put personal email addresses, credentials, secrets or connector identifiers into this public repository. The connector resolves the authenticated mailbox at execution time.

If Gmail access is unavailable, do not claim that staging occurred. Surface `GMAIL STAGING NOT COMPLETED` with the complete ready-to-stage instruction payload so a later connected session can send it.

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
