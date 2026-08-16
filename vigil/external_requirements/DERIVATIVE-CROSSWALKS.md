# Derivative External-Governance Crosswalks

Separate from Layer 1 direct-source requirements. Crosswalks record developer-asserted relationships; they do not supply target normative text or establish Caelestis conformity.

- Crosswalk records: 3
- Ingested mapping rows: 22

## SDOS-RuntimeGov-to-AI-RMF-v1.0

- ID: `XWALK-4DA14243F0798B04`
- Version/status: `1.0.0` / `final`
- Relationship: `supportive`
- Developer / host: AAM Cyber / NIST OLIR Program
- Rows represented: 0 (`not-ingested`)
- Conformance assertion permitted: `false`

- Provenance: NIST OLIR identifies this Final owner-authored informative reference as mapping SDOS v1.7 to NIST AI RMF 1.0 with a supportive, non-equivalent relationship.
- Provenance: NIST states that 49 AI RMF subcategories are mapped; the full row-level submission was not ingested in this work package.
- Provenance: The current SDOS primary source is v1.10. This v1.7 crosswalk is retained as version-bounded derivative evidence and must not be silently applied to later SDOS versions.
- Provenance: The live AAM SDOS page currently labels the AI RMF OLIR as Reference ID 220, while the NIST OLIR catalogue exposes the Final record at Reference ID 212. VIGIL treats the NIST catalogue as authoritative for OLIR record identity.

## SDOS-v1.10-to-ISO-IEC-42001-2023-supplementary

- ID: `XWALK-DC5FF445BBE12E1E`
- Version/status: `2026-05-12` / `owner-published`
- Relationship: `informative`
- Developer / host: AAM Cyber / AAM Cyber
- Rows represented: 9 (`representative-only`)
- Conformance assertion permitted: `false`

- Provenance: AAM Cyber labels this ISO/IEC 42001 mapping supplementary and informative and states that it is not part of the NIST OLIR submission.
- Provenance: VIGIL has not directly reviewed the ISO/IEC 42001 normative text in this work package. ISO clause/control labels are therefore preserved only as owner-authored derivative mapping data.
- Provenance: This crosswalk cannot be used to assert ISO/IEC 42001 requirement wording or Caelestis conformity.

## SDOS-v1.10-to-NIST-AI-RMF-1.0-representative

- ID: `XWALK-FBA9B555F37DB82F`
- Version/status: `2026-05-12` / `owner-published`
- Relationship: `supportive`
- Developer / host: AAM Cyber / AAM Cyber
- Rows represented: 13 (`representative-only`)
- Conformance assertion permitted: `false`

- Provenance: Rows are the representative mapping table published in the current owner-authored SDOS v1.10 reference document.
- Provenance: AAM states that a complete 49-subcategory mapping exists, but the current NIST OLIR Final record is explicitly version-bounded to SDOS v1.7; this file therefore does not represent the v1.10 sample as NIST-validated.
- Provenance: The mapping is informative/supportive and does not establish equivalence or conformity.
