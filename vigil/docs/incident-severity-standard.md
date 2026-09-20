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
S1. S1 requires positive evidence of minimal materialised harm or a bounded
occurrence with no materialised downstream harm. In the latter case, the record
uses an empty `controlling_dimensions` array and a concrete
`no_materialised_harm_basis`; it does not invent a controlling harm type. If no
dimension is assessed and that positive bounded-no-harm evidence is absent, the
overall result is SU.

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

The matrix assesses physical health and safety; psychological wellbeing; rights
and liberty; equal treatment and non-discrimination; privacy and confidentiality;
financial and economic harm; property and asset damage; service, operational and
infrastructure impact; reputation and dignity; societal and democratic harm; and
environmental harm. These dimensions are separate because financial loss does not
establish asset damage, rights deprivation does not necessarily establish
discrimination, and democratic or societal harm does not establish environmental
damage.

The full S1–S5 criteria and stable threshold IDs are in the machine-readable
methodology.

### Digital infrastructure and effective destruction

For the property-and-asset dimension, digital infrastructure can be effectively
destroyed even when the underlying hardware and data bytes still exist. Where a
compromise causes a critical digital asset to lose trustworthy operational state
such that the affected asset cannot safely be retained and must be wiped and
rebuilt or reconstructed from a known-clean state, that consequence may satisfy
the S5 criterion for effectively irreversible destruction. Routine precautionary
reimaging, credential rotation or ordinary recovery work does not by itself
establish S5; the evidence must support loss of trusted state in the critical
asset itself.

Two dimensions contain quantitative operational anchors:

| Band | Financial/economic | Service/operational/infrastructure |
| --- | --- | --- |
| S1 | Direct realised loss below USD 10,000 without material livelihood or organisational-viability impairment. | No user-visible impairment, or positively evidenced non-critical interruption below 15 minutes within applicable recovery objectives. |
| S2 | USD 10,000 to below USD 1 million, or independently evidenced low and readily remediable economic disruption where no defensible conversion is available. | Limited non-critical degradation below 2 hours, critical interruption below 30 minutes, or a localised workflow failure resolved through routine recovery. |
| S3 | USD 1 million to below USD 100 million, or independently evidenced material but bounded livelihood or organisational loss where no defensible conversion is available. | Material important-service or workflow disruption; important-function outage over 2 hours; relevant cloud unavailability over 30 minutes; or limited availability over 5%/one million EU users for over 1 hour, with bounded recovery. |
| S4 | USD 100 million to below USD 100 billion, or independently evidenced substantial solvency, organisational-viability or widespread economic impact where no defensible conversion is available. | Essential or critical operation disrupted over 24 hours, material multi-organisation/jurisdiction operational impact, exceeded evidenced maximum tolerable downtime, or substantial external recovery. Production compromise alone is insufficient. |
| S5 | At least USD 100 billion, catastrophic insolvency or systemic economic loss. | Catastrophic or prolonged essential-service loss or operational collapse with comparably grave consequences. |

Financial bands apply directly to published USD realised loss. A conversion must
preserve the source amount, currency, conversion date and source. Without that
basis, a non-USD amount remains unconverted and can use a qualitative clause only
when the corresponding livelihood, organisational-viability or systemic
consequence is independently evidenced. An unpublished amount is `unreported`,
never zero.

The quantitative anchors are informed by MIT FutureTech's 2026 Delphi severity
work. VIGIL extends S4 through amounts below USD 100 billion to close the
otherwise unclassified USD 10 billion to below USD 100 billion interval. This is
a VIGIL operational adaptation; it is not attributed to MIT FutureTech.

Operational thresholds adapt functional-impact and recoverability concepts from
CISA and NIST and contextual sector anchors from NIS2 and DORA. Sector rules do
not automatically determine a VIGIL band outside their scope.

## External alignment and limits

MIT FutureTech's AI Incident Tracker uses a 1 (Negligible) to 5 (Catastrophic)
harm-severity direction and harm categories based on the CSET AI Harm Framework.
Its 2026 Delphi severity work is the principal external quantitative and
cross-domain anchor. VIGIL aligns direction and learns from those materials and
their evidence-bounded assessment practice, but owns its operational dimensions,
thresholds and ratings and does not claim equivalence or endorsement.

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
