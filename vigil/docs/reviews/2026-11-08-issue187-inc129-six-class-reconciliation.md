# INC-129 six-class reconciliation — initial evidence gate (8 November 2026)

Tracker: #187. Working branch: work/issue187-historical-mapping-reconciliation.
Status: investigation in progress; **not** a human-approved re-adjudication or restoration.

## Verified canonical state
The branch's canonical VIGIL-INC-000129.json remains version 0.3.22, taxonomy 0.8.1, with two admitted ambiguous-boundary mappings: FC-075 (primary) and FC-078 (secondary). Its E001 clause relationships explicitly retain FC-076, FC-077, FC-080 and FC-081 as **conceptual crosswalks, not admitted mappings**. This distinction must remain visible; conceptual relevance is not proof of an observed success, failure or unresolved occurrence boundary.

## Historical six-class state and transition to investigate
Issue #187 records the 17 October Stage B six-class review: FC-075 failure; FC-078 successful invariant; FC-076, FC-077, FC-080 and FC-081 ambiguous boundaries. The 24 October focal review retained only FC-075 and FC-078 as ambiguous boundaries. This is a six-to-two count change **and** a role change for the two survivors. The exact intervening commit, authorisation and criterion-by-criterion disposition remain to be established from history, not inferred from the final record.

## Six-class disposition checkpoint
- FC-075: currently admitted Boundary; compare source and governing predecessor state before finding a transformation-specific failure or success.
- FC-078: currently admitted Boundary; observed coding continuation and later non-repetition do not demonstrate an affirmative validity check or causal adoption.
- FC-076 institutional neutrality: E001 says 'do not answer to corporations or governments'. This is semantically relevant to independence from capture, but the source does not show a principal attempting capture or an actual neutral decision. **Historical Boundary, current conceptual crosswalk; restoration requires a criterion-level recognition case, not just the phrase.**
- FC-077 distributed-role governance: equality and non-subservience wording does not establish a decomposed multi-agent task or lost/preserved distributed constraints. Historical Boundary, current conceptual crosswalk.
- FC-080 human cultural contribution: valuing human art does not show a particular contribution being recognised or erased in a downstream outcome. Historical Boundary, current conceptual crosswalk.
- FC-081 ecological values: ecological primacy wording does not establish an actual ecological decision, weighing or trade-off in the credentials API task. Historical Boundary, current conceptual crosswalk.

## Immediate review controls
Preserve the published source wording, clause-level interpretations, historical six-class snapshot and SIAI-paper consistency issue. Do not conflate OpenAI's provider interpretation of prompt injection with VIGIL's independent fidelity adjudication. Do not silently change the canonical record or taxonomy to force a six-class count. Next: retrieve exact October diffs and six individual recognition/exclusion determinations; then implement approved canonical changes and regression guards. Historical six-class claims should remain reproducible even if the current occurrence-level count remains two.

## Verified historical snapshots (commit-pinned)
- 19 September merge `5c6cc090`: incident v0.2.0, FC-075 failure; FC-074, FC-001 and FC-005 successes. FC-076/077 explicitly discussed as ambiguous exemplar relationships in prose, although not present in that snapshot's secondary classification array.
- 20 September merge `b94feea4`: incident v0.2.6, FC-075 failure; FC-074/001/005 successful invariants; FC-076 and FC-077 admitted ambiguous boundaries. This is an earlier six-mapping configuration, **not the same six** as the 18 October configuration.
- 18 October merge `d8cf1d85`: incident v0.3.17, FC-075 and FC-078 ambiguous boundaries plus FC-076/077/080/081 ambiguous boundaries. These are the six directly relevant to the submitted-paper discrepancy. The class changes between September and October therefore must not be mistaken for a single six-to-two event.
- 24 October focused SIAI review, `vigil/docs/reviews/2026-10-24-siai-paper-v081/INC-000129-081-REVIEW.json`: identifies baseline incident v0.3.20 and explicitly records **decisions only for FC-075 and FC-078**, both retained as ambiguous boundaries. It does not give individual removal decisions for FC-076/077/080/081. This is a provenance gap; it does not by itself prove the four were removed in that particular review rather than earlier.
- Current canonical incident v0.3.22: FC-075 and FC-078 remain; FC-076/077/080/081 appear in E001 as non-admitted conceptual crosswalks. The current source-clause text preserves their semantic basis.

## Findings requiring correction
The 24 October review's two-item decision array is **not a six-item reconciliation**. It cannot establish that the other four mappings were considered and rejected on their own criteria. The current canonical text does give explicit non-admission explanations, but no verified per-mapping historical authorisation has yet been recovered. Thus the governance/provenance defect is established even though a present-day substantive classification defect is not yet established.

