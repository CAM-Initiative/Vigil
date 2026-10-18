# Environmental and animal welfare — adoption and control-impact review

Date: 18 October 2026. Artefact class: REVIEW / AUDIT.

## Authority and exact implementation

The maintainer reviewed the five proposed animal-welfare bands, including the explicit individual-death S4 / catastrophic collective S5 choice, and agreed that the proposal was reasonable. They then instructed completion of the implementation, corpus review, outputs, validation and PR readiness steps. Approval is recorded in `../2026-10-18-issue-126-maintainer-decisions.md` and the PR conversation.

This implements a **dated amendment to working HIM 1.1.0**, consistent with this branch’s existing dated working-version amendment practice. It does not introduce 1.1.1, silently relabel earlier methodology versions, or imply that earlier reviewers applied the animal-welfare criteria. The matrix records the adoption date, authority and historical boundary. `methodology-before.json` preserves the exact pre-amendment matrix.

The stable dimension ID remains `environmental`; its label becomes **Environmental and animal welfare**. All twelve IDs and threshold IDs remain stable. The existing ecological text is preserved verbatim as `ecological_criterion`. The new `animal_welfare_criterion` supplies the alternative below; `criterion` exposes both pathways to existing consumers. S1 is explicit that every pathway directly at issue needs positive no-harm evidence. Use the highest supported criterion within the dimension, then the existing overall maximum. Do not sum animal and ecosystem consequences.

| Band | Exact animal-welfare criterion |
| --- | --- |
| S1 | Positive bounded evidence establishes no material injury, suffering or impairment where animal welfare was directly at issue. |
| S2 | Minor, temporary pain, distress or injury, with straightforward recovery and no lasting impairment. |
| S3 | Serious but recoverable injury, illness or suffering requiring substantial treatment or rehabilitation. |
| S4 | Death, permanent major impairment, or severe prolonged suffering affecting an individual animal or a bounded group. |
| S5 | Catastrophic animal-welfare consequences, such as widespread mortality or severe suffering, assessed against the affected population and context. |

Actual consequence and material AI contribution are required. Assess seriousness, suffering, reversibility, scope and affected population/context together. Raw animal counts and elapsed days are not automatic bands. The policy distinction is owned by VIGIL; neither these bands nor this corpus review are empirical validation or a clinical standard.

## Current and proposed admissibility

Before: ecosystem damage is defined, but individual companion-animal welfare has no explicit numerical mapping. After: a substantiated actual animal consequence can be banded without claiming ecosystem damage or importing the human-health thresholds. No human-injury, monetary, Aggregate Harm or other dimension threshold changes.

Examples:
- Substantiated minor reversible animal injury, with material AI contribution: animal-welfare S2.
- Substantiated serious recoverable injury requiring substantial treatment: S3.
- Substantiated individual animal death with material AI contribution: S4; not human-health S5.
- Independently supported catastrophic collective animal-welfare consequence: S5; a count alone is insufficient.
- Zero ecosystem damage but an AI-contributed animal death: not S1; use the higher animal-welfare criterion.
- Alleged misdiagnosis/death without sufficient clinical/attribution evidence: insufficient-evidence, potentially overall SU.
- Lawsuit demand or mere procedural court activity: neither a financial-loss band nor a clinical finding.

**Structural pass/fail delta: none.** The existing validator already loads version-specific dimension thresholds and enforces exact IDs, status/band/reference consistency, maximum derivation and SU requirements. It cannot authenticate clinical evidence or adjudicate causation. No validator, schema rule, builder rule or publication guard has been weakened, bypassed or changed. Normative threshold recognition belongs in the methodology and substantive review, not a keyword-based clinical validator.

## Read-only measured impact and record boundary

The restored baseline contains 194 active Incidents; **zero have an assessed environmental row**. A bounded scan of summaries and factual bases for animal/ecological cues identifies INC-048, 058, 167 and 187. Review distinguishes veterinary information associated with a human care decision (048), an animal injury predating a generated police image (058), alleged AI diagnostic contribution to animal injury/death (167), and access to a fire-history data service without established habitat damage (187). The one known direct animal-welfare scope hold is 167. This scan is reproducible in `preservation-and-impact.json` and is not a guarantee of exhaustive future coverage.

No animal-welfare S-band is assigned to 167: original clinical/diagnostic records and material AI contribution remain insufficiently substantiated. The new row records the allegation under environmental/animal welfare, and the twelve-dimensional assessment is completed as SU. All previously accepted 170 HIM 1.1.0 records remain byte-identical. No unrelated environmental rebanding or automatic corpus migration follows.

Affected public surfaces: the existing Harm Impact environmental row/basis and methodology text. Generated navigation severity changes only when an independently supported overall band changes. The separately maintained website renderer is not changed by this task. The stable environmental ID preserves compatibility; the website’s displayed dimension label may need a later scoped update to show the expanded title, without changing the score.

## Preservation risks and stops

Risks include animal allegations becoming findings, single deaths being escalated to S5 by human analogy, S1 ecological evidence hiding animal harm, and broad ecosystem words being treated as actual damage. The criteria and occurrence audit preserve those distinctions. Stop on unsupported causal attribution, new schema/control requirements, unrelated corpus repair, information loss or introduced validation failures. Source records, taxonomy, external assessments, original quotations and episode identities remain preserved. No release exception or paper submission is granted.

## Other decisions

INC-082 applies the monetary S1 rule to US$4,820 as explicitly instructed; the rejected financial functional exception is not implemented. Privacy and impersonation independently support overall S3. The reported arrears are retained. The wording proviso on livelihood impairment is not silently deleted; the maintainer’s explicit monetary precedence for this case is retained in its audit and provenance.

INC-148 uses S2. The separately approved test change removes only `RegistrySourceRoleTests.test_recovered_consequences_are_banded_per_him_evidence` and its five-entry dictionary. The exact removed method is archived in `removed-frozen-test.txt`. No replacement frozen S2 assertion is added. Existing generic contract coverage remains, and all other tests are unchanged. Expected suite count decreases by one method; the measured fresh results belong in validation.json.
