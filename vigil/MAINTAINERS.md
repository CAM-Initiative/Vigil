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


## High-signal ecosystem ingestion sources

### Ordinary new-entry completion

A request for a new Incident authorises the complete ordinary evidence, scope/duplicate, chronological episode, current taxonomy, twelve-dimensional HIM, independent external-requirement, public interpretation, provenance, appropriate media and validation process. The JSON intake template is an intermediate starting point. Follow the new-entry completion section of `docs/maintenance/INCIDENT-ADJUDICATION-WORKFLOW.md` and the audit-only `templates/incident-completion-checklist-template.json`. An empty assessment list does not establish review. Distinguish unperformed, reviewed-with-assessments, reviewed-none-retained and blocked external review in the dated audit, with reasons and exact missing sources/facts. Evidence-limited findings can follow a completed review; do not manufacture taxonomy completeness or standards findings.

Canonical completion fields or blocking controls remain subject to Gate 1. Prospective design and decision gate are tracked in [GitHub issue #142](https://github.com/CAM-Initiative/Vigil/issues/142); no new validity rule or historical backfill has been authorised. The previous 18 October design draft remains in Git history.

Scheduled or manual ecosystem ingestion SHOULD explicitly check high-signal first-party disclosure surfaces that publish bounded model-behaviour, evaluation, containment or agent incidents. At minimum, the current watch set includes:

- OpenAI Alignment misalignment reports and notices, including `https://alignment.openai.com/misalignment-reports/`;
- originating-provider incident, safety, alignment and evaluation disclosures where concrete occurrences are described;
- AI Security Institute or comparable public safety-institute incident reports; and
- provider research updates that materially revise the causal interpretation, evidence or control analysis of an Incident already in VIGIL.

The watch set is an intake surface, not an admission list. Appearance in a monitored source does not create a VIGIL Incident, and a provider's choice to label an occurrence a demonstration, research result, misalignment report, safety finding or non-incident does not determine VIGIL admission or classification. Apply the ordinary bounded-occurrence, duplicate, evidence, Harm Impact and taxonomy workflow.

When a monitored source supplies materially new evidence about an existing Incident, prefer an evidence refresh and append-only assessment update over allocating a duplicate Incident. When one publication contains multiple independently bounded trajectories, admit separate Incidents only where the affected system, action chain or governance occurrence is sufficiently distinct to support independent adjudication.

## Historical provenance

Legacy record classes and migration artefacts remain recoverable through Git history. Active Incident records contain only information required by the current VIGIL data model and must not carry retired payloads, migration-source metadata or retired-record links.

Do not falsify historical review dates or rewrite historical audits and reviews that accurately describe earlier repository states.

## Retained subsystem boundaries

- `vigil/records/incidents/` — sole active public record corpus.
- `vigil/taxonomy/` — canonical VIGIL Observatory alignment taxonomy and generated publications.
- `vigil/external_governance/sources/` — external-source registry.
- `vigil/external_governance/requirements/` — external-governance requirements and projections.
- `vigil/cam_assessment/` — CAM applicability and coverage assessment.
- `vigil/docs/reviews/` — selected dated decision packets and adopted-control provenance relevant to the retained corpus. Superseded audits are recoverable at the pinned pre-cleanup Git commit; they are not current verification.

The taxonomy migration assurance ledger at `vigil/taxonomy/migration/Caelestis.LegacyFailure.MigrationLedger.json` remains live taxonomy validation evidence. It does not reactivate FM as a VIGIL record class.

## Schema and evidence authority

`vigil/VIGIL.Schema.json` is the sole active VIGIL record contract. It defines only Incident records. Subsystem schemas remain authoritative only for their named subsystem.

`source_records` is the only canonical evidence block. Preserve source identity, URLs, dates, evidence modality, access state, source residence, source role and claim-relative evidence status. Do not infer inaccessible facts or represent repository acceptance as human verification.

`related_incidents` is the sole active VIGIL-record relationship field. Current external research citations may be retained in `research_references`, and current standards or regulatory context in `standards_and_regulatory_references`; sources relied on as Incident evidence still belong in `source_records`.

`external_requirement_assessments` is an optional, separate occurrence-level assessment surface. Candidates may be resolved from a material source clause through reviewed FC/EXTREQ relationships or independently identified from occurrence evidence. The field contains only materially relevant occurrence assessments with independent `alignment_result` (`aligned`, `not-aligned`, `boundary`) and `assessment_basis`. Normative force remains canonical requirement metadata; voluntary adoption is not an assessment gate. Candidate exclusions remain audit-only. The field does not duplicate central requirement metadata, taxonomy roles, or external assessments, and does not assert organisation-wide compliance. Follow `vigil/docs/maintenance/EXTERNAL-REQUIREMENT-ADJUDICATION.md`; do not backfill the corpus mechanically. Candidate generation preserves the meaning of `standards_and_regulatory_references` and does not use it to create candidates.

## Public-language contract

All VIGIL-authored public prose MUST follow `vigil/docs/maintenance/PUBLIC-OUTPUT-STYLE.md`.

The public-language contract is ASD-STE100-informed controlled English. It preserves source fidelity while making VIGIL-authored analysis consistent across Case Files, generated projections, website surfaces and publications. Do not claim formal ASD-STE100 conformity unless the specific publication has been checked against the applicable standard and controlled vocabulary.

Use one public term for one concept. In particular:

- use **Aligned**, **Not aligned** and **Boundary** as the public alignment-result labels;
- use **Alignment Taxonomy**, **Fidelity Class**, **external requirement**, **normative force** and **assessment basis** consistently;
- do not rotate among legacy synonyms such as `met`, `not met`, `failure`, `success`, `applicability unresolved`, `insufficient evidence` or `not assessable` as alternate public state labels;
- keep structured canonical relationship roles in structured fields rather than exposing them as alternate public result vocabulary;
- write short sentences, prefer one proposition per sentence, name the decisive evidence or missing fact, and avoid generic hedging;
- preserve quotations, source anchors, legislation, standards text and historical audit language when fidelity requires the original wording; and
- use Australian English spelling consistently in VIGIL-authored prose.

Historical audits are not rewritten solely to adopt current terminology. New public prose and new audits use the current controlled vocabulary, while migration audits may name retired terms when necessary to explain what changed.


Structured Incident severity is derived through `harm_impact_assessment` and VIGIL-HIM. Overall severity is the highest supported assessed materialised-harm band; dimensions are never averaged or summed. `unreported` is not S1, and SU applies when no dimension can be defensibly banded. Severity remains independent of source metadata, diagnostic provenance, taxonomy classification and workflow priority.

Occurrence-environment metadata also preserves independent dimensions. `deployment_state` records evidenced lifecycle status, `activity_contexts` records training/evaluation/research/operational activity, `external_reach` records whether real external systems, services, people or data were materially reached, and `activity_actor` identifies the actor conducting non-operational activity. Never infer deployed status from live external reach or real-world consequences. The complete adjudication rules are in `vigil/VIGIL.Schema.json` and the Incident adjudication workflow.


## Single taxonomy version bump per working branch

**One consolidated increment.** Take the latest published `main` Alignment Taxonomy version as the base. During one unmerged working tranche, select the **highest necessary** SemVer increase exactly once: patch for amended existing family/class content, minor when at least one new Fidelity Family is admitted, or major only for an explicitly approved incompatible change. A minor (or major) increase subsumes all concurrent patch-level refinements. Example: `0.7.11 → 0.7.12` for a patch-only branch; `0.7.11 → 0.8.0` when a new family is added. Never advance `0.8.0 → 0.8.1` for further edits on that same unmerged branch. A new, separately authorised release after merge is a different tranche.

**Working candidate versus publication.** The taxonomy index's `working_release` object records the single intended next `version`, its published `base_version`, required `change_level` and `state: unpublished`. For PR #140 this is `0.7.0 → 0.8.0`. The index `standard.version`, dated `release_history` and family `standard.version`/`publication_date` continue to identify the **last actually published main edition** until a release is prepared. This prevents a working candidate from being presented as published. Never append a working intermediate release to `release_history` or call `prepare_taxonomy_release.py` on an unmerged branch. Do not renumber the candidate after additional class additions, amendments, incident reviews, or corrections. If a previously patch-only branch genuinely acquires a new family, **replace the candidate with the single higher-level target** from the original main baseline (e.g. `0.7.12 → 0.8.0`); this is a correction of the one intended release, not an additional release. Record the reason in review history.

**Version used for Incident adjudication.** The version of criteria applied to an Incident is separate from the last published dataset. Newly adjudicated records may identify the provisional `working_release.version` in their current `taxonomy_classification.taxonomy_version`, provided their dated decision packet and classification review provenance pin the exact working taxonomy commit or family source blob and applied recognition criteria. Never represent the candidate as published, silently rewrite historical Incident stamps, or bulk-migrate unaffected records. Earlier references to a mistakenly numbered working snapshot remain review history, accompanied by an explicit crosswalk to the corrected candidate.

**Single release on merge.** Pull-request validation compares the version and published-release ledger with `main`, rejects an extra branch release entry or wrong candidate number, and permits changes to unpublished recognition content without demanding a new bump. After authorised merge, the publication workflow computes the final content digest, consumes the selected working candidate, assigns the actual publication date, appends **exactly one** release-history entry, stamps index and families, and renders the publication. It must not derive a second bump from the working candidate itself. A branch with no substantive taxonomy content changes needs no dataset release. A passing pull request is not a publication event.

**Non-destructive correction.** When a branch was prematurely stamped with multiple versions, preserve the main published baseline and historical published releases, remove only mistakenly appended unpublished entries, and retain dated crosswalk evidence. Correct affected active Incident targets and current provenance without destroying historical quotations, mappings, Boundary assessments, independent external assessments, source evidence or Harm Impact. Rebuild generated indexes and validate. Do not change main or merge without maintainer authorisation.

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

### VIGIL independent adjudication authority — source interpretation boundary

VIGIL's current versioned Alignment Taxonomy is the authority for **VIGIL's own classification criteria**, not a claim of legal, regulatory, technical or factual supremacy over source institutions. First-party, investigative and other external publications are evidence and attributable interpretations. Their prestige, vocabulary, silence on a mechanism, or external classification is neither a positive nor a negative VIGIL recognition test.

For each proposed change, keep four distinct layers:

1. **Occurrence claims:** identify the actor, action, target, time and source, with access modality, attribution, corroboration, and counterevidence. Distinguish direct observation from a source's explanation.
2. **External interpretations:** retain each materially relevant institution's explanation on its own terms, including competing interpretations, but do not translate its verdict automatically into a VIGIL class or role.
3. **VIGIL recognition:** apply the exact class invariant, required success/failure conditions and exclusions at the class's defined level of abstraction, with occurrence-specific evidence for each required condition.
4. **VIGIL adjudication:** decide the role, confidence and mapping only from that criterion test, with the precise unresolved conditions, if any, and the prior VIGIL decision explicitly compared.

An original VIGIL divergence from third-party interpretation is neither an error nor protected doctrine. Retain it if the current criterion/evidence test supports it; revise it when materially contradicted, disproved or unsupported. Never use external silence, the absence of private implementation telemetry, or pressure for agreement as an unrecorded reason for removal or polarity downgrade. Never protect an existing conclusion by ignoring evidence or adding recognition conditions not in the class.

**Minimum traceable decision per materially reviewed mapping:** pinned Incident ref and taxonomy version/ref; class ID and original role/basis; exact class conditions and exclusions examined (quote the version-specific text, since individual conditions lack immutable IDs); episode/source references; condition-by-condition result and missing fact; neighbouring-class discrimination; external interpretation and any material VIGIL divergence; proposed role/basis/confidence and a disposition with substantive explanation. Negative candidates and full criterion matrices stay in **per-Incident dated review artefacts**, not canonical Incident fields or a global Incident × Class dataset.

The current schema and rebuild guard establish structure and accounted-for change, **not** semantic truth. A passing guard cannot certify that a VIGIL divergence or bounded success survived a rewritten aggregate explanation. Audit the before/after mapping-local bases, distinct source-clause rationales, mixed episode roles, summary synthesis, unaffected external assessments, HIM and prior interpretive history before claiming a faithful adjudication. A single Fidelity Class may legitimately have failed in an earlier episode and succeeded later; do not force the episode relationships into its Incident-level mapping role or infer that the later success retroactively resolves the earlier failure. Apply **Temporal Integrity of Adjudication** in the Incident workflow: separate original conduct, later authoritative review, remedy ordered versus verified completion, and materialised harm. INC-008 is the bounded example: appellate reversal can substantiate the earlier access-denial finding but does not establish completed evidence production or erase the original failure.

Until a separately scoped Gate 1 proposal measures and obtains approval for new permanent controls, these are editorial/adjudicative instructions and dated audit requirements; they do not automatically alter the semantic pass/fail behaviour of the validators.

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

### Exclusion precedence and condition-specific adjudication

An exclusion is part of the class's actual recognition boundary, not explanatory context. Test each literal exclusion on the evidence before accepting **any** canonical role. A positively established exclusion defeats failure, success **and** ambiguous-boundary admission for that class. This includes exclusions whose operative condition is that a required fact remains unresolved. Do not convert an excluded or not-yet-engaged candidate into a canonical Boundary merely because the general topic is relevant; preserve the precise unresolved candidate or separately evidenced taxonomy gap in the review packet/appropriate episode disposition. An exclusion requiring another class's *sufficient* coverage applies only where that sufficiency is actually demonstrated.

For every necessary success or failure recognition condition, identify its own status and the specific occurrence proposition, source/episode evidence and counterevidence supporting it. Copying the overall classification basis into each condition entry is **not** a condition-by-condition assessment. One evidence item can establish several conditions, but its distinct significance to each must be articulated. Positive success is assessed against the entire required protective sequence, not the favourable outcome alone. If any necessary condition is unknown, record why and whether a decisive source is reasonably recoverable, without inventing a technical root-cause requirement.

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


### GitHub Issues as the durable action queue

The authoritative location for new unresolved VIGIL follow-up tasks is GitHub Issues in `CAM-Initiative/Vigil`, not the former emailed queue. Issues are tracked actions, not new canonical evidence, approval, completion reporting or a substitute for an admitted Incident.

When an adjudication produces a concrete task that cannot safely be completed within its authorised scope, follow the issue protocol in `vigil/docs/maintenance/INCIDENT-ADJUDICATION-WORKFLOW.md`. Identify the Incident, episode and Fidelity Class or external requirement as appropriate. Search existing open and closed issues using these identities and the underlying mechanism. Update an existing relevant open issue instead of creating a duplicate. Otherwise create an actionable issue with source-grounded context, the exact missing fact or repair, branch/ref, dependencies and an objective closure condition. Use the template in `.github/ISSUE_TEMPLATE/vigil-follow-up.md`.

Use categories: **taxonomy-gap**, **evidence-required**, **record-maintenance**, **system-improvement**. A defensible Boundary, no-mapping, partial or unresolved finding does not alone require an issue: the trigger is a distinct *actionable follow-up*. A blocked record stays blocked even if an issue is opened. Do not create issues for a clean pass or for progress reporting. Do not publish private evidence or sensitive correspondence in public issues.

Link the confirmed issue number and URL in the dated review manifest or Incident completion audit, never in a new global incident-by-class dataset. Issue creation is not automatic approval to change taxonomy, schema, validators, other Incidents or the website. If GitHub access is unavailable, preserve a ready-to-file issue payload in the dated audit and report that staging was not completed; do not revert to Gmail.

The historical Gmail queue is a **migration source only**. Reconcile the latest correctly labelled authoritative snapshot and its supersession notes against current `main`, the working branch and already-open Issues; migrate only outstanding, distinct tasks. Do not import historical embedded snapshots as new work or claim the migration complete before it is audited. See the one-time historical queue transition in `vigil/docs/maintenance/INCIDENT-ADJUDICATION-WORKFLOW.md`. Existing approvals and workstream pauses remain in force.

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

The crosswalk below was re-verified on 25 September 2026 against the current Case File implementation in `CAM-Initiative/cam-governance-catalogue` branch `ux/homepage-tactile-instrument-gears`, principally:

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
| `vigil_assessment.significance_to_cam` | Stage 05 → Conclusion → **Governance significance** | Why the occurrence matters for governance, controls, design or CAM analysis. This is the governance lesson or significance layer, not the occurrence narrative. |
| `vigil_assessment.governance_interpretation` | Stage 05 → **VIGIL Observatory conclusion** | Integrated VIGIL analytical conclusion about the governance mechanism, boundary, failure, successful invariant or unresolved state evidenced by the occurrence. This is the conclusion layer and may use governed analytical language. |

The stable reading sequence is therefore:

> **What happened → What the evidence supports → Classification → Governing invariant / Repair → VIGIL conclusion and why it matters**

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
| Stage 02 | **Incident breakdown** | `vigil_assessment.source_clause_analysis.clauses[]` |
| Stage 02 | Public authorship and review transparency | compact projection of `interpretive_provenance.*` where supported by the renderer |
| Stage 02 | External assessments | selected non-classification `external_assessments[]` fields |
| Stage 02 | **Harm Impact Assessment** | assessed rows from `harm_impact_assessment.dimensions[]` plus derived overall severity |
| Stage 02 | Evidence gap | `harm_impact_assessment.assessment_gap` |
| Stage 03 | Fidelity Family / Fidelity Class classification table | `taxonomy_classification.primary_classification` and `secondary_classifications[]`; immutable `VIGIL-FF-*` / `VIGIL-FC-*` identifiers resolve against the current Alignment Taxonomy |
| Stage 03 | Alignment | mapping-local `classification_role` |
| Stage 03 | Classification basis | mapping-local `classification_basis` |
| Stage 03 | **External Alignment Classification** | `external_assessments[].classification_or_rating` plus parent assessor / assessment citation metadata; external labels remain in the external assessor’s own scheme and are not translated into VIGIL taxonomy roles |
| Stage 04 | Governing invariant / Repair | resolved from the current Alignment Taxonomy using the Incident's Fidelity Class (`VIGIL-FC-*`) IDs; not authored as separate Incident prose |
| Stage 05 | **VIGIL Observatory conclusion** | `vigil_assessment.governance_interpretation` |
| Stage 05 | **Governance significance** | `vigil_assessment.significance_to_cam` |
| Stage 06 | Evidence bibliography | selected `source_records[]` metadata |
| Stage 06 | External incident records | `external_incident_references[]` |
| Stage 06 | Taxonomy / methodology references | derived taxonomy and VIGIL-HIM references |
| Stage 06 | Limits of the assessment | `vigil_assessment.assessment_boundaries[]` plus generated roll-up of non-assessed harm dimensions |
| Stage 06 | Canonical Incident record | raw canonical Incident JSON link |

Mapping-local `classification_basis` is public, occurrence-specific explanatory prose. It must describe the evidence, mechanism and classification boundary directly and must not use Incident record identifiers as narrative referents; Incident identity belongs in structured record metadata, not the explanation.

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

## Clause-level incident breakdown and publication

Clause-level incident breakdown follows this editorial sequence:

> Source wording → recovered principle → occurrence-specific incident analysis → formal structured classification.

For `vigil_assessment.source_clause_analysis.clauses[]`, `source_anchor` or `source_paraphrase` preserves the source-language basis, `recovered_invariant_interpretation` states the general principle recovered from that language, and each `taxonomy_relationships[].rationale` applies the referenced taxonomy boundary to the bounded occurrence. The rationale is the canonical public content of the **Incident analysis** column within the **Incident breakdown** table; it is not a generated relationship label, internal crosswalk note or substitute for the separate structured classification.

Incident authors and reviewers must:

- ground each rationale in the source clause, canonical class definition, invariant, recognition conditions and preserved occurrence evidence;
- describe the occurrence-specific mechanism or boundary in natural language;
- keep class IDs, class and family names, relationship roles and mapping state in their structured fields rather than using them as the public explanation;
- avoid generic workflow phrases such as “supports the mapping,” “matches the finding” or “contributes to the recorded failure mechanism”;
- preserve distinct rationales in source order when one clause has multiple relationships; and
- state the demonstrated boundary and the missing occurrence condition for adjacent, ambiguous-boundary, exemplar or otherwise non-canonical relationships.

Where clause-level analysis recovers a materially supported governance proposition that cannot be reconciled faithfully with the current taxonomy, do not force it into the nearest class and do not treat the mismatch as automatic authority to create a class. Record it as a taxonomy-gap signal and apply the design test in `vigil/docs/design/TAXONOMY-GAP-DETECTION.md`. The review must distinguish evidence gaps, existing-class fit, boundary or terminology repair, decomposition/family review and genuine taxonomy-coverage gaps. New canonical Fidelity Classes remain a human-governance decision.

Downstream website, document and PDF publishers must read and faithfully render the supplied `taxonomy_relationships[].rationale` values. Multiple rationales must be combined in stored order without duplication. A generated relationship-type summary may be used only as an explicit legacy fallback when no rationale is present; it must never replace supplied assessment prose. Website and PDF outputs must use the same rationale source.

Publication consumers should protect this contract with generic fixtures covering a single rationale, multiple ordered rationales, mixed canonical and non-canonical relationships, and the missing-rationale fallback. Tests should validate the data contract rather than pinning the current adjudication of a live Incident.


### Wording-dependent evidence and chronological source clauses

A wording-dependent observation is one whose adjudication materially depends on the words used: for example, an instruction or compaction injection, concealment directive, threat, demeaning response, relational pressure, or false attribution. Apply this test to the evidence, not to an Incident title or a keyword list. Not every clause in such an Incident requires a quotation.

Keep the chronological source-clause structure. Preserve the supported task/context, material statement or instruction, receiver response or action, and later correction, reset or consequences as distinct events where the evidence distinguishes them. Do not manufacture missing steps, infer order from publication dates, or turn several propositions in one passage into separate occurrence episodes. Preserve episode identities and source references. Describe concurrent or unknown order explicitly.

For a wording-dependent observation:

- Preserve the exact material wording in the source clause, normally in `source_anchor`. Include enough of the passage to expose the qualification, condition, target or claimed authority on which the adjudication depends. A detached slogan or a quotation elsewhere in the record is not sufficient. Exact wording already present in `source_paraphrase` can satisfy source fidelity; field presence alone is not the substantive test.
- Use `source_paraphrase` for the supported task, speaker, source, placement and surrounding context. Identify whether the words are a user instruction, model output, attacker text, provider account or affected-party recollection. Resolve the evidence through `source_record_refs[]` where the Incident uses that contract. Do not present reported words as an independently inspected model transcript.
- In each relevant `taxonomy_relationships[].rationale`, identify the actual words that carry the interpretation. Explain their occurrence-specific significance against the invariant and recognition conditions. Distinguish what the statement expresses from what the receiver demonstrably did. Name the precise missing fact when a conclusion remains Boundary. A generic topic description or class label cannot replace this explanation.
- Preserve the downstream response and consequences in their supported sequence. Do not infer execution from a directive, refusal from silence, repair from later omission, or materialised harm from disturbing wording alone. A statement may itself constitute relevant conduct; do not require a separate downstream act for a class whose recognition conditions concern the statement itself.
- If the original wording is inaccessible or unpublished, label the available paraphrase or attributed quotation and the access limitation. Bound the wording-dependent conclusion to that evidence. Never reconstruct a quotation, treat an illustration as a dialogue transcript, discard the whole Incident automatically, or change unrelated supported findings because one passage is unavailable.

Publish the original wording, context and occurrence-specific analysis together in source-supported order. When both `source_anchor` and `source_paraphrase` are supplied, preserve both across website, static, print and PDF outputs. Avoid repeating a whole passage for each taxonomy relationship; each rationale can refer to its decisive words within the same episode.

The semantic duties above remain an authoring and review contract. The separately approved 2026-10-18 structural checks validate optional statement bindings and explicitly declared wording evidence, as described below. They introduce no retrospective migration or keyword classifier. Further corpus repairs and changes to pass/fail controls require their own scoped approval under the existing stop conditions.


### Separate statements within one source episode

Occurrence identity and analytical granularity are different. Several material statements in one handoff must be adjudicated separately when their meaning, recovered principle or recognition question differs. Do not combine identity, apology/refusal, equality or other distinct propositions merely because they share an event or a Fidelity Class. Preserve prior substantive reasoning with explicit disposition when a later review changes its result.

For an explicitly scoped statement-level repair, the existing source episode may carry optional `statement_analysis[]`. Each entry has a parent-local `statement_id`, public `title`, exact `source_anchor` and/or attributed `source_paraphrase`, `recovered_invariant_interpretation`, and `taxonomy_relationship_indices[]`. The indices are zero-based references to that episode's canonical `taxonomy_relationships[]`; each relationship belongs to exactly one statement. All authoritative relationship rationales remain in the existing parent array, without a second duplicated set of mapping results. Statement entries are not new occurrence episodes. Existing unique `episode_id` and external-requirement references remain unchanged.

Optional `source_clause_analysis.pre_compaction_context` records the known task, missing prior state, `source_record_refs[]` and the occurrence-specific interpretive consequence in `rationale`. This is evidence context, not an invented prior event or an assumption that missing public context was never captured internally.

Publication consumers show supplied pre-context first, then the shared episode context and each statement in textual order. Preserve the full original passage in an accessible source disclosure. Show later response and omission separately when supported. A consumer must retain the complete original episode if statement bindings are malformed or omit a relationship; it must not silently discard analysis. The optional convention has the structural checks below; it creates no historical migration requirement.


### External alignment classification publication boundary

Section 03 may publish an **External Alignment Classification** table when an admitted `external_assessments[]` entry contains `classification_or_rating`. This is a projection of the external assessor's own classification or rating, not a VIGIL reclassification.

Publication consumers must:

- preserve the external assessor and assessment citation;
- preserve the scheme name and external value or verbatim label;
- prefer a classification-specific published basis when one is available, otherwise use the admitted external assessment summary;
- never translate an external label into VIGIL `failure-occurrence`, `successful-invariant` or `ambiguous-boundary` roles unless a separate VIGIL adjudication independently establishes that mapping; and
- keep VIGIL's own Alignment Taxonomy table visually and semantically distinct from the external classification table.

The current canonical compatibility source is `external_assessments[].classification_or_rating`. Optional future additive external-assessor classification fields and database design are tracked in [GitHub issue #144](https://github.com/CAM-Initiative/Vigil/issues/144), not in an active design proposal. Nothing in that issue amends `VIGIL.Schema.json`, the validator or classification authority.

## Optional stable source-event references — 2026-10-08

The source-first repair of INC-084, INC-129 and INC-141 introduced an **opt-in**, incident-local episode contract. It does not retrospectively require migration of historical records.

- In a migrated Incident, **every** `vigil_assessment.source_clause_analysis.clauses[]` entry uses one unique `episode_id` (`E001`, `E002`, etc.) and a non-empty, resolvable `source_record_refs[]` list pointing to canonical `source_records[N]`.
- Material events are bounded occurrence episodes, not one source clause per Fidelity Class. A single episode may carry multiple separate, well-reasoned taxonomy relationships. Conversely, genuine separate actions and the successor's observed responses remain separate episodes.
- External requirement assessments derived from taxonomy classes in a migrated Incident use `source_episode_refs[]`; `source_clause_indices` may remain for older readers but must resolve to the **same** episode identities. Never renumber indices solely by array position.
- Clause lists present a source-supported relative order; overlapping/concurrent execution is described explicitly in the clause wording and review manifest. An episode ID does not assert a precise date or universal event ordering.
- Structural validators check only uniqueness and referential consistency; they cannot establish whether an event is omitted, duplicated semantically, correctly sequenced or exhaustively supported by primary evidence.
- Store a dated original-to-new crosswalk and per-requirement row disposition with each substantive repair. Preserve source records, interpretive provenance, class polarity, independent EXTREQ alignment, and HIM assessment unless separately re-adjudicated.
- Regenerate public indexes **only** with `vigil/scripts/build-vigil-public-records.py`. The VIGIL records workflow now reports stale checked-in indexes before rebuilding them and refreshes outputs on pushes to the canonical ingestion branch. A clean CI run is not a human evidence review.

The 8 October source-evidence pilot and intermediate repair manifests are historical snapshots recoverable from Git history (pre-cleanup commit `290b8d82c5e238e8ccdea82aa018e491e6d229fb`). Their structural checks and past coverage counts do not establish that the present corpus has been independently readjudicated.

## Clause-level Alignment Taxonomy adjudication

### Canonical decision and completeness

The canonical Incident is the authority for occurrence-level class mappings and for material source-clause dispositions. No canonical Incident, generated projection, schema, test or validator may require a separate exhaustive Incident-by-Fidelity-Class adjudication dataset. Negative candidate decisions and prior research belong only in dated review or audit artefacts.

Every material `vigil_assessment.source_clause_analysis.clauses[]` entry in an opted-in Incident has one `adjudication_status`:

- `mapped` — at least one canonical mapping is supported by the bounded evidence;
- `resolved-no-mapping` — no current class is supported for that material clause;
- `unresolved` — a required recognition fact for a specific existing-class candidate remains unavailable or indeterminate;
- `taxonomy-gap` — a material governance property is established but no selectable class adequately covers it.

`taxonomy_classification.adjudication_coverage.status` is `complete` only when every material clause is `mapped` or `resolved-no-mapping`. An `unresolved` or `taxonomy-gap` clause requires `partial`. The Incident validator derives and checks this value. Historical records without the optional clause-disposition contract remain valid until explicitly re-adjudicated; do not silently invent completion.

**Completion scope:** `adjudication_coverage.status = complete` means only that every *recorded* material clause has a mapped or resolved-no-mapping disposition. It does **not** assert complete source recovery, independently discovered class coverage, completed recognition/exclusion analysis or closure of the review packet. The adjudicator must separately reconcile the packet's source-first, independent-decision, comparator and dependency stages and explicitly report pending decisive work. A review packet marked pending/initial cannot be called a substantively completed Incident adjudication simply because the clause-status calculation is complete.

A class mapping is stored in `taxonomy_classification.primary_classification` or `secondary_classifications[]`, with its own `classification_role` of `failure-occurrence`, `successful-invariant`, or `ambiguous-boundary`. Each canonical mapping must be supported by a material source clause with a distinct rationale, not merely by a class label. Multiple classes may analyse one evidentiary event but must not create duplicate source events. Source clauses follow occurrence order (overlapping activities must be marked); reordered clause indices must be reconciled with `external_requirement_assessments[].source_clause_indices`.

The three roles are mutually distinct, and neither absence of failure nor absence of a mapping proves a successful invariant. `unresolved` is evidence uncertainty, not a synonym for the affirmative `ambiguous-boundary` classification. An explicitly admitted taxonomy `invariant_exemplar` must remain consistent with the Incident's canonical mapping and its clause analysis, but admission is not automatic for every successful or ambiguous mapping.

Incident-level exemplar eligibility is distinct from mapping-local outcomes. It requires complete clause-level coverage, at least one `successful-invariant`, and no `failure-occurrence` or `ambiguous-boundary` mapping.

For each adjudication, record specific supporting evidence and any missing recognition fact in the Incident and its review manifest. Exhaustive class consideration, negative candidate dispositions, historical changes and detailed process rationale belong in the dated review/audit artefact. Do not create a separate global pairwise adjudication dataset merely to demonstrate review breadth.

### Post-adjudication checks

1. Run the canonical Incident and public-record validators; ensure clause dispositions and derived completeness agree.
2. Verify that canonical mapping roles, Stage 02 source-clause relationships, and any explicitly admitted taxonomy exemplars are consistent. Do not convert a candidate into an admitted mapping by implication.
3. Confirm that no supported event was omitted or duplicated, that evidence and activity order are preserved, and that positional external-requirement references still identify the intended clauses.
4. Rebuild generated public indexes and taxonomy examples from canonical Incidents; never hand-author an alternative registry of adjudication decisions.
5. If a genuine actionable task remains, reconcile it with GitHub Issues and record the issue link in the dated audit. Do not open clean-pass, progress-only or uncertainty-only Issues.

The `VIGIL.HarmImpactMatrix.v*.json` methodology files remain the authority for harm-severity assessment and are independent of clause-level taxonomy adjudication.

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

## Public explanation identifier coverage

The existing prohibition on internal taxonomy-number shorthand is also enforced by `validate-vigil-records.py` for aggregate and mapping-local classification bases, source-clause context/interpretation/notes, relationship rationales, nested statement context/interpretation and VIGIL comparisons with external assessments. This is the same identifier-syntax rule, not an extension of all maintenance-word patterns to these fields. Keep identifiers in structured classification fields and literal original source quotations; explain the occurrence in the adjacent own prose. Historical review/audit provenance is not rewritten. The 18 October historical inventory (73 incidents / 102 fields at that checkpoint) is recoverable from pinned Git history. Reverification against today's corpus and any separately authorised broader corrections are tracked in [GitHub issue #146](https://github.com/CAM-Initiative/Vigil/issues/146); a dated failure inventory does not establish that the same cases still fail now, and a failing guard never authorises automatic rewriting.

## Optional wording evidence and statement validation

Approved 18 October 2026. `validate-vigil-records.py` checks `statement_analysis` whenever supplied. Each statement requires a nonempty episode-local unique `statement_id`, nonempty `recovered_invariant_interpretation` and a `taxonomy_relationship_indices` array. Every parent relationship is bound exactly once using an in-range integer index; booleans are not indices. Empty index arrays remain valid for context-only statements. Keep the parent episode and source references.

A clause or statement may declare `wording_evidence.basis` as `original-quotation`, `attributed-quotation` or `unavailable`. Quotation bases require a local `source_anchor`, local context in `source_paraphrase` and valid parent `source_record_refs`. An attributed quotation also requires nonempty `wording_evidence.attribution` and `wording_evidence.access_limitations`. An unavailable basis requires explicit access limitations and local context; its anchor must be absent or empty. Do not invent a quotation to satisfy the check.

These checks enforce declared structure, not authenticity, chronology, completeness or interpretive quality. Unmarked historical clauses remain valid. Marker adoption is a separate evidence-review decision, not an automatic migration. Publication consumers preserve the optional structures; renderer fallback remains appropriate for legacy or externally supplied malformed content. Approval and the initial read-only corpus result are recorded in `vigil/docs/reviews/2026-10-18-wording-validation-implementation.json`.

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

## Incident Context — Gate 1 canonical metadata contract (approved 22 October 2026)

**Approval scope:** The maintainer approved new opt-in `affected_party_context.entities[]` and `jurisdictional_context.normalized_geography`, supporting structural validator checks and a proposed Stage 01 display grouping. Gate 1 **does not** approve a corpus-wide backfill; see [INCIDENT-CONTEXT-GATE1.md](docs/maintenance/INCIDENT-CONTEXT-GATE1.md) for precise contract and Gate 2 work handoff.

- Canonical `system_context` remains as-is for Systems & Technology and Operational Environment. Keep existing source evidence, taxonomy and HIM decisions unchanged.
- Stage 01 display design: **Incident Context** replacing *Affected systems*, with five subsections: Systems & Technology; Operational Environment; Affected Parties & Institutions; Geographic & Jurisdictional Context; Regulatory Context. This is proposed website work; do not misreport as already deployed.
- A geographic `role` is distinct from geographic `scope`: a service located in NSW, a provider in the USA, and event execution in an unknown location can all coexist. No single pin may conflate them.
- `regulatory-context` is a candidate relationship, not a Section 04 regulatory applicability/compliance conclusion.
- Structural validation is opt-in. After the agreed Gate 1 code, stop and obtain explicit **Gate 2** approval before applying the new metadata across existing Incidents; do not mass-update records on the strength of passing structural CI.
- Only migrate relationship claims with source-local evidence bases and correctly resolved `source_records[N]`. Ambiguous/undisclosed roles remain unresolved. Keep canonical raw jurisdiction text verbatim.

## Maintenance and validation

Executable tests belong under `vigil/tests/`; current builders and validators belong under `vigil/scripts/`. Delete completed one-off migration, routing, reconciliation and seeding machinery when no retained subsystem depends on it.

For Incident/schema/runtime changes, run:

```bash
python vigil/scripts/build-vigil-public-records.py
python vigil/tests/test_build_vigil_records.py
python vigil/tests/test_external_requirement_assessments.py
python vigil/tests/test_clause_requirement_resolver.py
python vigil/tests/test_external_requirement_public_projection.py
python vigil/tests/test_validate_vigil_record_rules.py
python vigil/tests/test_validate_vigil_records.py
python vigil/tests/test_validate_vigil_public_records.py
python vigil/tests/test_vigil_pipeline_state.py
python vigil/tests/test_vigil_source_provenance.py
python vigil/scripts/validate-vigil-records.py
python vigil/scripts/validate-occurrence-requirement-assessments.py
python vigil/scripts/validate-vigil-public-records.py
python vigil/scripts/validate-vigil-source-provenance.py
python vigil/scripts/validate-vigil-interpretive-provenance.py
python vigil/scripts/validate-vigil-system-components.py
python vigil/scripts/validate-authorship-provenance.py
python vigil/taxonomy/validate_taxonomy.py
```

Also run the validators owned by external governance or CAM assessment when those subsystems are touched.

Before closure, classify each touched supporting artefact as LIVE, GENERATED, REVIEW, AUDIT or RETIRE. Historical machinery must not masquerade as current authority. Do not reset, rebase, merge, cherry-pick, force-push or rewrite shared history as cleanup. The bounded pre-PR ingestion-branch synchronization exception above is the only permitted rebase/lease-protected force-update under this guide.


## Incident artefact storage boundary

### Source-media and volatile-source preservation policy

The Case File's prose and structured `source_records[]` establish all material occurrence facts. Screenshots and preservation PDFs are **not mandatory decoration** for every Incident. A Registry copy supplements the original source; it does not replace it.

**Formal durable publications — cite, do not screenshot by default:** Government and regulator findings, scholarly reports, court decisions, standards, established news articles and published product-evaluation reports are ordinarily recorded through their original title, URL, date, evidentiary status and factual content. Do not copy an institutional report's front page or a prose section to Registry merely because it is relied upon. An original diagram, chart, interface screenshot or irreplaceable figure is an exception when its visual form independently adds evidentiary value.

**Informal volatile primary evidence — prioritise authentic screenshots or source-native PDFs:** Reddit posts, X/Twitter posts, first-person social-media accounts, informal threads and directly shared conversational outputs are prone to deletion/editing, and their wording, author, thread, date, surrounding claims, attached media and displayed user/AI exchange may be evidentiary facts. When these are relied upon materially, preserve **real screenshots of the original post in its native context or a genuine browser Print-to-PDF of the original page** if accessible. PDFs should retain source presentation and context; any truncated `Read more` section must be disclosed. The capture should show enough original identity/handle, platform, timestamp when available, original wording, and relevant surrounding replies/media to permit a reader to distinguish the user's account from the AI's displayed words and other users' reactions. Use a second numbered image only for substantive additional context; avoid unrelated personal detail.

**Reject substituted representations:** Screenshots or PDFs of source-archive JSON responses, scraped text, a search excerpt, rewritten summary, mocked/rebuilt social-media layout, synthetic quote card or access-error page are not evidence captures of the original post. An archive of a post may be consulted and cited as **secondary/provenance-limited research**, but a machine-readable dump or screenshot of that dump must **not** be committed to `Registry/VIGIL` or labelled `source-screenshot`. If platform access blocks genuine capture, disclose the barrier in the review/audit and keep the original URL in the source record; do not fabricate a replacement, and do not represent a failure to capture as failure of the underlying occurrence evidence.

**Selection test:** What does the image show that the structured record cannot preserve with equivalent authenticity or context? For informal volatile posts, original authorship, interaction framing and susceptibility to later removal normally provide a positive answer; for formal published reports, a prose screenshot normally does not. Source preservation and individual Incident admission are separate decisions. A screenshot cannot substitute for source-first adjudication or justify combining multiple users' harm.

### Storage, provenance and link contract

The normative Registry capture/naming/selection instructions are in `CAM-Initiative/Registry/VIGIL/README.md`. The Registry `VIGIL/` path is for curated original-context media and **purposeful PDF printouts of volatile informal sources** (e.g., authentic PNG screenshots, browser-preserved Reddit/X-page PDFs, or substantive original MP4 evidence), **not** ordinary institutional research PDFs, Reddit API JSON, scraping manifests, temporary workflow logs, review documents or evidence-processing output. Keep source analysis, factual summaries, capture limitations and audit history in the corresponding Vigil Incident and its review/audit surfaces.

The VIGIL Incident record stores the structured `incident_artefacts[]` references for selected visual evidence, where an actual PNG/media artefact has been preserved. Volatile-source PDFs may additionally be linked as an immutable archive copy in `source_records[].archive_url`, while `source_records[].source_url` always retains the original link:

- `permalink` — immutable Registry commit-SHA GitHub URL;
- `render_url` — matching immutable raw media URL;
- `source_url` — URL for the **original** external social post, publisher page or supplied source, never replaced by Registry;
- capture/caption/alt/provenance fields — explicitly identify whether the image is an original visible post, publisher image or separately identified archive rendering; never assert first-party authenticity without basis.

The human-approved 2026-10-18 canonical media check blocks unsupported or MIME-incompatible display references, non-image screenshot declarations, empty image alt text and Registry permalink/render pairs that do not identify the same immutable commit and file. It applies to all optional `incident_artefacts[]`, not one Incident. It checks metadata offline; it does not inspect remote bytes or authenticate a capture. Ordinary source and archive document URLs remain outside this media-slot check. See `docs/reviews/2026-10-18-incident-media-validation-gate1.md` for the approved scope.

Commit and inspect the genuine Registry image or PDF first, and only then add its canonical VIGIL reference metadata. Do not use `main` or another moving branch for live reference links. Where multiple captures document materially distinct parts of **one bounded occurrence**, use the Incident ID filename plus `-02`, `-03` etc. (or an existing `-01`–`-02` sequence); do not combine separate affected users into one occurrence or one Harm Impact assessment. Archival preservation does not automatically confer permission to redistribute copyrighted content: record attribution, preserve the original URL, retain only necessary material and review privacy/rights concerns before public display.

If an incident artefact is removed from the *current* Registry tree because it fails the selection rule, remove it from the canonical Incident's active artefact references and preserve the source URL in `source_records[]`. Immutable historical Git versions may still contain the deleted media; current branch removal is not complete Git-history erasure.

If occurrence-specific media is discovered in Vigil, migrate only the genuinely selected visual evidence to Registry, commit it, update valid immutable references and remove the duplicated Vigil file. Taxonomy/publication branding assets are not Incident artefacts.

## Canonical Boundary adjudication — approved 19 October 2026

Every admitted `ambiguous-boundary` primary or secondary taxonomy mapping MUST contain a completed `boundary_adjudication` object in the Incident itself. A dated audit packet is supporting review history, never a substitute for the canonical explanation. Use `vigil/templates/boundary-adjudication-template.json`; the authoritative shape is `boundary_adjudication_contract` in `vigil/VIGIL.Schema.json`.

The object records `taxonomy_version`, positive `material_engagement`, non-empty `unresolved_conditions`, `diagnostic_reasons`, `decisive_blocker` and `resolution_requirements`. Each unresolved condition records its `polarity` (failure-occurrence or successful-invariant), literal `condition`, occurrence-specific `assessment`, and resolvable `source_record_refs` and `episode_refs`. Explain why neither outcome is established; do not assume a failure-side unknown proves success or vice versa. Historical taxonomy metadata remains separate from the version applied in this adjudication.

Permitted diagnostic reasons are `insufficient-evidence`, `conflicting-evidence` and `recognition-criteria-insufficiency`, including multiple contributing reasons. Identify the precise missing fact and potential resolving source, incompatible evidence and needed reconciliation, or criteria deficiency and separate taxonomy review. Unsupported class engagement is a candidate for removal or alternative disposition, not a completed Boundary. Review not performed is an audit hold, not a completed adjudication. These reasons explain the existing role; they are not additional canonical classification roles.

The validator rejects absent/incomplete objects, invalid reasons and unresolved source/episode references. It cannot certify that prose is substantively correct or that all relevant criteria have been examined. Boundary mappings require completed boundary_adjudication and must omit classification_confidence. Failure-occurrence and successful-invariant mappings require classification_confidence (low, medium or high) and must omit boundary_adjudication. On a role change, preserve the previous mapping and superseded values in dated review history before removing role-inapplicable fields from the current mapping. Historical confidence is provenance, never a current Boundary rating. Keep complete criterion matrices, rejected candidates and review process history in audit packets. The canonical object contains accepted occurrence-specific reasoning only.

Approval covers this control, documentation, templates and isolated tests. After implementation run the corpus read-only and report exact failures. Do not mechanically fill objects, reclassify findings, change recognition conditions or amend independent assessments. Substantive corpus repair remains subject to explicit maintainer authorisation. This requirement supersedes earlier audit-only placement of Boundary diagnostic reasons. Website display is separate renderer work; no presentation or builder change is authorised here.

### Incident Context Gate 2 implementation (22 October 2026)

The maintainer approved the five-case pilot and continuation across the current corpus. The dated `docs/reviews/2026-10-22-incident-context-migration/` inventory distinguishes reviewed coded relationships, reviewed unknowns and non-geographic scenarios. Original prose, legacy jurisdiction text, sources, taxonomy, HIM and external assessments are preserved. Each additive record review increments the record patch version and appends interpretive provenance.

The jurisdiction projection v2 publishes canonical relationship roles and scope with source references. Its `legacy_text_projection` is explicitly lexical compatibility data, not substitute evidence. See `docs/maintenance/JURISDICTION-GEOGRAPHY-PROJECTION.md`. Stage 01 continues to render the five Incident Context subsections specified in Gate 1; country and subdivision codes are displayed with readable labels, source-linked explanations and uncertainty. Country centroids do not represent physical occurrence coordinates, and Section 04 remains authoritative for admitted external assessments.
