# EN 18286:2026 — bounded source admission

Classification: REVIEW. Date: 16 October 2026.

AI-authored metadata review under human task approval. No substantive human review, source verification or certification is claimed.

## Authority and preserved baseline

The user requested registration of EN 18286:2026 and its OJEU citation decision. PR #136 was checked first and found to concern the Incident Admission constitutional proposal, not external governance. The user subsequently nominated and approved continuation on `work/infrastructure-governance-reconciled-20261014`, PR #135.

Verified before editing: PR #135 is open, unmerged and draft; title: “Recover infrastructure governance source registration and Gate 1 review from legacy branch”; head repository: `CAM-Initiative/Vigil`; base: `main`; head: `8ba4ee19a7896d1ddb2810b00dd3f5e5cfde88c1`. Existing `validate` and `validate-build` checks passed at that head. GitHub authenticated repository metadata confirmed push permission. The checkout was clean. No competing branch or PR was created, and no shared history was rewritten.

The existing infrastructure-source Gate 1 proposal remains pending. This package neither adopts that proposal nor approves its mappings. All 98 baseline source entries and all baseline source-scope entries are preserved as JSON values. Current `main` and the working branch were searched for `18286`, `2026/2274` and `32026D2274`; no duplicate source was found. The 1,102 canonical requirements and all taxonomy relationships remain unchanged.

## Separate source identities

| Representation | Canonical key | Authority boundary |
| --- | --- | --- |
| EN 18286:2026 | `EXT-992C92D6CAB4\|2026` / `EN-18286` | Voluntary European standard. CEN/CENELEC; CEN/CLC/JTC 21. Edition date 22 July 2026. OJEU citation date 14 October 2026. |
| Commission Implementing Decision (EU) 2026/2274 | `EXT-39722D487277\|2026-10-14` / `EU-DEC-IMPL-2026-2274` | Separate EU legal publication decision. Adopted 12 October 2026; OJ L publication 14 October 2026. |
| Existing AI Act | `EXT-7DB18E82C9D3\|2026-07-27` / `EU-AI-ACT-2024-1689` | Regulation (EU) 2024/1689 remains the source of the legal obligations. No duplicate source or requirement is allocated. |

IDs use the existing `stable_id(external_source_id)` SHA-256 allocation function. The source matrix already provides `cen-cenelec-ai` and `eu-eurlex`. The standard uses the existing matrix's `harmonised-standard` class and `ojeu-cited` lifecycle. The decision uses the descriptive `implementing-decision` class permitted by the schema's non-enumerated source-class string, and `published` lifecycle. No schema or controlled enumeration changed.

Article 17 reuses `EXTREQ-548AC1A3F63A1A72`. No canonical Article 40 requirement was found in either existing AI Act version; Article 40 is retained as a legal article reference, not newly decomposed. Article 40 limits presumption of conformity to requirements covered by the cited standard or parts. Citation does not make the standard mandatory or cover the whole Act. A registry cross-reference does not establish adoption, applicability, compliance, conformance or certification.

## Evidence and access boundaries

Official sources consulted for identity, dates and bounded subject matter:

