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

The visual-selection pass established a distinction between the complete Incident narrative and the role of a public-facing artefact.

The structured VIGIL Incident record remains responsible for the complete bounded factual account. A visual artefact should not be used to smuggle in material occurrence facts that are absent from the summary, factual basis or evidence spine. It should add information that is materially easier to understand in source-native visual or contextual form.

This review tested three candidate visual layers from the Transluce publication:

1. **raw urlquery report views** — useful underlying forensic traces, but poor public-facing visuals because they foreground request strings and scan metadata without explaining the occurrence;
2. **screenshots of Transluce incident prose** — human-readable, but largely duplicative of facts already represented in the VIGIL summaries and factual bases;
3. **Transluce's published urlquery activity timeline** — additive because it shows chronology, clustering, scan-volume pattern, confidence distinction and the relationship of the May–June incidents to RubyGems, collusion.wiki and Hugging Face context windows.

The third layer is therefore the final public-facing artefact selection.

### Final visual selection

The same complete Transluce timeline is preserved for each of the three related Incidents so every standalone Case File retains the cluster context:

- **VIGIL-INC-000161 — UNM:** the figure places the 25–26 May episode inside the sharp May–June rise in higher-confidence activity and alongside the RubyGems and collusion.wiki context windows.
- **VIGIL-INC-000175 — Data USA:** the figure makes the close temporal relationship to UNM visible and situates both inside the same dense May–June activity period.
- **VIGIL-INC-000172 — AIHW:** the figure places the 20–21 June episode at the end of that dense cluster, within the collusion.wiki context window and before the later fall in activity.

The complete source figure is preferable to incident-centred crops because the evidentiary value is the relationship between events. Cropping tightly around one marker removes some of the context the artefact is intended to add.

The three final PNGs are preserved in `CAM-Initiative/Registry` at commit `907db9efd81c72dccbc6971a292602a5d32f044b`:

- `VIGIL/VIGIL-INC-000161.png`;
- `VIGIL/VIGIL-INC-000172.png`;
- `VIGIL/VIGIL-INC-000175.png`.

The previously used second AIHW artefact was removed rather than retaining a redundant image slot.

The individual urlquery reports remain preserved as bounded supporting `source_records[]` entries. They remain available for provenance and direct technical inspection without being promoted as the public visual narrative.

### General artefact-selection rule

A prose screenshot is not automatically inappropriate. It can be valuable where the source-specific framing, qualification, comparison or surrounding context is itself evidentially useful and would be awkward or misleading to flatten into VIGIL's ordinary Incident prose. The governing test is not whether the artefact contains prose or graphics; it is whether it adds evidentiary or explanatory value beyond what the structured Incident record already conveys.

The Registry contract, VIGIL maintainer guidance and Incident schema were updated during this review to encode that rule.
