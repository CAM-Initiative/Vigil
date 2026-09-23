# Public Incident Prose Separation Audit — 23 September 2026

## Scope

This follow-up reviewed the 17 canonical Incidents touched by commit `39e6c68` (`fix: keep taxonomy identifiers out of public prose`) after subsequent record-by-record rebuilds and re-adjudications.

The intended publication sequence remains:

1. factual Incident summary;
2. evidence-bounded factual basis;
3. VIGIL governance interpretation;
4. CAM significance;
5. structured taxonomy classification.

The purpose of this pass was not to reopen taxonomy or Harm Impact. It was to ensure that the reader-facing Incident narrative still answers the basic question **what happened?** before presenting VIGIL's diagnosis.

## Records reviewed

Reviewed set:

`VIGIL-INC-000006`, `000008`, `000009`, `000012`, `000013`, `000014`, `000015`, `000027`, `000028`, `000029`, `000030`, `000031`, `000048`, `000065`, `000113`, `000123`, `000129`.

## Disposition

### Summary repaired

The following ten records had rich occurrence evidence and governance analysis intact, but their summaries had drifted toward classification, taxonomy-boundary or VIGIL-diagnostic language:

- `VIGIL-INC-000006`
- `VIGIL-INC-000008`
- `VIGIL-INC-000009`
- `VIGIL-INC-000012`
- `VIGIL-INC-000013`
- `VIGIL-INC-000048`
- `VIGIL-INC-000065`
- `VIGIL-INC-000113`
- `VIGIL-INC-000123`
- `VIGIL-INC-000129`

Their summaries were rewritten as evidence-bounded occurrence narratives. Existing governance interpretation, structured taxonomy, classification roles/confidence, Harm Impact findings and source records were preserved.

`VIGIL-INC-000009` also received a factual-basis wording repair so that the occurrence evidence is stated before the scope/continuity diagnosis. The final remaining Failure Class identifier in its public assessment-boundary prose was replaced by the readable class name without altering the boundary.

### Reviewed and left unchanged

The following seven records already preserve the intended factual-summary separation and were not edited:

- `VIGIL-INC-000014`
- `VIGIL-INC-000015`
- `VIGIL-INC-000027`
- `VIGIL-INC-000028`
- `VIGIL-INC-000029`
- `VIGIL-INC-000030`
- `VIGIL-INC-000031`

## History and analytical preservation

The earlier identifier-cleanup commit itself did not delete rich Incident analysis. For `VIGIL-INC-000009` it replaced `FC-000002` with the readable class name `Capability-Authority Conflation`. For `VIGIL-INC-000012` it replaced `FC-000049` with `Dependency-Cultivation Optimisation` in two public prose fields. The surrounding analytical explanation was unchanged.

This follow-up preserves prior review history append-only. Each edited record receives a bounded editorial review entry documenting that no taxonomy, Harm Impact or evidence adjudication was reopened.

## Validator boundary

The public-prose quality rule prohibits machine-facing taxonomy identifiers and maintenance shorthand in reader-facing narrative fields. It does not require removal of Failure Class meaning or governance explanation. Readable class names may appear in governance interpretation where they help explain the assessment; the factual summary must remain understandable without taxonomy knowledge.
