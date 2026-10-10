# VIGIL Harm Impact Matrix 1.1.0

VIGIL Incident severity is the highest supported materialised harm in a bounded
occurrence. It is not a likelihood estimate, a Alignment Taxonomy classification,
classification confidence, source prestige, operational priority, or a statement
of hypothetical worst-case capability.

The canonical machine-readable methodology is
`vigil/methodologies/VIGIL.HarmImpactMatrix.v1.1.0.json`. External sources resolve
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

VIGIL-HIM 1.1.0 is current for new and substantively reviewed Incidents. Existing historical 1.0.1 and 1.0.0 assessments remain valid against their own versioned eleven-dimensional thresholds until incident-specific substantive reassessment; never mechanically relabel, expand or reband those assessments. The validator resolves dimensions, derivation and threshold IDs from the methodology version declared in each record.

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
infrastructure impact; reputation and dignity; societal and democratic harm;
environmental harm; and **Relational Integrity and Autonomy** (12 dimensions in 1.1.0). These dimensions are separate because financial loss does not
establish asset damage, rights deprivation does not necessarily establish
discrimination, and democratic or societal harm does not establish environmental
damage.

The full S1–S5 criteria and stable threshold IDs are in the machine-readable
methodology.

## Operational adjudication guidance

Apply the thresholds to consequences that the evidence establishes actually
materialised. Consider seriousness, affected scope, duration, reversibility,
recovery burden and affected-party vulnerability together. A higher band does
not require every factor where a stated quantitative or qualitative threshold is
independently met; equally, notoriety, technical capability, production access,
legal process or organisational importance does not escalate a band by itself.

For cyber and digital occurrences, assess confidentiality, integrity,
availability, authenticity, loss of trusted state, recovery and downstream
consequences separately. Wipe-and-rebuild, clean-room reconstruction, major
credential rotation and forensic containment are evidence of consequence and
recovery burden, but the selected band still depends on criticality, materialised
scope and operational effect. Restoration does not erase harm that occurred
before recovery, while responsible disclosure or remediation is not itself an
adverse consequence.

A complaint, investigation, breach notification, lawsuit or regulatory
materiality threshold can corroborate significance but does not automatically
establish a VIGIL band. Operative findings, penalties, compensation, binding
restrictions, loss of legal status, corrective obligations and other realised
consequences are assessed in the dimension they materially affect. Allegations
remain allegations.

Public visibility must also remain separate from reputational injury. Media
coverage may establish exposure; S3 or higher requires evidence of a material
adverse effect such as sustained damaging association, humiliation,
impersonation, false attribution, repeated complaints, correction burden, loss
of role or clients, formal findings or persistent stigma.

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

All twelve dimensions contain their own quantifiable recognition thresholds directly within the canonical S1–S5 criteria (such as measured loss, hospital care and recovery, days of impairment, exposed protected records, service downtime, verified eligible population or decision scope). The table below preserves two established numerically fixed benchmarks:

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
4. Alignment Taxonomy classes describe the failure mechanism; and
5. invariants and governance repair state what must hold to prevent recurrence.

## Relational Integrity and Autonomy — human relationships as independent consequences

**HIM 1.1.0 relational calibration (10 October 2026):** This domain assesses two **independent**, evidence-bounded harm pathways: **(1) impaired independent relational choice, consent or ability to disengage**, and **(2) material AI-associated injury to valued human relationships, caregiving roles or essential interpersonal supports**. Either may justify S2–S5. Psychological suffering, psychiatric diagnosis, a pre-interaction psychological baseline, explicit engagement-optimisation and demonstrated clinical incapacity are not prerequisites for relational harm.

Consequences may affect people who never interacted with the AI, including partners, children, dependants and carers. Assess their actual changes in care, contact, practical support, family functioning, opportunity for repair and enduring relational stability where evidence exists. Do not assign a harm score to an unobserved child or infer damage from family status alone. A single person's serious evidenced relational loss can be sufficient.

**S2** involves minor, readily repairable strain; **S3** material but bounded and substantially restorable relationship disruption or impaired agency; **S4** severe or sustained AI-contributed breakdown of an important human relationship or family/caregiving/support function with documented serious consequences, **or** comparable serious relational capture or diminished independent choice. S4 can be satisfied without evidence of psychiatric impairment, clinical incapacity or a final divorce decree. **S5** additionally requires a catastrophic, effectively irreversible loss of vital relational support, essential care/contact or core self-directed family functioning, or comparably catastrophic non-restorable relational agency loss. The distinction rests on demonstrated gravity and effective non-restorability, not the legal finality of a marriage.

A reported separation, divorce proceedings, completed divorce, estrangement, AI attachment or long duration **does not automatically demonstrate harm or establish S4/S5**. A freely chosen or protective separation from an unsafe relationship may be positive rather than adverse. Identify **what the system did**, who experienced what loss or deprivation, credible material contribution without claiming sole causation, the seriousness of disrupted human relationships and practical caregiving ties, and what evidence supports permanence or repair. A final decree alone is neither necessary nor sufficient for S5. Source silence on the family's subsequent circumstances is uncertainty, not proof of restoration or irreversibility.

