# VIGIL Audit Archive

This directory contains retained, non-normative audit artefacts produced during bounded VIGIL review, migration, transition, assurance, and housekeeping passes.

Audit artefacts preserve what was inspected, the architecture or corpus state examined at the time, findings, transition reasoning, and validation outcomes. They are historical evidence of maintenance work; they are **not** current schemas, runtime contracts, canonical datasets, taxonomy definitions, or executable maintenance instructions unless an active document explicitly says otherwise.

## Organisation

- `taxonomy/` — taxonomy construction, transition, semantic-alignment, validator-closure, and publication audits.
- `external-requirements/` — external-governance extraction, metadata-fidelity, and review-queue audits.
- future audit families should receive their own bounded subdirectory rather than accumulating beside canonical data or executable code.

Implementation and reconciliation reviews that remain useful as current work records continue under `vigil/docs/reviews/`. Generated current-state inventories remain with the subsystem that generates and consumes them.

## Housekeeping rule

Repository maintenance is part of every substantive VIGIL pass, not a separate rescue activity. When work completes:

1. executable tests belong under `vigil/tests/`, never `vigil/scripts/`;
2. `vigil/scripts/` is reserved for repeatable current builders, validators, managers, routers, auditors, seeders, and explicitly retained maintenance tools;
3. completed transition or audit reports must not remain beside canonical schemas, taxonomy records, datasets, or live tools merely because that is where they were created;
4. retain a completed audit here when its findings, migration rationale, or assurance record remain useful; otherwise rely on Git history rather than creating a permanent archive of obsolete working debris;
5. a one-off migration or reconciliation script must be reviewed for retirement after its result is canonical and independently validated; do not delete it while current tests, documentation, or recovery procedures still depend on it;
6. path moves must update workflows and documented commands in the same administrative change; and
7. housekeeping-only changes do not create VIGIL PROP, PATCH, FM, OBS, or other substantive governance records.

The TAXONOMY-04A/04B/04C sequence is intentionally retained here as transition history. Its presence records how the taxonomy architecture evolved; it does not make those intermediate architectures current.
