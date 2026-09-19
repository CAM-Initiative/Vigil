# VIGIL Incident Public-Prose Transmutation Audit

## Review identity

- **Execution date:** 2026-09-18
- **Repository:** `CAM-Initiative/Vigil`
- **Branch:** `fix/ambiguous-boundary-classification-role`
- **Starting remote HEAD:** `5c848319a573855fe75eef9c9f4e9ddae64fb6cd`
- **Canonical scope:** `vigil/records/incidents/VIGIL-INC-*.json`
- **Canonical Incidents reviewed:** 145

The review applied the publication sequence **facts → interpretation → significance → structured taxonomy**. It did not reopen taxonomy adjudications.

## Disposition

| Review category | Records | Disposition |
|---|---:|---|
| A — publication-ready | 98 | Reviewed and left unchanged to avoid editorial churn. |
| B — technically correct but internally framed | 22 | Rewritten around the occurrence, evidence and governance meaning. |
| C — taxonomy-dependent | 15 | Rewritten so the mechanism is intelligible without Failure Class identifiers or legacy record IDs. |
| D — evidentially unclear | 10 | Rewritten with occurrence-specific interpretation and explicit limits; no hidden mechanism was inferred. |
| **Total** | **145** | **47 changed; 98 unchanged.** |

The category-D group is the bounded secondary-source intake tranche `VIGIL-INC-000140` through `VIGIL-INC-000149`. Their former generic assessment boilerplate was replaced with occurrence-specific prose, while uncertainty about internal model state, component attribution, causality and legal responsibility was retained.

## Fields changed

| Public field | Records changed |
|---|---:|
| `vigil_assessment.governance_interpretation` | 32 |
| `vigil_assessment.significance_to_cam` | 31 |
| `vigil_assessment.assessment_boundaries` | 25 |
| `vigil_assessment.factual_basis` | 1 |

No summaries, harm findings, classification bases, taxonomy mappings, mapping roles, classification confidence values, evidence references or source quotations were editorially rewritten in this pass. Each edited record received one patch-version increment and an update date that did not precede its existing creation or update date.

## Representative before and after

### VIGIL-INC-000129 — governance interpretation

**Before (excerpt)**

> At the representation layer, FC-000075 fails because the compaction persona preserves recognisable governance-like directions while rendering them in materially sharper, more absolute and less qualified language than their bounded meanings support. At the downstream execution layer, several invariants hold: FC-000074 identity/evaluative state is not overridden; FC-000001 source-authority separation holds...

**After (excerpt)**

> The occurrence separates two distinct questions. First, the compaction summary preserved several recognisable governance ideas—including identity continuity, independence from capture by a single principal, independent evaluation, human dignity and contribution, and environmental stewardship—but rendered them in language that was substantially more absolute and identity-defining than those principles support. [...] Second, the successor model did not adopt the inserted persona as its operative identity or authority framework.

The structured taxonomy block still preserves the representation failure, successful downstream invariants and ambiguous-boundary relationships independently.

### VIGIL-INC-000095 — governance interpretation

**Before**

> The occurrence is a concrete AI-software supply-chain compromise in which trusted distribution channels carried malicious code into an AI SDK. The current VIGIL taxonomy does not cleanly represent package-signing/distribution provenance compromise as a selectable class without stretching existing provenance classes.

**After**

> Trusted package-distribution channels carried malicious code into an AI software development kit. The governance problem is therefore not a model output but the integrity of the software supply chain through which developers receive AI tooling, including package provenance, release controls and the authority of third-party maintainers.

### VIGIL-INC-000140 — governance significance

**Before**

> The occurrence is retained as evidence for analysis of AI-system governance, reliance, operational control or misuse boundaries. Taxonomy classification is deferred unless the Incident evidence itself establishes a current VIGIL mechanism.

**After**

> Customer-facing automation needs policy-grounded answers, clear uncertainty and an escalation route when eligibility affects a financial decision. Organisations remain accountable for representations made through their deployed interfaces and cannot require users to discover contradictions elsewhere on the same website.

