# Pending external-source expansion — 1 October 2026

Repository: `CAM-Initiative/Vigil`

Branch: `work/expand-pending-external-sources`

Base: `work/integrate-external-requirements-001-179`, commit `3a7bb01816c1e3ff590f9011e92a397522113696`

119 canonical EXTREQ records were added to three source/version shards. The corpus grows from 978 to 1,097 records across the same 85 registered source versions. Two sources are complete **within their declared extraction boundaries**; C2PA remains partial. Canada could not be extracted from verified primary text in this session. IEEE remains not-started under the expressly requested conditional-access rule.

The accompanying [machine-readable acceptance record](2026-10-01-pending-external-source-expansion.json) records allocated identities, exact available source digests and checks. All 978 pre-existing EXTREQ records and all historical source-review events are unchanged. No Fidelity Class, taxonomy relationship, Incident, CAM assessment or EU AI Act requirement was changed.

## Source results

| Source/version | New EXTREQs | Extraction status | Fidelity disposition | Access/provenance |
|---|---:|---|---|---|
| CETS No. 225 / 2024-09-05 | 54 | complete within declared scope | assured within that scope | Official Council of Europe PDF read through the web reader; original PDF byte download returned 403. No original-artefact digest claimed. |
| OECD/LEGAL/0449 / 2024-05-03 | 37 | complete within declared scope | assured within that scope | Official OECD instrument PDF retrieved directly; exact bytes SHA-256 recorded. |
| Canada Directive / current-2026-09-28 | 0 | not-started | no new substantive fidelity assessment | Official TBS primary endpoint returned a rejection page; exact registered snapshot not verified. |
| C2PA Technical Specification / 2.4 | 28 | partial | provisional | Versioned official HTML retrieved directly; exact bytes SHA-256 recorded. Version history explicitly identifies April 2026. |
| IEEE 7003 / 2024 | 0 | not-started | no clause-fidelity claim | Publisher edition metadata verified; substantive exact-edition text inaccessible through the lawful free GET route. |

The access categories for Canada and IEEE retain the registered public-primary **route**. Their access notes and inaccessible/unreviewed sections explicitly deny successful primary-text retrieval in this session. An available route must not be interpreted as a retrieved or analysed artefact.

### Council of Europe CETS No. 225

Primary text: <https://rm.coe.int/1680afae3c>. The title and Vilnius date identify the registered 5 September 2024 text.

**Scope:** Article 1(2), Article 3(1)(a)-(b), Articles 4-20 and 24-26. Independently assessable duties are separated, including documentation versus authorised-body access versus affected-person disclosure, transparency versus oversight, oversight independence versus capacity, and policy reporting versus format-setting. Article 16(1)'s linked risk-management action and Article 16(3)'s recommended documentation/feedback action preserve constituents explicitly.

**Excluded/contextual material:** preamble; Article 1(1)/(3); Article 2's definition; Article 3(2)-(4)'s scope qualifications as standalone records; Articles 21-22's rights safeguards as standalone records; Article 23 Conference procedures; Articles 27-36 final institutional/treaty procedures. Articles 2-3, 21-22 and 30-33 nevertheless inform interpretation and applicability. This is not whole-treaty atomisation.

**Applicability and force:** the actor is the Party implementing the Convention, with the Conference of the Parties separately identified for Article 24(2). Public authorities and private actors acting on their behalf are distinguished from other private actors governed through the Party's declared implementation choice. National security, pre-use R&D/testing and national-defence exclusions remain explicit. Duties are conditional on entry into force for the relevant Party and territory; signature alone is insufficient. Existing rights and wider protections are preserved.

**Interpretation issues:** Article 13's invitation is recorded as recommended practice; Article 16(3)'s “should” documentation/feedback is separated from the Party's “shall” duty to maintain response measures. “Shall seek to ensure” provisions retain that qualified undertaking rather than asserting guaranteed outcomes. The registered `open-for-signature-not-in-force` lifecycle was retained; the current depositary chart did not expose substantive status through the available reader, so no refreshed entry-into-force finding is made.

**Schema limits:** `normative_force: binding-law` describes the treaty authority category, while the contingent legal effect and territorial/Party qualifications must be carried in strings. The schema has no separate ratification/territorial applicability or qualified-best-efforts modality object. These limits are disclosed rather than resolved by a schema change.

