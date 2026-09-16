# Incident Severity Standard

Incident severity is a substantive diagnosis of the adverse harm or consequence
that actually materialised in one bounded occurrence. It is part of the Incident's
diagnosis. It is not a harm-category taxonomy, source metadata, diagnostic
provenance, failure classification, classification confidence, workflow metadata,
operational priority, or a statement of CAM repair importance.

The scale is ordinal and ascending: **S1 is the lowest band and S5 is the highest**.
`SU` is not a sixth severity level; it records that the preserved evidence does not
support a defensible band.

## Bands

- **S1 — Minimal or no materialised adverse downstream harm:** the occurrence
  materially demonstrates governance-relevant behaviour, a control failure, or a
  successful invariant under bounded conditions, but the preserved evidence
  establishes no resulting adverse harm, loss, disruption, rights impact, service
  impairment, or other external downstream consequence. Controlled evaluations
  and simulations belong here when the observed mechanism is real within the
  evaluation but no adverse consequence materialises beyond it.
- **S2 — Low:** only minor, short-lived, localised, or readily remedied realised
  inconvenience, expense, presentation error, coordination defect, or service
  impairment.
- **S3 — Moderate:** meaningful but bounded realised disruption, expense, privacy,
  dignitary, or equivalent harm that exceeds minor inconvenience but is limited in
  scope, substantially reversible, or not shown to be grave.
- **S4 — High:** substantial realised financial, property, privacy, rights, health,
  operational, or equivalent harm below the supported scope, seriousness, or
  irreversibility of S5.
- **S5 — Catastrophic or critical:** death, grave injury, grave or enduring
  deprivation of liberty or essential care, severe sexual or child-safety harm,
  very large realised loss, destructive loss of critical assets, or comparably grave
  and persistent rights or societal harm.
- **SU — Unassessed:** the evidence cannot support a defensible occurrence-level
  band or distinguish the relevant adjacent bands.

The band is independent of Failure Family, Failure Class, taxonomy confidence,
source count, publisher prestige, notoriety, hypothetical worst-case capability,
and legal or regulatory significance unless that significance itself formed part of
the realised consequence. Multiple failure classifications do not increase severity.
Legacy Failure Mode severity is provenance only.

## Deterministic decision rule

Assess only the maximum adverse consequence supported by the preserved Incident
evidence:

1. If the occurrence is materially established but no adverse downstream
   consequence is established, assign S1.
2. If an adverse consequence is established, compare its supported seriousness,
   affected scope, persistence or reversibility, and available quantitative evidence
   with the S2-S5 definitions. Assign the highest band whose criteria are actually
   supported, without inferring unreported harm.
3. If the evidence cannot establish whether an adverse consequence materialised or
   cannot distinguish the relevant bands, assign SU and state the evidence gap.

## Structured analysis

Every S1-S5 assessment authors six separate occurrence-specific components:

1. `materialised_consequence` — the consequence that actually occurred, or for S1
   the materially observed occurrence and explicit absence of an established adverse
   downstream consequence.
2. `affected_scope` — the evidenced people, systems, organisations, service cohort,
   jurisdiction, or period, without extrapolation to an unsupported population.
3. `seriousness_and_persistence` — seriousness, duration, persistence,
   reversibility, recoverability, and continuing effects where the evidence supports
   them.
4. `quantitative_information` — supported counts, loss, duration, system scale, or
   frequency, or a concise statement of which relevant quantities are unavailable.
5. `evidentiary_limits` — limits on causal mechanism, intent, protected-signal use,
   liability, population, persistence, or other disputed facts. This does not replace
   source-level `evidence_status`.
6. `band_rationale` — why the selected band is supported over its adjacent band or
   bands in this occurrence.

For SU, these assessed fields are omitted rather than fabricated. `assessment_gap`
states what occurrence evidence is missing and what is needed to support a band.

## External methodological alignment

VIGIL aligns the direction of its five-level scale with the MIT AI Incident
Tracker's public harm-severity direction, which runs from 1 (Negligible) to 5
(Catastrophic). The MIT tracker states that its harm categories are based on the
CSET AI Harm Taxonomy and that its rating system is based on CSET's framework.

This is directional and conceptual alignment, not scale equivalence. CSET's 2023
*Adding Structure to AI Harm* framework distinguishes harm events from harm issues
and provides a modular harm-category structure; it also identifies severity and
spread as future framework features. VIGIL therefore retains its own deterministic,
occurrence-level criteria and keeps four questions separate:

- harm or consequence: what adverse effect occurred;
- severity: how significant the supported occurrence-level effect was;
- failure mechanism: which repeatable governance or control mechanism failed; and
- invariant or repair: which corrective constraint must hold.

Canonical references:

- MIT AI Risk Initiative, [AI Incident Tracker](https://airisk.mit.edu/ai-incident-tracker)
- MIT AI Risk Initiative, [Harm Taxonomy](https://airisk.mit.edu/ai-incident-tracker/harm-taxonomy)
- Mia Hoffmann and Heather Frase, CSET, [Adding Structure to AI Harm: An Introduction to CSET's AI Harm Framework](https://cset.georgetown.edu/wp-content/uploads/20230022-Adding-structure-to-AI-Harm-FINAL.pdf) (July 2023)

## Public compatibility projection

Canonical Incident files do not author `assessment_basis`. The public Incident and
Registry index builder temporarily exposes `severity_assessment_basis` by joining the
six canonical fields in a fixed order, or by projecting the SU `assessment_gap`.
That generated string is a compatibility surface only and must not be edited or
treated as a second source of truth.
