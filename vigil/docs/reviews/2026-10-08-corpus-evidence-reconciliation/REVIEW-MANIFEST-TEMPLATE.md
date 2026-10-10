# Per-Incident source-first reconciliation manifest — working template

This is an authoring template for future dated `INC-XXXXXX` review manifests; it is **not** a schema, a validator, or permission for automated canonical changes.

- **Identity and baseline:** Incident ID, frozen branch/commit, canonical file SHA, incumbent class/review/HIM status, all independent EXTREQ row counts.
- **Source ledger:** source record index, exact URL, publisher, publication date, retrieval date, role (primary, affected party, reporting, context), reviewed section/range, availability/access limits, confidence and conflicting accounts.
- **Material episode ledger:** stable *review-local* candidate episode label, actor and bounded activity, environment and target, observed output/effect, relative time, explicit unknowns or concurrent branches, source-specific supporting record indices. A review-local ID is not a canonical schema addition.
- **Proposition disposition:** each material claim from reviewed sources is included, source-context-only, a supported duplicate, outside occurrence scope, unresolved or material omission. Explain why.
- **Old-clause crosswalk:** for each original source-clause index, preserve original text reference and exact candidate new episode(s); record retain, merge, split, reorder, contextualise or unresolved; state evidence and risk of lost detail.
- **Taxonomy crosswalk:** every existing canonical class and role; source episode support and invariant/success/failure recognition. Flag potential new/withdrawn/revised class, but never implement role changes merely because clauses merge.
- **External governance crosswalk:** all `external_requirement_assessments[]` row identifiers, existing position pointers, evidenced old/new episode(s) and unchanged/changed assessment determination. Keep independent alignment result unless specifically re-adjudicated.
- **Harm review:** existing HIM basis and severity; classify as unchanged, review-triggered or unresolved. Do not inflate harm from an estimate or from theoretical effects.
- **Public projection:** compare Stage 01 summary, Stage 02 chronology and explanation, Stage 03 classifications, Stage 04 compliance and Discussion/Conclusion; preserve uncertainty.
- **Evidence review gate:** completeness must mean *source set reviewed and material propositions dispositioned*, not mapped-clause count. Distinguish AI-authored candidate, human-reviewed/approved, validated in worktree and published.
- **Verification:** commands, deterministic builder output diffs, all validator/test results, commit links and known unavailable checks; never claim CI green unless verified.
- **Stop/escalate:** if primary evidence is disputed, taxonomy boundary changes, harm changes, schema controls change or index references cannot be reconciled, leave canonical file unchanged and record maintainer decision needed.

Do not silently delete source statements, fabricate chronology, flatten successful boundary recognitions or reinstate the obsolete Incident × FC matrix.
