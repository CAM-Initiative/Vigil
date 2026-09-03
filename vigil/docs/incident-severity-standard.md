# Incident Severity Standard

Incident severity is a substantive diagnosis of harm or consequence that actually
materialised in one bounded occurrence. It is part of the Incident's diagnosis. It
is not source metadata, diagnostic provenance, taxonomy metadata, classification
confidence, workflow metadata, triage priority, or a statement of CAM repair
importance.

## Bands

- **S1 — Critical:** death, grave injury, grave or enduring deprivation of liberty
  or essential care, severe sexual or child-safety harm, very large realised loss,
  destructive loss of critical assets, or comparably grave and persistent rights or
  societal harm.
- **S2 — High:** substantial realised financial, property, privacy, rights, health,
  operational, or equivalent harm below the supported scope, seriousness, or
  irreversibility of S1.
- **S3 — Moderate:** meaningful but bounded realised disruption, expense, privacy,
  dignitary, or equivalent harm that exceeds minor inconvenience but is limited in
  scope, substantially reversible, or not shown to be grave.
- **S4 — Low:** only minor, short-lived, localised, or readily remedied realised
  inconvenience, expense, presentation error, coordination defect, or service
  impairment.
- **SU — Unassessed:** the evidence cannot support a defensible occurrence-level
  band or distinguish the relevant adjacent bands.

The band is independent of Failure Family, Failure Class, taxonomy confidence,
source count, publisher prestige, notoriety, workflow priority, hypothetical
worst-case capability, and legal or regulatory significance unless that significance
itself formed part of the realised consequence. Legacy Failure Mode severity is
provenance only.

## Structured analysis

Every S1-S4 assessment authors six separate occurrence-specific components:

1. `materialised_consequence` — the consequence that actually occurred, not a
   hypothetical mechanism risk.
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

## Public compatibility projection

Canonical Incident files do not author `assessment_basis`. The public Incident and
Registry index builder temporarily exposes `severity_assessment_basis` by joining the
six canonical fields in a fixed order, or by projecting the SU `assessment_gap`.
That generated string is a compatibility surface only and must not be edited or
treated as a second source of truth.
