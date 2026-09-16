# Completed migrations

Files in this directory are retained solely to reproduce or audit completed
one-time transformations. They are not part of the VIGIL runtime, build or
validation pipeline.

- `2026-09-16-initial-harm-impact-migration.py` records the superseded,
  legacy-severity-led transformation and requires `--historical-replay`.
- `2026-09-16-evidence-derived-harm-impact.py` records the corrected
  Incident-by-Incident evidence adjudication and requires `--apply`.

Do not run either migration against a later corpus state. Git history is the
authoritative recovery mechanism for their input state.
