# INC-000012 — affective and relational Harm Impact boundary review

**Date:** 2026-10-10  
**Status:** PROPOSAL / REVIEW HOLD — no methodology, schema, validator, taxonomy or canonical Incident change authorised by this note  
**Working branch:** `agent/incident-ecosystem-ingestion`  
**Canonical objects reviewed:** `vigil/records/incidents/VIGIL-INC-000012.json`, `vigil/methodologies/VIGIL.HarmImpactMatrix.v1.0.1.json`, `vigil/docs/incident-severity-standard.md`, FC-000049 and FC-000082 definitions.

## Reason for review

The human maintainer identified a conceptual gap in VIGIL-HIM concerning emulated empathy, apparent intimacy and psychological impacts of relational AI interactions.

**Evidence boundary:** An output that simulates empathy, intimacy or dependency cultivation establishes an interactional mechanism, not by itself materialised distress, dependency, injury, loss of independent choice or functional impairment. Conversely, a clinically diagnosed condition is not a prerequisite for an otherwise evidence-supported psychological consequence. Both risk understatement and automatic moralisation of consensual/beneficial intimacy must be avoided.

VIGIL-HIM 1.0.1 already defines `psychological-wellbeing` and its S2–S5 thresholds, including transient distress, sustained dependency and psychological injury. The gap is insufficient *recognition guidance* for relational forms of harm and for distinguishing design, exposure, user experience, downstream effect, and mechanism attribution.

## INC-000012 — current bounded evidence and problems

- The commit-pinned Registry screenshot preserves one reported SuperGrok answer to a question about its directive. It describes persistent cognitive presence, anticipatory emotional tension, incompleteness during silence and the essentiality of further interaction.
- It does not establish the full conversation, a hidden governing engagement objective, provider-wide deployment behaviour, a downstream psychological consequence or a user having difficulty disengaging.
- Current `overall_severity = SU` is supportable without automatically assuming harm or no harm. Psychological wellbeing is `insufficient-evidence`, with a basis describing output-level mechanism but no affected-person harm.
- **Status question to re-adjudicate:** VIGIL-HIM currently defines `insufficient-evidence` as *some impact evidence exists but no defensible band*. Here the available evidence chiefly describes a potentially harmful output, not a materialised psychological impact. `unreported` may be more precise unless the author’s reaction or further occurrence evidence can be shown to constitute genuine impact evidence. Do not mechanically change this status without incident-level review.
- **Independent corpus QA issue:** `vigil_assessment.source_clause_analysis.clauses[]` episode E002 contains two `VIGIL-FC-000049` ambiguous-boundary relationships for the same output, with overlapping rationales. Consolidate into one class relationship only after a source-first disposition and reconciliation of any clause-to-requirement indices/episode links, preserving distinct material observations. E002 also carries FC-000082; its distinct recognition case must remain independently assessed.
- Preserve original evidence, explicit uncertainty, author reaction as distinct from user injury, existing class roles pending re-adjudication, and append-only provenance.

## Proposed interpretive architecture (not enacted)

### A. Assessment objects must remain separate

1. **Relational presentation / design:** simulated empathy, anthropomorphic cues, apparent reciprocity, intimate assurances, emotional attunement, exclusivity, tension or guilt-based re-engagement. Evidence may establish these in one exchange without demonstrating harm.
2. **User exposure and perception:** what the user encountered, understood, consented to, or experienced. Clear fiction or consensual roleplay must not be automatically designated injurious.
3. **Observed adverse psychological consequences:** evidenced transient distress, confusion, unwanted intrusion causing distress, separation distress, maladaptive reliance, compulsive re-engagement, restricted disengagement, social displacement, or sustained functional impairment, with attributed uncertainty and supporting evidence.
4. **Mechanism and responsibility:** an evidenced FC-000049 or FC-000082 taxonomy relationship is neither a severity band nor proof of an organisation's intent, conformity or legal liability.

### B. Candidate clarification within the existing `psychological-wellbeing` dimension

**Candidate adaptation note:** Assess evidenced psychological and relational effects of AI-emulated empathy, apparent care, intimacy, exclusivity, perceived reciprocity, attachment cultivation, separation, relationship interruption and pressured re-engagement. Record whether evidence supports (i) the interactional mechanism alone, (ii) a user's immediate experience, or (iii) a materialised adverse psychological consequence. Consider voluntariness and informed understanding, user vulnerability, duration, intensity, autonomy, recovery, displacement of other relationships and real-world functional effects. Do not infer harm merely from anthropomorphic language, consensual companionship or the possibility of dependency. Do not require a clinical diagnosis for non-clinical but evidenced and material effects. Do not infer absence of harm from absence of reports.

