# AI Governance Standards Baseline Dataset

**Dataset version:** 0.2.0

The AI Governance Standards Baseline is a machine-readable VIGIL dataset combining registered governance-source metadata with clause/control records derived from laws, standards, frameworks and technical guidance relevant to AI governance.

The dataset is intended to help third parties understand what each source is, how it relates to AI governance, which lifecycle stages it informs, when its substantive assessment was last reviewed, and—where clause records are available—the individual governance requirements represented from that source.

## Release 0.2.0 coverage boundary

Release 0.2.0 contains **85 registered source versions** and **978 canonical clause/control records**. Four source versions were newly registered at source level: Council of Europe CETS No. 225, OECD/LEGAL/0449, the Government of Canada Directive on Automated Decision-Making, and C2PA Technical Specification 2.4. Their extraction state is `not-started`; they contribute no EXTREQ records and must not be presented as clause-level Compliance coverage.

No new structured requirement extraction was completed for 0.2.0. IEEE 7003 and the four newly registered sources await primary-source analysis, the consolidated EU AI Act remains partial, and the prioritised ISO/IEC standards remain pending lawful access. See `CHANGELOG.md` for the source-by-source release boundary.

## Package contents

A published dataset package should contain:

- `README.md` — dataset purpose, structure, versioning and use notes;
- `CITATION.cff` — machine-readable dataset citation metadata;
- `manifest.json` — dataset version, build metadata, file inventory and integrity information;
- `sources.json` — registered source records, including public knowledge and review-freshness fields;
- `clauses.json` — clause/control-level governance requirement records;
- `CHANGELOG.md` — substantive dataset release history when release changes exist;
- applicable licence information.

## Source-level public knowledge

Current active source records are expected to provide a third-party-facing knowledge layer including:

- `public_summary`;
- `ai_governance_relevance`;
- `applicable_lifecycle_stages`;
- `relevance_scope`;
- `last_substantive_reviewed`.

Internal curation and workflow notes are not substitutes for these fields and should not be projected as public source summaries.

## Review freshness

Active sources should be substantively reviewed at least every 90 days. A metadata sync, unchanged-source check, automated registry refresh or file modification does not constitute substantive review and must not reset `last_substantive_reviewed`.

A source may therefore be marked review-due even when the underlying law, standard or framework has not changed.

## Versioning

The dataset uses semantic versioning and is currently released as **0.2.0** while the public dataset contract remains pre-1.0 and experimental.

- **Patch** changes are reserved for substantive corrections that should be represented as a new dataset release.
- **Minor** changes are used for material expansion, such as substantial new source or clause coverage, while the dataset remains on its pre-1.0 release line.
- **Major** changes are reserved for incompatible changes to the dataset contract or structure.

A review-freshness update by itself does **not** require a dataset version increment. Review-only refreshes may regenerate the current package under the same dataset version; `manifest.json` records the package build/update timestamp and hashes so individual generated artefacts remain distinguishable.

The dataset version should therefore describe the substantive release contract, while build metadata records when that version was packaged or refreshed.

## Clause/control records

A single source clause or control may produce more than one atomic analytical requirement record where the source provision contains several distinct governance propositions. Repeated clause/control references therefore do not necessarily indicate duplicate records. Consumers should distinguish records by their stable `requirement_id` and treat `clause_or_control` as the shared source locator.

## Authority and interpretation

The baseline does not convert external materials into CAM authority and does not itself establish legal applicability, compliance, conformance or legal advice. Source authority remains with the originating issuer. VIGIL records structured analytical representations and public governance context subject to the evidence and access limitations recorded for each source.

## Citation

Use the accompanying `CITATION.cff` for this dataset package. Where a specific source or clause is relied upon, cite the originating authority in addition to the VIGIL dataset representation.
