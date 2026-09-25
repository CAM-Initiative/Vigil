# VIGIL Maintainer Guide

## Active architecture

VIGIL's active public record corpus is Incident-only:

```text
vigil/records/incidents/
```

INC records preserve bounded occurrences, source evidence, occurrence-level diagnosis, severity, taxonomy classification and provenance. FM, OBS, RESEARCH, PROP, PATCH and LEARN are retired record classes. Their files, templates, generated indexes, routing rules, validators, lifecycle machinery and publication dependencies do not belong in the active tree.

Historical architecture remains recoverable through Git history and `stabilization/pre-fm-schema-migration`. Do not recreate an active-tree archive of retired records.

## Canonical Incident allocation and ingestion branch

`agent/incident-ecosystem-ingestion` is the single canonical allocation branch for new `VIGIL-INC-*` identifiers.

- Every newly allocated canonical Incident MUST originate on `agent/incident-ecosystem-ingestion`, regardless of whether the candidate was discovered by scheduled ecosystem ingestion, manual research, taxonomy work, feature development or another maintenance activity.
- Other branches MUST NOT independently allocate new `VIGIL-INC-*` identifiers. If work on another branch identifies a new Incident candidate, create the canonical Incident on `agent/incident-ecosystem-ingestion` first, then consume or reference that canonical ID from later work as appropriate.
- Existing Incidents may be amended on other branches where the maintenance task requires it, provided their stable IDs are preserved and ordinary schema, evidence and provenance requirements are followed.
- While `agent/incident-ecosystem-ingestion` exists, preserve its accumulated Incident work and continue appending bounded ingestion changes there. Do not recreate the branch from `main` merely because it is ahead of or behind `main`.
- When an ingestion tranche has been merged and the branch has been consumed/deleted, recreate `agent/incident-ecosystem-ingestion` from the exact current `main` head before allocating the next Incident.
- Incident-ID allocation should therefore check current `main` plus `agent/incident-ecosystem-ingestion`; scanning unrelated feature branches for speculative Incident reservations is not required under this contract. If a branch is found to contain an independently allocated new Incident, treat that as a maintenance-contract violation and reconcile it before further allocation rather than silently creating competing IDs.

Before opening a pull request from `agent/incident-ecosystem-ingestion`, synchronize it with the current `main` so the PR is based on the current canonical repository state. A deliberate pre-PR rebase of this dedicated ingestion branch onto current `main` is permitted for that synchronization step when no concurrent ingestion work is in flight and the branch is not already under review. Because rebasing rewrites branch history, use it only at this bounded pre-PR boundary and update the remote with lease-protected force semantics rather than an unconditional force push. Do not use rebasing, resetting or force-pushing as routine cleanup while the ingestion branch is accumulating work.

## Historical provenance

Legacy record classes and migration artefacts remain recoverable through Git history. Active Incident records contain only information required by the current VIGIL data model and must not carry retired payloads, migration-source metadata or retired-record links.

Do not falsify historical review dates or rewrite historical audits and reviews that accurately describe earlier repository states.

## Retained subsystem boundaries

- `vigil/records/incidents/` — sole active public record corpus.
- `vigil/taxonomy/` — canonical VIGIL Observatory alignment taxonomy and generated publications.
- `vigil/external_governance/sources/` — external-source registry.
- `vigil/external_governance/requirements/` — external-governance requirements and projections.
- `vigil/cam_assessment/` — CAM applicability and coverage assessment.
- `vigil/docs/reviews/` — bounded reviews that remain operationally useful.
- `vigil/docs/audits/` — retained non-normative historical audit evidence.

The taxonomy migration assurance ledger at `vigil/taxonomy/migration/Caelestis.LegacyFailure.MigrationLedger.json` remains live taxonomy validation evidence. It does not reactivate FM as a VIGIL record class.

## Schema and evidence authority

`vigil/VIGIL.Schema.json` is the sole active VIGIL record contract. It defines only Incident records. Subsystem schemas remain authoritative only for their named subsystem.

`source_records` is the only canonical evidence block. Preserve source identity, URLs, dates, evidence modality, access state, source residence, source role and claim-relative evidence status. Do not infer inaccessible facts or represent repository acceptance as human verification.

`related_incidents` is the sole active VIGIL-record relationship field. Current external research citations may be retained in `research_references`, and current standards or regulatory context in `standards_and_regulatory_references`; sources relied on as Incident evidence still belong in `source_records`.

Structured Incident severity is derived through `harm_impact_assessment` and VIGIL-HIM. Overall severity is the highest supported assessed materialised-harm band; dimensions are never averaged or summed. `unreported` is not S1, and SU applies when no dimension can be defensibly banded. Severity remains independent of source metadata, diagnostic provenance, taxonomy classification and workflow priority.


