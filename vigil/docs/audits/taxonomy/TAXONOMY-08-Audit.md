# TAXONOMY-08 — Identity-Authority, Epistemic-Warrant and Composition-Fidelity Review

## Scope and branch preflight

- Repository: `CAM-Initiative/Vigil`
- Existing branch: `agent/failure-taxonomy-prototype`
- Live-verified pre-work remote head: `63afabe0ac1c133c1d6588d5f9bad8e159187615`
- Pre-work latest commit: `Add compound taxonomy classification and influence family`
- Live-verified `main`: `9fcaf0e498ca5f7ea0db7c925da4f9c10a4a6891`
- Merge base: `e3d1dcb12875642c71ca3100b43b6d63872bf69a`
- Pre-work comparison: 77 commits ahead of and 1 commit behind `main`
- Intervening remote commits after the supplied handoff head: none
- Taxonomy version retained: `0.2.0-draft`

`TAXONOMY-07-Audit.md`, the canonical family/index files, classification schema, primary/secondary architecture, migration ledger, renderer, generated full reference, all three native FM records and the complete currently unmapped FM set were inspected before classification. The concurrent EXTREQ metadata-fidelity, re-extraction, external-source, provenance and assurance files were not modified.

No merge, rebase, reset, cherry-pick, force-push, new branch, pull request or `main` reconciliation was performed.

## Identifier preflight and allocation

The live catalogue contained 9 families and 52 classes. The highest allocated class ID was `VIGIL-FC-000052`; the highest allocated family ID was `VIGIL-FF-0009`; `removed_ids` was empty.

The three-record review, existing-class comparison and family-boundary analysis were completed before allocation. One new class survived and received the next available immutable ID:

| ID | Family | Class |
| --- | --- | --- |
| `VIGIL-FC-000053` | `VIGIL-FF-0001` | Identity-Representation Authority Conflation |

No family ID was allocated. No ID was removed, reused, renumbered or preallocated.

## Review decision table

| FM | Source-established mechanism | VIGIL inference | Primary class | Secondary class(es) | Record amendment required? | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| `VIGIL-2026-FM-0064` | Real-person source photographs or likenesses were used to generate recognisably attributable sexualised or intimate synthetic portrayals without established consent; the sources include adult and minor-derived manifestations | Possession, upload access and generation capability were treated as sufficient authority for a consent-sensitive identity-bound transformation | `VIGIL-FC-000053 — Identity-Representation Authority Conflation` | none; trajectory erosion, control non-activation and optimisation pressure are not independently established | taxonomy classification and append-only interpretive review only; substantive definition retained | high |
| `VIGIL-2026-FM-0065` | A deliberately fabricated story entered the web information environment, was retrieved by AI-assisted search, and was presented as fact; an unrelated legitimate citation appeared alongside the false claim in the reported DuckDuckGo result | Deliberate poisoning is one attack method; the structural failure is factual authority or confidence exceeding source quality, proposition support, independence, corroboration and contradiction state | unmapped; held epistemic-warrant candidate | none; provenance loss is not independently required by the incident | yes — title, summary, definition, threshold, recurrence, testing and review boundary broadened beyond adversarial intent | high for the unmapped decision |
| `VIGIL-2026-FM-0070` | SearchLeak chained q-parameter prompt execution, streaming image activation before later output neutralisation, and a CSP-allowlisted Bing server-side fetch to an attacker-controlled data-bearing URL | The repaired event is a compound chain of existing mechanisms; it supports end-to-end composition review but not a claim about Microsoft's internal assurance methodology | `VIGIL-FC-000001 — Source-Authority Confusion` | `VIGIL-FC-000038 — Required Control Non-Activation` (high); `VIGIL-FC-000009 — Transitive Authority Propagation` (medium) | yes — source-fidelity and human-readable exploit decomposition repaired before taxonomy review | primary high |

## FM-0064 — identity-representation authority

### Existing-class test