- [Commission harmonised-standards register](https://single-market-economy.ec.europa.eu/single-market/goods/european-standards/harmonised-standards/artificial-intelligence-ai_en): names the decision, adoption date, AI Act base and OJ L publication date.
- [CEN/CENELEC announcement, 15 October 2026](https://www.cencenelec.eu/news-events/news/2026/en-in-the-spotlight/2026-10-15-en-18286-2026-published-in-ojeu/): confirms the EN designation, citation milestone and Article 17 quality-management focus.
- [CEN/CENELEC July announcement](https://www.cencenelec.eu/news-events/news/2026/en-in-the-spotlight/2026-07-30-ai-quality-management/): confirms published standard identity and bounded quality-management subject matter; the displayed posting date is 31 July, not the standard's edition date.
- [Standards-body catalogue metadata](https://tienda.aenor.com/p/norma-cen-en-18286-2026-80556): edition date 22 July 2026 and CEN/CLC/JTC 21 committee. Only identity, date and committee metadata were used. The page expressly restricts AI use of protected content. No extract or normative standard was downloaded or processed.
- [User-supplied SIST catalogue locator](https://ecommerce.sist.si/catalog/standards/cen/34ea911c-a980-4433-85ac-1344f93da01b/fpren-18286): returned a JavaScript application shell, not readable final normative text. The draft-looking URL is not treated as evidence of a final clause.
- [Official decision ELI](https://data.europa.eu/eli/dec_impl/2026/2274/oj) and [EUR-Lex CELEX record](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32026D2274): retained as authority locators. Direct HTML/PDF retrieval returned an access check or empty response. Indexed official metadata was available, but no complete final legal artefact was retrieved.

The admission proposition is that the decision's Annex cites EN 18286:2026. Official Commission metadata and the CEN/CENELEC announcement establish the citation event. Direct verification of the exact Annex entry, qualifications and entry-into-force provision remains held. The decision's `effective_date` is therefore null; `published` does not assert that an operative provision was reviewed. No reviewed-primary-text digest was fabricated. The source-review assurance overlay remains unchanged.

Both new source-scope entries use `official-metadata-only` and `blocked-access`. The dated substantive review events concern source metadata, public knowledge and relevance only, not normative clauses or legal coverage. They remain `review-required`, with human review and verification `not-reviewed` / `not-verified`. Exact runtime model identity was not disclosed by this session and is recorded as such, rather than guessed.

## Relationship representation and holds

The current source-registry schema has no dedicated typed source-to-source relation or citation-date field. Reciprocal canonical keys, citation dates, authority URLs and legal context are preserved in `notes`; public summaries preserve the voluntary-standard / legal-decision / regulation distinction. No unsupported fields or pseudo-EXTREQ relationships were introduced.

Actionable holds are also stored canonically in each new `source-scope.json` entry:

1. Obtain authorised final EN text and permission for the intended AI processing. Do not upload or commit copyrighted text merely because a copy is available.
2. Retrieve the final official decision through an authorised route. Check Articles 1 and 2, the exact Annex citation and any qualification; verify the effective date before populating it.
3. Separately approve any EN clause extraction, Annex ZA coverage assessment, EN-to-Act equivalence or FC relationship work. Review the final normative text first.

No incident adjudication, HIM, severity, taxonomy, unrelated instrument, schema, validator, permanent test or CI change is authorised or included.

## Validation evidence

Baseline source and requirement validators passed before edits: 98 source versions / 1,102 requirements. Candidate source and requirement validators pass with `--check-generated`: 100 source versions / 1,102 requirements. Both new sources have zero EXTREQ records. All 98 baseline registry/scope entries and existing requirements are preserved. Duplicate source/version and hashed-ID collision checks pass. Draft 2020-12 schema checks, including date formats, pass for source registry and source scope.

`PYTHONPATH=/tmp/vigil-en18286-test-deps:vigil/scripts python -m unittest discover -s vigil/tests -p 'test_*.py'` passes: 246 tests. The first attempt exposed a missing environment dependency (`jsonschema`), not a record defect. Installing jsonschema 4.26.0 into an isolated temporary dependency directory resolved it without repository changes. Expected rejection diagnostics from negative fixtures are not corpus failures. The separate EU AI Act re-extraction check passes (8 retired identities, 102 successors; unchanged 175-record EU shard).

Read-only checks pass: external source registry, external requirements, external-requirement metadata, external-requirement fidelity, CAM assessments, authorship provenance, Incident records, public Incident records, source provenance, interpretive provenance, system components and occurrence requirement assessments. Metadata validation still reports the pre-existing 584 review-required fields in 73 requirements; no new field reviews are claimed.

The additional thin referential-integrity check fails identically on the candidate and a detached untouched worktree at the verified baseline:

```text
VIGIL-INC-000060: clause class ID does not resolve: VIGIL-FC-000084
VIGIL-INC-000189: clause class ID does not resolve: VIGIL-FC-000084
```

These are unrelated baseline defects. No repair is included. The test/build suite refreshes a pre-existing CaseFileExamples projection difference for INC-032; that unrelated generated change was discarded to preserve this bounded source-only scope. No incident or taxonomy files are included in the final diff.

LIVE changes: `source-registry.json` and `source-scope.json`. GENERATED changes: source catalogue, source-review queue, requirement index, completeness report, source-coverage manifests, external requirements catalogue, source-access limitations, blocked-source priorities and derivative-crosswalk index. REVIEW change: this document. Generated outputs are produced only by the two existing manager scripts. No canonical requirement shard changed. `git diff --check` must pass before publication.

This is source admission, not completed clause extraction or alignment. No merge or automatic merge is authorised.
