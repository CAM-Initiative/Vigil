# Incident media validation — Gate 1 proposal

Status: approved by the human maintainer on 2026-10-18 and implemented. Approval: “This is APPROVED. thank you!” The proposal below is retained as the approved scope.

## Current behaviour and measured coverage

The schema authoring contract and `vigil/MAINTAINERS.md` require selected authentic media, immutable Registry references and accurate captions. The canonical Incident validator does not inspect `incident_artefacts` for media compatibility. It would accept the former INC-000043 Markdown reference even though a Markdown document is not an image.

Website PR 158 already includes a shared media selector for Case File, print and static publication. It rejects Markdown/text paths even when given an image MIME declaration, permits supported images and videos, and presents PDFs as document links. Two regression tests cover unsupported media and use of the shared selector. These safeguards prevent unsupported references becoming image slots, but do not reject the canonical record itself.

Read-only inventory at the repair baseline plus the approved prose repairs: 23 artefacts across 16 Incidents — 22 PNGs declared image/png and one MP4 declared video/mp4. All 23 have commit-pinned Registry permalink/render references. No incompatibility was found in those metadata. This is not an independent authentication or byte-level availability check.

## Proposed behaviour

Add an offline canonical-validation check for optional `incident_artefacts` entries:

- Require a supported HTTP(S) render URL and a nonempty compatible MIME declaration. Supported pathname extensions: png, jpg/jpeg, gif, webp, avif, svg for images; mp4, webm, ogg/ogv, m4v, mov for video; pdf for linked documents. Use the same media families as the website selector. Do not infer image status from a title, caption or MIME alone.
- Reject Markdown, JSON, HTML and other text/data references as renderable Incident media, including `.md` declared `image/png`.
- Require `source-screenshot` entries to resolve to image metadata and carry meaningful nonempty alt text. PDFs remain documents; they cannot satisfy a screenshot-image declaration.
- Require immutable Registry URLs for both permalink and render URL, identifying the same Registry file and 40-character commit SHA. Keep the original external source in its existing source-evidence role; this rule does not replace or rewrite source records.
- Report the Incident, artefact index and offending property. Do not silently delete entries or rewrite evidence.

## Pass/fail delta and affected surfaces

The former INC-000043 `.md` entry, a PNG declared `text/markdown`, a PDF labelled `source-screenshot`, or a moving-branch Registry image would pass today's canonical media checks and fail the proposed checks. Existing compatible, pinned images/video continue to pass. No currently rejected record becomes accepted. Incidents without optional artefacts remain valid.

The exact canonical scope is `incident_artefacts[].artefact_type`, `media_type`, `render_url`, `permalink` and image `alt_text`. The affected public surface is Stage 01 Incident media, with corresponding print/static copies. Taxonomy, sources, source-clause adjudication, Harm Impact and source archive links are outside this rule.

## Expected corpus impact and repair implications

All 23 current entries are expected to pass. Fixtures would demonstrate rejection of the historical bad Markdown pattern, MIME-family mismatch, PDF-as-screenshot and moving-branch references, alongside valid image/video/document and absent-artefact cases. A full read-only corpus run follows implementation.

Any unexpected failures must be reported with exact fields before multi-record repairs. Fixes could require correcting media metadata, committing a genuine capture in Registry, or removing an invalid active media reference while preserving the original source. None is to be done mechanically. This proposal authorises no deletion, source substitution, media reconstruction or fresh classification.

## Why validation and its limits

A rendering filter protects the page but allows the invalid evidence-media record to persist and fail again elsewhere. Canonical validation makes the defect a blocking authoring error before projection/publication. This check is deterministic and offline; it does not fetch every media asset, authenticate screenshots, establish redistribution rights, or prove a `.png` contains genuine PNG bytes. Committing and inspecting the actual Registry asset remains mandatory under the existing capture contract. A future remote content/decoder check would need a separate proposal covering network reliability and supported formats.

The main semantic risk is mistaking a rejected display reference for invalid underlying source evidence. Preserve sources, quotations, archive links and limitations. Do not replace a document with a fabricated image, or discard evidence to obtain a pass.

## Approval and stop condition

`vigil/MAINTAINERS.md`, Gate 1: “No semantic validator/schema/test change may be implemented until the human maintainer explicitly approves that described behaviour.”

Request approval of the above blocking metadata checks and fixture scope. After implementation, run the corpus read-only and stop before any broad repair if new failures occur. The separately approved 73 public-prose repairs do not change or implement this media-validation proposal.

## Implementation

Implemented in `vigil/scripts/validate-vigil-records.py` through `validate_incident_artefacts`, called by canonical `validate_record`. The check is offline and non-mutating. It enforces supported media families and nonempty MIME declarations, nonempty image alt text, screenshot/image compatibility and matching commit-pinned Registry permalink/raw file identities. Its errors identify the Incident path, artefact index and affected property. Original source URLs and archive links are outside this check.

Twelve regression tests in `vigil/tests/test_incident_artefact_media.py` include the former Markdown-reference failure pattern, spoofed image declarations, MIME mismatch, PDF/video as screenshot, empty image descriptions, moving/short refs, mismatched file/commit, non-Registry/non-HTTP URLs and malformed entry structures. Positive cases cover every supported extension, optional absent/empty artefacts, videos without image alt text, linked PDFs and ordinary source documents. A full-validator integration test prevents accidentally leaving the helper disconnected. No canonical Incident repair is required or performed.

The check establishes metadata compatibility and immutability only. It does not authenticate media, inspect remote bytes or certify that alt text adequately explains the visual evidence. The existing human/source-native capture and inspection duties remain in force.

## Verification result

All 194 canonical Incidents pass with the control enabled. The 23 current artefacts across 16 Incidents pass; no canonical records, sources, taxonomy mappings, Harm Impact fields or generated projections changed. All 12 new fixtures pass and full discovery passes 276 tests. Public-index, source (703 records), interpretive, component-role and authorship validators pass; `git diff --check` passes. Test-only jsonschema 4.26.0 was supplied through the environment. No remote media fetch or authenticity certification is claimed.