## Incident rebuild and re-adjudication control

The normative maintainer workflow for substantive Incident rebuilds is `vigil/docs/maintenance/INCIDENT-ADJUDICATION-WORKFLOW.md`.

The key maintenance distinction is:

- ordinary schema validation asks whether a record is structurally admissible;
- rebuild validation asks whether an existing governed record was changed **non-destructively and explicitly**.

A structurally valid Incident can still be a failed rebuild if it silently drops evidence, compresses supported occurrence detail, removes a taxonomy relationship, changes mapping role/confidence without recording the change, or adjudicates against a stale taxonomy.

### Required rebuild artefacts

For `full-rebuild` work, maintainers must keep a temporary adjudication manifest based on `vigil/templates/incident-rebuild-adjudication-template.json`. The manifest is maintenance evidence, not canonical Incident content and not a public-record field.

The manifest records:

- the exact baseline ref/version;
- external evidence-search activity;
- confirmation that the current taxonomy and complete class set were reviewed;
- candidate classes tested against recognition criteria and exclusions;
- for each materially rejected candidate, the **actual canonical recognition condition that remains unestablished**, rather than a generic statement that the internal mechanism or root cause is unknown;
- comparator Incidents reviewed where they materially inform the evidentiary threshold for the same Fidelity Class;
- a disposition for every baseline taxonomy mapping;
- reasons for new mappings and any removed source evidence;
- any justified material reduction in factual prose;
- whether Harm Impact was reopened or deliberately preserved; and
- completion of the integrated governance-interpretation pass.

Run `vigil/scripts/validate-vigil-incident-rebuild.py` before ordinary corpus validation.

The rebuild guard is intentionally generic. `VIGIL-INC-000129` informed its design because that Incident demonstrates mixed mapping roles and repeated re-adjudication, but permanent validation must not freeze one Incident's current answer.

### Taxonomy evidence-abstraction rule

Taxonomy adjudication MUST apply each Fidelity Class at the level of abstraction stated by its canonical definition, invariant, recognition criteria and exclusions.

**Do not silently raise the evidentiary burden beyond the class definition.**

Maintain a strict distinction between:

- **governance-mechanism evidence** — evidence sufficient to establish the structural condition described by the Fidelity Class; and
- **implementation-location evidence** — evidence locating that mechanism in a particular model component, classifier, filter, threshold, service, code path, hidden state or other technical subsystem.

Implementation-location evidence is required only when the Fidelity Class itself requires it. The absence of private implementation telemetry, source code, hidden prompts, internal chain-of-thought, classifier scores, execution traces or a vendor root-cause report does not defeat a governance-level classification when the canonical recognition conditions are otherwise established.

Before rejecting a candidate because evidence is unavailable, ask:

> Is the missing evidence required to establish this Fidelity Class, or would it only explain an already-established mechanism at a lower technical level?

If the missing evidence would only locate or explain an established governance mechanism more precisely, preserve that uncertainty in the classification basis or assessment boundary. Do not convert:

> we do not know which internal component failed

into:

> we do not know whether the governance mechanism occurred.

Conversely, do not infer a governance mechanism merely from an adverse outcome. Every canonical recognition condition must still be evidenced at the abstraction level the class actually requires, and no exclusion may defeat the mapping.

### Minimum-sufficient-evidence and candidate-rejection rule

Use the **minimum sufficient evidence required by the canonical class**, not the maximum evidence that could theoretically be obtained.

For each materially plausible candidate Fidelity Class:

1. identify each required recognition condition;
2. identify the occurrence evidence that satisfies it;
3. identify any genuinely unresolved required condition;
4. test the canonical exclusions; and
5. classify when all required conditions are established and no exclusion defeats the mapping.

A rejected candidate must name the specific canonical recognition condition that is not established, or the specific exclusion that applies.

Statements such as `internal mechanism unknown`, `exact control unknown`, `root cause unavailable`, `vendor telemetry unavailable` or `implementation details unavailable` are not sufficient rejection reasons unless that missing information is itself required by the canonical class.

Do not add unstated recognition conditions such as an exact model build, exact internal component, source-code access, hidden system prompt, classifier score, execution trace or vendor root-cause determination unless the class definition actually depends on that information.

### Policy, control and outcome evidence

Keep policy, control and occurrence evidence analytically distinct.

- **Policy evidence** can establish what state, conduct or outcome is prohibited, required or governed.
- **Control evidence** can establish that an operational safeguard, gate, review process, classifier, filter, approval state or other governance-control posture exists and is applicable.
- **Occurrence evidence** can establish that the triggering or prohibited condition occurred and that the required governance effect was absent, bypassed, lost or otherwise failed according to the candidate class.

