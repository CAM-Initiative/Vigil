# Security Policy

VIGIL may document public platform failures, governance failures, account-access issues, and AI ecosystem security-adjacent incidents. It should not publish secrets, private user data, or sensitive reproduction details that enable abuse.

## Reporting sensitive issues

Do not open public issues or public pull requests containing:

* secrets, tokens, API keys, private keys, credentials, or session cookies;
* private user data, private chat exports, private account identifiers, or doxxing material;
* exploit details, bypass steps, or operational platform-security details that would materially increase abuse risk;
* confidential internal evidence that has not been cleared for public release.

If a private reporting channel is not available, maintainers should create one before accepting sensitive vulnerability reports. Do not invent or use an unofficial email address for sensitive submissions.

## Public documentation boundary

VIGIL can document public, already-disclosed, or safely summarised platform failures where the governance relevance is clear. Security-relevant records should minimise operational exploitability while preserving enough context for governance analysis.

Where public disclosure would create risk, submissions may be:

* redacted;
* represented with an internal locator rather than a public URL;
* summarised at a higher level;
* deferred for maintainer review;
* excluded from public records until safe to publish.

## Private/internal evidence

Private evidence, internal notes, ChatGPT conversations, repository-local files, field observations, CAM/Caelestis internal review material, and other non-public material must be clearly marked as internal. Do not represent private/internal evidence as external public evidence.

If internal evidence is necessary to preserve record integrity, use the best available internal locator and avoid exposing private content, credentials, personal data, or sensitive operational details.

## Maintainer review

Flag suspected vulnerability, private-evidence, or sensitive-disclosure concerns for maintainer review before publishing. When in doubt, preserve the evidence privately and ask for review rather than committing sensitive details.
