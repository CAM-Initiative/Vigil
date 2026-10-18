# Issue 126 — maintainer decisions, 18 October 2026

Branch: `agent/incident-ecosystem-ingestion`. Existing PR: [137](https://github.com/CAM-Initiative/Vigil/pull/137).
This document records subsequent maintainer instructions. It supersedes the corresponding pending choices in the runtime checkpoint; it does not assert that implementation or canonical publication has occurred.

## INC-082: monetary threshold, no functional exception

Maintainer instruction: “The financial harm threshold is the threshold. INC-082 would have to reflect S1 due to the amounts. Sorry, can't make exceptions unfortunately.”

Apply financial S1 to the reported US$4,820. Preserve monetary evidence and the reported rent/electricity consequences. Withdraw the proposed functional-impairment exception; no new financial pathway or validator exception is authorised. Assess other dimensions independently and derive overall severity by the existing maximum rule. Record this instruction explicitly in adjudication provenance rather than deleting source-supported consequences.

## INC-148: S2 and removal of frozen test requirement

Maintainer instruction: “ok. approve inc-148 as s2 and remove the test requirement.”

Approved reassessment: S2 on the reviewed occurrence-specific evidence. Approved permanent-test change: remove `RegistrySourceRoleTests.test_recovered_consequences_are_banded_per_him_evidence` and its five-entry expected dictionary from `vigil/tests/test_registry_source_roles.py`. Preserve other tests and generic dimension, threshold, reference, maximum and controller checks. Do not replace a hardcoded S3 with a hardcoded S2. The canonical change, provenance, builders and fresh validation remain required.

## Environmental and animal welfare: agreed threshold direction

The maintainer requested ecological/animal-welfare thresholds and, after reviewing the proposed table and the individual-death policy choice, replied: “got you. what you've proposed seems reasonable.”

Record this as agreement to the presented threshold direction, including S4 for individual death/permanent major impairment and S5 for catastrophic collective consequences. This is not evidence of any particular animal's injury, death or AI causation. The exact versioned methodology/schema/control implementation contract remains to be prepared under the existing governance process.

Proposed dimension label: **Environmental and animal welfare**, retaining twelve dimensions and separate ecological and animal-welfare criteria within this dimension.

| Band | Existing ecological criteria, summarised | Agreed animal-welfare direction |
| --- | --- | --- |
| S1 | Positive evidence establishes no material biophysical degradation. | Positive evidence establishes no material injury, suffering or impairment. |
| S2 | Minor, localised, readily reversible ecological damage; recovery within 30 days is illustrative. | Minor, temporary pain, distress or injury, with straightforward recovery and no lasting impairment. |
| S3 | Meaningful but bounded damage requiring active remediation; restoration over 30–365 days is illustrative. | Serious but recoverable injury, illness or suffering requiring substantial treatment or rehabilitation. |
| S4 | Substantial, persistent or cross-jurisdiction degradation; serious ecosystem effects. | Death, permanent major impairment, or severe prolonged suffering affecting an individual animal or a bounded group. |
| S5 | Catastrophic, widespread or effectively irreversible loss of critical habitat, species or ecosystem function. | Catastrophic animal-welfare consequences, such as widespread mortality or severe suffering, assessed against the affected population and context. |

Ecological thresholds remain authoritative in the current matrix until an adopted amendment. Their time periods are illustrative, not automatic band triggers. The animal-welfare scale above is a VIGIL proposal, not an externally validated scientific conversion.

For implementation:
- Preserve the ecological criteria and keep their recognition separate from animal welfare; a companion-animal consequence need not imply ecosystem damage.
- Require actual consequences and material AI causal contribution; assess seriousness, suffering, reversibility, scope and context together. Raw animal counts and elapsed days alone do not determine severity.
- Use the highest independently supported criterion within the dimension and the existing overall maximum derivation, without summing outcomes.
- Missing information remains unreported or insufficient-evidence as appropriate, with overall SU where no dimension is bandable. S1 requires positive evidence.
- Preserve allegations, source-access limits and independent human consequences. A complaint, damages demand or procedural court activity does not establish an animal-welfare band.
- Prepare exact threshold wording, version handling, schema/validator/builder consequences, pass/fail examples and a fresh read-only corpus-impact assessment before control implementation. The earlier scan identified INC-167 as the known direct scope hold; INC-058's animal injury preceded the AI-generated police image. These are investigation leads, not a current exhaustive count or approval for unrelated rebanding.

## INC-167 and closure

INC-167 has no accepted new band from these decisions. The proposed scope expansion addresses methodology coverage; the missing complaint/clinical evidence, source limitations and causal uncertainty remain. Preserve the historical assessment until an admissible reassessment is implemented and reviewed.

Issue 126 stays open pending canonical publication, generated outputs, dated per-record audit and corpus facts, fresh validation, and accepted dispositions for every remaining case. No merge, deployment, manuscript submission or release exception is authorised.