A policy violation alone does not automatically establish a control-activation failure. However, a provider policy does not need to name an internal component when separate evidence establishes an applicable operational control posture and the occurrence establishes that the required protective effect was absent.

For `VIGIL-FC-000038 — Required Control Activation`, do not require the exact classifier, filter or runtime component to be identified. The class is satisfied where the evidence establishes that:

1. an available and applicable governance control or protective control posture existed;
2. a defined condition requiring that protection to become operative occurred; and
3. the governed action proceeded without the required protective effect becoming operative.

The exact technical fault location may remain unresolved and must be recorded as such without erasing the governance-control classification.

### Comparator-consistency rule

Before rejecting a candidate mapping for insufficient evidence, inspect relevant canonical Incidents already classified under that Fidelity Class.

Do not impose a materially stricter evidentiary threshold on the current Incident than VIGIL applies to comparable canonical occurrences unless:

- the existing comparators are themselves being reopened as potentially incorrect; or
- a documented taxonomy change has altered the recognition threshold.

Where comparable Incidents establish the same class from product-level, process-level or governance-level evidence, do not reject the current Incident merely because lower-level implementation telemetry is unavailable.

If inconsistent evidentiary thresholds are discovered, treat that as a **corpus-consistency problem requiring re-adjudication**, not as permission to select whichever threshold is stricter.

### Unclassified is an evidentiary conclusion, not a caution default

`unclassified` is valid and often necessary, but it must result from failure to establish an actual canonical recognition condition.

Do not use `unclassified` merely because:

- causal implementation details remain unknown;
- the provider has not published a root-cause analysis;
- internal telemetry is inaccessible;
- multiple technical pathways could have produced the same established governance mechanism; or
- a more detailed technical explanation would be desirable.

The adjudication record should state the specific recognition condition that remains unestablished. If every canonical recognition condition is supported at the class's defined level of abstraction and no exclusion applies, uncertainty about lower-level implementation does not justify leaving the Incident unclassified.

### Human-challenge recheck

When a human maintainer challenges a taxonomy disposition because the occurrence evidence appears to satisfy a class directly, do not defend the existing adjudication by default.

Re-run the candidate from the canonical class definition and explicitly check for:

- an invented evidentiary requirement;
- abstraction-level mismatch;
- inconsistent treatment relative to canonical comparators;
- confusion between policy evidence and control evidence;
- confusion between mechanism uncertainty and implementation-location uncertainty; and
- use of `unclassified` as a caution default rather than an evidentiary conclusion.

If an earlier adjudication used an unstated recognition condition, correct the record and preserve that correction in interpretive provenance.


### Gmail as the durable next-action staging point

VIGIL uses the maintainer Gmail account as the durable staging point for unresolved actions that cannot or should not be completed inside the current Incident edit.

**Gmail is an exception/action channel, not a completion log.** Do not send a Gmail notification merely because an Incident, pair, tranche or validator run completed successfully. A clean adjudication, an unchanged taxonomy, an exact matrix-to-Incident/Section 02 match, or an empty update queue requires **no email**.

The current queue is the **latest** Gmail message whose subject begins `[CURRENT VIGIL QA ACTION]` and that carries the label `VIGIL/CURRENT QA ACTION`. That message is a complete authoritative snapshot of unresolved work and supersedes earlier queue notes.

When adjudication identifies a new unresolved taxonomy requirement or another unresolved manual action:

1. read the current queue first;
2. reconcile its items against the actual working-branch state;
3. preserve unresolved items;
4. add the new instruction with Incident IDs, evidence basis, tested taxonomy boundaries or other relevant context;
5. send a replacement self-email using the same subject prefix;
6. apply the same Gmail label; and
7. make the supersession rule explicit in the new body.

A taxonomy escalation should explain the mechanism or invariant that is not faithfully representable, the nearest classes tested and rejected, and whether the likely next task is a new class, boundary amendment, family review or terminology repair.

This is intentionally a connector-mediated maintainer workflow, not repository automation. GitHub Actions must not contain mailbox credentials or attempt to impersonate the ChatGPT Gmail connector.

### Mapping preservation invariant

For every mapping present in the baseline, exactly one disposition is required:

`retained`, `role-changed`, `confidence-changed`, `role-confidence-changed`, `superseded`, or `removed-unsupported`.

A mapping absent from the candidate without `superseded` or `removed-unsupported` is an error. A new candidate mapping requires an explicit evidence-bounded reason. Source removal likewise requires a disposition reason.

This control does not make the old mapping presumptively correct. It makes changing governed analytical state an explicit adjudication rather than an accidental side effect of rewriting.

