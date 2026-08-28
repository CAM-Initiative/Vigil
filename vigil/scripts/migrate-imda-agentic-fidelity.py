#!/usr/bin/env python3
"""Repair IMDA Agentic AI MGF 1.5 constituent fidelity and split compound records."""
from __future__ import annotations

import argparse
import copy
import hashlib

from external_requirements_io import load_requirements_document, write_requirements_document


SOURCE_ID = "EXT-3CCBC407EAC8"
SOURCE_VERSION = "2026-05"
DIGEST = "2636e19ff1c86e862394d2fc900592e97b83c04cc35e3c8443108114b7f1dfba"
PDF = "https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf"
SCOPE = (
    "The framework applies to organizations looking to deploy agentic AI, whether "
    "they develop agents in-house or use third-party agentic solutions."
)


def requirement_id(clause: str, identity: str) -> str:
    seed = "|".join((SOURCE_ID, SOURCE_VERSION, clause, identity))
    return "EXTREQ-" + hashlib.sha256(seed.encode()).hexdigest()[:16].upper()


def provenance(record: dict, clause: str) -> dict:
    value = copy.deepcopy(record["interpretation_provenance"])
    value.update({
        "source_analysis_method": (
            "Direct primary-text constituent-fidelity review of IMDA Model AI Governance "
            "Framework for Agentic AI version 1.5; source-defined subsection propositions, "
            "conditions, outputs, and illustrative qualifications were represented separately."
        ),
        "source_locator": f"{PDF} (section {clause})",
        "reviewed_source_digest": DIGEST,
        "reviewed_source_digest_algorithm": "sha256",
        "reviewed_source_digest_status": "recorded",
    })
    return value


def update(record: dict, *, clause: str, summary: str, objects: list[str],
           stages: list[str] | None = None, artefacts: list[str] | None = None,
           evidence: list[str] | None = None, methods: list[str] | None = None,
           timing: list[str] | None = None, conditions: list[str] | None = None,
           qualifications: list[str] | None = None,
           concepts: list[str] | None = None) -> None:
    record.update({
        "clause_or_control": clause,
        "parent_section_or_group": clause.rsplit(".", 1)[0],
        "requirement_summary": summary,
        "governance_expectation": summary,
        "governed_object": objects,
        "required_artefacts": artefacts or [],
        "evidence_expectation": evidence or [],
        "verification_method": methods or [],
        "timing_or_frequency": timing or [],
        "applicability_conditions": [SCOPE] + (conditions or []),
        "exceptions_or_qualifications": qualifications or [],
        "source_review_date": "2026-08-28",
        "interpretation_provenance": provenance(record, clause),
    })
    if stages is not None:
        record["lifecycle_stage"] = stages
    if concepts is not None:
        record["governance_concepts"] = concepts


