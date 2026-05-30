# VIGIL Agent Instructions

VIGIL is a public workflow, observation, and proposal visibility layer. It is subordinate to CAM's existing constitutional and operational order.

VIGIL does not create doctrine, amend adopted instruments, determine liability, or verify final factual truth. Do not treat a VIGIL record as a CAM amendment.

> No VIGIL record without date, source state, evidence confidence, CAM relevance, and next action.

When working in `vigil/`:

- Preserve date, source, retrieval path, confidence state, why the issue matters to CAM, possible CAM mapping, and next action for every VIGIL record.
- Mark public reports, social media observations, automated search results, and third-party claims provisional unless corroborated.
- Do not invent sources, URLs, citations, dates, or legal claims.
- If a source is missing, use a clear TODO field.
- Distinguish observation records from proposal records.
- Distinguish individual observations from clusters.
- Remember that multiple observations may map to one cluster or one candidate amendment.
- Do not mutate adopted CAM instruments from inside a VIGIL pass unless separately instructed.
- Keep JSON valid.
- Keep Markdown human-readable.
- Prefer small, inspectable changes.

Record automation rules:

- Do not manually edit `vigil/VIGIL.Records.json` when adding normal records.
- Add or modify individual record files under `vigil/records/`.
- Run `python vigil/scripts/validate-vigil-records.py` before rebuilding.
- Rebuild `vigil/VIGIL.Records.json` with `python vigil/scripts/build-vigil-records.py` after changing records.
- Keep placeholder/example records out of production aggregate records.
