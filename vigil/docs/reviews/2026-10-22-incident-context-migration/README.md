# Incident Context migration — canonical review complete

The maintainer approved Gate 2 on 22 October 2026: “Thats perfect. Please proceed with the rest of the full record set.” Country and subdivision codes carry structured geography; evidence explanations and all original text remain.

All 200 current Incidents have individual source-bounded context reviews: **98 reviewed-and-recorded, 87 reviewed-unresolved, 15 reviewed-non-geographic; zero not-yet-reviewed**. Of these, **93 have coded country relationships**. Five further reviewed multi-country or global records have no individually established country codes. Unknown is an evidence outcome, not skipped work.

`inventory.json` and `inventory.csv` contain the complete crosswalk inventory. Per-ID audits identify the sources used, evidence limits, versions and preservation hashes. `batches.json` records the five pilots and ten bounded batches (maximum 20 records each). `preservation.json` verifies all 200 against baseline e06710c; existing prose, sources, legacy geography, taxonomy, harm, external assessments and prior review history are unchanged. New reviews are AI-authored, not human authentication. Record-local source evidence was reviewed throughout; fresh public retrieval was selective and is stated per record.

The first 64 reviews are published in 0ede86c6a2f22d538ffe51a60d3bbe54f1b61b97. The remaining 136 reviews and geography v2 projection are published in 9e6da45c41de1b57633d3d0cc0c77564280a5887; all 200 per-ID audit commit references are populated. No new canonical records were admitted during this pass. The current branch was re-enumerated at the checkpoint.

## Evidence holds

See each audit’s `evidence_limitations` and canonical unresolved relationships. These include undisclosed users or infrastructure, unverified operator attribution, redacted evaluation targets, and incompletely enumerated multi-country populations. No provider headquarters, public-internet reach, language, currency, press-conference venue or contextual country mention substitutes for occurrence evidence. New sources can refine these completed evidence-limited reviews; no schema gap was found.

## Validation and projection

All canonical, public-record, source, interpretive, component and authorship checks pass. The final suite has 332 passing tests, including 11 projection tests. Early batch runs exposed a missing runtime jsonschema dependency; it was installed and the complete suite rerun. See validation.json for the exact final result.

The official builder regenerates public outputs, followed by the existing textbook-publication eligibility filter. The first publication omitted that final filter and therefore failed the generated-output CI gate: INC-032 / FC-035 and INC-043 / FC-088 must remain excluded from textbook examples under the existing preferred-evidence policy. The 23 October reconciliation applies that filter without changing either Incident or its classifications. Geography projection v2 publishes reviewed roles, scope, source refs and distinct-Incident country counts, retaining explicitly labelled lexical compatibility data. Unresolved geography never falls back to legacy text.

Website integration and its visual/accessibility checks follow on the existing catalogue branch. PR #155 remains draft. No merge is authorised.