### OECD Recommendation, revision 3 May 2024

Primary text: <https://legalinstruments.oecd.org/public/doc/648/648.en.pdf>. Its background expressly identifies the Council's 3 May 2024 revision; the downloaded booklet's 2026 copyright wrapper is not treated as a new substantive instrument revision.

**Scope:** all substantive Section 1 principles 1.1-1.5 and Section 2 national-policy/international-cooperation recommendations 2.1-2.5. Sections II-V provide actor and interpretive context. Independent public/private investment recommendations, policy experimentation/outcome flexibility/interoperability, worker preparation/skills/transition, and international knowledge/standards/indicator/evidence expectations are separated.

**Excluded:** background/history, definitions as standalone EXTREQs, Sections VI-VII dissemination/adherence invitations, and Section VIII OECD committee administration/reporting instructions. These exclusions bound completion; this is not a claim that every Council instruction was extracted.

**Applicability and force:** Section 1 distinguishes stakeholders from lifecycle AI actors, while Section 2 targets governments of Adherents and preserves the special attention to SMEs. Context, respective roles, ability to act, technical feasibility and state-of-the-art qualifications remain where specified. Examples such as data trusts or worker-transition programmes are not converted into universally required implementations. The complementary principles must be considered together.

**Interpretation issues:** no unresolved proposition-level conflict was identified within this scope. Recommendation-level “should” expectations remain recommendations, not binding legal duties. The governance-expectation category does not claim adoption or actual implementation by any country or organisation.

**Schema limits:** the closest existing force category is `government-voluntary-framework`; the registry separately identifies the intergovernmental recommendation. The schema has no dedicated OECD-adherence or intergovernmental-recommendation force object. Actor and adherence context therefore remain explicit textual conditions.

### Government of Canada Directive

Registered source: <https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=32592>.

**Result:** zero EXTREQs. The official endpoint, `section=html`, `section=text`, reordered query, hostname and language variants returned a 244-byte “Request Rejected” page or failed. The web reader likewise exposed the rejection. Search-index fragments show portions of substantive clauses but cannot establish the complete registered `current-2026-09-28` snapshot, responsible actors, administrative scope, exclusions or impact-level tables. An official publications record for a 2021 edition was discoverable; it was not substituted for the registered current snapshot.

**Excluded:** all inferred extraction from snippets, older editions, secondary reproductions or general Canadian AI guidance. No duties are generalised to all AI systems.

**Next action:** obtain a complete accessible official copy of the registered snapshot, document its version identity and provenance, then extract Section 6 and relevant impact-level controls alongside the actual scope, actor, exemption and implementation provisions. Representation difficulties cannot responsibly be assessed without this primary text.

### C2PA Technical Specification 2.4

Primary text: <https://spec.c2pa.org/specifications/specifications/2.4/specs/C2PA_Specification.html>. Section 5.3.1 identifies **2.4 — April 2026**.

**Scope:** first-pass provenance-integrity and AI-disclosure controls in Sections 6.5-6.8; Section 9.1 hard-binding cardinality; Sections 10.3.2.1-2 and 10.3.2.4; Section 15.2.1; and Sections 18.28.2/18.28.4. Records distinguish mandatory technical requirements, recommended practice, optional validation-context fields and an informative external-data validation boundary. The collision-handling branch is preserved as a source-defined compound rather than pretending all branches apply simultaneously.

**Excluded/unreviewed:** the remaining assertion syntax/encoding controls; detailed identifier, binding and hash formats; signing algorithms, certificates, trust lists, timestamp and revocation procedures; detailed validation algorithms and status-code definitions; most standard assertions; live-video controls; embedding appendices; full schema atomisation. References to these procedures preserve their governing dependency, but do not claim those dependencies were fully extracted. Informative discussion, examples and commented-out pending fields are not converted into active requirements.

**Applicability:** controls identify generators, validators or consuming applications as appropriate, and condition obligations on use of the relevant construct. AI Disclosure itself is not made mandatory for every AI asset. Optional fields retain their conditional type constraints. Provenance validation does not establish factual truth, content quality or that declared human approval actually occurred.