### Factual-detail preservation invariant

The rebuild guard detects large reductions in the word count of `summary` and `vigil_assessment.factual_basis`. It does not prohibit concise writing; it requires a maintainer to state why a material reduction improves fidelity rather than losing supported content.

Do not satisfy this guard with generic text such as "made concise". The reason should identify duplication, unsupported detail, corrected scope, or another concrete fidelity basis.

## Incident authoring and website-rendering crosswalk

This section is a maintainer contract for canonical Incident prose. It exists to prevent repository maintenance from confusing VIGIL's internal data fields with the labels and stages rendered by the CAM Initiative website.

**Before editing `summary`, `vigil_assessment.factual_basis`, `vigil_assessment.governance_interpretation`, or `vigil_assessment.significance_to_cam`, read this section first. Do not infer field purpose from a validator name such as “public prose”.**

The crosswalk below was verified on 23 September 2026 against the current Case File implementation in `CAM-Initiative/cam-governance-catalogue`, principally:

- `src/pages/vigil-case-file.tsx`
- `src/lib/vigilPublicDisplay.ts`
- `src/components/vigil/EvidenceCard.tsx`
- `src/components/vigil/CaseTaxonomyAssessment.tsx`
- `src/components/vigil/CaseTaxonomyClassification.tsx`
- `src/components/vigil/HarmImpactMatrix.tsx`
- `src/lib/vigilAffectedSystems.ts`
- `src/lib/vigilExternalAssessments.ts`

If the website projection changes, update this crosswalk before changing corpus prose to fit the new presentation.

### Canonical prose roles

These four fields are not interchangeable.

| Canonical VIGIL field | Current website surface | Authoring purpose |
| --- | --- | --- |
| `summary` | Stage 01 → Incident → **What happened** | Plain-language occurrence narrative. It must be rich enough for a lay reader to understand the event: who or what was involved, what occurred, when materially relevant, what happened next, and material consequences. It may attribute disputed facts and preserve essential uncertainty, but it must not perform VIGIL evidence adjudication, taxonomy analysis, governance diagnosis, or state what “the evidence establishes”. |
| `vigil_assessment.factual_basis` | Stage 02 → Assessment → **Factual basis** | Evidence-bounded synthesis of what the preserved sources establish, corroborate, dispute, do not establish, or leave unresolved. Phrases such as “the evidence establishes”, “the reviewed sources do not establish”, and “the available record supports X but not Y” belong here rather than in Stage 01. |
| `vigil_assessment.significance_to_cam` | Stage 02 → Assessment → **Governance significance** | Why the occurrence matters for governance, controls, design or CAM analysis. This is the governance lesson or significance layer, not the occurrence narrative. |
| `vigil_assessment.governance_interpretation` | Stage 05 → **VIGIL Observatory conclusion** | Integrated VIGIL analytical conclusion about the governance mechanism, boundary, failure, successful invariant or unresolved state evidenced by the occurrence. This is the conclusion layer and may use governed analytical language. |

The stable reading sequence is therefore:

> **What happened → What the evidence supports → Why it matters → Classification / governing invariant → VIGIL conclusion**

Do not move content between these fields merely to satisfy a prose validator. A validator may identify an offending token or internal phrase, but it does not redefine the authoring role of the field.

### Current Case File field-to-render crosswalk

