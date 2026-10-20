# FC-045 — authorised investigative evidence access operational-scope repair

Date: 2026-10-20. Work branch `work/incident-taxonomy-reasoning-readjudication-20261018`. PR #140. Taxonomy 0.8.1 (patch after FF-0017 v0.8.0 admission).

## Approved governance instruction and exact scope

The maintainer approved P2: FC-045 must include the **effective operation** of an otherwise existing investigative evidence access pathway. A missing/defective pathway and an **unjustified denial, restriction or delay within an authorised pathway** may each independently breach the class where a valid authority, requested scope and material investigative impairment are demonstrated.

This is not a general mandate for self-authorised inspection, unrestricted research-model access, compulsory discovery or automatic disclosure of private information. Applicable lawful or otherwise valid voluntary agreements may create appropriately bounded obligations; lawful and proportionate confidentiality/privilege/security restrictions remain exclusions. An appeal or subsequent correction is not proof the original denial was justified; a production order is not proof evidence was actually produced.

## Normative changes

- Versioned FC-045 definition, invariant, failure and success recognition conditions and exclusions, along with the family FF-0004 parent invariant/inclusion/failure description, to include provision and effective operation of governed pathways.
- Preserve immutable class and family identifiers: `VIGIL-FC-000045` and `VIGIL-FF-0004`, including peer FC-044 and surrounding family allocations; parent family version 0.1.4.
- Revised examples distinguish route-absence, route-operation denial, governed fulfilment, justified withholding, and separate remedial episodes.
- Two prior taxonomic ambiguous-boundary exemplars updated in *interpretation only* so INC-008 no longer rests on the mistaken assumption that any existing discovery route excludes FC-045. INC-109 no longer needs compulsory statutory power as a universal prerequisite. Their outcomes remain evidence-limited.
- Dataset release advanced from 0.8.0 to 0.8.1 (patch), dated 2026-10-20, with canonical content digest and all existing family standard version/date headers advanced. Release history preserved.
- Two explicit invariant-regression tests added to prevent reintroduction of absent-route-only logic or substitution of appeal success for original-decision success.

## Incident evidence and holds

**INC-008**: A source-supported original denial of FRT discovery was appealed and ordered corrected. The source evidence must be independently assessed to determine original withholding's authority/scope/justification and appropriate role under v0.8.1; appellate ordering of production is not proof of fulfilled production, custody or review safeguards. Keep original decision and remedy episodes separate.

**INC-109**: Public evaluation roles, provider restrictions, reported limited and later access do not reveal the exact operative pre-release agreement or the lawfully permitted restriction/withholding basis. The amended class permits genuinely independent **voluntary** obligations but no unlimited entitlement. Retain evidence-limited disposition pending source-based adjudication.

This commit does **not** rewrite the Incident corpus or its historical taxonomy stamps, especially while independent FC-089 readjudication runs in a concurrent thread. Neither taxonomy amendment changes HIM or independently establishes EXTREQ compliance.

## Validation and publication

Validate taxonomy schema, family membership/peer relationships, SHA-256 content release digest, focused and full tests and three PR CI workflows. Generated Full Reference PDF is refreshed through the established workflow after merge to `main`, not overwritten manually here.

P1 FF-0017/FC-089 is canonical as of v0.8.0 and remains intact; P3 FC-079 expansion is separately unapproved and pending resubmission. External ISO source admission is tracked in issue #154, not implied by FC-045.