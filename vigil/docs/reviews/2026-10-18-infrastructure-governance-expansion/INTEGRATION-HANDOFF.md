# Incident integration and website follow-up

Date: 18 October 2026. Classification: REVIEW. No canonical Incident or website change is applied by this package.

## Integration baseline

The initial ingestion HEAD was `59a19ab5c35832d2a255ad377645a2de8c02fb9e`. During this session it advanced to `adac7b35b5f8edd3a0f9d666666ff3b6a40dd123`, a hold-register reconciliation commit. The three affected records were byte-unchanged between those commits. Proposals are pinned to the latter HEAD and retain full record-byte digests. The development branch remains separate; no ingestion history is merged here and no Incident file is copied into this branch.

| Proposal | Retained rows | Excluded canonical candidates | Main distinction |
| --- | --- | --- | --- |
| INC-000199-proposal.json | 5 | 10 | Backend device-authorisation and logical-access outcomes are Not aligned. Configuration, service-monitoring and final containment evidence has named Boundary facts. Authentication, backend authorisation, reported camera access and the separate PIN route remain distinct. |
| INC-000200-proposal.json | 8 | 7 | Actual unauthorised logical use is Not aligned. Account/permission mechanics, configuration controls, monitoring and restoration checks are separately reviewed. Most-U-store intervention, Mirepoix losses, Gradignan changes and other site effects are not flattened into one command or mechanism. |
| INC-000203-proposal.json | 8 | 7 | Unauthorised configuration interference is distinct from the successful Bordeaux intervention, Lescure's prior defensive changes, Lescure losses and unresolved command/access origin. |

Each candidate review retains the exact requirement ID, relevance decision, evidence or exclusion, and decisive missing fact where applicable. Proposed rows use independent identification because source relevance is adjudicated directly. This does not bypass source/relationship admission; class candidates were also exercised separately in pipeline-qa.json. A class role never selects external polarity.

For INC-203, the site audit explicitly records the bounded Bordeaux containment outcome as **Aligned** and the Lescure containment question as **Boundary**. The proposed single RS.MI-01 occurrence row is **Boundary** because Lescure's containment timing, scope and persistence are unresolved. Its basis explicitly preserves the positive Bordeaux finding. This respects the existing uniqueness rule of one canonical assessment per requirement ID; it does not average results or treat successful detection as comprehensive compliance. The source-specific monitoring outcomes remain separately unresolved because temperature supervision is not proof of network security-event coverage.

No Aligned finding is inferred from absent failure evidence. No Not aligned finding is inferred merely from food loss. No Boundary result is based on unknown certification/adoption. Requirements with unestablished plan-initiation, backup-use, temporary-access or producer-default conditions remain excluded, rather than turning every unknown into a public row.

## Safe later application

1. Re-read the then-current ingestion records and compare the recorded byte digests and evidence. Re-adjudicate any material intervening changes.
2. Ensure the canonical requirement/source/relationship additions are available to the integration target through a separately authorised integration. Do not apply assessment IDs before they resolve centrally.
3. Apply only the accepted proposal rows through the ingestion branch's current adjudication and provenance workflow. Append review provenance and preserve its existing evidence, clauses, taxonomy, HIM and occurrence narratives. No broad repair or Incident rebuild is proposed here.
4. Run the occurrence, canonical/public, provenance and subsystem checks on that branch. Rebuild its generated indexes through the supported builder. Do not overwrite that branch or combine divergent histories as an incidental step.

The development branch still has 189 canonical Incidents, so its production index cannot truthfully publish rows for the later ingestion-only cases. The in-memory overlays validate the proposed assessment fields, resolving evidence references and navigation counts without making that publication claim. There are 21 proposed rows, not 21 already published findings.

## Section 04 and renderer follow-up

No change is made to `CAM-Initiative/cam-governance-catalogue`. The earlier source-path inspection in the 11 October PUBLIC-CATALOGUE-TRACE.md remains historical evidence, not a fresh deployed-render check.

The exact consumer contract is:

- Read `external_requirement_assessments` from the canonical Incident. The lightweight index exposes only `external_requirement_assessment_count` and search metadata.
- Resolve each `requirement_id` through the canonical EXTREQ corpus. Preserve `external_source_id`, `source_version`, `clause_or_control`, `requirement_summary`, `source_role`, `normative_force`, `applicable_actor`, `applicability_conditions` and `exceptions_or_qualifications` in the requirement/source view.
- Render `alignment_result` as Aligned / Not aligned / Boundary. Display `assessment_basis`, `assessed_on` and resolving `source_record_refs` without converting voluntary force into a weaker result or a legal-breach claim.
- A registered source with zero extracted requirements is listable as a source, with its actual role, access and extraction status. It must not appear as a completed occurrence assessment. IEC 62443-3-3 and the held EN sources have no fabricated EXTREQ rows.
- Contextual references, relationship-ledger candidates and taxonomy roles cannot create Section 04 rows, counts, polarity, filters or exports. Empty assessments mean no published assessment, not positive compliance.
- Preserve scope in the evidence explanation. For a multi-site occurrence, do not display Bordeaux's success as a claim about Lescure, or Lescure's losses as failure of all Bordeaux controls. If a future renderer offers site-level assessment rows, that needs a separate explicit data-contract decision; no new Incident field is introduced here.
- Source-list and dossier umbrella wording should accommodate governance instruments beyond AI-specific standards. Do not describe every framework or law as a consensus standard. Check print/PDF views against the same field and label contract.

These are reviewable downstream acceptance requirements, not a claim that the live website has been tested or changed.

## Holds

IEC 62443-3-3:2013 requires authorised normative-text access and intended-use permission before provision extraction. NIST Rev.4 remains draft. EN 18286 and its citation-decision access holds are unchanged. NIS2 entity/transposition conditions and CRA commencement/reporting conditions are documented in SOURCE-REVIEW.md. The two baseline FC-084 referential defects remain separate and unmodified. No Gate 2 corpus repair was performed.

Gmail staging is unavailable in this Codex session. The ready-to-merge action payload is preserved in MAINTAINER-ACTION-EMAIL.md; it has not been sent or merged with an existing queue.