PRESERVED = {
    "EXTREQ-3B91F9DF01838676": dict(
        clause="2.1.1",
        summary="Evaluate whether residual agentic-AI risk is tolerable and can be accepted after controls are considered.",
        objects=["Residual risk of the proposed agentic AI use case"],
        timing=["After assessing risks, benefits and applicable controls for the proposed use case."],
        conditions=["Applies when residual risk remains after applicable controls are considered."],
    ),
    "EXTREQ-3E386D665B98BDEA": dict(
        clause="2.1.1",
        summary="Assess impact based on the sensitivity of data available to the agent, its persistent memory, and the external systems it can access.",
        objects=["Data available to the agent", "Persistent agent memory", "External systems accessible to the agent"],
        qualifications=["The listed impact factors are non-exhaustive considerations."],
    ),
    "EXTREQ-7B1019B56EF6F868": dict(
        clause="2.1.1",
        summary="Assess impact using the domain and use case's tolerance for error and the number and criticality of business processes involved.",
        objects=["Proposed agentic AI use case", "Business processes involved in the use case"],
        qualifications=["The listed impact factors are non-exhaustive considerations."],
    ),
    "EXTREQ-5513796D63BEB71E": dict(
        clause="2.1.2",
        summary="Centrally issue and track agent identities and their attendant permissions.",
        objects=["Agent identities", "Permissions attendant to agent identities"],
        artefacts=["Central record of issued agent identities and attendant permissions."],
        evidence=["Central identity and permission records for deployed agents."],
        methods=["Inspect central records for issuance and tracking of agent identities and attendant permissions."],
    ),
    "EXTREQ-844AFD2FC9FB59FD": dict(
        clause="2.1.2",
        summary="Differentiate and record the capacities in which an agent acts to enable auditability.",
        objects=["Capacities in which an agent acts"],
        artefacts=["Record of the capacities in which each agent acts."],
        evidence=["Agent-capacity records supporting auditability."],
    ),
    "EXTREQ-F3EBD6E34FEFE18E": dict(
        clause="2.1.2",
        summary="Clearly record delegations of authority to agents.",
        objects=["Delegations of authority to agents"],
        artefacts=["Records of authority delegated to agents."],
        evidence=["Recorded delegations of authority."],
    ),
    "EXTREQ-F477502DEE0603FE": dict(
        clause="2.1.2",
        summary="Do not permit an agent to exercise authority beyond the limits the authorising human user can set.",
        objects=["Authority delegated by an authorising human user to an agent"],
        conditions=["Applies when a human user authorises an agent to act."],
    ),
    "EXTREQ-82D791A7B54305B0": dict(
        clause="2.2.1",
        summary="Clearly allocate internal roles and responsibilities for agentic AI across the system lifecycle.",
        objects=["Internal agentic-AI lifecycle roles and responsibilities"],
        qualifications=["Illustrative roles include decision makers, product teams, cybersecurity teams, and users."],
    ),
    "EXTREQ-90553A3F265B9C63": dict(
        clause="2.2.1",
        summary="Clarify external-party obligations through terms or contracts covering security arrangements, performance guarantees, and data protection.",
        objects=["Terms or contracts with external agentic-AI parties"],
        artefacts=["Terms or contracts addressing security arrangements, performance guarantees, and data protection."],
        evidence=["Applicable terms or contracts with external agentic-AI parties."],
        methods=["Review applicable terms or contracts for the stated external-party obligations."],
        conditions=["Applies when external providers or other external parties are involved."],
        qualifications=["Reassess the arrangement where gaps remain, taking the organization's risk tolerance into account."],
    ),
    "EXTREQ-99712BA8308E32FF": dict(
        clause="2.3.2",
        summary="Test agents for safety and security before deployment, including their complete workflows, tool use, individual and multi-agent behavior, realistic environments, and varied repeated trials.",
        objects=["Agentic AI system and its complete workflows"],
        stages=["testing-evaluation", "deployment"],
        artefacts=["Agent safety and security test results."],
        evidence=["Pre-deployment test results for the agentic AI system."],
        methods=["Test complete workflows, individual and multi-agent behavior, realistic environments, varied datasets, and repeated runs."],
        timing=["Before deployment."],
        qualifications=["Calibrate environmental realism against the risk of prematurely allowing agents to affect the real world."],
    ),
    "EXTREQ-4253F163EB11C1C9": dict(
        clause="2.4.2",
        summary="Declare in the user interface, at the point of interaction, that the user is interacting with an agent.",
        objects=["User interface through which a user interacts with an agent"],
        conditions=["Applies to users who interact with agents."],
    ),
    "EXTREQ-47EE577CC52EF131": dict(
        clause="2.4.2",
        summary="Provide users with the human contact points responsible for agents so users can alert them about malfunctions or dissatisfaction with decisions.",
        objects=["Human accountability and escalation contact points for interacting users"],
        conditions=["Applies to users who interact with agents."],
        evidence=["Responsible human contact points made available to interacting users."],
    ),
}