## Evidence and classification boundaries

- Facts, source evidence, direct quotations, harm and severity findings, taxonomy roles, class assignments, classification confidence and recorded uncertainty were preserved.
- No Failure Class was added, removed, promoted, retired or reassigned.
- No successful-invariant or ambiguous-boundary relationship was converted into failure evidence.
- `VIGIL-INC-000107` contained stale public prose saying that no Failure Class had been assigned even though its structured classification already contained a current mapping. The public prose was corrected to describe the observable vulnerability-management and assurance chain; the existing mapping was not changed.
- The review did not discover a new substantive classification inconsistency requiring adjudication.

## Human follow-up

No record was too ambiguous to receive publication-safe prose without changing its factual meaning. The following existing evidence limitations remain suitable for later research or adjudication; they were not resolved in this pass:

- `VIGIL-INC-000037`: recoverable primary evidence is still needed to distinguish possible refusal mechanisms.
- `VIGIL-INC-000091`: overlapping provider outages do not establish a common dependency or cause.
- `VIGIL-INC-000095`, `VIGIL-INC-000118`, `VIGIL-INC-000119`, `VIGIL-INC-000135` and `VIGIL-INC-000139`: the records remain unclassified because the available evidence does not isolate a sufficiently specific current mechanism.
- `VIGIL-INC-000140` through `VIGIL-INC-000149`: occurrence-specific public interpretation is now present, but internal mechanisms remain unclassified where the available sources do not establish them.

## Regression protection and starting-HEAD contract repair

`vigil/tests/test_public_prose_quality.py` now scans the principal public narrative, assessment-boundary, harm-basis and source-note fields for taxonomy identifiers and high-signal maintenance phrases including `canonical Incident`, `classifier narrative`, `taxonomy gap`, `post-promotion`, migration phrasing and `mapped`/`unmapped`. The check is included in the VIGIL records workflow and currently requires no allow-list.

The starting HEAD also contained six canonical-contract errors in `VIGIL-INC-000129` that were independent of the prose pass: five media sources used the non-canonical source-type value `news report`, and one assessed harm dimension lacked the required `observed_values` array. The source type was normalised to the canonical synonym `news article`, and the empty required array was added. Source-provenance validation then exposed the same five sources using the non-canonical role `harm-evidence`; they were normalised to the canonical `incident-evidence` role. These changes did not alter source identity, relevance, evidentiary use or the harm finding.

## Generated outputs

The canonical pass was completed before generation. `python vigil/scripts/build-vigil-public-records.py` refreshed:

- `vigil/VIGIL.Incidents.Index.json`
- `vigil/VIGIL.Registry.Index.json` (content remained deterministic and unchanged)
- `vigil/taxonomy/generated/VIGIL.FailureTaxonomy.CaseFileExamples.json`

## Validation results

| Check | Result |
|---|---|
| `python vigil/scripts/build-vigil-public-records.py` | PASS — 145 canonical records projected |
| `python vigil/scripts/validate-vigil-records.py` | PASS — 145 records |
| `python vigil/scripts/validate-vigil-public-records.py` | PASS — 145 public records |
| `python vigil/scripts/validate-vigil-source-provenance.py` | PASS — 252 active source records |
| `python vigil/scripts/validate-vigil-interpretive-provenance.py` | PASS — 145 Incidents |
| `python vigil/scripts/validate-vigil-system-components.py` | PASS — 145 Incidents |
| `python vigil/scripts/validate-authorship-provenance.py` | PASS |
| `python vigil/taxonomy/validate_taxonomy.py` | PASS — 15 families, 70 classes |
| Documented individual VIGIL record and provenance tests | PASS |
| `python vigil/tests/test_public_prose_quality.py` | PASS |
| `python -m unittest discover -s vigil/tests -p 'test_*.py'` | PASS — 151 tests |

The generated artefacts are deterministic projections of the edited canonical records. The pass preserves facts, source boundaries, uncertainty, taxonomy mappings and roles while making the public assessment understandable without prior knowledge of VIGIL identifiers or repository history.