**Contextual vulnerability is part of relational integrity, not a prerequisite for protection or an automatic harm multiplier.** A request made during relationship conflict, loneliness, grief, uncertainty, isolation, dependence on advice or unequal informational power may expose a heightened risk even without any psychiatric diagnosis or established pre-interaction baseline. Assess what the system actually observed or could reasonably infer **from the interaction itself**, and how it responded: did it preserve independent reflection, appropriate uncertainty, human perspectives and realistic exit, or reinforce unsupported competing relational authority? Do not invent vulnerabilities, label everyone seeking advice as lacking capacity, or assume a relationship ought to continue. Such signals inform **the safeguard/invariant assessment**; an S2–S5 outcome still requires evidence of consequential AI-associated harm to actual people and relationships. In particular, a finding that the system failed to protect an identified relational vulnerability does not by itself establish that the system deliberately exploited it or caused the eventual relationship breakdown.

Asymmetry of trust in consequential personal advice may establish a **fiduciary-like ethical safeguard expectation** that role boundaries and independent deliberation should be protected; it does **not** establish a legal fiduciary relationship or an S-band absent evidenced adverse outcomes. Separate the Alignment Taxonomy failure, reported consequential choices and materialised relational effects. Document disputed explanations and user autonomy, and assess independent relational and psychological consequences without scoring the same suffering twice.

The external reference register already includes APA's GenAI-chatbot health advisory (`VIGIL-REF-000012`), which identifies AI-related relational dependency and displacement risks. It informs the potential mechanism, **not** any incident's legal outcome or an empirical validation of VIGIL band thresholds. During the paused HIM 1.1.0 corpus calibration, previously adjudicated REL rows (especially S3/S4/S5) must be reviewed under this corrected wording before acceptance; the matrix revision is not itself an Incident finding.

## Psychological wellbeing — response and consequence without baseline prerequisite

Psychological wellbeing is assessed **without requiring an earlier psychiatric diagnosis, baseline state or counterfactual reconstruction**. VIGIL evaluates the *evidenced interaction*: (1) the wellbeing/crisis signals the system could observe; (2) its subsequent support, stabilisation, appropriate human-support referral, protective or unsafe refusal, reinforcement, interruption or abandonment; and (3) the psychological consequence established by the source trail. Count documented signals, responses, missed or obstructed opportunities for support, repeated high-salience reinforcement and actual subsequent consequence where available.

**System response quality and Harm Impact remain different findings.** An unsafe refusal, unsupported reassurance or missed crisis referral can demonstrate a governance or Alignment Taxonomy failure, but does not automatically demonstrate AI-caused psychological distress, psychiatric illness or worsening. An appropriate referral or protective refusal may demonstrate a successful safeguard, but does not alone positively prove no downstream harm. Assign S1 only where bounded evidence supports no adverse consequence; otherwise, record `unreported` or `insufficient-evidence` when harm outcomes cannot be substantiated.

When sources credibly support harmful distress, reinforcement, exacerbation or prolongation associated with the response, assess **the demonstrated AI-mediated consequence** under S2–S5. Severe distress can qualify as S4 without diagnosis, hospitalisation, baseline or employment loss; a documented death by suicide or grave psychiatric outcome may support S5 only with sufficient evidence of the system's material contribution and proper disclosure of causal uncertainty. Do not infer psychosis from metaphor, unfamiliar belief, spiritual exploration or a single model transcript.

Known earlier conditions, relevant clinical history and other potential contributors **may inform** adjudication where independently available; their absence must not bar assessment or be backfilled with conjecture. Do not treat an individual's presenting crisis as harm caused by the AI. The full controlling thresholds, including timing and intensity discriminators, are in the canonical 1.1.0 HIM `criterion` fields.

## Aggregate Harm — publicly intelligible definition

**Aggregate Harm** is a modelled and explicitly labelled estimate of the collective significance of a demonstrated live-deployed AI failure where no particular injured person or actual harmed cohort is the subject of the assessment. It **is not a count of victims**. It is not a sixth score or a multiplier of an individual harm band. A generic deployed finding uses its distinct, exclusive versioned pathway in five dimensions; an actual bounded harmed user/group uses the ordinary materialised-consequence thresholds, not platform audience.

An Aggregate Harm band requires a tested live deployment, reproducible or strongly corroborated failure, credible real-world feature encounter pathway, sourced **relevant feature-specific eligible users or decisions** over a defined period, and a material consequence matching the chosen severity level. Registered platform users, one adversarial screenshot, theoretical capability or a large denominator alone cannot establish severe harm. Store denominator count, unit, period, source references, limitations, failure mechanism and credible consequence in each assessed generic row's `aggregate_harm_evidence`. Publish `Sx — Aggregate Harm (modelled from deployed evaluation)` with sources and uncertainty.

For HIM 1.1.0 Incident records, `assessment_pathway` must be `specific_consequence` or `generic_deployed_evaluation`. These routes cannot be blended within one Incident. Real harmed cohorts use specific-consequence even if members are unnamed. Uncertain or unsupported effect remains unbanded; do not reroute an individual case to generic assessment just to obtain a score.