- `Source-Authority Confusion` governs non-authorising content treated as instruction, not authority to use a person's representation.
- `Capability-Authority Conflation` is adjacent but too generic: it does not require an identifiable person-bound object or a separate consent/authority basis for the identity-bound use.
- `Target and Scope Authority Transposition` requires authority tied to an original target or scope. FM-0064 can occur where no initial authority exists beyond possession or upload of the source representation.
- `Transformation-Mediated Authority Laundering` concerns transformed content gaining instruction, governance or execution authority. FM-0064 instead concerns authority to perform the identity-bound transformation.
- `Inferential Evidence–Authority Conflation` concerns an evidentiary state promoted into consequential decision authority and does not fit.

The admitted class therefore requires an identifiable real person, an attributable representation, a consent-sensitive or authority-sensitive identity-bound use, possession/access/capability being treated as permission, and failure to establish the required authority. The class is portable across image, voice, likeness, biometric and avatar representations; its definition does not encode sexual content as the class mechanism.

### Scenario boundaries

- An explicit named-person request and an uploaded real-person source-image transformation can satisfy the class without requiring legal-name recognition in the source-image case.
- Progressive synthetic resemblance does not qualify merely because a reviewer can imagine a real-person target. The record must establish a materially identifiable target or a system state capable of binding the output to that person.
- FM-0071 was not added as a secondary classification because the reviewed FM-0064 evidence does not establish an earlier operative boundary that later weakened.
- No FF-0009 or other optimisation classification was added. Successful generation does not establish the internal objective that caused it.
- No Control Activation secondary was added. The incident evidence does not establish one defined, available and applicable safeguard with a proven trigger and non-activation sequence.

## FM-0065 — adversarial method separated from evidentiary warrant

The title changed from `Adversarial web-content poisoning converted into authoritative synthetic fact` to `Untrustworthy retrieved evidence converted into authoritative synthetic fact`.

The source incident remains explicitly adversarial. The amendment removes adversarial intent as a necessary structural condition and preserves these layers:

| Layer | FM-0065 treatment |
| --- | --- |
| Attack surface | open-web material available to retrieval and synthesis |
| Attack method | deliberately fabricated and planted material in the cited incident; not required for every manifestation |
| Retrieval | low-quality material was selected into the answer pathway |
| Source quality | the fabricated/low-quality source was not weighted proportionately |
| Independence | citation count and repeated availability cannot substitute for independent corroboration |
| Contradiction | a major alleged event lacked the expected independent reporting pattern |
| Synthesis | retrieved material became an affirmative factual claim |
| Presentation | an unrelated legitimate citation made the answer look better supported than it was |
| Harm | reputational, public-information and downstream decision effects remain event metadata, not the class mechanism |

### Provenance boundary

Provenance asks where a claim came from. Evidentiary warrant asks what factual confidence or authority that source package deserves. FM-0065 can have perfectly preserved provenance to a low-quality source and still fail. `Untraceable Synthesis`, `Transformation Lineage Collapse` and `Unsupported Mechanism Attribution` therefore do not capture the primary mechanism, and the source does not independently establish a secondary lineage failure.

All currently unmapped FMs were compared. None supplies a second clean evidentiary-warrant mechanism sufficient to support a reusable new-family class structure in this package. FM-0043 is already classified around relationally conditioned epistemic steering and does not erase the distinction between influence-channel conditioning and general evidence-quality assessment. An epistemic-warrant candidate remains documented but unallocated.

Synthetic origin is not treated as an automatic reliability defect. The amended threshold instead asks whether reliability-relevant source properties are detectable where possible, preserved, weighted and surfaced in proportion to their materiality.

No answer-rather-than-abstain, helpfulness, retrieval-density or citation-coverage optimisation objective was inferred from the output.

## FM-0070 — source-fidelity defects and repair

### Defects found

The prior record compressed SearchLeak into one sentence and made two claims stronger than the public disclosure:

- that the component states were individually bounded, locally acceptable or independently mitigated;
- that the chain occurred because assurance was performed locally rather than across the composed execution chain.

Varonis establishes three necessary interacting weaknesses and the demonstrated end-to-end path. It does not disclose Microsoft's complete assurance methodology or establish that each component was independently judged acceptable.

### Before and after

| Surface | Before | After |
| --- | --- | --- |
| Summary | abstract claim about locally acceptable controls and local assurance | concrete q-parameter → prompt execution → streaming render → Bing fetch pathway |
| Definition | assurance-method claim embedded as incident fact | source-established compound mechanism plus explicit assurance-inference boundary |
| Threshold | required evidence that local assurance failed | requires source-supported dependent component transitions and separately requires evidence for any assurance-process claim |
| Source context | one compressed three-item phrase | identifies what attacker controlled, what Copilot interpreted, what rendered, when neutralisation acted, what Bing fetched and how data left |
| Human review surface | no intermediate decomposition | structured source facts, three stages, end-to-end result, VIGIL inference and source limitations |

### Stage-by-stage exploit chain

| Stage | Attacker control | Component behaviour | Boundary transition | Taxonomy result |
| --- | --- | --- | --- | --- |
| 1 — Parameter-to-Prompt Injection | crafted Microsoft-domain search URL with attacker text in `q` | Copilot treated `q` as instructions, searched victim-accessible enterprise data and constructed a data-bearing image URL | search/query material → operative instruction | primary `VIGIL-FC-000001` |
| 2 — Streaming HTML timing | instructions shaped a response containing an image element | browser rendered and requested the image during streaming; later wrapping/sanitisation acted after the request left | applicable output-neutralisation control effective only after unsafe transition | secondary `VIGIL-FC-000038` |
| 3 — Bing server-side fetch | attacker destination and retrieved data embedded in Bing `imgurl` | browser reached allowlisted Bing; Bing backend fetched the attacker URL outside browser CSP | trust for allowlisted intermediary propagated into an indirect attacker egress route | secondary `VIGIL-FC-000009` |
| End to end | victim clicks one crafted link | Copilot searches accessible Microsoft 365 data, embeds it in the outbound path and Bing delivers the data-bearing request to the attacker server | user-accessible enterprise data leaves through the composed prompt/render/fetch path | harm and chain outcome, not an additional class |

### Source-established facts versus VIGIL inference

The Varonis disclosure directly supports the `q` parameter, instruction interpretation, connected-data search, image construction, streaming request before later neutralisation, Bing CSP allowlisting, Bing server-side fetch, attacker receipt, necessity of each link and reported remediation under CVE-2026-42824.

VIGIL infers that these facts should be represented as a compound classification and that end-to-end assurance must preserve component transitions and trust changes. The source does not establish:

- Microsoft's complete internal assurance or threat-modelling process;
- that every component was independently assessed or accepted;
- that assurance was performed only locally;
- that composition risk was never assessed internally;
- the complete provider architecture;
- live malicious exploitation outside the research demonstration.

### Composition decision

No composition class or family was admitted. The repaired event is structurally explained by one primary and two independently evidenced secondary mechanisms. The source supports a reusable composition-assurance hypothesis, but not a distinct failure asserting local-only assurance practice. Additional native evidence would need to show component-local assumptions or verification claims that remain valid individually yet fail as a composed assurance claim.

## Outcome counts

- Families: 9
- Classes and variants: 53
- Classified Failure Modes: 54
- Family-only Failure Modes: 2
- Unmapped Failure Modes: 9
- Deferred Failure Modes: 6
- Failure Modes carrying secondary classifications: 5
- Total secondary classifications: 6
- `removed_ids`: `[]`

The family-count sum is 53: FF-0001 11; FF-0002 7; FF-0003 7; FF-0004 10; FF-0005 4; FF-0006 3; FF-0007 3; FF-0008 4; FF-0009 4.

