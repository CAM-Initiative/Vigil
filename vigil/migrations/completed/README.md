# Completed migrations

Files in this directory are retained solely to reproduce or audit completed
one-time transformations. They are not part of the VIGIL runtime, build or
validation pipeline.

- `2026-09-16-initial-harm-impact-migration.py` records the superseded,
  legacy-severity-led transformation and requires `--historical-replay`.
- `2026-09-16-evidence-derived-harm-impact.py` records the corrected
  Incident-by-Incident evidence adjudication and requires `--apply`.
- `2026-09-21-incident-metadata-normalisation.py` records the corpus-wide
  removal of legacy `system_context` projections and the canonical wording
  applied to duplicated model/runtime, interface and nested evidence-basis
  metadata. It is retained for audit only.

Do not run completed migrations against a later corpus state. Git history is the
authoritative recovery mechanism for their input state.
