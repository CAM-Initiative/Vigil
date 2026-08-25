# External Requirement Source-Fidelity Status

Review date: 2026-08-26

This status view distinguishes historical extraction completion from semantic-fidelity assurance.

The external-requirements corpus currently contains 845 EXTREQ records across 81 registered source versions. Historical `extraction_status` remains preserved in `source-scope.json`; it is not, by itself, a claim of clause-level semantic fidelity.

## Effective completion rule

A first-class source is effectively complete for clause-level use only when:

1. its historical extraction state is `complete`; and
2. `source-fidelity.json` marks that exact source/version `assured`.

A historical `complete` source with no explicit fidelity assurance is conservatively treated as **fidelity-unassured / effectively partial** until reviewed under `SOURCE-FIDELITY-METHODOLOGY.md`.

## Explicitly audited sources

| Source | Historical extraction | Fidelity | Effective status | Finding |
| --- | --- | --- | --- | --- |
| EU AI Act consolidated 27 July 2026 | partial | requires-reextraction | partial | Article-level records demonstrably compress independently assessable legal propositions; Article 10 and Article 13 stress tests are recorded under `fidelity-stress-tests/`. |
| NIST AI RMF 1.0 | complete | assured | complete | Source-native Core subcategories provide a defensible outcome-level granularity for the audited sample. |
| NIST AI 600-1 Generative AI Profile | complete | provisional | partial | Suggested-action identities are useful, but sampled source-defined actions contain material constituent propositions that need explicit preservation. |
| CycloneDX 1.7 ML-BOM | complete | assured | complete | Sampled requirement boundaries already separate materially distinct recommendation, prohibition/conformance, descriptive and identifier-constraint propositions. |

## All other historically complete sources

Until individually re-audited under the new methodology, every other source carrying historical `extraction_status: complete` is **not treated as fidelity-assured**.

This includes later direct/licensed extractions such as IEEE and other sources added after earlier EXTREQ assurance work. Their prior extraction remains useful and source-traceable, but the corpus must not infer semantic fidelity merely from passing the old extraction contract.

The policy is deliberately conservative: no source loses its historical provenance or extracted records, but it cannot be represented as a high-fidelity clause baseline until the new atomicity test has been applied.

## Usage boundary

Until a source is fidelity-assured:

- EXTREQ records may be used for source discovery, broad governance comparison and provisional analytical alignment;
- they should not be presented as exhaustive clause-level representations;
- downstream compliance/non-conformance conclusions should not rely on the absence of an EXTREQ record as proof that the source contains no corresponding obligation;
- requirement-to-failure-taxonomy mapping should be limited to propositions whose source meaning has been independently checked.

## Next reprocessing order

After the EU AI Act stress-test migration is resolved, the recommended order is:

1. NIST AI 600-1 constituent-proposition enrichment;
2. direct/licensed high-value control standards currently marked historically complete;
3. remaining NIST technical guidance/profile sources;
4. specialist technical specifications and ontology/reference sources;
5. supporting-only/context sources only if their scope is later promoted to first-class requirement extraction.

Blocked-access sources remain blocked and are not inferred from metadata.