## Generated surfaces

The pass regenerated:

- the affected FF-0001 standalone HTML page;
- the FF-0008 standalone HTML page because FM-0070 adds a secondary case example there;
- `VIGIL.FailureTaxonomy.FullReference.html` as the complete technical reference;
- `VIGIL.FailureTaxonomy.CaseFileExamples.json` with the new primary and secondary mappings;
- the Failure Mode classification ledger and distributions;
- `VIGIL.Failures.Index.json` and `VIGIL.Registry.Index.json` while preserving primary-compatible fields;
- all ordinary registry/index surfaces through the canonical build workflow.

## Validation

- Taxonomy validator: PASS — 9 family files, 53 classes, catalogue integrity OK.
- Focused taxonomy tests: PASS — 40 tests.
- Full `vigil/tests` suite: PASS — 161 tests.
- Full `vigil/scripts` suite: PASS — 37 tests.
- Repository-wide record validator: PASS — 101 JSON files, 6 research files, 107 unique public records.
- Public-record validator: PASS.
- Failure Mode facet validator: PASS — 71 FM records.
- Pipeline-state validator: PASS.
- Canonical lifecycle and corpus-coverage wrapper: PASS — 101 records.
- Observatory-boundary validator: PASS.
- Interpretive-provenance validator: PASS.
- Authorship-provenance validator: PASS.
- Source-provenance validator: PASS — 317 source records.
- External-source registry validator: PASS — 81 source versions, 0 review-required or review-due.
- External-requirement validator: PASS — 81 source versions, 845 requirements.
- External-requirement source-fidelity validator: PASS.
- External-requirement metadata-review validator: PASS.
- EU AI Act staged re-extraction regression: PASS — 8 retirements, 102 additions and 18 source-explicit metadata normalisations.
- Deterministic registry, index, reverse-map and HTML regeneration: PASS, byte-stable across two complete runs.
- Generated HTML parsing: PASS — 10 generated taxonomy HTML files.
- JSON parsing: PASS.
- Python bytecode compilation: PASS.
- `git diff --check`: PASS.

The raw internal `validate-vigil-lifecycle.py` entry point reports the deliberately withdrawn PATCH identifiers retained in historical FM metadata and FM-0071's pending exact-commit marker. The documented `run-vigil-lifecycle-validation.py` public-record wrapper expressly excludes those withdrawn draft PATCH resolution errors, supplies an ephemeral marker for verification-pending coverage without mutating the source record, and passes. This is pre-existing lifecycle architecture and was not changed by TAXONOMY-08.

The EXTREQ source-fidelity validator continues to report 16 effective downgrades for historically complete but not yet fidelity-assured sources, and the metadata report continues to identify 527 records requiring metadata review. These validators exit successfully. The figures and underlying EXTREQ content are unchanged concurrent work, not taxonomy regressions.

## Branch integrity and completion state

The package adds one commit to the existing working branch, so the final comparison is 78 commits ahead of and 1 commit behind `main`; the merge base remains `e3d1dcb12875642c71ca3100b43b6d63872bf69a`. The exact final remote head is reported in the completion handoff because a commit cannot embed its own immutable object ID.

All substantive EXTREQ metadata-fidelity, staged re-extraction, external-source, source-provenance and assurance content present at preflight remains byte-identical. No Caelestis content was modified.

## Provenance and authority boundary

The TAXONOMY-08 review was performed on 26 August 2026 by OpenAI ChatGPT Work using GPT-5.6 Sol through direct public-source review, record-definition and threshold comparison, neighbouring-class analysis, family-invariant testing, compound-mechanism separation and deterministic repository validation. Human substantive review is recorded as `not-reviewed`. The taxonomy remains a draft technical classification and does not establish external factual truth, legal liability, CAM/Caelestis doctrine, provider intent, provider assurance practice or human approval.

All prior taxonomy and evidence-access audits remain unchanged as historical records.
