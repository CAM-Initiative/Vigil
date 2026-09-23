# VIGIL Incident Adjudication Workflow

Status: maintainer contract

Applies to: substantive Incident rebuilds, refactors, re-adjudications and taxonomy migrations.

This workflow exists because an Incident is not a summarisation object. It is a bounded evidence record plus separate factual, taxonomy, harm and governance adjudications. A capable model may assist with the work, but free-form model judgement is not a substitute for the control sequence below.

## Core invariant

A rebuild MUST be non-destructive by default.

Existing source evidence, supported factual detail, taxonomy relationships, mapping roles, confidence, harm findings and interpretive provenance are the starting state. They may change only through explicit re-adjudication. No prior taxonomy mapping or source record may disappear silently.

The required control sequence is:

```text
BASELINE → EVIDENCE → FACTUAL RECORD → TAXONOMY → HARM → INTERPRETATION → VALIDATION
```

The sequence is deliberately short. Each gate has a distinct authority boundary and must be completed before the next gate is treated as final.

## 1. BASELINE — establish the record being rebuilt

Before editing:

- read the complete canonical Incident;
- record the baseline Git ref or commit;
- inventory all existing `source_records`;
- inventory the primary and every secondary taxonomy mapping, including mapping-local role, basis and confidence;
- note the current taxonomy version, Harm Impact assessment and current interpretive provenance;
- read `vigil/VIGIL.Schema.json`, `vigil/templates/incident-record-template.json`, the current taxonomy families/classes and comparable Incidents.

Do not begin from a generated index, website projection, handoff summary or an older working branch when a newer canonical record exists.

## 2. EVIDENCE — reconstruct before rewriting

For a full rebuild, existing sources are the floor, not the ceiling.

Search for additional occurrence evidence before rewriting the record. Prefer, in order:

1. originating first-party or primary artefacts;
2. regulator, court, standards-body, research-lab or other authoritative records;
3. independent technical or investigative corroboration;
4. later corrections, updates or consequence reporting;
5. reputable secondary reporting where it contributes material occurrence or harm evidence.

The maintainer must record the search in the adjudication manifest. A full rebuild may not use `new_external_source_research: false` merely because the current record already contains sources.

Evidence search is not permission to inflate the record. Add a source only when it materially supports occurrence facts, evidentiary limits, external assessment, harm or another canonical field. Preserve claim-relative evidence status.

A source may be removed only when the manifest records the source and an explicit reason such as duplication, wrong occurrence, inaccessible/non-verifiable replacement, or demonstrated unreliability.

## 3. FACTUAL RECORD — write facts before diagnosis

Rebuild `summary` and `vigil_assessment.factual_basis` from the evidence before performing taxonomy adjudication.

- `summary` is the rich lay occurrence narrative.
- `factual_basis` states what the preserved evidence establishes, corroborates, disputes and leaves unresolved.
- Neither field should be compressed merely to make the record shorter.
- Material chronology, actors, systems, actions, outcomes, quantities and uncertainty must survive the rebuild when supported.
- Governance diagnosis, taxonomy labels and severity reasoning belong in their governed fields.

If a rebuild materially shortens the baseline `summary` or `factual_basis`, the adjudication manifest must explain why the reduction is a fidelity improvement rather than information loss.

## 4. TAXONOMY — retrieve, test and adjudicate

Taxonomy classification is a separate analytical pass.

For a full rebuild the maintainer must:

- load the current canonical VIGIL Failure Taxonomy, not remembered labels or an older branch copy;
- inspect the complete current class set at least once before selecting candidate classes;
- recover every baseline mapping before considering deletion;
- test candidate classes against their technical definition, recognition criteria and exclusions;
- test nearby/distinguishing classes where the taxonomy itself identifies a boundary;
- adjudicate each mapping independently as `failure-occurrence`, `successful-invariant` or `ambiguous-boundary`;
- keep consequence/severity reasoning out of taxonomy membership;
- allow the Incident to remain unclassified when the mechanism is not evidenced.

### Prior-mapping disposition rule

Every taxonomy mapping present in the baseline must appear in the adjudication manifest with exactly one disposition:

- `retained`;
- `role-changed`;
- `confidence-changed`;
- `role-confidence-changed`;
- `superseded`; or
- `removed-unsupported`.

`superseded` and `removed-unsupported` require a substantive reason. `superseded` must identify the replacement class or classes.

Any class newly added to the candidate record must appear in `new_taxonomy_mappings` with its evidence-bounded rationale.

A missing baseline mapping with no disposition is a rebuild failure.

### Mixed relationships are valid

An Incident may simultaneously contain failure occurrences, successful invariants and ambiguous boundaries. Do not collapse a mixed Incident into a single “good” or “bad” label.

`VIGIL-INC-000129` is the design exemplar for this property: its value is that different taxonomy boundaries can have different roles in the same bounded occurrence. It is not a permanent answer key, and its current class set may itself be re-adjudicated through this workflow.

## 5. HARM — review materialised consequence separately

Re-open VIGIL-HIM only after the factual record is stable.

Review all eleven dimensions against current VIGIL-HIM. Search for later consequence evidence where a full rebuild is being performed. Do not derive severity from taxonomy, notoriety, capability, source prestige or hypothetical worst-case outcomes.

If the rebuild is taxonomy-only, record that Harm Impact was deliberately not reopened and preserve the prior assessment unchanged.

## 6. INTERPRETATION + VALIDATION — integrate only after the governed passes

Write `vigil_assessment.significance_to_cam` and `vigil_assessment.governance_interpretation` after evidence, taxonomy and harm adjudication are stable.

