# VIGIL Harm Impact Matrix 1.0.0

VIGIL Incident severity is the highest supported materialised harm in a bounded
occurrence. It is not a likelihood estimate, a Failure Taxonomy classification,
classification confidence, source prestige, operational priority, or a statement
of hypothetical worst-case capability.

The canonical machine-readable methodology is
`vigil/methodologies/VIGIL.HarmImpactMatrix.v1.0.0.json`. External sources resolve
through the separate `vigil/references/VIGIL.ObservatoryReferenceRegistry.json`.

## Derivation

`Incident evidence → harm impact threshold(s) → highest supported harm → overall severity`

For every canonical dimension, record exactly one status:

- `assessed`: evidence supports a materialised impact and a threshold band;
- `unreported`: the dimension is relevant but published evidence does not report
  whether or how harm materialised;
- `insufficient-evidence`: some impact evidence exists but cannot support a band;
- `not-applicable`: affirmative context puts the dimension outside the bounded
  occurrence.

Absence of published evidence is not evidence of no harm. `unreported` is never
S1. S1 requires positive evidence of minimal or no materialised downstream harm.
If no dimension is assessed, the overall result is SU.

Overall severity is `max(assessed dimension bands)`. Do not average or add
dimensions. Multiple S2 harms remain S2 unless evidence independently supports a
higher threshold. Every dimension tied at the maximum is controlling.

## Bands

| Band | Canonical meaning |
| --- | --- |
| S1 | Minimal or no materialised adverse downstream harm, positively supported. |
| S2 | Low, minor, short-lived, localised or readily remediable materialised harm. |
| S3 | Moderate, meaningful but bounded materialised harm. |
| S4 | High or substantial materialised harm below catastrophic or critical consequence. |
| S5 | Catastrophic or critical materialised harm. |
| SU | No defensible overall band because no dimension has sufficient evidence for assessment. |

## Harm dimensions

The matrix assesses physical health and safety; psychological wellbeing; rights,
liberty and equal treatment; privacy and confidentiality; financial, economic and
property harm; service, operational and infrastructure impact; reputation and
dignity; and societal, democratic and environmental impact.

The full S1–S5 criteria and stable threshold IDs are in the machine-readable
methodology. Two dimensions contain quantitative operational anchors:

| Band | Financial/economic/property | Service/operational/infrastructure |
| --- | --- | --- |
| S1 | Positively evidenced no loss, or direct realised loss below USD 1,000 without livelihood or critical-asset impairment. | No user-visible impairment, or positively evidenced non-critical interruption below 15 minutes within applicable recovery objectives. |
| S2 | USD 1,000 to below USD 100,000 without substantial livelihood or viability impact. | Limited non-critical degradation below 2 hours, or critical interruption below 30 minutes, with normal recovery. |
| S3 | USD 100,000 to below USD 10 million, or meaningful bounded livelihood/property impact. | Important-function outage over 2 hours; relevant cloud unavailability over 30 minutes; or limited availability over 5%/one million EU users for over 1 hour, with bounded recovery. |
| S4 | USD 10 million to below USD 1 billion, or substantial livelihood, solvency or critical-property impact. | Essential operation disrupted over 24 hours, multi-organisation/jurisdiction impact, exceeded evidenced maximum tolerable downtime, or substantial external recovery. |
| S5 | At least USD 1 billion, catastrophic insolvency/systemic loss, or destructive loss of critical assets. | Catastrophic or prolonged essential-service loss, operational collapse, or destructive critical-asset loss with comparably grave consequences. |

Financial bands use USD-equivalent realised loss. A conversion must preserve the
source amount, currency, conversion date and source. An unpublished amount is
`unreported`, never zero. Qualitative threshold clauses apply only when the
corresponding consequence is evidenced.

Operational thresholds adapt functional-impact and recoverability concepts from
CISA and NIST and contextual sector anchors from NIS2 and DORA. Sector rules do
not automatically determine a VIGIL band outside their scope.

## External alignment and limits

MIT FutureTech's AI Incident Tracker uses a 1 (Negligible) to 5 (Catastrophic)
harm-severity direction and harm categories based on the CSET AI Harm Framework.
VIGIL aligns direction and learns from the evidence-bounded assessment practice,
but does not claim that its dimensions, thresholds or ratings are identical to,
interchangeable with, or directly derived from MIT/CSET.

VIGIL also adapts functional-impact, recoverability, continuity and regulatory
materiality concepts from CISA, NIST, NIS2, DORA and ASD. Those references supply
context and defensible anchors. VIGIL-HIM remains VIGIL's own deterministic
methodology for evidence-to-repair governance analysis.

The conceptual layers remain separate:

1. evidence establishes what is reported;
2. harm dimensions describe materialised consequences;
3. severity records the highest supported magnitude;
4. Failure Taxonomy classes describe the failure mechanism; and
5. invariants and governance repair state what must hold to prevent recurrence.
