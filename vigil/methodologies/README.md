# VIGIL Harm Impact Methodology — versioned artefacts

The controlling current methodology on this branch is **VIGIL-HIM 1.1.0**, effective 2026-10-10:

- `VIGIL.HarmImpactMatrix.v1.1.0.json` — **current methodology** with 12 domains, S1–S5 domain-specific quantitative criteria incorporated directly into the controlling `criterion` wording, a distinct Relational Integrity and Autonomy domain, source-tested psychological attribution guidance, and exclusive specific-consequence versus explicitly modelled deployed-evaluation Aggregate Harm assessment pathways.
- `VIGIL.HarmImpactMatrix.v1.0.1.json` — **historical authoritative version**, effective 2026-09-20; preserve unchanged for currently adjudicated 11-dimension Incident assessments until individually re-reviewed.
- `VIGIL.HarmImpactMatrix.v1.0.0.json` — **retired version**, retained unchanged for earlier assessment provenance only.

New and substantively readjudicated Incident harm assessments use 1.1.0 and all 12 dimension rows. Older Incident assessments continue to validate against their **recorded version's own** dimension set, derivation rule and threshold IDs. Do not mechanically upgrade old versions, score new relational dimensions without evidence, or treat the presence of an old version as a missing/invalid record.

**Psychological harm:** attribute only evidenced new or incremental harm the AI caused, materially exacerbated or prolonged. A failure to respond to severe pre-existing distress may be a taxonomy/safety finding without proof of additional psychological harm. High-salience reinforcement is a mechanism, not itself a diagnosis or a severity band.

**Aggregate Harm:** a single alternative 1.1.0 assessment pathway for live deployed-model evaluation findings without a particular harmed person or group. Its band is **modelled from deployed evaluation**, not a victim count. It requires verified feature-specific eligible population or decision denominator, sources, real-world test route, substantive consequence and qualified evidence. It does not alter a specific incident's materialised-harm band and must not be conflated with registered platform users. Record `assessment_pathway`, and for each assessed generic row a source-backed `aggregate_harm_evidence` object, as enforced by the validator.

Reference and adoption history: `vigil/docs/reviews/2026-10-10-him-12-dimension-scale-exposure-proposal.md` remains a historical development record; it is **not** the controlling methodology. The public website catalogue is a separate repository and may still display 1.0.1 until separately updated and deployed.
