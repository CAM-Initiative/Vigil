# FC-084 migration readiness

> **21 October 2026 identifier update:** This document originated under provisional, unmerged FC-089. The maintainer reassigned the identical Service Availability and Degradation Integrity class to the unused FC-084 slot before publication. The earlier FC-084 Verification Laundering proposal was never a selectable class and its broken Incident references were resolved separately. See the [identifier crosswalk](../2026-10-21-fc084-prepublication-renumber/FC-089-TO-FC-084-IDENTITY-CROSSWALK.json). The dated baseline and underlying findings are unchanged.

The bounded migration is complete for review: 194 Incidents screened, 34 FC-084 candidates adjudicated, one new secondary failure in INC-156, and obsolete transition-gap findings corrected in INC-044. Thirty-one reviews end at explicit evidence limits and two at scope-limited non-admission. None of those conclusions proves the historical mechanism absent. The other 192 canonical Incident files are byte-identical to the adjudication baseline.

## Verification

* **307 tests pass** after installing CI's pinned `jsonschema==4.26.0`. The initial attempt failed to import that dependency; its output is preserved in [the pinned historical validation receipt](https://github.com/CAM-Initiative/Vigil/blob/2519291962d1da0b01a1ae28caf38275496efdf2/vigil/docs/reviews/2026-10-20-fc089-corpus-migration/VALIDATION.json), not reported as a substantive regression.
* Canonical/public-record, source and interpretive provenance, authorship, system-component, and occurrence-to-requirement validators pass.
* Both full-rebuild guards pass against the exact `be4bf1c784f956ff32c27377ff9e48c94a6fcb77` baseline.
* Taxonomy validation passes for 17 families and 80 classes. Taxonomy, schema, validators and tests are unchanged.
* Builders and publication filtering were rerun after the full suite. A second rebuild/filter cycle produces identical hashes. The generated public index and case examples are included.
* Semantic preservation assertions pass for original source metadata, primary mappings, original episode paraphrases and relationships, all HIM dimensions, independent assessments and historical review entries. See `SEMANTIC-PRESERVATION.json`.

**Resolved on 20 October 2026:** the two noncanonical Verification Laundering proposal references in INC-060 and INC-189 were removed after a finite evidence-limited candidate review. This is historical review evidence, not an outstanding validator hold or a current FC-084 service-availability mapping.

## Authority and remaining decisions

The grouped proposal in `TAXONOMY-AMENDMENT.md` awaits maintainer approval. It corrects exclusions 3/4 so that adequate restriction and recovery do not defeat expressly recognised successes. The proposal does not block the supported failure correction, and no candidate currently has all success conditions independently established. Moxie's historical transition obligation, the garage episode's response timing and provider-specific service commitments remain finite evidence limits, not unfinished generic research tasks.

Issue #154's external-standard admission remains independently held for authoritative source access and applicability review. No ISO requirement, universal uptime obligation or independent requirement assessment has been manufactured.

Concurrent commits through `51f807171c013fcce54e4046e7b72c9a98b97fb4` add only disjoint FC-045/079 review documents; those contents are preserved. [the pinned concurrency receipt](https://github.com/CAM-Initiative/Vigil/blob/2519291962d1da0b01a1ae28caf38275496efdf2/vigil/docs/reviews/2026-10-20-fc089-corpus-migration/CONCURRENCY.json) records the comparison. Publication is to the existing working branch and PR #140 only, with a non-force expected-head update. No merge is performed.

This report certifies the bounded migration's completion and recorded validation, not a new all-class source adjudication or paper freeze. The existing PR's broader maintainer merge gates still require reconciliation. Remote workflow status and the exact published commit are reported in the PR comment after publication; they must not be inferred from local test results.
