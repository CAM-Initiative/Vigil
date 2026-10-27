# Approved design implementation — 27 October 2026

**Current branch state.** The maintainer approved the concrete two-class/new-family proposal and instructed proceeding. Implementation remains in the same integrated PR #172 on `agent/taxonomy-development`. This approval permits the reviewed class and standards proposal to be materialised. It does not authorise merge, publish the taxonomy, verify inaccessible ISO text or rewrite Incidents.

| Taxonomy identity | Approved property |
| --- | --- |
| VIGIL-FF-0018 | Information Protection and Custody Integrity |
| VIGIL-FC-000089 | Protected Information Access Integrity |
| VIGIL-FC-000090 | Authentication Material Custody Integrity |

The canonical index retains published **v0.8.1** and its date and release history. Its single `working_release` proposes **v0.9.0**, minor, unpublished. The new family contains both approved classes, complete independent positive/adverse recognition, scoped exclusions and precise standards references. Existing class identities and family assignments are unchanged. The existing identity-preservation test fixture now includes the two authorised identities in their new family; its assertion and all validation logic remain unchanged.

## Source and requirement promotion

Nine requirements have been promoted to canonical source/version shards:

- NIST SP 800-53 Rev. 5 Release 5.2.0: AC-3; AC-6; IA-5(a); IA-5(g); IA-5(h); SC-8; SC-28.
- NIST IR 8587, September 2026 final: the signing-key storage/use protection proposition in §5.1.1.3, and the backup/archive distribution protection proposition in §5.1.1.2.

Eleven class relationships now resolve through the canonical relationship dataset and source-specific review-evidence packets. Each has the exact source version, control locator, canonical requirement identity, requirement digest, class-semantic digest, scope correspondence, support strength and limitation. Both classes have resolving `external_references`. The requirements have compatible field-level metadata dispositions and source-fidelity entries. The canonical requirement count is **1,130**.

The initial proposal used “partial” to describe the limited lifecycle or object coverage of some relationships. The retained admission review now distinguishes **strength of component correspondence** from **breadth of coverage**. AC-3 and IA-5(g) directly support their stated properties. Recipient verification, specific authenticator protection, task-limited access, selected information protection at rest/in transit and the narrowly scoped signing-key controls substantially support their stated components. Their admitted strength is strong-supporting; their coverage remains explicitly limited and `whole_invariant_supported` remains false. The requirement and class criteria are not altered to manufacture equivalence. The complete before/after relationship-strength reasons are retained in `approval-and-admission.json`.

Six propositions remain review-only: IA-5(b), (c), (d), (e), (f) and (i). Initial content, strength, administrative procedures, default changes and rotation context do not independently provide a substantial relationship to the approved access/custody properties. No corresponding EXTREQ reference is left dangling in a canonical class. IA-5(d) is retained only as clearly labelled source-level contextual guidance.

Both NIST extraction scopes are **partial**. The existing fidelity ledger uses **provisional** for their source-level state because other sections remain unreviewed. The selected propositions were compared with their primary text, but neither complete extraction nor whole-source assurance is claimed. The SP 800-53 OSCAL digest remains pinned. The IR PDF byte-download limitation remains recorded; no PDF digest is invented. SP 800-53A assessment content is not misattributed to SP 800-53 control statements.

## Remaining ISO blocker

ISO/IEC 27001:2022 and ISO/IEC 27002:2022 remain metadata-only registrations with blocked normative extraction. Their proposed controls, exact wording, qualifications and class relationships have not been verified from authorised normative text. No ISO requirement identity has been manufactured. The 27001 amendment and 27002 corrected-version qualification remain explicit. Final integrated completion is therefore **not claimed**.

The maintainer's design approval does not resolve the source-access/permission blocker. Keep PR #172 draft while the requested ISO control-level integration remains incomplete. Do not silently publish a supposedly complete ISO/NIST-backed taxonomy.

## Evidence and validation boundary

The seven preserved-evidence design tests and two hypothetical calibration cases remain review evidence. No Incident adjudication, source clause, harm assessment, external requirement assessment or historical interpretation has changed. The canonical class and requirement additions are an unpublished proposal until the controlled release sequence completes.

`validation-admission.json` records the final checks for this implementation. The original `validation.json` remains the audit of the earlier proposal-only state. The original proposed payloads are retained as review history, not a second governing taxonomy or duplicate active requirement corpus. Approval, allocations, admitted requirements and the six retained review-only propositions are recorded in `approval-and-admission.json`.
