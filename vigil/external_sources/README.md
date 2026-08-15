# External Governance Source Ledger

This directory contains VIGIL maintenance machinery for detecting changes in external AI-governance sources. It is Layer 0: source identity, version, lifecycle and coarse review workflow. It is not a VIGIL record class and it does not create CAM/Caelestis authority.

Layer 1 under `vigil/external_requirements/` classifies source scope and preserves requirement-level analytical reference data. It is deliberately separate from this ledger: a registered source is not itself a requirement, and requirement extraction state is not an external-source lifecycle or internal-alignment state.

## Boundary

The pipeline is deliberately one-way:

`external source -> VIGIL change ledger -> human alignment review -> Caelestis repair (if required) -> VIGIL verification`

An upstream change may create or update maintenance state in this directory. It MUST NOT directly edit Caelestis, create a VIGIL PATCH, or determine substantive alignment automatically.

## Source authority

The canonical source for legal or standards status is the official publisher or regulator. Third-party trackers may be used only for discovery. Vorp Labs is intentionally excluded from this source matrix and ingestion design.

Primary source families currently registered:

- Australia: Federal Register of Legislation API.
- European Union: EUR-Lex / CELLAR and official OJEU material.
- United Kingdom: legislation.gov.uk API and Atom publication feeds.
- United States federal legislation: Congress.gov API and GovInfo.
- United States federal regulation: Regulations.gov API and GovInfo/Federal Register.
- ISO/IEC metadata: ISO Open Data.
- NIST: NIST/CSRC publication feeds and datasets.
- IEEE: official IEEE Standards metadata, currently manual/low-frequency pending a supported bulk metadata feed.
- CEN/CENELEC harmonised AI standards: development metadata plus OJEU citation as the legal harmonisation trigger.
- Regulations.ai and OECD.AI: optional discovery-only inputs; neither is authoritative for lifecycle state.

## State separation

External lifecycle and CAM review state are independent.

`source_lifecycle_state` describes the external instrument, for example `draft`, `consultation`, `adopted`, `published`, `effective`, `superseded`, or `withdrawn`.

`alignment_state` describes CAM/VIGIL disposition: `unassigned`, `review-required`, `mapped`, `patch-required`, `patched`, `verified`, `no-change-required`, `not-applicable`, or `superseded-before-review`.

Only configured final/adopted lifecycle states are alignment-eligible. Draft and consultation material may be observed but does not automatically enter the alignment queue.

## Stable identity

Each row has an internal `vigil_source_id` plus a publisher-native `canonical_identifier`. The durable review key is:

`external_source_id + source_version`

Upstream-provider identity is provenance only. Changing discovery providers must not change the VIGIL source identity.

## Files

- `source-matrix.json` — source families, authority posture, lifecycle mappings, and automation readiness.
- `ledger.schema.json` — maintenance-ledger contract.
- `ledger.json` — accepted external-source observations.
- `alignment-queue.json` — generated review queue; no substantive alignment judgement.
- `../scripts/manage-external-governance-ledger.py` — deterministic canonicalise/hash/diff/filter/queue engine.
- `../tests/test_external_governance_ledger.py` — unit tests for lifecycle and state transitions.

## Commands

Validate current files:

```bash
python vigil/scripts/manage-external-governance-ledger.py validate
```

Ingest a normalised JSON array exported by a source adapter or prepared from an official feed:

```bash
python vigil/scripts/manage-external-governance-ledger.py ingest \
  --source australia-frl \
  --input /path/to/items.json
```

Regenerate the review queue:

```bash
python vigil/scripts/manage-external-governance-ledger.py queue
```

Run tests:

```bash
python vigil/tests/test_external_governance_ledger.py
```

The normal ingestion path is intentionally model-free: fetch -> validate -> canonicalise -> hash -> diff -> lifecycle filter -> queue. Semantic assessment begins only after an item reaches `review-required`.