| Website stage / surface | Website label or content | Canonical VIGIL source |
| --- | --- | --- |
| Case header | Title | `record_identity.title` |
| Case header | Incident | `id` |
| Case header | Classification | derived from `taxonomy_classification` |
| Case header | Severity | `harm_impact_assessment.overall_severity` |
| Case header | Updated | `record_identity.updated` with fallbacks |
| Stage 01 | **What happened** | `summary` |
| Stage 01 | Incident artefact / image | `incident_artefacts[]` |
| Stage 01 | Affected systems | selected `system_context.*` fields |
| Stage 01 evidence card | Evidence source title | `source_records[].source_title` |
| Stage 01 evidence card | **What the source establishes** | primarily `source_records[].source_context`; `vigil_assessment.factual_basis` is only a first-source fallback when no source-level confirmed-evidence field is available |
| Stage 01 evidence card | Evidence relevance | `source_records[].interpretive_reliance`, then `relevance_note` fallback |
| Stage 01 evidence card | Evidence-status basis | `source_records[].evidence_status_basis` |
| Stage 01 evidence card | Limits of the evidence | source limitations / `primary_artefact_access.limitations` |
| Stage 01 evidence metadata | Publisher, date, source type, evidence status, role, residence, modality, reviewer, access | selected `source_records[]` and `primary_artefact_access` fields |
| Stage 02 | **Factual basis** | `vigil_assessment.factual_basis` |
| Stage 02 | **Governance significance** | `vigil_assessment.significance_to_cam` |
| Stage 02 | **VIGIL taxonomy assessment** | `vigil_assessment.source_clause_analysis.clauses[]` |
| Stage 02 | Governance assessment provenance | `diagnostic_provenance.*` |
| Stage 02 | External assessments | selected `external_assessments[]` fields |
| Stage 02 | Real-world harm assessment | assessed rows from `harm_impact_assessment.dimensions[]` plus derived overall severity |
| Stage 02 | Evidence gap | `harm_impact_assessment.assessment_gap` |
| Stage 03 | Classification table | `taxonomy_classification.primary_classification` and `secondary_classifications[]` |
| Stage 03 | Alignment | mapping-local `classification_role` |
| Stage 03 | Classification basis | mapping-local `classification_basis` |
| Stage 04 | Governing invariant / Repair | resolved from the current Alignment Taxonomy using the Incident's class IDs; not authored as separate Incident prose |
| Stage 05 | **VIGIL Observatory conclusion** | `vigil_assessment.governance_interpretation` |
| Stage 06 | Evidence bibliography | selected `source_records[]` metadata |
| Stage 06 | External incident records | `external_incident_references[]` |
| Stage 06 | Taxonomy / methodology references | derived taxonomy and VIGIL-HIM references |
| Stage 06 | Limits of the assessment | `vigil_assessment.assessment_boundaries[]` plus generated roll-up of non-assessed harm dimensions |
| Stage 06 | Canonical Incident record | raw canonical Incident JSON link |

### Important Stage 01 evidence-card distinction

Stage 01 contains more than one factual-looking layer.

The standalone **What happened** text comes from `summary`.

Each evidence card separately renders **What the source establishes**. The website normally takes that text from the relevant `source_records[].source_context`. Only when no source-level confirmed-evidence text is available for the first source can `vigil_assessment.factual_basis` act as a fallback.

Therefore:

- `summary` is not a condensed `factual_basis`;
- `factual_basis` is not a replacement for `summary`;
- `source_context` is source-local evidence description and must not be treated as the Incident-level narrative; and
- maintenance must not copy analytical or evidentiary-adjudication wording into `summary` merely because it is factual.

The public-display helper currently also derives an internal `whatHappened` property for an evidence card from `summary`, but the ordinary `EvidenceCard` component does not render that property. Do not rely on this unused projection as a public surface.

### Canonical Incident fields currently not rendered, or only partly rendered

Canonical data must not be deleted merely because the ordinary Case File does not currently show it.

The following fields are currently unrendered or only partially projected in the ordinary Case File WebUX:

- `record_identity.version` and `record_identity.created`;
- `record_state`;
- most `incident_identity.*`, including occurrence dates, date precision, date basis and historical event name;
- `preferred_evidence.*`;
- `jurisdictional_context.*` as visible Case File content (it may contribute to search/indexing);
- `related_incidents[]`;
- `research_references[]`;
- `standards_and_regulatory_references[]`;
- `cam_internal.*`;
- `interpretive_provenance.review_history[]` and the full current-review object;
- `taxonomy_classification.classification_review_provenance`;
- ordinary-WebUX display of taxonomy version and mapping confidence;
- `system_context.component_role`;
- agent-context evidence basis and source references;
- occurrence-environment detail, evidence basis and source references;
- `harm_impact_assessment.coverage_note`;
- harm row `threshold_id` and `evidence_confidence`;
- `observed_values` when an `assessment_basis` is already present;
- individual unassessed harm-dimension assessment bases, which are generally rolled up rather than rendered row by row;
- many `external_assessments[]` fields including assessment title, type, relationship, scope note, VIGIL comparison note, status, version and supersession;
- `source_records[].incident_source_order`, `source_url_status`, `model_or_algorithm` and `system_or_product` as ordinary visible fields;
- `primary_artefact_access.access_status`;
- `incident_artefacts[].caption`, `artefact_type` and `media_type`.

Absence from the current website is not permission to remove these fields. They remain part of the canonical Incident record where required by schema, evidence integrity, provenance, auditability, future rendering, report/PDF output or downstream tooling.

### Maintainer editing guardrails

Before changing Incident prose:

1. identify the exact canonical field being edited;
2. identify the exact website surface that consumes it;
3. compare the proposed wording against that field's authoring purpose above;
4. preserve supported occurrence detail and evidence uncertainty;
5. do not use a validator failure as authority to rewrite neighbouring prose;
6. do not perform corpus-wide `summary`, `factual_basis`, `significance_to_cam` or `governance_interpretation` rewrites mechanically;
7. when a field appears semantically wrong for the current website, fix the field contract or renderer first rather than repeatedly rewriting records to compensate for projection ambiguity.