The conclusion should integrate the bounded occurrence, evidentiary limits, taxonomy relationships and materialised consequences without turning uncertainty into fact.

Before accepting a rebuilt Incident:

1. complete an adjudication manifest based on `vigil/templates/incident-rebuild-adjudication-template.json`;
2. run the rebuild guard against the baseline and candidate;
3. run the ordinary VIGIL builders and validators;
4. inspect the generated/public projection for information loss or role collapse.

Example:

```bash
python vigil/scripts/validate-vigil-incident-rebuild.py \
  --baseline-ref main \
  --candidate-file vigil/records/incidents/VIGIL-INC-000129.json \
  --manifest /tmp/VIGIL-INC-000129-adjudication.json

python vigil/scripts/build-vigil-public-records.py
python vigil/scripts/validate-vigil-records.py
python vigil/scripts/validate-vigil-public-records.py
python vigil/scripts/validate-vigil-source-provenance.py
python vigil/scripts/validate-vigil-interpretive-provenance.py
python vigil/scripts/validate-vigil-system-components.py
python vigil/scripts/validate-authorship-provenance.py
```


## Gmail staging for unresolved action

The adjudication workflow has an explicit maintainer-output channel. When a rebuild establishes that work must occur outside the current Incident edit, the reviewing agent must stage that next action in Gmail rather than leaving it only in chat, a branch note or an ephemeral handoff.

Two escalation classes use this channel:

### Taxonomy action required

Stage a taxonomy action when the occurrence contains a materially evidenced governance mechanism or invariant that cannot be represented faithfully by the current taxonomy without stretching an existing class beyond its definition, recognition criteria or exclusions.

Typical triggers include:

- no current class fits despite a well-evidenced mechanism;
- the same uncaptured mechanism recurs across more than one Incident;
- an existing class boundary is demonstrably too broad, too narrow or internally conflates distinct mechanisms;
- a recovered invariant has no corresponding current taxonomy boundary; or
- correct classification would require redefining an existing class rather than merely applying it.

Do **not** create or amend the taxonomy opportunistically inside the Incident rebuild. Finish the Incident as far as the current taxonomy permits, preserve the gap explicitly, and stage a taxonomy instruction containing:

- affected Incident ID(s);
- concise mechanism/invariant description;
- evidence supporting the gap;
- nearest current classes tested;
- why each current class is insufficient;
- whether the likely action is a new class, class-boundary amendment, family review or terminology repair;
- any cross-Incident comparators; and
- the exact branch/ref from which the instruction was generated.

### Maintainer action required

Stage a maintainer action when the rebuild cannot be completed safely without another task, including:

- manual recovery of a source or artefact;
- occurrence re-bounding or possible retirement;
- unresolved branch-state conflict;
- inaccessible primary evidence that materially affects adjudication;
- a material cross-record consistency issue;
- a taxonomy ambiguity requiring separate taxonomy work;
- a source-provenance repair outside the current record; or
- another stop condition that should survive beyond the current chat.

### Gmail queue protocol

The Gmail staging queue is the authenticated maintainer Gmail account emailing itself.

The authoritative action queue uses:

- subject prefix: `[CURRENT VIGIL QA ACTION]`;
- Gmail label: `VIGIL/CURRENT QA ACTION`.

When Gmail access is available, the reviewing agent must:

1. search Gmail for the latest message with the exact subject prefix and label;
2. read that current authoritative queue before writing a replacement;
3. merge the new action into the existing unresolved queue, removing an older item only when the record/branch state shows it has already been resolved;
4. send a new self-email with the same exact subject prefix and a current date;
5. apply the `VIGIL/CURRENT QA ACTION` label to the new message; and
6. state in the body that the new note supersedes earlier queue notes.

Do not send a one-item replacement that accidentally erases unresolved staged work. The newest labelled message is a complete queue snapshot, not an append-only fragment.

Use explicit headings such as `TAXONOMY ACTION REQUIRED`, `MANUAL ACTION REQUIRED`, and `NO LONGER ACTIONABLE / RESOLVED` where useful. Each item must contain enough repository and evidence context for a later agent to act without reconstructing the originating conversation.

Do not put personal email addresses, credentials, secrets or connector identifiers into this public repository. The connector resolves the authenticated mailbox at execution time.

If Gmail access is unavailable, do not claim that staging occurred. Surface `GMAIL STAGING NOT COMPLETED` with the complete ready-to-stage instruction payload so a later connected session can send it.

## Review modes

Use `full-rebuild` for the current corpus refactor/rebuild and for any work that reopens factual evidence, taxonomy or harm.

Use `bounded-edit` only where the work scope is explicitly narrow, such as prose separation, metadata normalisation or a single-source correction. A bounded edit must preserve governed fields outside scope and still account for any taxonomy or source change it makes.

A maintainer must not describe a full re-adjudication as a bounded edit merely to avoid evidence or taxonomy review.

## Stop conditions

Stop the rebuild and escalate rather than guessing when:

- the current taxonomy cannot be loaded;
- primary evidence is inaccessible and the classification depends on it;
- two candidate classes remain materially indistinguishable after recognition/exclusion review;
- the record appears to combine multiple distinct occurrences that require re-bounding;
- a source or mapping would need to be removed without a defensible reason;
- the candidate record becomes materially less informative than the baseline without a fidelity justification; or
- the evidence supports harm but not the mechanism needed for taxonomy classification.

The correct result may be a richer unclassified Incident. Classification is not a completeness metric.
