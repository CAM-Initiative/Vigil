# INC-000065 provenance re-adjudication

Date: 2026-09-22
Branch: `fix/source-clause-taxonomy-assessments`

## Decision

Withdraw `VIGIL-FC-000053 — Identity-Representation Authority Conflation` as the primary diagnosis for INC-000065.

The materialised harm remains non-consensual synthetic sexual representation using a real person's likeness. That harm is important to the Incident and Harm Impact assessment, but it is not the clearest recurring structural mechanism exposed by the occurrence.

The stronger governance mechanism is **loss or absence of legally useful creator / transformation provenance**. The public record preserves the harmful synthetic artefacts and their consequences while creator attribution remains disputed. For legal accountability, the material provenance question is not merely whether the content is AI-generated; it is whether the chain can establish who initiated creation, under which account/session or service identity, from which source assets, using which system/model, through which transformations, and how the resulting artefact entered distribution.

## Taxonomy boundary

The current taxonomy family `VIGIL-FF-0002 — Provenance & Lineage Integrity Failures` is the correct family.

### Best current class candidate: VIGIL-FC-000011 — Untraceable Synthesis

FC-000011 currently requires:

- a materially synthesized, derived, merged, transformed or recomposed output;
- one or more material antecedents or transformations that cannot be reconstructed with sufficient reliability; and
- missing lineage that affects attribution, auditability, authority, validation, rights, identity or downstream reliance.

INC-000065 materially engages that boundary because the available public evidence concerns a synthesized sexual representation, while the creator, toolchain, source/transform history and distribution chain are not sufficiently established to resolve responsibility.

However, the occurrence evidence available to VIGIL does **not** prove that the underlying platform or tool technically failed to preserve all such data. It proves that creator attribution remains unresolved in the public/legal account available to VIGIL. Platform, account, forensic or law-enforcement records may exist outside the public record.

Therefore the class should not be represented as conclusively established without stronger forensic or provider evidence.

### VIGIL-FC-000013 — Transformation Lineage Collapse

FC-000013 is adjacent because it concerns preservation of the final artefact while material intermediate transformation history is lost or collapsed. It is not preferred at present because the public record does not establish which intermediate states once existed and were subsequently lost. The stronger evidenced problem is inability to reconstruct the synthesis provenance required for attribution.

### VIGIL-FC-000010 — Authorship or Source Misattribution

Do not use FC-000010 merely because the complainant attributed creation/distribution to a named person and that person denied it. FC-000010 requires an attribution that provenance shows to be wrong or materially unsupported as a represented system/source attribution. The legal allegation and denial should instead remain expressly disputed.

## Recommended Incident classification

- Remove FC-000053.
- Set `classification_status` to `classification-disputed`.
- Use `VIGIL-FC-000011 — Untraceable Synthesis` as the primary candidate at medium confidence, with the classification basis expressly limited to the provenance gap visible in the available occurrence evidence.
- State that this does not establish that no provider-side, account-level or law-enforcement provenance exists.
- Do not add FC-000013 unless evidence establishes that a previously available transformation chain was actually collapsed, removed or lost.

## Governance interpretation

The governance failure is not simply that a sexual deepfake exists. It is that a legally consequential synthetic artefact can become detached from the provenance needed to attribute creation and transformation reliably. A synthetic-content label can establish that content was generated or manipulated by AI without establishing the identity of the human actor responsible for initiating or directing the generation. Where consent, identity misuse, sexual representation, civil liability or criminal responsibility are material, provenance should support reconstruction of the creator/operator, account or service identity, source assets, generation event, transformation history and relevant distribution chain, subject to lawful privacy and access controls.

## Comparative legal context

### Germany

Germany's Kunsturhebergesetz §22 generally requires consent for dissemination or public display of a person's image, subject to statutory exceptions. In March 2026 the German government publicly stated that producing pornographic deepfakes was not necessarily criminal under existing law and announced work to close that gap. Reuters' reporting on the Collien Fernandes controversy records both the allegation and the accused party's denial and reports that the case contributed to pressure for legal reform.

Sources:
- https://www.gesetze-im-internet.de/kunsturhg/__22.html
- https://www.bundesregierung.de/breg-de/aktuelles/regierungspressekonferenz-vom-20-maerz-2026-2414604
- https://www.reuters.com/business/media-telecom/german-deepfake-porn-case-sparks-protests-pressure-change-law-2026-03-26/

### Australia

Australian law and eSafety treatment expressly encompass intimate images that are digitally altered or faked to look like a person. The Commonwealth Criminal Code also expressly includes images, video or audio edited or wholly created using digital technology, including AI, where they create a realistic but false depiction in the relevant sexual-material provisions.

Sources:
- https://www.esafety.gov.au/key-topics/image-based-abuse
- https://www.esafety.gov.au/industry/tech-trends-and-challenges/deepfakes
- https://www.legislation.gov.au/C2004A04868/2026-06-30/2026-06-30/text/original/epub/OEBPS/document_3/document_3.html

### United Kingdom

