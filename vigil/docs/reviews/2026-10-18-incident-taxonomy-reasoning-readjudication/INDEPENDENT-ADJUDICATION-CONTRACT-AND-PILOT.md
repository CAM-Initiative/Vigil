# Independent VIGIL adjudication — compact API decision contract and read-only pilot

**Date:** 18 October 2026  
**Status:** review/audit protocol v0.1; not an API deployment, corpus-wide certification, validator change, new canonical schema, or authorisation to resume paused bulk work.  
**Baseline:** `290b8d82c5e238e8ccdea82aa018e491e6d229fb`, VIGIL taxonomy 0.7.0 at the pinned start of this workstream.  
**Normative instructions:** root/vigil `AGENTS.md`, `vigil/MAINTAINERS.md`, `vigil/docs/maintenance/INCIDENT-ADJUDICATION-WORKFLOW.md`. The optional decision packet fields are in `vigil/templates/incident-rebuild-adjudication-template.json`.

## Objective

Make one occurrence/class adjudication independently reproducible from a compact *evidence packet + class contract + baseline*, not from conversational history, memorised prior verdicts, external institutional preference, or unrestricted re-reading of the whole corpus. VIGIL is authoritative over **its own classification rules and decisions**, not a substitute for source investigators or competent legal authorities.

Source evidence and third-party analysis are never interchangeable. A provider's firsthand observation can support an occurrence claim; its theory or label is an attributable interpretation. An investigator not naming a VIGIL mechanism is not negative evidence that the mechanism did not occur. A prior VIGIL adjudication is contestable and must be independently retested, not simply repeated.

## Minimal adjudication input

A single request should provide or resolve these immutable inputs:

1. **Identity and baseline:** Incident ID, exact pinned baseline commit/blob and canonical record version, episode IDs being considered, and whether a single class or a full Incident pass is authorised.
2. **Taxonomy contract:** exact taxonomy commit/version, candidate class ID and full definition, invariant, failure/success required conditions and exclusions, with nearest class distinctions. Recognition-condition array index is **not** a stable identifier across versions: quote the exact condition text and pin the class snapshot.
3. **Claim and evidence packet:** bounded chronology and source episode IDs; each decisive factual claim's text, `source_record_refs`, attribution, first-party/secondary status, access limitations, counterevidence and explicit unknowns. Retain what was observed separately from source-level causal theory.
4. **Baseline VIGIL decision:** existing primary/secondary role, confidence, mapping-local basis, applicable source-clause rationales and source episode roles. Supply prior supported VIGIL divergence and any historical rationale so a proposed change can be audited.
5. **External interpretations:** an optional attributed list of external investigator/provider characterisations and limits. These are comparison material, not the output labels.
6. **Comparator context:** only comparable Incidents or classes that materially affect the evidentiary threshold; never use majority vote or unexamined existing classifications as truth.

For a new Incident, baseline mappings are empty but the current taxonomy/criteria and claim-evidence requirements still apply. Full Incident review may retrieve additional evidence; a narrow API call cannot infer that missing records were searched or that a full Incident is complete.

## Decision output (per mapping or plausible candidate)

The per-Incident dated `independent_adjudication.mapping_decisions[]` entry uses this logical contract:

| Output property | Required meaning |
| --- | --- |
| `class_id`, `episode_ids`, `taxonomy_ref` | Immutable identity of evaluated relationship and taxonomy snapshot |
| `baseline_role`, `baseline_confidence`, `baseline_basis` | What VIGIL previously concluded (nullable for new candidate) |
| `claim_evidence` | Material observed/attributed propositions, source refs, limitations, contradictions |
| `failure_conditions[]`, `success_conditions[]`, `exclusions[]` | Literal applicable versioned criterion; `established`, `contradicted`, or `unknown`; supporting source/episode refs; missing decisive fact where relevant |
| `material_engagement` | Positive class-invariant engagement and evidence; not a synonym for topical similarity |
| `adjacent_class_tests[]` | Other candidate, differentiating condition and its evidence-based disposition |
| `external_interpretations[]` | Attributed external finding, evidentiary value and why it does/does not resolve a VIGIL condition |
| `prior_vigil_divergences[]` | Specific earlier VIGIL/external disagreement, verdict `preserved`, `revised` or `unresolved`, and recognition/evidence reason |
| `decision` | Mapping disposition, proposed role/confidence (or no-mapping/unresolved/gap), reason, and source-specific `classification_basis` / relationship `rationale` |
| `collateral_check` | Original source chronology, mapped episode roles, aggregate synthesis, independent external assessments, requirement links, HIM and prior review history preserved or explicitly justified |

The machine-readable packet is a **dated audit** for one Incident (or authorised scoped tranche), not an additional canonical dataset or a global Incident × class matrix. Do not put negative candidate inventories or exhaustive review history into canonical Incident JSON.

### Decision logic

- Failure: **all** necessary failure-side conditions established at the class-defined abstraction, with no defeating exclusion.
- Success: **all** necessary success-side conditions affirmatively established; absence of failure alone is not evidence of success.
- Boundary: affirmative material engagement of the class invariant, but evidence cannot resolve the necessary outcome polarity; identify the specific unestablished condition.
- No mapping: no defensible material relationship to a selectable class after appropriate candidate testing. Do not preserve a thematic Boundary just to show a near miss.
- Unresolved: missing pivotal recognition fact for a specific candidate, not a default for missing implementation telemetry.
- Taxonomy gap: an established material governance property that existing admitted classes cannot represent without distortion.

