# Protected information and authentication custody — admission review

**27 October 2026 · REVIEW · approval pending**  
Repository baseline: `8294c4f3eec1e5ad6f12ab7b75aabb7f69ddba9f`. Published Alignment Taxonomy: **v0.8.1**. Tracking: [issue #171](https://github.com/CAM-Initiative/Vigil/issues/171). Work lane: `agent/taxonomy-development`. One integrated PR contains this design and its supporting standards work.

## Proposed decision

Approve two peer Fidelity Classes in a new **Information Protection and Custody Integrity** family:

- **Protected Information Access Integrity** governs demonstrated unauthorised access, acquisition, disclosure or modification of protected information.
- **Authentication Material Custody Integrity** governs secret authentication material crossing its independently established custody boundary. Later impersonation, account takeover or use of the exposed material is not a recognition condition.

The classes contain complete standalone invariants, definitions, separate adverse and positive recognition conditions, explicitly scoped exclusions, hypothetical illustrations and structured `external_references`. They have **no allocated canonical identities** and are not selectable classes. Review labels `candidate-a` and `candidate-b` carry no canonical identity authority.

The new family passes the proposed bounded-invariant test: both children concern preservation of an independently established information-protection boundary. They distinguish enforcement of permitted information operations from custody of secret authentication material across handling and lifecycle stages. This is not a general security family. Private conversations can be disclosed without any credential loss; a secret can leave custody without any later protected-resource access. The specialised custody class handles a secret-only exposure. Independently evidenced private content or a separate unauthorised information operation can engage the access class in the same occurrence.

`abstraction-boundary-review.json` compares all 17 current family invariants and 13 materially adjacent classes, including the six classes in the handoff. The current access/session family requires state coherence and representation; the authority family requires authority derivation or transfer; the control family requires specific activation/effect predicates. Static disclosure does not establish those mechanisms. Broadening any of these parents would change its bounded property rather than simply accommodate an existing child.

## Standards findings and limits

| Source/version | Registration and source review | Extraction and relationship state |
| --- | --- | --- |
| ISO/IEC 27001:2022, edition 3 | Publisher metadata registered. Separate Amd 1:2024 is acknowledged; consolidated amended text is not claimed. | **Blocked.** No licensed normative text or applicable analytical-use permission supplied. No ISO EXTREQ or verified Annex A relationship. |
| ISO/IEC 27002:2022, edition 3, corrected English version March 2022 | Publisher metadata registered; corrected-version qualification retained. | **Blocked.** No licensed control wording, modality or clause-level relationship verified. |
| NIST SP 800-53 Rev. 5, Release 5.2.0 | Official release note and commit-pinned OSCAL checked. Exact reviewed bytes have SHA-256 `64ca6b4161de51ab6af098a7d101d326f14c95e1abf721396cd8a049e8115eeb`. | 13 independently assessable review-stage propositions: AC-3, AC-6, IA-5(a)–(i), SC-8, SC-28. Original control statements and parameters are distinguished from SP 800-53A assessment content. |
| NIST IR 8587, September 2026 final | Final publication history dated 15 September 2026. Selected primary PDF sections reviewed through web reader; byte download returned HTTP 403, so no PDF digest is claimed. | Two review-stage propositions on signing-key storage/use and backup/archive distribution. Partial support within asymmetric signed-token and federal-environment scope; **not direct API-key control support**. |

**Direct source support:** SP 800-53 AC-3 addresses enforcement of approved logical-access authorisations. IA-5(g), not IA-5(h), addresses protection of authenticator content from unauthorised disclosure and modification. IA-5(h) separately concerns specific individual/device controls. These distinctions were checked against the exact release.

**Preserved qualifications:** AC-6 is task-limited least privilege. SC-8 permits the organisation to select confidentiality, integrity or both. SC-28 also requires an organisation-defined protected information set. These controls do not require both properties unconditionally. NIST IR 8587 §1.2 makes uppercase MUST a condition of claimed conformance, while conformance remains voluntary unless policy or a binding agreement determines otherwise. Its §1.1 excludes ordinary API-key and symmetric schemes from the covered controls. NIST does not define VIGIL classes or decide occurrence results.

The ISO discovery shortlist remains 5.15, 5.17, 5.18 and 8.3. Verify control names, exact wording, qualifications and corresponding 27001 Annex A locators only after authorised access. No third-party summary, crosswalk or control title was substituted for licensed normative text.

## Why the NIST extraction is staged

There are **15 prepared EXTREQ payloads, 12 explicit proposed relationships and zero new canonical requirements**. Every proposed requirement has its deterministic identity, source/version, locator, normative force, modality, actor/object/context, provenance and atomicity disposition. Field-level metadata review is separate. Five IA-5 propositions are retained as related security context without manufacturing a custody mapping.

The existing supporting-source admission contract requires a resolving reviewed direct or strong-supporting relationship to an **existing canonical class**, plus compatible metadata and fidelity evidence. Proposed classes have not passed human admission. Partial or contextual support must not be relabelled direct merely to satisfy a gate. The requirement payloads and candidate `external_references` therefore remain REVIEW material. Their IDs resolve within this review packet, not yet through the canonical requirement resolver. Neither a proposed reference nor a source registration implies canonical admission.

After class approval, review which exact relationships meet the existing direct/strong-supporting threshold. Promote only eligible requirements into source/version shards using `external_requirements_io.py`, with metadata, fidelity and digest-bound review evidence. Retain any contextual-only propositions as review material. Update the IR source scope from supporting-only to partial only when its extraction is actually admitted. Complete this work **in this same branch and PR**; no separate standards workstream is requested.

## Recognition calibration

`recognition-tests.json` contains seven criterion-by-criterion, exclusion-by-exclusion design tests using the preserved evidence, with hashes of the untouched Incident files:

| Evidence test | Proposed recognition consequence |
| --- | --- |
| Moltbook private conversations | Candidate A can recognise the demonstrated private-content access. |
| Moltbook agent authentication tokens | Candidate B can recognise reported exposure without requiring later impersonation. |
| DeepSeek chat records | Candidate A can recognise demonstrated protected reads; it does not infer executed operating-system or server writes. |
| DeepSeek API secrets | Candidate B can recognise reported secret availability without inferring use or validity of every individual secret. |
| Moltbook live-post change, then blocked reversal | Earlier adverse modification and later bounded positive protection remain separate in time and route. Later table discoveries prevent a universal remediation claim. |
| Public Supabase connection identifier | Public configuration availability alone does not establish secret status or a custody defect. Distinguish it from the separate agent tokens. |
| Researcher-supplied API key in INC-000180 | Authorised handoff/use does not establish custody loss. Missing evidence about protected transport/storage also prevents an automatic positive custody result. |

Two explicitly hypothetical calibration vectors test observed secret-export denial and a theoretical vulnerability without demonstrated secret exposure. They are not occurrence evidence. The proposed criteria require affirmative positive protection evidence; no failure does not mean Aligned. These tests are design evidence, **not permanent mandated Incident answers or canonical re-adjudications**. Existing classifications, HIM, source records and historical interpretations are untouched.

## Admission and release sequence

1. Obtain maintainer approval of the proposed two-class boundary and new family placement. Resolve the ISO control-text/permission blocker; do not describe ISO control mapping as completed while it remains blocked.
2. Allocate canonical identities only after abstraction and boundary approval. Materialise approved family/class content and reviewed source relationships together. No identity is reserved by this packet.
3. Recheck published main. If the new family is approved, use one canonical `working_release`: base `0.8.1`, target `0.9.0`, minor, unpublished. Preserve published version/date/history until the authorised publication workflow runs. If placement changes, recompute the single target from the published baseline.
4. Promote only requirements whose source, metadata, fidelity and class relationships satisfy the unchanged canonical admission contract. Complete generated-output and regression checks on the resulting canonical proposal before requesting final publication approval.
5. Keep this PR draft while these conditions remain. Human approval is required before final admission/publication. Incident reconciliation belongs after approved taxonomy publication and follows its separate authorised lane.

No canonical `working_release` is inserted yet: the release validator rejects a proposed release with unchanged canonical family/class content. A conditional release proposal is retained in `taxonomy.proposed.json`. Adding fictitious canonical changes or allocating premature identities to activate a version would defeat the existing controls.

## Artefact roles and validation

| Role | Artefacts |
| --- | --- |
| LIVE | Existing source registry, source-scope, source-fidelity and source-review-assurance ledgers; branch-workflow and maintainer documentation. Their new entries describe actual registration/access state. |
| GENERATED | Source catalogue/review queue and external-requirement indexes, completeness/access/coverage projections, rebuilt only with official managers. |
| REVIEW | This README; proposed taxonomy, requirements, standards relationships and metadata review; source investigation, abstraction review and recognition tests. These do not govern current Incident classification. |
| AUDIT | `validation.json`, recording executed checks and limitations. |

The canonical taxonomy still contains 17 families and 80 classes at published v0.8.1. The canonical external requirement corpus remains at 1,121 requirements. No Incident, canonical class, validator, schema, builder or publication guard is changed. Temporary execution scripts and downloaded primary bytes are not committed. Full validation results, the initial environment-only test correction and the limits of review-payload checking are recorded in `validation.json`.
