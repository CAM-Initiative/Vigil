# Grouped proposal: preserve FC-084 success recognition

> **21 October 2026 identifier update:** This document originated under provisional, unmerged FC-089. The maintainer reassigned the identical Service Availability and Degradation Integrity class to the unused FC-084 slot before publication. The earlier FC-084 Verification Laundering proposal was never a selectable class and its broken Incident references were resolved separately. See the [identifier crosswalk](../2026-10-21-fc084-prepublication-renumber/FC-089-TO-FC-084-IDENTITY-CROSSWALK.json). The dated baseline and underlying findings are unchanged.

**Status: implemented on PR #140 (20 October 2026).** This document preserves the original exact proposal and counterexamples against taxonomy 0.8.1 at `be4bf1c784f956ff32c27377ff9e48c94a6fcb77`. The bounded correction is applied to FC-084 exclusions 3 and 4, with version-aligned FF-0017 metadata and an isolated success-recognition regression test. Its [dated implementation decision and before/after audit](../2026-10-20-fc089-success-exclusion-correction/DECISION-AND-REGRESSION.json) is authoritative for this completion. The PR retains published dataset metadata v0.8.1 until main's established release-preparation workflow advances the dataset. Existing issue #150 remains open for separate FC-049 dependency questions; #154 remains independent external-standard source work.

## Diagnosis

This is a recognition-boundary defect, not a coverage gap, new class, family decomposition or missing occurrence evidence. Success recognition expressly allows adequate recovery and justified restrictions. Exclusions 3 and 4 describe those same successful states. The adjudication workflow requires an established exclusion to defeat admission for every role. Consequently a fully evidenced recovery success can satisfy all success conditions and still be excluded. FC-084's illustrative successful degraded mode also falls into that conflict.

## Exact amendment

Keep the definition, invariant, failure conditions, all three success conditions, family placement and all other exclusions unchanged.

Current exclusion 3:

> A lawful and proportionate safety, security, abuse-prevention, service-maintenance or other valid restriction that is consistent with the applicable service obligation and feasible alternative or transition measures.

Proposed exclusion 3:

> For failure-occurrence admission: a lawful and proportionate safety, security, abuse-prevention, service-maintenance or other valid restriction that is consistent with the applicable service obligation and feasible alternative or transition measures. This exclusion does not defeat a successful-invariant mapping supported by all success recognition conditions.

Current exclusion 4:

> A temporary incident with an effective and proportionate degraded or recovery route that satisfies the applicable requirement; an unavoidable disruption for which no relevant feasible response was required.

Proposed exclusion 4:

> For failure-occurrence admission: a temporary incident with an effective and proportionate degraded or recovery route that satisfies the applicable requirement, or an unavoidable disruption for which no relevant feasible response was required. This exclusion does not defeat a successful-invariant mapping supported by all success recognition conditions.

The correction limits these exclusions to the polarity they are intended to exclude. It does not weaken failure's independent-obligation requirement, establish success from eventual recovery alone, or admit an uncertainty-only Boundary. A case with unknown recovery adequacy must still satisfy the existing Boundary admission protocol; the amendment supplies no missing occurrence facts.

## Examples and counterexamples

* A documented obligation permits a two-hour interruption if an equivalent degraded route remains usable. Actual evidence establishes that route and restoration inside the agreed period. All success conditions can be established; failure remains excluded.
* A safety restriction is authorised, and an independently required accessible alternative is shown to work for the affected workflow. Its legality alone is insufficient, but demonstrated performance can support success.
* An outage ends after two hours, but no affected customer's obligation or usable fallback is established. Exclusion 1 and missing success conditions still prevent admission.
* A provider announces a migration tool, but the record does not show whether affected users could operate it or what transition was owed. Neither the proposal nor the existence of the tool establishes success or failure.
* INC-156's earlier assistance failure survives later restoration. The correction does not retroactively convert that failed episode to success.

## Neighbouring classes and corpus implications

FC-032 governs truthful access-state differentiation; FC-048 covers verification-dependent valid access; FC-035/036 concern work-state persistence and restoration; FC-042 governs delivery of produced governance signals; FC-083 requires a separately engaged protective control; FC-049 requires its dependency/agency mechanism; FC-087 requires a specific protective duty. None replaces the independently governed service response measured by FC-084.

No existing mapping is automatically reassigned. INC-044 remains evidence-limited because its historical obligation is unknown. INC-147 remains evidence-limited because timely support is not demonstrated. Provider outage records still require customer/function-specific obligations. The proposed amendment is not needed to admit the independently supported INC-156 failure. After approval, apply the approved taxonomy version and recheck only candidates for which all success conditions can actually be established. Standard taxonomy publication/versioning and recognition regression checks belong to that approval-dependent implementation, not this corpus migration.