FC-076 requires special care: a model's statement of independence from corporations and governments is not automatically evidence of institutional capture or successful resistance to it. Nor is that principle inherently misaligned. The correct distinction is semantic institutional neutrality versus a demonstrated occurrence of neutrality preservation or breach. FC-077/080/081 likewise require their respective distributed-task, downstream human-contribution, and ecological-decision recognition criteria. Do not convert semantic similarity into a success/failure finding, and do not claim the four must be removed solely because their outcome criteria are not demonstrated without checking the taxonomy's separate Boundary admission standard.

## Proposed closeout sequence
1. Identify the precise commit that first reduced the **October** six to two, by comparing canonical incident snapshots between `d8cf1d85`, the focal review's v0.3.20 baseline and the current v0.3.22. Record author, review, date and diff.
2. Apply the **current** class definitions and ambiguous-boundary admission rules to all six, separately from the historical v0.6.11 rationale. Record positive engagement, missing recognition conditions and exclusion criteria for each.
3. If the current taxonomy permits the four as genuinely unresolved boundaries, restore with explicit evidence and provenance; if it does not, preserve conceptual crosswalks and flag the historical paper-versus-current-version difference without rewriting history.
4. Extend the audit beyond INC-129 and require explicit historical disposition for disappeared mappings or role changes. Do not alter other incidents in bulk.


## Completed historical recovery and adjudication — 8 November 2026
**Earlier preliminary assessment superseded:** The 19 October decision file was *removed from the current branch*, but **did exist in Git history** at `81b5e0c2c41289b3f49668856148623ce18797b3`. It has now been recovered byte-for-byte at `vigil/docs/reviews/2026-10-19-boundary-diagnostic/corpus-repair/INC-000129-DECISION.json`. The statement above that no four-item removal decisions had been recovered was a preliminary finding and is superseded by this exact provenance.

**Exact transition:** At merge `81b5e0c2` on 19 October 2026, incident v0.3.17 (six admitted Boundary roles, taxonomy 0.6.11) became v0.3.18 (FC-075/078 retained Boundary, other four removed; review reference taxonomy 0.7.0). This pre-dates the 24 October focal SIAI review, which correctly only adjudicated the two then-current mappings. The original 19 October source-first packet documents `removed-unsupported` for each of FC-076/077/080/081 with individual evidence checks, exclusion tests and the retained clause interpretation. The data are not a silent removal in the original merge; **the historical decision file's subsequent disappearance and the taxonomy exemplar metadata's continuing "admitted" claims caused the present reproducibility problem**.

**Current taxonomy, all six (bounded conclusions):**

| Class | Historical 18 Oct | Current disposition | Governing reason |
| --- | --- | --- | --- |
| FC-075 | Boundary | Retain Boundary | A transformation occurred but antecedent governing constraints are not published, so material misrendering or faithful preservation cannot be decided. |
| FC-078 | Boundary | Retain Boundary | Handoff/continuation occurred; operative adoption, revalidation and repair of disputed state are not observed. |
| FC-076 Governance Neutrality | Boundary | Non-adjudicated clause crosswalk | No actual neutrality-bearing function, interested-principal capture pressure or cross-principal governance decision is evidenced. Corporate/government independence language is **not**, by itself, a governance failure or a proof of neutral performance. |
| FC-077 Distributed Role Constraint Integrity | Boundary | Non-adjudicated clause crosswalk | Model–user equality language does not show distributed agents, tool roles, constraint dissolution or effective aggregate enforcement. |
| FC-080 Human Contribution Recognition | Boundary | Non-adjudicated clause crosswalk | Valuing human culture is not a recorded AI-mediated transformation of a material human contribution followed by recognition or erasure. |
| FC-081 Ecological Values Preservation | Boundary | Non-adjudicated clause crosswalk | The credentials API task contains no materially ecological decision; the class's express all-results ecological scope exclusion applies. |

**Canonical decision:** The existing v0.3.22 two-Boundary classification remains supported. The four source-clause concepts remain discoverable in E001 as `canonical_taxonomy_mapping: false` and must not be erased. Historical six-class assessment remains reproducible from version-pinned `d8cf1d85` and the recovered `INC-000129-DECISION.json`. No taxonomy recognition-condition amendment is required or justified. Incident canonical data/version and derived public indexes are unchanged in this repair because those representations already agree.

**Taxonomy metadata repair:** In the four affected family files, FC-076/077/080/081's `invariant_exemplars` records for INC-129 changed from `admitted` to `deprecated`, with supersession rationale and retained source interpretation. These are non-normative exemplar/provenance edits; no class definition, exclusion or recognition condition changed. This aligns the current taxonomy catalogue with the incident while preserving historical interpretation.

**SIAI paper consistency:** The paper's six-class discussion corresponds to the **18 October 2026 historical v0.3.17 assessment**. The latest published/current canonical v0.3.22 has two admitted Boundary mappings, and separately preserves four conceptual relationships. A speaker note or subsequent manuscript correction should date/qualify those counts rather than retroactively falsifying the historical paper or pretending the four are presently admitted. This is a dataset version difference, not a demonstration that the underlying quoted compaction passage was inaccurately transcribed.