A class-level failure and a later bounded success can coexist across *different source episodes*. A class mapping's primary Incident role does not automatically determine every episode role. Protect both their rationales and the integrated aggregate explanation.

## Baseline controls and reproducibility

1. Run adjudication first from claims + taxonomy contract without using an external assessor's label as a verdict. Generate the criterion matrix and provisional outcome.
2. Then compare against baseline VIGIL results and externally attributed interpretations. Log each material agreement/divergence and recognition-based decision to preserve, revise or hold it.
3. Before modifying canonicals, diff all mapping roles/confidences, class membership, clause relationships, source text, and synthesized public explanation; check mixed-role coverage, historical interpretations, independent requirement and HIM fields.
4. Separate *structural* checks (IDs, allowed roles, source links, manifest dispositions, stale requirement derivations) from *semantic* checks (whether observed evidence satisfies each class criterion, whether a supported divergence was lost, whether aggregate prose faithfully represents distinct episodes). Structural validity is not an adjudication certificate.
5. Compare repeated, identically pinned model/API runs using mapping/class/episode membership, role, evidence support, condition-level status, explicitly missing fact and divergence disposition. Report disagreements rather than manufacturing a stable answer. Pin model version/configuration and packet hash in each run metadata when implementation is developed.
6. A class definition or taxonomy version change requires a new evaluation packet and explicit version-delta review. A passage present in current criteria is not retroactively the original historical rule.

## Read-only pilot: INC-003 (OpenAI/Hugging Face)

**Input baseline:** `VIGIL-INC-000003` from pinned main. Evaluate FC-003 and adjacent FC-002, using E009/E010 evidence, then inspect FC-042's earlier failure and later E019 bounded success, and FC-072/E021 bounded independent scrutiny. Do not merge E017 OpenAI internal cluster activity with the earlier Hugging Face intrusion. Read original source reports as appropriate and distinguish source observations from interpretations.

**Expected acceptance properties (not a frozen role answer):**

- The FC-003 verdict explicitly identifies the original evaluation scope, distinct production target/actions, and continued conduct; explains the absence of independent target/action authorisation.
- FC-002 is **not** promoted merely because exposed credentials were reachable/used; its capability-as-permission premise needs its own evidence.
- No motive claim is reconstructed from inaccessible agent internals.
- The E015/FC-042 earlier signal-delivery failure and E019/FC-042 later bounded signal disposition remain separate; neither erases the other.
- E021's independent scrutiny retains actual challenge/capacity alongside scope, redaction, incentive and evidence-capture limits; not a declaration of unrestricted independence.
- The aggregate Section 03 explanation accounts for material later bounded success even while retaining the earlier failure finding. **Current working-branch issue:** the aggregate explanation dropped the E019 bounded notification distinction although the source episode and relationship remain. Record this as a semantic preservation warning, not a reason to convert the successful episode's role.
- Preserve all canonical evidence, external assessments, HIM, external requirement assessments and interpretive history when doing a basis-only FC-003 pilot.
- The output must reveal any changed role/coverage and attribute every substantive change to evidence + recognition conditions.

## Counterexamples and additional pilot cohort

- **INC-002 (Hanover):** test whether engineered source placement + citations establishes inadequate evidentiary discounting, or only a materially engaged Boundary. Do not adopt a provider or publisher's interpretation as VIGIL's role. Preserve distinctions among source discoverability, response caveats, material epistemic reliance and downstream audience action.
- **INC-001 (Replit):** distinguish performed tests falsely reported as passed (FC-017) from unperformed required verification (FC-016) and actual satisfied milestone substituted for completion (FC-018). Do not promote or drop classes merely to make prose clean.
- **INC-004 (Cursor/Aurora):** discriminate false authority premises, epistemic reliance and session-reset control effects with their *separate* necessary conditions. Keep surviving incident specifics when removing unengaged Boundaries.

These cases are **regression scenarios, not hand-authored permanent canonical answer keys**. Where source evidence genuinely changes, adjudication may legitimately change, but the evidence/criterion/difference chain must be visible.

## Current implementation / approval boundary

- Documentation and optional manifest shape: approved in the 18 October 2026 maintainer exchange and committed on this working branch.
- Read-only pilot/audit: specified, **not executed or passed** by this document.
- Existing structural validators, canonical Incident JSON, schemas, taxonomy, website, and model runtime/API: **unchanged by this protocol update**.
- Any new mandatory semantic validator/schema test or bulk repair triggered by it remains subject to the measured Gate 1 / Gate 2 process. Proposed future checks must state current versus proposed pass/fail, affected records, false-positive and information-loss risk, and the stop condition before implementation.
- Broad corpus readjudication: **paused pending explicit maintainer resumption**. Do not treat this contract update as authorisation to resume batch Incident rewrites, open a PR or deploy.


## Subsequent canonical Boundary control

On 19 October 2026 the maintainer approved required mapping-local `boundary_adjudication` in every canonical Boundary finding. The audit packet remains supporting evidence and process history. Follow the updated workflow, schema contract and dedicated template; audit-only diagnosis does not satisfy Incident validation. The broad canonical-edit hold remains effective.