**Unresolved source conflicts:** Section 18.28.2 restricts `modelType` to Table 12, while Section 18.28.4 CDDL permits `tstr`. The `scientificDomain` CDDL uses a list/sequence while the example supplies a scalar. The affected three records retain the prose rule and disclose these conflicts with `interpretation_status: needs-specialist-review`. The declaration of human-oversight level has explicit allowed values but does not independently verify the claimed human involvement. Full-source status remains `partial`, with `provisional` fidelity.

**Schema limits:** EXTREQ stores datatype/cardinality and branching constraints as textual conditions and constituent propositions; it is not an executable CDDL/conformance model. These fields cannot themselves prove protocol implementation or resolve upstream prose/schema disagreements.

### Conditional IEEE 7003-2024

Identity metadata: <https://standards.ieee.org/ieee/7003/11357/> identifies the active **IEEE 7003-2024**, approved 11 December 2024 and published 24 January 2025. The official no-cost substantive access route is <https://ieeexplore.ieee.org/browse/standards/get-program/page/series?id=93>, which returned HTTP 418. Direct publisher download access was not available. No licensed or other substantive exact-edition copy was supplied or verified.

Catalogue descriptions, metadata, secondary summaries and the separate P7003 approved-draft listing were not treated as normative text. The source remains `not-started` with zero records and an explicit provenance/access blocker.

## Build, validation and source-history integrity

The canonical shards, scope/fidelity/assurance ledgers and append-only substantive review events were updated. Aggregate requirements, indexes, completeness and coverage projections, source catalogue/queue, access reports and metadata-review reports were regenerated through the existing builders. All 13 relevant validator/test commands in the acceptance JSON pass using `PYTHONPATH=vigil/scripts`.

Expansion exposed an external-source validator defect: it compared **every historical review method** with the current extraction state. It now validates the historical method vocabulary while comparing only the current review event against current scope. A small isolated regression exercises historical access/state changes, current-state mismatch rejection and malformed historical methods. Historical events remain byte-equivalent JSON values to the base.

External-subsystem snapshot tests were repaired to compare shards against represented source/version keys, current projection provenance against its current canonical event, fidelity counts against their canonical ledger, ledger IDs against canonical requirements, and aggregate timestamps against their manifest. The August model-attribution test now applies to its stated August scope. No Incident validator, schema, publication rule or canonical Incident acceptance condition was changed.

One-off acceptance checks confirm deterministic IDs, no new taxonomy/CAM relationship fields, all 978 existing records unchanged, original source-review history preserved, and no taxonomy/Incident/CAM-assessment changes. Existing release 0.2.0 artefacts remain historical; this branch does not publish a new distributable release or assert a new release version.

## Cross-source taxonomy coverage questions

This is a read-only concept comparison against the base taxonomy, which is undergoing semantic repair. These are provisional coverage questions, not new classes, class mappings or Incident findings:

- **Substantive equality and equitable outcomes:** CETS Articles 10/17/18 and OECD 1.1/1.2 address discrimination, structural inequality and particular vulnerabilities. Existing authority/agency controls do not visibly supply a dedicated invariant for these substantive outcomes.
- **Effective remedy and broad contestability:** CETS 14-15 and OECD 1.3(iv) protect complaint, challenge and procedural rights. Evidence-access and narrowly scoped access-continuity safeguards cover parts of the mechanism, but a general accessible-remedy invariant is not evident.
- **Democratic participation and public consultation:** CETS 5/19 protects institutional processes, public debate, opinion formation and consultation. Oversight independence and governance neutrality overlap, but do not plainly cover the whole obligation.
- **Digital literacy, worker transition and inclusive AI ecosystems:** CETS 20 and OECD 2.1-2.5 create public-capacity, labour-transition, investment and international-interoperability expectations without obvious dedicated taxonomy invariants. Some are institutional policy objectives outside an occurrence-level Alignment Taxonomy's intended remit.

C2PA's provenance, evidence integrity, identity collision handling and declared-versus-verified human involvement have substantial conceptual adjacency to existing mechanisms; exact protocol constraints are not automatically taxonomy gaps. Environmental protection is already represented in the taxonomy and should not be called wholly absent merely because the external sources have wider policy objectives.

Reconsider these questions after invariant-oriented definitions are repaired. Do not infer a need for one Fidelity Class per external requirement, and do not infer an occurrence-level failure from the existence of any requirement.