The Data (Use and Access) Act 2025 created offences relating to creating or requesting the creation of purported intimate images of an adult without consent or reasonable belief in consent. The Crime and Policing Act 2026 expanded the regime further, including offences concerning purported intimate-image generators / nudification tools and additional platform duties.

Sources:
- https://www.legislation.gov.uk/ukpga/2025/18/notes/division/3/index.htm
- https://www.legislation.gov.uk/ukpga/2026/20/notes/division/11/index.htm

### European Union

The GDPR defines biometric data as personal data resulting from specific technical processing of physical, physiological or behavioural characteristics that allow or confirm unique identification, including facial images, and treats biometric data used for unique identification as a special category. The EU AI Act separately requires disclosure where AI generates or manipulates image, audio or video constituting a deepfake.

Sources:
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679
- https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng

### China

China's Deep Synthesis Provisions require real-identity authentication for users of publication services, separate consent when editing facial or voice biometric information, technical labels for generated/edited content, preservation of relevant logs, and visible labelling for specified deep-synthesis services. This is a comparatively direct example of regulation linking deep-synthesis capability to identity, consent, labelling and traceability controls.

Source:
- https://www.cac.gov.cn/2022-12/11/c_1672221949354811.htm

### United States / California

The federal TAKE IT DOWN Act creates a removal/enforcement regime for non-consensual intimate imagery, including AI-era abuse. California's AI Transparency Act is especially relevant to the provenance distinction: it requires latent disclosures to convey provider, model/version, creation/alteration time and date, and a unique identifier where technically feasible. However, its public detection tool is expressly required not to output personal provenance data. This demonstrates that even relatively advanced statutory content provenance can identify the generating system and event without publicly identifying the human creator.

Sources:
- https://www.ftc.gov/news-events/news/press-releases/2026/05/ftc-begins-enforcing-take-it-down-act
- https://leginfo.legislature.ca.gov/faces/billVersionsCompareClient.xhtml?bill_id=202320240SB942

## Current provenance technology

### SynthID

Google DeepMind's SynthID embeds an imperceptible watermark into supported AI-generated or altered content and supports detection that content originated from, or was edited by, supported Google AI systems. The signal is designed to survive common transformations better than ordinary metadata. It answers a system-origin question; it does not inherently identify the human user who initiated generation.

Source:
- https://deepmind.google/models/synthid/

### OpenAI provenance

OpenAI currently combines C2PA metadata, SynthID watermarking and public verification tooling for supported generated content. The public verifier reports whether supported OpenAI provenance signals are detected. OpenAI's published provenance material describes the verification question as whether media was generated with OpenAI tools; it does not state that the public watermark or verifier exposes the generating account-holder's identity.

Sources:
- https://openai.com/index/advancing-content-provenance/
- https://openai.com/research/verify/
- https://deploymentsafety.openai.com/chatgpt-images-2-0/image-provenance

### C2PA / Content Credentials

C2PA provides tamper-evident provenance describing origin, creation and editing actions. Its core model can preserve software/service signer identity, transformations and ingredients. Human or organisational identity can be added through identity assertions, but C2PA expressly does not require creator identity in the core specification. Current C2PA guidance recommends separate identity mechanisms, such as CAWG identity assertions, when human or organisational attribution is desired.

Sources:
- https://c2pa.org/specifications/specifications/2.2/explainer/Explainer.html
- https://spec.c2pa.org/specifications/specifications/2.2/guidance/Guidance.html
- https://spec.c2pa.org/specifications/specifications/2.4/identity/identity.html

Adobe's Content Credentials implementation demonstrates the optional identity model: credentials may include a verified creator name and linked accounts, but identity is an add-on rather than an unavoidable property of every generated asset.

Sources:
- https://helpx.adobe.com/creative-cloud/apps/adobe-content-authenticity/content-credentials/types-of-information.html
- https://helpx.adobe.com/creative-cloud/apps/adobe-content-authenticity/customization.html

## Conclusion for INC-000065

The legal and technical evidence supports a distinction between **synthetic-content provenance** and **actor attribution provenance**.

A watermark or Content Credential may reliably establish that an artefact was AI-generated, identify the provider or model, record when it was created, or preserve parts of its transformation history. Those controls are valuable, but they do not necessarily establish the identity of the human creator or operator. Human identity is optional in C2PA-based ecosystems, and some regulatory designs intentionally prevent public disclosure of personal provenance.

For high-harm synthetic sexual media, VIGIL should therefore treat legally useful provenance as a stronger control objective than simple AI labelling. Subject to lawful privacy and access safeguards, the accountable provenance chain should be capable of supporting authorised investigation of:

`depicted person / source asset -> generation request -> authenticated account or service identity -> model/tool -> generation event -> transformations -> resulting artefact -> distribution pathway`

The public Fernandes occurrence does not establish that every element of that chain was technically unavailable; it establishes that creator responsibility remains unresolved in the evidence available to VIGIL. The Case File should preserve that uncertainty while identifying `VIGIL-FC-000011 — Untraceable Synthesis` as the best current disputed taxonomy fit and removing FC-000053.