# EXTREQ-13 — IEEE 7009-2024 identity retirement

**Source:** IEEE Std 7009-2024
**VIGIL source:** EXT-564A4CAA4F00
**Decision date:** 2026-09-04
**Decision basis:** explicit maintainer approval following licensed-primary semantic-fidelity review

## Decision

Four legacy aggregate analytical identities were retired from the live IEEE 7009 corpus because each compressed multiple independently assessable source-native propositions already represented by linked atomic records.

The retired immutable IDs are preserved in retirements/IEEE-7009-2024.json together with clause locators, reasons and successor IDs. Git history remains the authoritative record of their prior full canonical content.

No atomic successor was created by this retirement pass: all successors were already canonical and source-reviewed.

## Result

The live IEEE 7009 shard now contains 63 records. The four source-specific re-extraction backlog entries are resolved. IEEE 7009 is promoted from requires-reextraction / partial to assured / complete only because the aggregate identities are no longer live alongside their atomic successors.

No IEEE source text is stored in VIGIL and no human verification of the standard text is claimed beyond the maintainer's explicit architectural approval of the retirement action.