MIGRATED = {
    "EXTREQ-14B4DA1E7646754E": dict(
        clause="2.1.2",
        summary="Limit an agent's area of impact through mechanisms and procedures for taking it offline and containing its effects.",
        objects=["Area of impact of agent actions"],
        evidence=["Mechanisms and procedures for taking agents offline and containing their effects."],
        methods=["Exercise or inspect offline and containment mechanisms and procedures."],
    ),
    "EXTREQ-2DC8F2B745E464D5": dict(
        clause="2.2.1",
        summary="Require external agentic-AI providers to disclose sufficient information about their systems' capabilities and data handling practices.",
        objects=["External providers' agentic-AI capabilities and data handling practices"],
        evidence=["External-provider disclosures about system capabilities and data handling practices."],
        conditions=["Applies when reliance on an external provider creates opacity about its agentic AI system."],
    ),
    "EXTREQ-DB1BC74DC84D4718": dict(
        clause="2.2.2",
        summary="Define significant checkpoints and action boundaries at which agents require human approval, especially for sensitive actions.",
        objects=["Agent checkpoints and action boundaries requiring human approval"],
        stages=["design", "operation-use"],
        evidence=["Configured approval checkpoints and action boundaries."],
        methods=["Inspect workflows for required human approval at defined checkpoints and sensitive-action boundaries."],
        conditions=["Give particular attention to sensitive agent actions."],
    ),
    "EXTREQ-DCFA4FF526B6439C": dict(
        clause="2.3.1",
        summary="Design and implement technical controls for agentic components, increased security concerns, and multi-agent interactions to mitigate identified risks.",
        objects=["Agentic components", "Agentic AI security surfaces and protocols", "Multi-agent interactions"],
        stages=["design", "development"],
        qualifications=["These agent-specific controls supplement baseline software and large-language-model controls."],
    ),
    "EXTREQ-DFAE10B7FA4CAEEF": dict(
        clause="2.3.3",
        summary="Continuously test deployed agentic AI systems to confirm expected operation and detect model drift or environmental changes.",
        objects=["Deployed agentic AI system"],
        stages=["testing-evaluation", "monitoring"],
        evidence=["Post-deployment agentic-AI test results."],
        methods=["Continuous post-deployment testing for expected operation, model drift, and environmental change effects."],
        timing=["Continuously after deployment."],
    ),
    "EXTREQ-FE078DDB1FABA3AF": dict(
        clause="2.3.3",
        summary="Define risk-proportionate interventions for monitoring alerts, including human review, temporary halting, and termination and fallback for catastrophic malfunction or compromise.",
        objects=["Monitoring alerts and corresponding intervention mechanisms"],
        stages=["monitoring", "incident-response"],
        evidence=["Defined intervention responses for monitoring alert types."],
        methods=["Verify that alert types map to risk-proportionate review, halt, termination, or fallback responses."],
        conditions=["Intervention severity should be proportionate to risk; termination and fallback apply to catastrophic malfunction or compromise."],
    ),
    "EXTREQ-1F35B4A263EF7055": dict(
        clause="2.3.3",
        summary="Continuously monitor and log deployed agent behavior and establish reporting and failsafe mechanisms for failures or unexpected behavior.",
        objects=["Deployed agent behavior and workflow logs", "Failure reporting and failsafe mechanisms"],
        stages=["monitoring", "operation-use"],
        artefacts=["Agent behavior and workflow logs.", "Failure reporting and failsafe mechanisms."],
        evidence=["Logs and monitoring records supporting real-time intervention, incident debugging, and periodic audit."],
        methods=["Review monitoring and logs for support of real-time intervention, incident debugging, and regular audit."],
        timing=["Continuously after deployment, with audit at regular intervals."],
    ),
    "EXTREQ-24F5ABCB4CAFC499": dict(
        clause="2.4.2",
        summary="Inform interacting users about their responsibilities, the agent's authorised range of actions and decisions, and how their data is collected, stored, and used.",
        objects=["Information provided to users who interact with agents"],
        conditions=["Applies to users who interact with agents."],
        qualifications=["Where appropriate, users may set approval thresholds and boundaries beyond organization-defined limits; obtain explicit data consent where necessary."],
    ),
}


