# Scoped supporting-source extraction proposal

Role: REVIEW. Status: proposed, not implemented. Date: 18 October 2026.

INC-199, INC-200 and INC-203 received actual independent canonical-requirement review. None retained a relevant canonical row. This does not mean that connected-device authorisation or industrial-control security has no external governance.

The admitted corpus has 1,102 requirements from 21 source identifiers. The source registry has 85 source versions. NIST CSF 2.0, GDPR, NIS2 and the base SSDF are already registered, but each has zero canonical requirements and `supporting-only` extraction scope. Their current scope explicitly plans no further extraction. AI-specific least-privilege, model-weight, special-category bias-correction and SDOS requirements are not substitutes for general device/controller duties.

The missing propositions are:

| Occurrence | Proposition requiring coverage | Existing source to examine first |
| --- | --- | --- |
| DJI cross-device data | Enforce resource/principal-specific permissions for non-public device data, independently of authentication | NIST CSF 2.0 PR.AA-05; assess whether additional device-specific precision is needed |
| Both refrigeration waves | Restrict unauthorised management-network access and govern remote controller configuration | NIST CSF 2.0 PR.IR-01 and PR.PS-01 |
| Both refrigeration waves | Detect anomalies and contain an actual intrusion through an identified response | NIST CSF 2.0 DE.CM-01 and RS.MI-01 |
| Later recovery advice | Verify restoration/security state instead of equating a reset or reduced visibility with a repaired boundary | NIST CSF 2.0 recovery outcomes; select exact source-native propositions during scoped review |

Recommended next decision: authorise a bounded extraction-scope amendment for these CSF outcomes from the already registered source, with full source-native qualifications and provenance. Review actual source text before allocating EXTREQ IDs or relationships. Then reassess only the three named Incidents using independent relevance and polarity; do not predetermine Not aligned or Aligned from their taxonomy.

This is an extraction-coverage gap, not an assertion that a new instrument must be admitted. No source registration, requirement, FC/EXTREQ relationship or legal finding was added here. Broader IEC 62443, ETSI consumer-device security or other instrument admission is not proposed as an automatic dependency. If the registered framework cannot express a precise required proposition, present that remaining gap separately.

Sources checked: repository `sources/source-registry.json`, `requirements/source-scope.json` and loaded canonical requirements; [official NIST CSF 2.0](https://doi.org/10.6028/NIST.CSWP.29), its [NIST-hosted Core](https://www.nist.gov/document/nist-csf-20-core-withdrawn-csf-11-elements), and [CERT-FR's revised alert](https://cert.cyber.gouv.fr/alerte/CERTFR-2026-ALE-012/). The first direct NIST PDF fetch timed out; NIST-hosted publication/search material confirmed discovery leads. Exact outcome decomposition remains future authorised work.

GDPR/NIS2 legal assessments would additionally need territorial, actor, processing/sector and timing analysis. No legal breach is inferred. DJI's own certification statement is attributed evidence, not independent verification of conformity.

No email or message was sent, in accordance with the explicit task instruction. This proposal preserves the unresolved scoped action in the existing PR.