For `summary` specifically, the repair rule is:

> **Remove or relocate only material that belongs to evidence adjudication, governance interpretation, significance or classification. Preserve and, where necessary, restore the rich lay account of the occurrence.**

## Clause-level taxonomy assessment and publication

Clause-level assessment follows this editorial sequence:

> Source wording → recovered principle → occurrence-specific taxonomy assessment → formal structured classification.

For `vigil_assessment.source_clause_analysis.clauses[]`, `source_anchor` or `source_paraphrase` preserves the source-language basis, `recovered_invariant_interpretation` states the general principle recovered from that language, and each `taxonomy_relationships[].rationale` applies the referenced taxonomy boundary to the bounded occurrence. The rationale is the canonical public content of the **Taxonomy assessment** column; it is not a generated relationship label, internal crosswalk note or substitute for the separate structured classification.

Incident authors and reviewers must:

- ground each rationale in the source clause, canonical class definition, invariant, recognition conditions and preserved occurrence evidence;
- describe the occurrence-specific mechanism or boundary in natural language;
- keep class IDs, class and family names, relationship roles and mapping state in their structured fields rather than using them as the public explanation;
- avoid generic workflow phrases such as “supports the mapping,” “matches the finding” or “contributes to the recorded failure mechanism”;
- preserve distinct rationales in source order when one clause has multiple relationships; and
- state the demonstrated boundary and the missing occurrence condition for adjacent, ambiguous-boundary, exemplar or otherwise non-canonical relationships.

Downstream website, document and PDF publishers must read and faithfully render the supplied `taxonomy_relationships[].rationale` values. Multiple rationales must be combined in stored order without duplication. A generated relationship-type summary may be used only as an explicit legacy fallback when no rationale is present; it must never replace supplied assessment prose. Website and PDF outputs must use the same rationale source.

Publication consumers should protect this contract with generic fixtures covering a single rationale, multiple ordered rationales, mixed canonical and non-canonical relationships, and the missing-rationale fallback. Tests should validate the data contract rather than pinning the current adjudication of a live Incident.

## Alignment Taxonomy adjudication matrix

`vigil/taxonomy/VIGIL.FailureTaxonomy.Adjudications.json` is the maintenance coverage table for exhaustive Incident-by-class review. Its legacy filename is retained for compatibility; it is governed by the current VIGIL Observatory Alignment Taxonomy. It is not a second taxonomy and it is not a public classification narrative.

Each enrolled Incident must have exactly one row for every current selectable Fidelity Class. The matrix is a taxonomy-role adjudication matrix, not a failure-only matrix. Exhaustive adjudication tests every class independently for failure occurrence, successful invariant and ambiguous boundary. A NO failure decision is not proof that the class has no taxonomy relationship to the Incident.

Rows contain one semantic decision and a short occurrence-specific reason:

- `failure-occurrence` — the occurrence establishes violation of the class invariant and must carry the same canonical Incident and Section 02 role;
- `successful-invariant` — the invariant was materially tested or engaged and affirmatively preserved; the Incident mapping and an admitted reciprocal taxonomy `invariant_exemplar` are required;
- `ambiguous-boundary` — the occurrence materially illuminates the invariant boundary but establishes neither failure nor successful preservation; the Incident mapping and an admitted reciprocal taxonomy `invariant_exemplar` are required;
- `no-mapping` — sufficient recognition facts establish that the class is not materially engaged;
- `unresolved` — a required recognition fact remains genuinely unavailable or indeterminate, and the reason must name that fact; and
- `MISSING` — mechanical placeholder only; validation must fail until a reviewer adjudicates it.

`unresolved` MUST NOT be used as a substitute for `ambiguous-boundary`. An ambiguous boundary is an affirmative taxonomy relationship; unresolved is evidence uncertainty. Ordinary absence of failure is neither a successful invariant nor an ambiguous boundary.

Run `python vigil/scripts/sync-vigil-taxonomy-adjudications.py` after adding a selectable class or enrolling an Incident. The sync may create `MISSING` cells but must never choose a semantic disposition. During the v0.1 failure-only migration, prior `YES` becomes `failure-occurrence`, prior `UNRESOLVED` remains `unresolved`, and prior `NO` is retained under `prior_failure_adjudication` while the role-aware decision becomes `MISSING`; the sync MUST NOT infer `no-mapping` from prior failure rejection. Run `python vigil/scripts/validate-vigil-taxonomy-adjudications.py` to enforce current-class coverage and role-by-role canonical consistency.