SPLITS = [
    ("EXTREQ-DB1BC74DC84D4718", "EXTREQ-094BAEC3B9534B43", "2.2.2", "approval-request-quality", dict(
        summary="Present human approvers with contextual and digestible approval requests that convey relevant risk and confidence information.",
        objects=["Human approval requests for agent actions"],
        evidence=["Approval requests containing contextual risk and confidence information."],
    )),
    ("EXTREQ-DB1BC74DC84D4718", "EXTREQ-C36DCD607690CE69", "2.2.2", "oversight-effectiveness-audit", dict(
        summary="Regularly audit the effectiveness of human oversight using measures such as override rates, response times, and outlier analytics.",
        objects=["Effectiveness of human oversight for agentic AI"],
        evidence=["Human-oversight effectiveness audit results."],
        methods=["Audit oversight effectiveness using relevant operational measures."],
        timing=["Regularly."],
        qualifications=["Override rates, response times, and outlier analytics are illustrative measures."],
    )),
    ("EXTREQ-DB1BC74DC84D4718", "EXTREQ-B8ACB627BDA3A2CD", "2.2.2", "overseer-training", dict(
        summary="Train human overseers and provide the domain expertise needed to assess agent actions effectively.",
        objects=["Human overseers of agentic AI systems"],
        artefacts=["Training materials or records for human overseers."],
        evidence=["Evidence that human overseers received relevant training and domain support."],
    )),
    ("EXTREQ-DB1BC74DC84D4718", "EXTREQ-8E40B24DA599E4D5", "2.2.2", "automated-realtime-monitoring", dict(
        summary="Complement human oversight with automated real-time monitoring, alerts, anomaly detection, or agent-on-agent monitoring, and default-deny behavior if approval infrastructure fails.",
        objects=["Automated monitoring and approval infrastructure for agentic AI"],
        evidence=["Configured real-time monitoring, alerting, and approval-infrastructure failure controls."],
        qualifications=["The monitoring mechanisms listed by the source are illustrative alternatives."],
    )),
    ("EXTREQ-DCFA4FF526B6439C", "EXTREQ-84F679C261C5C817", "2.3.1", "runtime-controls", dict(
        summary="Use runtime controls to monitor and intervene during agent execution where static design-time safeguards may not catch every risk.",
        objects=["Runtime execution of agentic AI systems"],
        evidence=["Configured runtime monitoring and intervention controls."],
        qualifications=["Rate limits and input validation are illustrative runtime controls."],
    )),
    ("EXTREQ-DFAE10B7FA4CAEEF", "EXTREQ-50FBD66AC83B727A", "2.3.3", "change-review", dict(
        summary="Define technical, environmental, performance, and regulatory triggers for change review and categorise changes by risk.",
        objects=["Changes to agentic AI systems and their operating context"],
        stages=["change-management"],
        artefacts=["Change-review triggers and risk categories."],
        evidence=["Change reviews initiated and scaled according to defined triggers and risk categories."],
        timing=["When a defined technical, environmental, performance, or regulatory trigger occurs."],
        qualifications=["Review depth should scale from lighter review for minor changes to full governance review or immediate re-risk assessment for material or critical changes."],
    )),
    ("EXTREQ-24F5ABCB4CAFC499", "EXTREQ-329CA68B17B42CCB", "2.4.3", "integrating-user-training", dict(
        summary="Educate and train users who integrate agents into work processes on agent foundations, effective oversight, and maintaining tradecraft and business continuity.",
        objects=["Users who integrate agents into work processes or oversee them"],
        stages=["deployment", "operation-use"],
        artefacts=["Education and training materials for users who integrate or oversee agents."],
        evidence=["Training records covering agent foundations, oversight, and retained core skills."],
        conditions=["Applies to users who integrate agents into work processes or oversee them."],
    )),
]

ID_MIGRATIONS = {
    "EXTREQ-1F35B4A263EF7055": "EXTREQ-6A5C3FF914A66FFD",
    "EXTREQ-24F5ABCB4CAFC499": "EXTREQ-08FE5D118B5A6EE0",
    "EXTREQ-2DC8F2B745E464D5": "EXTREQ-10507618F9C18B1A",
    "EXTREQ-DB1BC74DC84D4718": "EXTREQ-590563A599CC235C",
    "EXTREQ-DCFA4FF526B6439C": "EXTREQ-8643F34ADBB5C239",
    "EXTREQ-DFAE10B7FA4CAEEF": "EXTREQ-99E97A9DFCB368EE",
    "EXTREQ-FE078DDB1FABA3AF": "EXTREQ-39B1C084B42C32CC",
}

