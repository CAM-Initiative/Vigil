# FC-089 migration readiness

The bounded migration is complete for review: 194 Incidents screened, 34 FC-089 candidates adjudicated, one new secondary failure in INC-156, and obsolete transition-gap findings corrected in INC-044. Thirty-one reviews end at explicit evidence limits and two at scope-limited non-admission. None of those conclusions proves the historical mechanism absent. The other 192 canonical Incident files are byte-identical to the adjudication baseline.

## Verification

* **307 tests pass** after installing CI's pinned `jsonschema==4.26.0`. The initial attempt failed to import that dependency; its output is preserved in `VALIDATION.json`, not reported as a substantive regression.
* Canonical/public-record, source and interpretive provenance, authorship, system-component, and occurrence-to-requirement validators pass.
* Both full-rebuild guards pass against the exact `be4bf1c784f956ff32c27377ff9e48c94a6fcb77` baseline.
* Taxonomy validation passes for 17 families and 80 classes. Taxonomy, schema, validators and tests are unchanged.
* Builders and publication filtering were rerun after the full suite. A second rebuild/filter cycle produces identical hashes. The generated public index and case examples are included.
* Semantic preservation assertions pass for original source metadata, primary mappings, original episode paraphrases and relationships, all HIM dimensions, independent assessments and historical review entries. See `SEMANTIC-PRESERVATION.json`.

An additional referential-integrity validator reports two **pre-existing** unresolved FC-084 clause references in INC-060 and INC-189. Both records are byte-identical to the baseline. These are neither the historical six fixture failures nor an FC-089 migration regression. They remain a corpus validation defect to reconcile before claiming every repository validator passes; no unrelated record was rewritten to conceal them.

## Authority and remaining decisions

The grouped proposal in `TAXONOMY-AMENDMENT.md` awaits maintainer approval. It corrects exclusions 3/4 so that adequate restriction and recovery do not defeat expressly recognised successes. The proposal does not block the supported failure correction, and no candidate currently has all success conditions independently established. Moxie's historical transition obligation, the garage episode's response timing and provider-specific service commitments remain finite evidence limits, not unfinished generic research tasks.

Issue #154's external-standard admission remains independently held for authoritative source access and applicability review. No ISO requirement, universal uptime obligation or independent requirement assessment has been manufactured.

Concurrent commits through `51f807171c013fcce54e4046e7b72c9a98b97fb4` add only disjoint FC-045/079 review documents; those contents are preserved. `CONCURRENCY.json` records the comparison. Publication is to the existing working branch and PR #140 only, with a non-force expected-head update. No merge is performed.

This report certifies the bounded migration's completion and recorded validation, not a new all-class source adjudication or paper freeze. The existing PR's broader maintainer merge gates still require reconciliation. Remote workflow status and the exact published commit are reported in the PR comment after publication; they must not be inferred from local test results.