During a staged pair-by-pair recovery, use repeatable `--incident VIGIL-INC-NNNNNN` arguments to validate only the completed pair under the same rules. An Incident-scoped pass does not make unreviewed `MISSING` cells elsewhere complete and must not be reported as a full-matrix pass.

A taxonomy review must not describe an enrolled Incident as exhaustively reviewed while any current cell is `MISSING`. Candidate shortlisting never substitutes for this matrix.

For deterministic handover, disposition polarity is evidence-sensitive: `no-mapping` requires sufficient facts to reject all three positive roles; `unresolved` preserves a specific evidence gap; each positive role requires the same role in the canonical Incident and Section 02. Public nondisclosure of an internal state is not itself proof that the state failed.

Adjudication reasons must also be occurrence-specific. Boilerplate templates, generic applicability statements, and duplicate normalised reasons within one Incident are validator failures. In particular, do not use forms such as `No material [class] mechanism is present ...`, `required conditions are outside the evidenced pathway`, `class does not apply`, or equivalent repetitive filler. A `no-mapping` reason must identify the recognition condition or exclusion resolved by the occurrence; an `unresolved` reason must identify the exact missing recognition fact.

Stage 02 canonical role parsing is exact rather than impressionistic. Accepted values are `failure-occurrence` and `failure-occurrence contribution` for the `failure-occurrence` role, `successful-invariant` for the `successful-invariant` role, and `ambiguous-boundary exemplar` for the `ambiguous-boundary` role. Similar-sounding legacy text such as `canonical failure mapping` is not silently treated as equivalent; it is a maintainer normalisation action.

### Post-adjudication record-update report

The matrix campaign is analytically separate from canonical Incident repair.

After completing an Incident or tranche:

1. run the adjudication validator;
2. repair all matrix-quality failures first, including `MISSING`, boilerplate, duplicate reasons and invalid `NO`/`UNRESOLVED` polarity;
3. compare each clean positive role set with the same role in canonical `taxonomy_classification` mappings and Stage 02 canonical `source_clause_analysis.taxonomy_relationships`, and verify admitted reciprocal taxonomy exemplars for successful-invariant and ambiguous-boundary mappings;
4. place an Incident on the **record update required** list only when the clean matrix disagrees with either canonical surface;
5. do not modify the canonical Incident during a matrix-only campaign unless the maintainer separately authorises record repair;
6. stage a Gmail action only when a genuine unresolved change is required, such as a canonical Incident/Section 02 repair that was identified but not performed, a taxonomy boundary/class/family change that remains to be made, or a genuinely new taxonomy class/proposal; and
7. when the clean matrix matches both canonical surfaces and no taxonomy or other unresolved maintainer action is required, **do not send Gmail**.

Do not send empty record-update reports, clean-pass notices, progress summaries or “no changes required” emails. If an authorised task already completed the required repair and no further action remains, Gmail staging is also unnecessary. GitHub Actions must not contain mailbox credentials.

A matrix that fails its own adjudication-quality controls is not evidence that the Incident record needs repair. The matrix must become internally valid first. The validator marks clean matrix-to-canonical mismatches as `GMAIL ACTION REQUIRED`; intrinsic matrix-quality failures remain ordinary validation errors and must be repaired before any such notification is staged.


## Generated outputs

The active public outputs are:

```text
vigil/VIGIL.Incidents.Index.json
vigil/VIGIL.Registry.Index.json
vigil/taxonomy/generated/VIGIL.FailureTaxonomy.CaseFileExamples.json
```

Build all three with:

```bash
python vigil/scripts/build-vigil-public-records.py
```

The master registry contains one registry, `incidents`. It is a registry-of-registries manifest and must not duplicate Incident entries. `VIGIL.Incidents.Index.json` is intentionally a lightweight catalogue/search/routing projection; canonical evidence, diagnosis, structured severity, taxonomy detail and provenance remain in the source Incident JSON. Do not manually edit generated outputs or recreate retired-class indexes.

## Human-maintainer stop conditions for validators, schema rules and corpus-wide tests

Validators, schemas and permanent corpus tests are **governance controls over the record set**. A change to one of these controls can silently redefine what canonical Incident content is permitted and can induce large-scale record rewrites. Treat semantic validator changes as maintainer decisions, not routine implementation cleanup.

### Gate 1 — approval before changing the control

Before editing any validator, schema rule, permanent test, builder rule or publication guard that can change whether canonical Incident content passes or fails, the agent or maintainer must first present the proposed change to the human maintainer and **STOP**.

The pre-change explanation must state, in plain language:

1. **Current behaviour** — what the existing rule checks and which canonical fields or structures it governs.
2. **Proposed behaviour** — exactly what will change.
3. **Pass/fail delta** — examples of content that passes today but would fail after the change, and content that fails today but would pass after the change.
4. **Affected surface** — the exact VIGIL fields, website stages, generated outputs or subsystems involved.
5. **Expected corpus impact** — known or estimated records likely to be affected. If this has not been measured, say so explicitly.
6. **Repair implication** — whether satisfying the new rule could require prose rewrites, taxonomy changes, evidence changes, provenance changes, field movement, deletions, migrations or generated-output rebuilds.
7. **Data-loss / semantic-drift risk** — what valuable information could be flattened, moved, hidden or deleted if the rule is applied mechanically.
8. **Why the validator is the right place to enforce the rule** — rather than the schema, renderer, documentation, authoring contract or a bounded review.
9. **Proposed stop condition** — what will happen after the validator change if existing records fail.

No semantic validator/schema/test change may be implemented until the human maintainer explicitly approves that described behaviour.

A change is semantic if it can alter the accepted meaning, placement, wording, classification, evidence state, harm state, provenance state or public presentation contract of canonical records. Renaming a test, fixing a syntax error, improving diagnostics or repairing execution without changing the accepted/rejected record set is not semantic; if there is any doubt, treat the change as semantic and stop for approval.

### Gate 2 — approval before repairing records exposed by a changed control

Human approval to change a validator **does not authorise automatic corpus repair**.

After an approved validator/schema/test change is implemented:

1. run it read-only against the corpus;
2. report the exact failing records and fields;
3. distinguish mechanical defects from semantic/content defects;
4. for semantic/content defects, show representative before/after repair examples and explain which canonical field role each proposed edit preserves;
5. **STOP again for human-maintainer approval before broad, multi-record or corpus-wide edits.**

Do not combine “change the validator” and “rewrite every record that now fails” into one unattended maintenance action.

### Mandatory stop conditions

Stop and seek explicit human-maintainer direction when any proposed validator or repair would:

- change the authoring role of `summary`, `vigil_assessment.factual_basis`, `vigil_assessment.significance_to_cam` or `vigil_assessment.governance_interpretation`;
- move prose between website stages or canonical fields;
- remove or prohibit previously accepted factual, analytical, evidentiary or provenance content;
- introduce a new corpus-wide prose restriction or regex;
- require more than a small bounded set of canonical Incident edits;
- affect taxonomy mappings, classification roles/confidence, VIGIL-HIM results, source evidence, source-clause analysis or interpretive provenance;
- convert a presentation preference into a canonical-record validity rule;
- create a migration or rewrite requirement for records that were valid under the previous contract;
- produce uncertainty about whether the validator or the website renderer is wrong.

When a validator failure conflicts with the documented field-to-render contract, **do not repair the record first**. Stop, identify the contract conflict, and ask the human maintainer whether the validator, renderer, schema or record should change.

### Validator failures are diagnostic, not editing authority

A validator reports that a rule has been breached. It does not itself authorise deletion, simplification, paraphrase, field movement or re-adjudication.

For prose in particular, the smallest possible fix is preferred only **after** the governing rule and field semantics are already approved and unambiguous. If the required repair is not obvious from the canonical contract, stop rather than infer the desired rewrite.

## Maintenance and validation

Executable tests belong under `vigil/tests/`; current builders and validators belong under `vigil/scripts/`. Delete completed one-off migration, routing, reconciliation and seeding machinery when no retained subsystem depends on it.

For Incident/schema/runtime changes, run:

```bash
python vigil/scripts/build-vigil-public-records.py
python vigil/tests/test_build_vigil_records.py
python vigil/tests/test_validate_vigil_record_rules.py
python vigil/tests/test_validate_vigil_records.py
python vigil/tests/test_validate_vigil_public_records.py
python vigil/tests/test_vigil_pipeline_state.py
python vigil/tests/test_vigil_source_provenance.py
python vigil/scripts/validate-vigil-records.py
python vigil/scripts/validate-vigil-public-records.py
python vigil/scripts/validate-vigil-source-provenance.py
python vigil/scripts/validate-vigil-interpretive-provenance.py
python vigil/scripts/validate-vigil-system-components.py
python vigil/scripts/validate-authorship-provenance.py
python vigil/taxonomy/validate_taxonomy.py
```

Also run the validators owned by external governance or CAM assessment when those subsystems are touched.

Before closure, classify each touched supporting artefact as LIVE, GENERATED, REVIEW, AUDIT or RETIRE. Historical machinery must not masquerade as current authority. Do not reset, rebase, merge, cherry-pick, force-push or rewrite shared history as cleanup. The bounded pre-PR ingestion-branch synchronization exception above is the only permitted rebase/lease-protected force-update under this guide.
