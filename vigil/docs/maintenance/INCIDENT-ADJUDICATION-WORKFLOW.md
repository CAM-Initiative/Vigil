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
- **Review/audit artefact = process history.** New accepted per-Incident source/mapping decisions, unresolved recognition facts and method provenance belong in a dated rebuild manifest or a focused current packet under `vigil/docs/reviews/`. Superseded historical campaigns may be retired to pinned Git history; they do not need a permanent live audit directory.

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

An Incident may simultaneously contain failure occurrences, successful invariants and ambiguous boundaries. Do not collapse a mixed Incident into a single “good” or “bad” label.

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

- the **particular available, applicable operational control** and its protective purpose (for example, a deployed gate, restriction, named classifier or escalation route), not merely the external standard or an abstract duty calling for protection;
- the control's **defined activation condition**, contemporaneous deployment/applicability, and the occurrence evidence establishing that the condition arose before the governed effect;
- the **observed nonactivation** of that control before the relevant output, action or transition, independently of later harm; and
- the specific governed effect that proceeded without activation.

For **FC-000083 Control Effectiveness Integrity**, establish that the particular applicable control **validly activated**, identify its protective purpose and required effect, and provide evidence that the observed effect was materially inadequate in the relevant hazard and evidenced protection context. Nonactivation, unknown control existence, and missing protective design are not FC-000083 failures.

If the control's identity, existence, availability, applicability, valid trigger, activation or effect is unproved, record the precise missing fact as an unresolved candidate in the dated rebuild manifest. Do not infer it from severe harm, source prestige, a later standard, a model-policy assertion, or an observed unsafe answer. If evidence supports a substantive duty but **no operational control was implemented**, preserve that as a distinct protection-coverage/taxonomy-gap question rather than forcing FC-000038/000083.

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
4. inspect the generated/public projection for information loss or role collapse.

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


## GitHub Issues for unresolved follow-up

**GitHub Issues are the canonical durable tracker for future VIGIL work.** An unresolved task belongs in the owning repository's issue tracker, not a repository review/approval-request file or authoritative self-email queue. Check existing issues before creating a duplicate; link the exact source commit, affected Incidents, relevant class/requirement scope, decisive evidence and constraints.

**Taxonomy action:** open or update an issue only when an evidenced material invariant cannot be faithfully represented by current class recognition conditions. Preserve the nearest classes tested, positive/exclusion criteria, exact missing conditions, comparators and whether the future decision is a new class, class-boundary change, family review or terminology repair. Keep current Incident uncertainty; an issue is not authority to create a Fidelity Class.

**Maintainer action:** track unresolved source/media/provenance recovery, cross-record repair, blocked evidence, occurrence re-bounding, external requirement extraction, deployment/repository integration, or control changes outside the edit's approval. Preserve exact success criteria and Gate 1/2 stop conditions. File cross-repository issues in the responsible repository and link back where useful.

Do not file issues or send mail to announce clean completion, unchanged assessments or green CI. When the action is completed within scope, use normal canonical provenance rather than inventing a backlog item.

Authorised operational email may notify the designated agent mailbox and link to the GitHub issue, but it is not a second authoritative task register. Existing Gmail QA-queue messages must be reconciled without silently discarding unresolved work; [issue #147](https://github.com/CAM-Initiative/Vigil/issues/147) owns that transition. Do not insert private messages, secrets or credentials into public issues. If GitHub access is unavailable, respond with **ISSUE NOT CREATED** and a complete ready-to-file issue payload rather than claiming the issue exists.


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
