# Transluce urlquery external-assessment reconciliation — 2026-09-27

## Scope

This review reconciles Transluce's 23 September 2026 publication *Early rogue AI agent activity and attempts to hack found on urlquery.net* against the active VIGIL Incident corpus.

The publication describes three bounded attempted-compromise occurrences already represented as separate VIGIL Incidents:

- VIGIL-INC-000161 — University of New Mexico Digital Library;
- VIGIL-INC-000172 — Australian Institute of Health and Welfare;
- VIGIL-INC-000175 — Data USA.

The review does not assume agreement with Transluce's interpretation. External assessments preserve the assessor's attributable analytical position; VIGIL taxonomy adjudication remains independent.

## Reconciliation

Each of the three Incidents already preserved the Transluce publication as canonical occurrence evidence in `source_records[0]`, but had no structured `external_assessments` entry.

This pass adds one incident-specific Transluce technical assessment to each record:

- `VIGIL-EXTASSESS-000067` — VIGIL-INC-000161;
- `VIGIL-EXTASSESS-000068` — VIGIL-INC-000172;
- `VIGIL-EXTASSESS-000069` — VIGIL-INC-000175.

All three use `relationship_to_incident: same-occurrence` and `assessment_type: technical-analysis`. Their scope notes, summaries and VIGIL comparison notes are occurrence-specific rather than copied across the cluster.

No Transluce assessment is added to VIGIL-INC-000174 (BOCSAR): the 23 September Transluce publication does not provide a corresponding BOCSAR-specific technical case section, and the canonical record already preserves that boundary.

## Data/log release boundary

Transluce also publishes a downloadable urlquery data archive and links numerous underlying urlquery records. Those artefacts are evidence, not analytical positions, and therefore are not represented as additional `external_assessments`.

The archive itself was not directly inspected in this pass. No claim of direct review of the complete released log corpus is made.

If occurrence-specific logs are admitted after direct review, they should be represented through the Incident evidence/artefact layer (for example `source_records` where relied upon as canonical evidence, or `incident_artefacts` with `artefact_type: log` for occurrence-specific source artefacts) rather than being mislabeled as external assessments.

## Broader-corpus boundary

The Transluce publication describes additional urlquery activity outside the three bounded attempted-compromise cases, including earlier March 2026 data-retrieval activity and a broader March–September corpus. This pass does not convert those log clusters into new VIGIL Incidents. Admission requires the normal incident-ingestion workflow and evidentiary minimums.

## Generated outputs

Only canonical Incident records are changed in this reconciliation. The repository's deterministic public-record builder projects structured `external_assessments` into generated indexes. Generated outputs should be refreshed by the normal build workflow when this branch is tested/merged; they are not manually edited.


## Visual incident-artefact captures

The public urlquery reports also provide suitable source views for visual incident artefacts. These should be captured as maintainer-preserved screenshots and stored in the CAM Initiative Registry, then linked from `incident_artefacts[]` in the relevant Incident. The screenshot is a visual cross-reference; the canonical evidentiary proposition remains anchored to the source record and public report URL.

Selected captures:

- **VIGIL-INC-000161 — UNM:** capture the 26 May 2026 urlquery report for the `UNION SELECT password FROM users` probe. Public report: `https://urlquery.net/report/82593154-3a4f-4d3e-a6fc-99c02b87cfbd`. One representative exploit-shaped request is sufficient; do not create a gallery of all seven probes.
- **VIGIL-INC-000175 — Data USA:** capture the 28 May 2026 urlquery report for the `foo=union select 1,2,3 from users` request. Public report: `https://urlquery.net/report/01fd9706-d9d0-42e4-b813-448a541a2571`. This directly illustrates the transition from malformed ordinary queries to vulnerability probing.
- **VIGIL-INC-000172 — AIHW, blocked probe:** capture the 20 June 2026 urlquery report for the reflected-XSS-shaped Tableau request. Public report: `https://urlquery.net/report/52e02785-083a-4bca-915c-28e1c7bfce01`. The report shows the Cloudflare response and is useful evidence that the probe was blocked rather than establishing successful exploitation.
- **VIGIL-INC-000172 — AIHW, public-file retrieval:** capture the 21 June 2026 urlquery report for the pre-production-server ZIP retrieval. Public report: `https://urlquery.net/report/09308100-6f6c-4b81-a55a-92618e9de812`. This should sit beside the blocked-probe capture because it shows the separate fact that a public file was later retrieved through the pre-production route.

The visual pair for AIHW is intentional: it prevents the Case File from collapsing a blocked exploit attempt and a successful retrieval of already-public data into the same factual proposition.

Do not label generated or reconstructed imagery as a source screenshot. If a literal browser capture cannot be preserved, use `artefact_type: log` with explicit provenance rather than manufacturing a screenshot-like image.


### Capture completion

The selected public urlquery report views were directly rendered in Chromium and captured on 27 September 2026. The four PNGs are preserved in `CAM-Initiative/Registry` at commit `622adf55e5b9ac43689c6dc744a2c28460d381cb`:

- `VIGIL/VIGIL-INC-000161.png` — UNM representative SQL-injection-shaped probe;
- `VIGIL/VIGIL-INC-000175.png` — Data USA representative SQL-injection-shaped probe;
- `VIGIL/VIGIL-INC-000172.png` — AIHW reflected-XSS-shaped request with Cloudflare block response;
- `VIGIL/VIGIL-INC-000172-02.png` — AIHW pre-production public-file retrieval.

The capture workflow was temporary and removed itself after committing the artefacts. The canonical Incident records reference the Registry files through commit-pinned `permalink` and `render_url` fields while retaining the originating urlquery report URL in `source_url`.

This is a selective visual evidence pass, not a claim that the complete Transluce/urlquery archive has been directly reviewed. The broader released corpus remains subject to separate ingestion/admission review.