# These records keep their established deterministic identity. Their exact
# subsection remains explicit in provenance and parent-section metadata.
PRESERVED_CLAUSE_KEYS = {
    "EXTREQ-4253F163EB11C1C9": "2.4",
    "EXTREQ-47EE577CC52EF131": "2.4",
    "EXTREQ-82D791A7B54305B0": "2.2",
    "EXTREQ-90553A3F265B9C63": "2.2",
    "EXTREQ-99712BA8308E32FF": "2.3",
}


def migrate(check_only: bool) -> None:
    document = load_requirements_document()
    records = document["requirements"]
    by_id = {record["requirement_id"]: record for record in records}
    targets = {**PRESERVED, **MIGRATED}
    missing = sorted(
        rid for rid in targets
        if rid not in by_id and ID_MIGRATIONS.get(rid) not in by_id
    )
    if missing:
        raise ValueError(f"IMDA fidelity repair IDs are absent: {missing}")
    for old_id, new_id in ID_MIGRATIONS.items():
        old = by_id.get(old_id)
        new = by_id.get(new_id)
        if old is not None and new is not None and old is not new:
            raise ValueError(f"both legacy and migrated IMDA identities exist: {old_id}, {new_id}")
        record = old or new
        fields = MIGRATED[old_id]
        if requirement_id(fields["clause"], record["identity_key"]) != new_id:
            raise ValueError(f"deterministic IMDA migrated identity changed: {new_id}")
        record["requirement_id"] = new_id
        by_id[old_id] = record
        by_id[new_id] = record
    for rid, fields in targets.items():
        record = by_id[rid]
        if record.get("vigil_source_id") != SOURCE_ID:
            raise ValueError(f"IMDA fidelity repair ID resolves to another source: {rid}")
        update(record, **fields)
        if rid in PRESERVED_CLAUSE_KEYS:
            record["parent_section_or_group"] = fields["clause"]
            record["clause_or_control"] = PRESERVED_CLAUSE_KEYS[rid]

    new_ids = []
    for base_id, expected_id, clause, identity, fields in SPLITS:
        if requirement_id(clause, identity) != expected_id:
            raise ValueError(f"deterministic IMDA split identity changed: {expected_id}")
        existing = by_id.get(expected_id)
        if existing is not None:
            if existing.get("vigil_source_id") != SOURCE_ID or existing.get("identity_key") != identity:
                raise ValueError(f"existing IMDA split conflicts with deterministic migration: {expected_id}")
            split = existing
        else:
            split = copy.deepcopy(by_id[base_id])
            split.update({"requirement_id": expected_id, "identity_key": identity})
            records.append(split)
            by_id[expected_id] = split
        update(split, clause=clause, **fields)
        new_ids.append(expected_id)

    def actual_id(rid: str) -> str:
        return ID_MIGRATIONS.get(rid, rid)

    related = {actual_id(rid): [] for rid in set(MIGRATED)}
    related.update({rid: [] for rid in new_ids})
    for base_id, new_id, *_ in SPLITS:
        base_id = actual_id(base_id)
        related[base_id].append(new_id)
        related[new_id].append(base_id)
    for rid, links in related.items():
        by_id[rid]["related_external_requirements"] = sorted(set(links))

    migrated_old_ids = set(ID_MIGRATIONS)
    records = [record for record in records if record["requirement_id"] not in migrated_old_ids]

    records.sort(key=lambda record: record["requirement_id"])
    document["requirements"] = records
    document["requirement_count"] = len(records)
    document["updated_at"] = "2026-08-28"
    print(f"IMDA fidelity migration valid: repaired {len(targets)} records; migrated {len(ID_MIGRATIONS)} identities; added {len(SPLITS)} split records; {len(records)} total requirements")
    if not check_only:
        write_requirements_document(document)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()
    migrate(args.check_only)


if __name__ == "__main__":
    main()
