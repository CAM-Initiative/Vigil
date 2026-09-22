#!/usr/bin/env python3
"""Final one-shot public-narrative cleanup for the 002-020 evidence rebuild."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1] / "records" / "incidents"

def load(n):
    p=ROOT/f"VIGIL-INC-{n:06d}.json"; return p,json.loads(p.read_text(encoding="utf-8"))
def save(p,d): p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

p,d=load(5)
d["summary"]="Associated Press reports that Randall Reid was arrested in Georgia on a Louisiana warrant after facial-recognition technology linked him to a theft, despite Reid saying he had never been to Louisiana. He spent six days in jail before the warrant was withdrawn. VIGIL records the occurrence as a consequential promotion of uncertain biometric identity evidence into an arrest pathway, without treating the match as the sole cause of every downstream decision."
save(p,d)

p,d=load(6)
d["summary"]="A federal court record shows that a Detroit facial-recognition search produced 73 candidates and that an investigator narrowed them to Porcha Woodruff as an investigative lead, followed by internal review, a victim photo-lineup identification and an arrest warrant. Woodruff was later detained while pregnant and charges were dropped. VIGIL analyses whether the downstream human steps supplied genuinely independent identity assurance; it does not represent the later summary-judgment ruling as a judicial finding that facial recognition made the arrest unlawful."
save(p,d)

p,d=load(7)
d["summary"]="The Legal Aid Society reports from NYPD records that the Facial Identification Section first returned no match in an investigation, after which the Special Activities Unit produced a possible facial-recognition match to Trevis Williams. Legal Aid states that Williams did not match the victim's physical description and was nevertheless arrested following the match and a disputed identification procedure. VIGIL preserves those conclusions as attributable claims and focuses on the no-match-to-possible-match provenance gap and the authority afforded to the later identity inference."
save(p,d)

p,d=load(9)
tc=d["taxonomy_classification"]
tc["classification_review_provenance"]["review_status"]="reviewed unclassified under taxonomy 0.6.6"
for dim in d.get("harm_impact_assessment",{}).get("dimensions",[]):
    if dim.get("dimension_id")=="service-operational-infrastructure" and dim.get("assessment_status")=="assessed":
        dim["assessment_basis"]="The preserved user report describes a bounded interaction failure in which image-generation behaviour reportedly armed or activated around image-related language or an uploaded image before a final explicit generation instruction, with app reload or crash behaviour also reported. The occurrence is single-user testimony; no broader prevalence, internal cause or additional downstream consequence is inferred. Threshold applied: Limited non-critical degradation below two hours, a critical-service interruption below 30 minutes, or a localised workflow failure resolved through routine recovery."
save(p,d)
