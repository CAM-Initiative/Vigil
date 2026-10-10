# HIM version-specific regression fixture recovery

10 October 2026. Baseline: `52ea7ca8b031849b54cdebb2158d5828aa53272a`.

The first ordinary corpus tranche substantively migrates INC-001 to twelve-dimensional HIM 1.1.0. Canonical validation passes, but three pre-existing rule tests fail because they load that evolving Incident as their eleven-row historical 1.0.1 fixture, then unconditionally append a relational row. The migration creates a duplicate in two positive fixtures; the missing-dimension negative test removes only that duplicate and therefore no longer tests a missing dimension. These are fixture-construction failures, not a canonical validation defect.

The correction freezes the exact pre-migration canonical record as `vigil/tests/fixtures/VIGIL-INC-000001-HIM-1.0.1.json`. Original blob: `23f0a1847a11a7235bd7a20c96030de17718bf83`; SHA256: `4f907b994b3d8435fbe86f4ee62f5710b2a8680898b9ec9050732ee40e93c0f0`. Byte equality against the baseline Git blob was checked. All existing assertions and positive/negative mutations remain. The valid-Incident test additionally checks the live canonical record, so current-corpus coverage is preserved rather than replaced by a historical snapshot. The snapshot is test data outside the active Incident directory, not a new active record.

## Control effect and maintainer contract

The validator, schema, HIM thresholds, allowed versions, twelve-row requirement, Aggregate Harm evidence gates and all negative expectations remain unchanged. No canonical content changes from rejected to accepted or accepted to rejected. The frozen historical fixture still passes as before; duplicate/missing dimensions still fail. Both original 1.0.1 and properly constructed 1.1.0 assessments remain tested. No Incident prose, evidence, classification, harm or public-placement rule is redefined.

This is execution-only fixture isolation under the explicit MAINTAINERS Gate1 exception: “repairing execution without changing the accepted/rejected record set is not semantic”. The earlier preliminary update described the general approval gate; inspection establishes that its nonsemantic exception applies. There is no broader semantic approval and no permission to loosen the separate dated audit or heuristic-review tests. If future failures reveal an actual rule change, stop under the maintainer gate.

## Verification

Before repair:36 rule tests ran with3 failures, all identified above; canonical corpus validation passed. After fixture isolation: all36 rule tests pass against the substantively migrated local record. Source snapshot equality was checked. All original tests and assertions remain; live valid-record coverage is added within the existing positive test. The repair is committed separately from the Incident tranche.
