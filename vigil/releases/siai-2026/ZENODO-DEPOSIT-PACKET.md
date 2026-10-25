# VIGIL Observatory v1.0.0 — Zenodo deposit and release handoff

**Prepared:** 25 October 2026 · **State:** DRAFT / NOT PUBLISHED · **Working PR:** [#162](https://github.com/CAM-Initiative/Vigil/pull/162)

This is an operational handoff, not a licence grant, human certification, final citation, frozen dataset, assigned DOI or release authorisation. Do not merge, tag, create a GitHub Release, enable automatic archiving or publish to Zenodo as a consequence of this file alone.

## 1. Proposed Zenodo metadata — manual *dataset* deposit

| Field | Proposed value / action |
|---|---|
| Resource type | Dataset |
| Title | VIGIL Observatory: AI Governance Incident Corpus and Alignment Taxonomy — Release 1.0.0 |
| Version | 1.0.0 (**dataset** edition, distinct from taxonomy 0.8.1) |
| Creator | O'Rourke, Michelle (CAM Initiative); use the author's approved identity and affiliation; no ORCID guessed |
| Publisher | CAM Initiative |
| Publication date | **Actual deposit date only**, after human approval |
| Language | English |
| Related code | https://github.com/CAM-Initiative/Vigil |
| Project website | https://cam-initiative.org |
| DOI | **Unassigned.** Let Zenodo mint it on publication or reserve a DOI in a manual draft after approval; never invent one |
| Keywords | AI governance; AI incidents; alignment taxonomy; evidence provenance; assurance; algorithmic accountability; VIGIL Observatory |
| Rights holder | Phoenix Covenant Pty Ltd trading as CAM Initiative |
| Rights contact | research@cam-initiative.org |
| Licence | **CUSTOM:** “VIGIL Observatory Proprietary Licence” — use the exact [LICENSE.md](../../../LICENSE.md), not the default Creative Commons Attribution 4.0 |
| File visibility | Human decision. Public files are possible without an open reuse licence; restricted visibility is a distinct option |

### Deposit description (draft)

> VIGIL Observatory is an evidence-linked, versioned research corpus of 200 admitted AI-governance Incident records, accompanied by the VIGIL Alignment Taxonomy, Harm Impact methodology, external governance source/requirement mappings, and provenance and validation artefacts. Incident records distinguish source-attributed occurrence evidence, taxonomy classifications, unclassified and unresolved conditions, harm assessment, and external-instrument interpretation. The dataset release version is 1.0.0; the published Alignment Taxonomy edition recorded in the release is 0.8.1. Incident records may retain earlier taxonomy editions where a current-edition review has not been completed. The corpus is principally AI-authored and AI-assisted under human governance. Its records are not independently human-certified, and disputed or incomplete evidence remains explicitly qualified. The release does not establish legal compliance, universal factual accuracy, model-safety certification or professional reliance rights. See the included licence for substantive reuse restrictions and the deposited research snapshot for exact source-commit and per-file SHA-256 identities.

**Verify every quantitative claim against the final post-merge manifest before publishing.** In particular, the current working-branch preflight is **164/200 incidents at taxonomy v0.8.1**, not a statement that all 200 are fully reviewed. The five approved pending promotions, if executed and validated, would change this to 169/200; rewrite the sentence only after checking the final canonical manifest.

## 2. Rights and upload-route decision — release blocker

The repository is publicly readable but the [proprietary licence](../../../LICENSE.md) does not grant open reuse, scraping, machine-learning training or derivatives. [RIGHTS.json](../../../RIGHTS.json) records the same ownership and permissions. A GitHub/Zenodo software integration may assign a default or SPDX licence from metadata and can automatically archive a GitHub Release.

**Preferred safety-conscious route:** prepare a **manual Zenodo dataset draft**. Set a custom licence titled “VIGIL Observatory Proprietary Licence” with the public LICENSE.md URL and rights summary. **Inspect the actual pre-publication rights field.** Do not accept Zenodo's default CC BY 4.0 and do not use an approximate SPDX licence that grants rights VIGIL does not offer. Record the rights-holder's explicit approval of any visibility setting and licence metadata.

**Before tagging:** the maintainer must check whether Zenodo's GitHub integration is enabled for this repository. If it is, prevent duplicate or accidental automatic archiving before creating the GitHub Release. A `.zenodo.json` file is **not** added here: Zenodo gives it priority over CITATION.cff, and using a substitute SPDX licence would be inaccurate. An automatic deposit is permissible only after verifying that its actual licence and record type reproduce the authorised proprietary terms; otherwise use the manual route.

Zenodo descriptive **metadata is separately subject to Zenodo's metadata reuse rules**; do not mistake the file-level proprietary licence for a restriction on its metadata. Confirm that the planned description is suitable for an openly indexed metadata record.

## 3. Content and reproducibility boundary

- Scientific inventory is defined by [build_research_snapshot.py](build_research_snapshot.py): canonical Incident records; taxonomy; methodologies; external-governance artefacts; code/templates/tests; relevant maintenance sources; selected index/schema and rights files. The transient `vigil/docs/reviews/` campaign packets and release-preparation notes are **outside the scientific checksum scope**, although they remain accessible in Git history and the source repository.
- The generator reads exact committed **Git blobs** and records per-file SHA-256 and an aggregate digest. Its working-branch CI artifact is **preflight**, not the final research release. Run `--write --require-main` and `--check --require-main` on the **final approved main commit**. Publish the generated manifest as a file alongside the frozen payload.
- If a **full GitHub source ZIP/tarball** is deposited, its contents include non-scientific documentation and review packets beyond the manifest's scientific scope. State this explicitly: the aggregate scientific checksum does **not** attest to every byte of the full GitHub archive. Prefer an audited **scientific-scope bundle** plus the manifest and rights/citation documentation if the maintainer wishes to avoid depositing process material.
- Check third-party source-material rights before bundling any screenshot, archived article, PDF or external full text. A source citation is not an assignment of copyright; links to third-party evidence are not a licence to upload it.
- Confirm any repository-integrated publish process did not advance main after approval. **Tag only the exact main commit whose final scientific inventory was checked.**

## 4. Release sequence and authorisation gates

1. **Finish the five pre-approved promotions** (INC-034, 062, 101, 145, 195). The one-time script `apply_approved_five.py` is **staged but not executed** as of 25 October. It must remove itself and regenerate the public indexes. INC-118 retains its evidence hold. If promotions cannot be completed, explicitly elect a 164/200 release instead; do not claim 169/200.
2. Review the PR #162 diff for temporary files, non-scientific research notes, publication labels and unexpected code changes. Complete all pinned non-destructive rebuild checks, Incident/taxonomy/external tests, rights checks and exact-HEAD CI. Do not erase genuine source uncertainty for coverage.
3. Obtain **maintainer approval** for the specific release branch content, dataset v1.0.0, proposed licence, Zenodo metadata and deposit route. Mark PR ready and merge **only then**.
4. Freeze and identify the integrated `main` commit. Update `CITATION.cff` on main to the **actual v1.0.0 release version/date when known** (remove legacy 0.1.0 / 2026-06-01); never guess the DOI. The final tagged source tree, citation and manifest identity must agree.
5. Run `python vigil/releases/siai-2026/build_research_snapshot.py --write --require-main` and then `--check --require-main`. Keep the resulting JSON preflight manifest outside any self-hashing loop and attach the exact approved manifest to the release/deposit. Re-run CI after all code and citation changes. Record the commit SHA, taxonomy edition/count, Incident taxonomy-version distribution, file count and aggregate SHA-256.
6. With approval, create the immutable `v1.0.0` Git tag at the checked commit; prepare GitHub Release notes from section 5 below. Inspect the actual downloadable archive and compute its separate SHA-256. Check the scientific manifest and archive's **different scopes** as explained above.
7. Create the **manual Zenodo dataset draft**, enter vetted metadata, attach the rights-approved frozen archive/bundle and research manifest, set the correct custom licence, and inspect the full draft (creator, rights, file visibility, title, version, commit, checksum and files). **Publishing is a separate maintainer action.**
8. Publish after rights and source-archive approval. Record the resulting *version-specific* Zenodo DOI and record URL; update downstream citations, website and the SIAI manuscript. Never substitute the concept DOI for the specific version DOI when reproducibility needs this edition.

**Release stops:** incompatible/open licence metadata; missing rights approval; scientific checksum not matching the tagged commit; stale canonical/generated indexes; failing source/validation CI; an undeleted temporary promotion script; unverified third-party uploads; contradictory declared edition counts; an unapproved DOI/citation.

## 5. Draft GitHub Release notes (not yet a published release)

**Title:** VIGIL Observatory v1.0.0 — SIAI 2026 Research Dataset

VIGIL Observatory v1.0.0 freezes a versioned, evidence-linked public research corpus of 200 admitted AI-governance Incidents and its accompanying Alignment Taxonomy v0.8.1, Harm Impact methodology, external governance references, schemas and validation utilities.

**Publication boundaries:** Cases preserve source attribution, evidence limitations, unresolved/disputed classifications, role-specific alignment results and historical taxonomy editions. The corpus is AI-assisted and human-governed; the release is not a claim of complete original-source authentication, independent human coding, legal compliance or safety certification. The exact research commit and per-file scientific checksums are documented in the release manifest.

**Rights:** © 2026 Phoenix Covenant Pty Ltd trading as CAM Initiative. Proprietary VIGIL Observatory Licence; publicly viewable and citable, with substantive reuse subject to the accompanying LICENSE.md. Third-party referenced materials remain under their own rights.

**Complete these fields only after release approval:** final tagged commit, incident edition distribution, aggregate research SHA-256, archive SHA-256, actual release date, Zenodo version DOI and access URL.

## 6. Final receipt template

- Maintainer approval and rights approval: **PENDING**
- PR #162 merge commit: **PENDING**
- Final tagged `main` commit / `v1.0.0`: **PENDING**
- Final CFF version/release date/creator confirmation: **PENDING**
- Canonical Incident count / taxonomy edition: **200 / 0.8.1** (verify at tag)
- Final canonical incident-edition distribution: **PENDING**
- Exact-HEAD CI run links: **PENDING**
- Research-manifest source commit / aggregate SHA-256: **PENDING**
- Archive filename, scope and SHA-256: **PENDING**
- Third-party upload rights assessment: **PENDING**
- Zenodo route, visibility, custom licence and rights-holder approval: **PENDING**
- Zenodo version DOI / concept DOI / public URL: **PENDING**
