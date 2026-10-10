# Phase 3 tranche 17C1 — 10 October 2026

Exact recovered baseline: `9a4f072351f217ddab47e7a1473660f73296f588`. Remote and checkout agreed before editing. PR #118 remains draft.

| Incident | Source-first correction | Old clauses | Episodes | Positional EXTREQ rows |
| --- | --- | ---: | ---: | ---: |
| INC-156 | Separate infrastructure outage, fleet confirmations/backlog, three emergency impacts, aggregate hotline evidence, transit effects, pause/retrieval, announced changes and later city review. Add SFMTA's originating 13 February filing. Correct the unsupported absence of emergency obstruction. Admit medium-confidence FC-042 from produced relocation signals stalled on the response channel. Retain unresolved fleet-clearance effectiveness. | 3 | 11 | 0 |
| INC-158 | Add Wiz's originating technical report. Separate missing RLS from the public connection key, information exposure, token capability, disclosure, partial fixes, demonstrated live post modification, write restriction/verification, later table fixes and cleanup. Combine the old authority-analysis duplicate with the actual access episode. Correct publication versus disclosure dates. | 5 | 9 | 0 |

Eight clauses became twenty episodes. Individual manifests preserve baseline source sets, clauses, taxonomy, HIM and every old-clause disposition. The two existing independent external results for INC-156 and three for INC-158 retain their outcomes. Changed bases incorporate the newly evidenced effects; no automatic compliance finding or class-derived candidate expansion occurred. Cumulative positional reconciliations remain 940.

City filing: https://www.sfmta.com/media/44577/download?inline=

Wiz report: https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys

The city describes 42 unduplicated reports, 829 vehicles and 1,593 provider-reported stoppages using different denominators. Hotline aggregates overlap the reconstructed emergency events; they are not added as 31 independent vehicle incidents. Operational effects overlap in time. The pause does not precede every obstruction or prove immediate clearance. The filing is originating agency evidence, not a CPUC finding. Private dispatch records and confidential vehicle submissions were not inspected. No collision, injury or patient outcome is established.

Wiz's disclosure timeline begins on January 31 and ends with its reported final fix at 01:00 UTC on February 1. The earlier exposure-start time is unknown. Research post modification is realised; credential impersonation and downstream prompt execution remain capabilities. Write restriction and failed reversal are bounded verification, not proof of discovery or recovery of every third-party copy. Cleanup timing is not forced into a wholly linear sequence.

HIM 1.0.1: INC-156 retains overall S3 with a strengthened operational basis. INC-158 retains privacy S4 and separately records S2 for the minor reversible test-post impairment. All eleven dimensions were reconsidered. No missing physical outcome is inferred from ambulance delay. No catastrophic data misuse is inferred from credentials alone.

Taxonomy 0.6.10 definitions and recognition/exclusions were screened. FC-042 is admitted at governance abstraction, consistent with INC-003's delivery threshold. FC-083 fleet-clearance performance remains unresolved; INC-156 therefore has partial taxonomy coverage despite completed bounded evidence review. INC-158 retains the noncanonical FC-002 boundary and complete unclassified disposition. Neither FC-084 nor FC-085 was promoted. No retired matrix was restored.

## Validation

Both `validate-vigil-incident-rebuild.py` guards passed against the exact baseline. The following commands passed:

```text
python vigil/scripts/build-vigil-public-records.py
python vigil/scripts/validate-vigil-records.py
python vigil/scripts/validate-vigil-public-records.py
python vigil/scripts/validate-vigil-source-provenance.py
python vigil/scripts/validate-vigil-interpretive-provenance.py
python vigil/scripts/validate-vigil-system-components.py
python vigil/scripts/validate-authorship-provenance.py
python vigil/scripts/validate-occurrence-requirement-assessments.py
python vigil/taxonomy/validate_taxonomy.py
python vigil/tests/test_vigil_pipeline_state.py
python vigil/tests/test_vigil_source_provenance.py
```

Canonical/public validation: 182 records. Source provenance: 637 sources. Taxonomy: 76 classes / 15 families. Second regeneration was byte-identical for all three generated outputs. Case File field crosswalk inspected: rich summary, factual basis, episode rationales, new classification and independent external bases retained in their separate canonical surfaces. The external website renderer was not run in this repository.

82 selected unit tests passed across record validation, record rules, episode integrity, prose quality, authorship, external assessments, clause resolver, external projection, rebuild guard and occurrence-role independence. The external assessment, resolver and projection scripts also passed directly (8, 3 and 2 tests).

Full discovery initially ran 234 entries with two failures and one missing-module error. Installing local `jsonschema` 4.26.0 resolved that environment error. The rerun completed 233 tests with two failures:

- `test_agent_environment_metadata.test_audit_counts_reconcile_to_corpus`: historical audit says 171; current corpus has 182.
- `test_external_assessment_candidate_audit.test_reconciled_corpus_has_no_unresolved_candidate_flags`: the heuristic expects no flags; 83 flags exist on the untouched baseline and 85 after the two added originating reports. Both new sources received explicit occurrence-evidence dispositions in their manifests. Changing the helper or permanent passing contract requires the maintainer gate.

Both failures were reproduced from a `git archive` of the exact baseline in an independent directory. No schema, validator, builder, permanent test or CI semantics changed. The complete suite is not reported as passing. Applicable remote CI must still be verified on the published commit.

## Recovery checkpoint

**162 of historical 179 reviewed; 17 awaiting, including seven holds. 72 of original 89 completed.** Active corpus: **182 records, 637 sources, 853 clauses/episodes, 1,315 external rows**. INC-189–191 are outside the frozen campaign baseline and still require acceptance review. Next subgroup: INC-160/163, then tranche 18 and the held track.

Gmail's latest labelled action snapshot was read. It preserves the retired-matrix correction and proposal actions. This clean checkpoint does not warrant a completion email; final outstanding actions will be reconciled under the existing protocol. AI-authored bounded review; independent human certification and exhaustive source verification remain unasserted.
