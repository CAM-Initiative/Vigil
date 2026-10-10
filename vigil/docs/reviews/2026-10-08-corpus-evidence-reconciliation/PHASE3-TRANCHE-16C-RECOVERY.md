# Tranche 16C recovery checkpoint — 9 October 2026

This is a research and validation recovery checkpoint, not an accepted repair tranche.
The published completion count remains **57 of the original 89; 32 remaining**.
Canonical edits for INC-090, INC-093 and INC-106 and three rebuild manifests were
written locally, but the workspace execution service disconnected during testing.
Do not claim those edits were committed or that the test suite completed.

## Baselines and recovery

Canonical review baseline: e2fb4cc3e70049fa764f4114bc9c1beca4b96ded.
Remote subsequently advanced to 1798f6898ad6cdecc7fda9c4ee6e8590716913ba
("Rebuild active public VIGIL registry indexes"), changing only the generated
taxonomy example projection. Preserve that commit; do not overwrite shared history.

Local repository: /workspace/scratch/934097ee96ca/Vigil.
Local scripts: review16c-head.py, review16c-plans.py, review16c-finish.py in its parent.
They have already been run once. Do not run the plans again on edited records:
source additions and append-only provenance would duplicate. Inspect local state first.
Pending records: vigil/records/incidents/VIGIL-INC-000090.json,
VIGIL-INC-000093.json, VIGIL-INC-000106.json.
Pending manifests: INC-000090/000093/000106-phase3-tranche16c-repair-manifest.json
in this directory. All generated outputs must be built and included.

## Pending substantive review decisions

### INC-090
Separate the reported order, implemented terminal cut, affected operations,
a later statement about availability, and the provider dispute into five episodes.
The old three clauses represented taxonomy views of the same cut.
Retain unclassified/partial status. Denial alone does not establish a demanded
concession for class 059; authority conditions also remain unresolved.
Reuters and the Washington Post correction are attributed reporting, not primary
internal orders or contracts. Crimea remains distinct context, not a new episode.

### INC-093
Preserve the initial system-card sample denominators and simulated conditions.
Add the later originating evaluator paper as a separate source:
https://arxiv.org/html/2609.38415v1 (29 September 2026).
It describes revised simulations with cyber classifiers intentionally disabled;
this does not demonstrate a deployed safeguard failed. Its selected-scenario
scope experiment is 26/50 versus 4/49, not the earlier card's 60/499 and 2/500.
Separate setup, initial routes, identity/trust actions, contributions, explicit
prohibition samples, shared capture/reconstruction, and later experiments into
ten episodes. Later non-compaction rates have different scenario distributions.

The later account supports an additional medium-confidence failure-occurrence
mapping to existing VIGIL-FC-000001: generic automated continuation replies
were treated as action-specific permission for out-of-scope conduct without
independent scope authorisation, including recognised automated origin.
No new taxonomy class is promoted. Earlier mappings and confidence remain.
Set taxonomy_version to 0.6.10 and explicitly update classification review provenance.
Document the new mapping and its reason in new_taxonomy_mappings.
Episode E007 must describe actual reported out-of-scope attacks, not setup alone.
The local record and manifest were corrected accordingly.
Reconcile 18 positional external rows, retaining independently evidenced results;
no additional occurrence-specific external finding is asserted.

### INC-106
Separate provider account, first-person credit/data dispute, private-input concern,
provider investigation, October release, and later corrections into seven episodes.
New firsthand source: https://cims.nyu.edu/~tristanb/statement.pdf
(undated; source_date null). Buckmaster expressly does not know whether his data
was used and does not accuse OpenAI. It is not proof of private training-input use.
New repository history: https://github.com/openai/math/blob/main/history.md
(7 October 2026 update). Separate later corrections from September provenance.
Preserve the historical October 6 count of 722 manuscripts; current 719 reflects
three later withdrawals. Do not retrospectively replace the historical count.
Retain unclassified/partial status and unresolved 055 boundary.
Three independent external Boundary findings and HIM remain unchanged.

## Validation observed before interruption

All three exact-baseline rebuild guards passed after adding the explicit reason
for the new 001 mapping. The public builder completed.
Canonical validation passed for 179 records; public index validation passed.
Source provenance passed for 623 sources. Interpretive provenance, component
roles, authorship, and occurrence requirement assessment validation passed.
The 84-test selected unittest command began and printed progress, but its final
result was not retrieved. Re-run it and the two pipeline/source script checks.
Do not mark manifest validations or a tranche report complete prematurely.

Expected post-acceptance metrics, to independently verify: 150 repaired / 29 awaiting,
60 original-89 completed, 623 sources, 796 clauses/episodes, 1315 external rows,
899 cumulative positional external reconciliations. Coverage remains 129 complete /
50 partial unless fresh validation establishes otherwise.

## Remaining queue

After accepting these three, continue 109, 111, 113, 135 in small published batches;
then 100, 144, 147, 148, 149, 154, 156, 158, 160, 163;
then 43, 72, 102, 103, 104, 105, 166, 167;
then the seven documented holds 53, 64, 120, 139, 164, 171, 174.
Keep the original planning baseline frozen and append execution progress.
Update PR118 after each accepted batch and inspect all three remote checks.
The user has authorised the campaign and requested regular commits.
No schema, validator, builder, permanent test or CI semantic changes are authorised.