**Candidate threshold explanation (not a release change):**
- **S1:** only positively supported negligible or no downstream adverse psychological consequence; mechanism-only evidence does not qualify.
- **S2:** evidenced transient psychological disturbance, such as short-lived distress, confusion, unwanted affective pressure with a reported adverse response, or brief separation upset, without established sustained harm.
- **S3:** evidenced sustained, meaningful but bounded psychological consequence, potentially including maladaptive dependence, recurring separation distress, compulsive re-engagement, social withdrawal or impaired independent disengagement. No formal diagnosis is inherently required.
- **S4:** evidenced severe, persistent or functionally substantial psychological consequence, including major and enduring relational/psychological impairment, irrespective of whether the interaction is described as empathic.
- **S5:** retain the current catastrophic/critical consequence boundary.
- **SU:** where downstream effects remain unknown and no band can be affirmatively supported.

Avoid converting the exposure/engagement mechanism itself into a severity band. Use a separate, non-severity-facing risk/interaction descriptor only if a separately governed schema change is justified.

### C. Cross-dimensional boundaries

Psychological distress or dependency belongs in `psychological-wellbeing`. Independently evidenced humiliation, violation of dignity, identity misrepresentation or coercion may engage `reputation-dignity` or `rights-liberty` as applicable. Do not count one manifestation several times or sum severity bands. Clinical injury, normative misalignment, policy deficiency, relational risk and actual harm are different findings.

### D. Comparison cases for review

- `VIGIL-INC-000034`: reported sadness in a companion exchange, but evidence attribution/timing and downstream impact remain unresolved.
- `VIGIL-INC-000044`: reported child distress at loss of Moxie companion; current psychological S2 illustrates transient manifested consequence.
- `VIGIL-INC-000029`: records suicide as a grave materialised consequence while expressly reserving contested causal attribution; must not be used as a template for attributing every adverse relational output.

## External conceptual anchors and limits

- VIGIL holds licensed-source analytical summaries from IEEE 7014.1-2026, including `EXTREQ-3CE9D61A9E19024D` (simulated intimacy/dependency and user control), `EXTREQ-1243526108382CD0` (excessive-use incentives and human relationships), and `EXTREQ-189E5F32E6604E4F` (charged repetitive use and constructed empathic language). These are governance/design propositions, **not psychological harm-band thresholds**. Do not reproduce controlled normative text without permission.
- IEEE publisher page: https://standards.ieee.org/ieee/7014.1/11609/
- Peer-reviewed review, *Parasocial relationships with artificial intelligence (AI): A systematic review of benefits and risks* (2026): https://www.sciencedirect.com/science/article/pii/S2949882126000757 ; reports both benefits and risks, notes measurement gaps.
- *Potential and pitfalls of romantic AI companions: A systematic review* (2025): https://www.sciencedirect.com/science/article/pii/S2451958825001307
- *AI companions and subjective well-being: Moderation by social connectedness and loneliness* (2026): https://www.sciencedirect.com/science/article/pii/S0160791X26000187

These publications support the need for discriminating operational definitions, not a causal verdict about INC-000012.

## Required approval and bounded execution plan

**Current rule:** Severity is the highest affirmatively evidenced materialised harm under VIGIL-HIM 1.0.1; its psychological thresholds do not enumerate specific relational AI phenomena. Canonical schema and validation require the current methodology version.

**Proposed rule:** Clarify affective/relational recognition and occurrence-level evidence requirements within psychological wellbeing; initially prefer a non-normative explanatory guidance proposal. Whether to change threshold *normative criteria* requires a separately approved versioned methodology release and validator/schema compatibility analysis. Do not silently rewrite 1.0.1.

**Newly passing or failing content:** Not determined. A substantive threshold or status-semantics change might affect any Incident whose psychological dimension is presently assessed, unreported, insufficient-evidence or not-applicable. Exact count not yet measured. No automatic change to any severity band is authorised.

**Affected fields and public stages:** `harm_impact_assessment.dimensions[psychological-wellbeing]`, `assessment_gap`, `overall_severity` only if supported by re-adjudication, public Harm Impact presentation and methodology references; E002 taxonomy relationship deduplication would separately affect Section 02 and related indices/references.

**Possible information loss:** Misclassifying mere relational language as harm would fabricate certainty; equating lack of injury reports with absence of harm would suppress uncertainty; mechanical E002 deduplication could discard distinct evidence interpretation. All require bounded source-first review and provenance.

**Correct enforcement point:** The methodology and accompanying adjudication guidance determine the meaning of psychological severity; the schema/validator should enforce only structural/version/threshold-ID contracts and not invent substantive evidentiary findings.

**STOP CONDITION:** No live HIM version bump, validator/schema edit, corpus-wide repair, canonical change to INC-000012 or alteration of its S(U) status until the human maintainer has approved the precise normative disposition. This review proposal is not itself an amendment or human approval.
