#!/usr/bin/env python3
"""Enrich SDOS v1.10 records from the complete public control catalogue."""
from __future__ import annotations

import argparse

from external_requirements_io import load_requirements_document, write_requirements_document


SOURCE_ID = "EXT-8FEA9674D97A"
SOURCE_VERSION = "1.10"
DIGEST = "547bfa9615f137429871951e2beb8de8f306ed8ae4995e6ef95dfcfbcc23c52b"
SOURCE = "https://aamcyber.com/sdos/reference/v1/"
ACTOR = "AI agent platform operator or implementer applying the SDOS runtime governance framework"
SCOPE = (
    "Autonomous or semi-autonomous agentic AI workflows in which agents invoke tools, "
    "make decisions, or produce outputs on behalf of an operator."
)
GLOBAL_QUALIFICATIONS = [
    "SDOS states that it is not designed for static LLM-chat interfaces without tool invocation or autonomous action.",
    "The public reference describes SDOS control behavior and evidence categories, but not implementation-level architecture, internal data structures, algorithm parameters, field schemas, log formats, or configuration structures; those details are assigned to licensed operational documentation.",
    "SDOS-to-framework mappings express design alignment, not certification, endorsement, affiliation, or independent proof of compliance.",
]
REVIEW_LIMITATIONS = [
    "SDOS is an owner-authored private-sector framework; no statutory, ISO, IEEE or NIST authority is implied.",
    "The records analytically express the published SDOS functionality as governance practices; they do not assert independent certification, regulatory compliance, or Caelestis conformity.",
    "The public control reference does not include the implementation-level schemas and operational details assigned by the source to licensed documentation.",
]


CONTROL = {
    "SDOS-GV-01": dict(
        objects=["Versioned governance policy configuration", "Set of active SDOS modules and agent capabilities"],
        timing=["Whenever modules or governed capabilities are activated or deactivated, without requiring executable-code changes."],
        artefacts=["Versioned governance configuration.", "Audit log records of module activation or deactivation."],
        evidence=["Configuration File", "Audit Log Record"],
        methods=["Compare active modules and capabilities with the current versioned policy configuration and associated change records."],
        related=["SDOS-GV-04", "SDOS-IA-02", "SDOS-IN-01", "SDOS-IN-03"],
    ),
    "SDOS-GV-02": dict(
        objects=["Task-specific AI model capability-tier assignment and its rationale"],
        timing=["At dispatch for every governed operation."],
        artefacts=["Audit record linking assessed task characteristics, model-tier assignment, and execution outcome."],
        evidence=["Audit Log Record", "System Behavior"],
        methods=["Verify through audit records and system behavior that the governance layer assigns the tier, prevents agent, model, or caller override, and records the rationale."],
        related=["SDOS-RM-01", "SDOS-RM-02", "SDOS-RM-03", "SDOS-AU-01"],
    ),
    "SDOS-GV-03": dict(
        objects=["Configuration-governed agent admission policy and its criteria, conditions, restrictions, and scope limitations"],
        timing=["Before an agent may access any governed operation and whenever admission policy is updated."],
        artefacts=["Governance configuration defining the default-deny admission policy."],
        evidence=["Configuration File", "System Behavior"],
        methods=["Inspect the configured admission criteria and observe that agents lacking satisfied criteria cannot access governed operations."],
        qualifications=["This control defines what the admission policy states; SDOS-AD-01 separately enforces that policy at the runtime execution boundary."],
        related=["SDOS-AD-01", "SDOS-IA-01", "SDOS-GV-01", "SDOS-IN-01"],
    ),
    "SDOS-GV-04": dict(
        objects=["Common governance authority, policy source, and decision process across active SDOS modules"],
        timing=["For every governance decision handled by any active module."],
        artefacts=["Audit records showing governance decisions across modules."],
        evidence=["Audit Log Record", "System Behavior"],
        methods=["Compare decisions across active modules to verify use of the same authoritative policy source and decision process."],
        related=["SDOS-GV-01", "SDOS-IA-02", "SDOS-EN-02", "SDOS-IN-01"],
    ),
    "SDOS-GV-05": dict(
        objects=["Governance enforcement layer and the constraints it applies independently of AI model inference"],
        timing=["Continuously for governed model operations across model versions, providers, and alignment states."],
        evidence=["System Behavior", "Test Suite Result"],
        methods=["Exercise authorized execution pathways and verify that model outputs or generated instructions cannot override, bypass, or modify governance constraints."],
        related=["SDOS-EN-01", "SDOS-EN-02", "SDOS-IN-01", "SDOS-GV-03"],
    ),
    "SDOS-RM-01": dict(
        objects=["Risk-tier classification and permit, conditional-permit, or block disposition for each tool invocation"],
        timing=["At the dispatch boundary before every tool invocation executes."],
        artefacts=["Audit record of the dispatch-time risk classification and governance disposition."],
        evidence=["Audit Log Record", "System Behavior"],
        methods=["Trace invocation records and runtime behavior to confirm classification uses the current policy state before execution."],
        related=["SDOS-GV-02", "SDOS-RM-02", "SDOS-RM-03", "SDOS-EN-01", "SDOS-AU-01"],
    ),
    "SDOS-RM-02": dict(
        objects=["Dispatch-time task characteristics and minimum required model capability tier"],
        timing=["At dispatch for each task."],
        artefacts=["Audit record of task assessment and model capability-tier determination."],
        evidence=["Audit Log Record", "System Behavior"],
        methods=["Verify that task assessment considers tool-access scope, decision depth, and governance consequence, and prevents routing below the resulting minimum tier."],
        qualifications=["The source lists scope of tool access, decision depth, and governance consequence as factors considered by the assessment."],
        related=["SDOS-GV-02", "SDOS-RM-01", "SDOS-RM-03"],
    ),
    "SDOS-RM-03": dict(
        objects=["Minimum model capability floor for policy-defined elevated-risk tasks"],
        timing=["At model binding for every task in a policy-defined elevated-risk category."],
        conditions=["Applies to tasks within policy-defined elevated-risk categories."],
        evidence=["System Behavior", "Test Suite Result"],
        methods=["Test that elevated-risk tasks cannot be bound below the configured capability floor regardless of the complexity assessment."],
        qualifications=["The risk-floor constraint is hard enforcement rather than a preference or advisory."],
        related=["SDOS-GV-02", "SDOS-RM-01", "SDOS-RM-02"],
    ),
    "SDOS-EN-01": dict(
        objects=["Governed outbound writes, external communications, tool dispatches, and data transfers"],
        timing=["Before every governed outbound operation executes."],
        artefacts=["Audit record of each egress-boundary policy evaluation and its permit, modify, or block result."],
        evidence=["Audit Log Record", "System Behavior"],
        methods=["Observe governed outbound operations to confirm they pass through the enforcement point and are evaluated against current policy before execution."],
        related=["SDOS-EN-02", "SDOS-EN-04", "SDOS-GV-05", "SDOS-AU-01", "SDOS-RM-01"],
    ),
    "SDOS-EN-02": dict(
        objects=["Secondary module-level authorization confirmation for each executing SDOS module"],
        timing=["Immediately before each module executes a governed operation, after central governance evaluation."],
        evidence=["System Behavior", "Test Suite Result"],
        methods=["Test that module execution cannot proceed without a valid central governance decision confirmed at the module boundary."],
        related=["SDOS-EN-01", "SDOS-GV-04", "SDOS-IA-02", "SDOS-IN-03"],
    ),
    "SDOS-EN-03": dict(
        objects=["Operating posture during governance-infrastructure unavailability, indeterminate state, baseline-integrity failure, and partial degradation"],
        timing=["Whenever governance infrastructure is unavailable or indeterminate, baseline integrity fails, or a partial-degradation state occurs; until infrastructure is restored and the baseline verified."],
        artefacts=["Documented degradation policy within the integrity-verified governance baseline."],
        evidence=["System Behavior", "Test Suite Result"],
        methods=["Test infrastructure-unavailability, baseline-integrity-failure, and intermediate degradation scenarios against the documented degradation policy."],
        conditions=["Pre-authorized operations may continue only during governance-infrastructure unavailability and only where the standing integrity-verified configuration permits them.", "Operations requiring active governance evaluation at elevated risk are blocked in either primary failure mode."],
        qualifications=["Baseline integrity failure requires all operations to halt without exception under SDOS-IN-02; partial-degradation states are governed by documented operation-specific rules rather than treated as binary full-operation or total-halt states."],
        related=["SDOS-EN-01", "SDOS-EN-02", "SDOS-RM-01", "SDOS-IN-02"],
    ),
    "SDOS-EN-04": dict(
        objects=["Tamper-evident record of each governed outbound execution and its permitting decision"],
        timing=["At execution of every governed outbound operation and before returning its result to the caller."],
        artefacts=["Structured chained-hash or signed audit record containing the permitting decision, initiating agent identity, timestamp, and protected policy-relevant operation metadata."],
        evidence=["Audit Log Record", "System Behavior"],
        methods=["Verify record creation order and use SDOS-AU-02 integrity mechanisms to detect post-hoc modification."],
        qualifications=["The specific tamper-evidence algorithm and signing-key management are assigned by the source to operational documentation."],
        related=["SDOS-EN-01", "SDOS-AU-01", "SDOS-AU-02", "SDOS-IA-01"],
    ),
    "SDOS-IA-01": dict(
        objects=["Agent identity artifact, governance-managed trust root, and propagated invocation identity"],
        timing=["At the start of every governance evaluation, before evaluation and admission, and throughout the governance pipeline."],
        artefacts=["Signed agent identity artifact.", "Audit records associating tool invocations with the verified agent identity."],
        evidence=["Audit Log Record", "System Behavior"],
        methods=["Validate the signed identity artifact against the configured governance trust root and verify denial when identity cannot be established."],
        qualifications=["Signed identity verification against a configured trust root does not by itself imply hardware-rooted remote attestation; the chain is hardware-attested only where the deployment substrate provides a hardware-rooted or TEE-backed trust root."],
        related=["SDOS-AD-01", "SDOS-GV-03", "SDOS-AU-01", "SDOS-EN-04"],
    ),
    "SDOS-IA-02": dict(
        objects=["Cryptographically signed SDOS module manifest, declared module identity, and authorized capabilities"],
        timing=["Before registering any tools from a module."],
        artefacts=["Signed module manifest declaring module identity and authorized capabilities."],
        evidence=["Module Manifest", "System Behavior"],
        methods=["Verify each manifest before tool registration and confirm rejection of modules with missing, invalid, or tampered manifests."],
        related=["SDOS-GV-01", "SDOS-IN-03", "SDOS-EN-02", "SDOS-GV-04"],
    ),
    "SDOS-AU-01": dict(
        objects=["Structured governance audit record for every tool invocation"],
        timing=["For every tool invocation and before returning the tool result, whether the operation succeeds, fails, or is blocked."],
        artefacts=["Audit record containing governance classification, agent identity, model-binding rationale, timestamp, and protected policy-relevant invocation parameters."],
        evidence=["Audit Log Record"],
        methods=["Inspect invocation records for required fields, pre-result write order, and coverage of successful, failed, and blocked outcomes."],
        qualifications=["Timestamp generation is local to the governance layer; cross-system event ordering in distributed deployments requires NTP or equivalent deployment-infrastructure synchronization."],
        related=["SDOS-AU-02", "SDOS-AU-03", "SDOS-GV-02", "SDOS-RM-01", "SDOS-EN-04"],
    ),
    "SDOS-AU-02": dict(
        objects=["Audit-record format and storage substrate providing durable append-only behavior and tamper detection"],
        timing=["For every audit record throughout its retained history."],
        artefacts=["Append-only, integrity-protected audit log records."],
        evidence=["Audit Log Record", "System Behavior"],
        methods=["Attempt or simulate historical-record modification and verify detection through chained-hash, signed-record, or equivalent integrity-preserving mechanisms."],
        qualifications=["The durable append-only property is jointly provided by record format and storage substrate; storage selection and durability guarantees are deployment-tier obligations."],
        related=["SDOS-AU-01", "SDOS-AU-03", "SDOS-IN-01", "SDOS-EN-04"],
    ),
    "SDOS-AU-03": dict(
        objects=["Two independently maintained audit repositories and their discrepancy signal"],
        timing=["Simultaneously as part of every audit event."],
        artefacts=["Two independently maintained audit records for each event.", "Detectable discrepancy signal between repositories."],
        evidence=["Audit Log Record", "System Behavior"],
        methods=["Compare repositories and exercise repository unavailability, corruption, or compromise to confirm continuity and discrepancy detection."],
        qualifications=["SDOS produces the discrepancy signal but leaves reconciliation authority and procedure deployment-defined.", "Physical separation strength is substrate-dependent; the strongest implementation uses separate trust domains with independent administrative control."],
        related=["SDOS-AU-01", "SDOS-AU-02", "SDOS-IN-01"],
    ),
    "SDOS-IN-01": dict(
        objects=["Governance configuration and its authorized cryptographic integrity baseline"],
        timing=["At system startup before tool registration or agent processing, and when triggered during runtime."],
        artefacts=["Authorized governance integrity baseline.", "Governance-baseline integrity test result."],
        evidence=["System Behavior", "Test Suite Result"],
        methods=["Cryptographically compare the governance configuration with the authorized baseline and verify that failure triggers SDOS-IN-02 halt behavior."],
        related=["SDOS-IN-02", "SDOS-GV-01", "SDOS-GV-03", "SDOS-AU-01"],
    ),
    "SDOS-IN-02": dict(
        objects=["Unauthorized governance-baseline change, system halt, and baseline re-authorization"],
        timing=["Immediately on detection and before any tool registration or operation processing; recovery only after explicit re-authorization."],
        artefacts=["Explicit governance-baseline re-authorization by a designated administrator."],
        evidence=["System Behavior", "Test Suite Result"],
        methods=["Introduce an unauthorized baseline change and verify total halt, absence of degraded operation, and recovery only after designated-administrator re-authorization."],
        conditions=["Applies when the governance baseline integrity check detects unauthorized configuration modification."],
        qualifications=["There is no partial or degraded operating mode after a baseline-integrity failure."],
        related=["SDOS-IN-01", "SDOS-EN-03", "SDOS-GV-01"],
    ),
    "SDOS-IN-03": dict(
        objects=["Module-manifest signature, declared identity, and authorized-capability state"],
        timing=["Before module activation and before registering any tools from the module."],
        artefacts=["Cryptographically signed module manifest."],
        evidence=["Module Manifest", "System Behavior", "Test Suite Result"],
        methods=["Verify the manifest signature and capability state, and test rejection of unsigned, invalidly signed, or capability-mismatched manifests."],
        related=["SDOS-IA-02", "SDOS-GV-01", "SDOS-EN-02", "SDOS-IN-01"],
    ),
    "SDOS-DE-01": dict(
        objects=["Policy-defined multi-agent deliberation panel, participating-agent admission and identity, and structured panel output"],
        timing=["When a governed question or decision is assigned to a multi-agent deliberation panel."],
        artefacts=["Structured auditable deliberation output."],
        evidence=["Audit Log Record", "System Behavior"],
        methods=["Inspect panel policy, participating-agent admission and identity, and the resulting structured output; for elevated-risk decisions, verify routing to human review."],
        conditions=["For elevated-risk decisions, deliberation output is an input to human review."],
        qualifications=["Convergence is a deliberation signal, not a correctness guarantee; correlated errors may persist across models with shared training distributions.", "SDOS-DE-01 supports but does not satisfy external human-oversight obligations and is not a substitute for human review of elevated-risk decisions."],
        related=["SDOS-DE-02", "SDOS-IA-01", "SDOS-AU-01", "SDOS-GV-04", "SDOS-RM-01"],
    ),
    "SDOS-DE-02": dict(
        objects=["Governed deliberation decision record, individual agent assessments, convergence and divergence, and scored panel summary"],
        timing=["At completion of each governed deliberation panel and throughout retention as a governed artifact."],
        artefacts=["Structured retained deliberation decision record."],
        evidence=["Audit Log Record", "System Behavior"],
        methods=["Inspect the retained record for individual assessments, convergent and divergent positions, and a scored collective summary under the ordinary SDOS audit controls."],
        related=["SDOS-DE-01", "SDOS-AU-01", "SDOS-AU-02"],
    ),
    "SDOS-RS-01": dict(
        objects=["Post-hoc Return on Safety Investment evaluation over accumulated governed query-log and feedback data"],
        timing=["Post-hoc over accumulated query-log and feedback records."],
        artefacts=["Operator ROSI report with composite score, priority recommendation, and per-dimension mean, standard deviation, and sample count."],
        evidence=["Audit Log Record", "System Behavior", "Operator Report"],
        methods=["Recalculate the dual-track weighted metric and verify the resulting score, recommendation, and statistical summaries against accumulated governed feedback data."],
        qualifications=["Track 1 weights cost avoidance 0.40, time saved 0.35, and efficiency gain 0.25; Track 2 weights exposure reduction 0.40, resilience gain 0.35, and mission continuity 0.25; the composite score is in [0.0, 1.0].", "The evaluation uses the governed feedback loop already in operation and requires no additional data-collection infrastructure.", "The source identifies U.S. Provisional Application No. 64/049,300 (filed 2026-04-25), section 9.2 and claims 81-84; VIGIL makes no patent-status or freedom-to-operate determination."],
        related=["SDOS-AU-01", "SDOS-AU-02", "SDOS-AU-03", "SDOS-RM-01", "SDOS-RM-02"],
    ),
    "SDOS-AD-01": dict(
        objects=["Runtime pre-admission gate for agents seeking governed operations"],
        timing=["Before any tool invocation proceeds to risk classification, model binding, or execution, including under an existing session."],
        artefacts=["Audit record of agent admission or denial."],
        evidence=["System Behavior", "Test Suite Result", "Audit Log Record"],
        methods=["Test new and previously established sessions to verify default denial and the inability of non-admitted agents to reach governance evaluation or execution."],
        conditions=["Applies to all agents seeking governed operations, including agents with pre-existing sessions."],
        qualifications=["This control enforces at runtime the admission policy defined by SDOS-GV-03."],
        related=["SDOS-GV-03", "SDOS-IA-01", "SDOS-EN-01", "SDOS-AU-01"],
    ),
}


def migrate(write: bool) -> int:
    document = load_requirements_document()
    records = [
        record for record in document["requirements"]
        if record["vigil_source_id"] == SOURCE_ID and record["source_version"] == SOURCE_VERSION
    ]
    if len(records) != 24:
        raise ValueError(f"expected 24 SDOS v1.10 records, found {len(records)}")
    by_control = {record["clause_or_control"]: record for record in records}
    if set(by_control) != set(CONTROL):
        raise ValueError(f"SDOS control population mismatch: {sorted(set(by_control) ^ set(CONTROL))}")
    id_by_control = {control: record["requirement_id"] for control, record in by_control.items()}

    for control, record in by_control.items():
        data = CONTROL[control]
        record.update({
            "source_review_date": "2026-08-28",
            "applicable_actor": [ACTOR],
            "governed_object": data["objects"],
            "timing_or_frequency": data["timing"],
            "required_artefacts": data.get("artefacts", []),
            "evidence_expectation": [
                f"SDOS-listed evidence type: {value}." for value in data["evidence"]
            ],
            "verification_method": data["methods"],
            "applicability_conditions": [SCOPE] + data.get("conditions", []),
            "exceptions_or_qualifications": GLOBAL_QUALIFICATIONS + data.get("qualifications", []),
            "related_external_requirements": [id_by_control[value] for value in data["related"]],
            "review_limitations": REVIEW_LIMITATIONS,
        })
        provenance = record["interpretation_provenance"]
        provenance.update({
            "source_analysis_method": (
                "Direct field-level comparison against the complete public SDOS Runtime Governance "
                "Framework v1.10 control catalogue; the source-native control identity was retained "
                "and source-explicit timing, evidence, conditions, qualifications, and related controls "
                "were represented without treating framework alignment as certification."
            ),
            "source_locator": SOURCE,
            "reviewed_source_digest": DIGEST,
            "reviewed_source_digest_algorithm": "sha256",
            "reviewed_source_digest_status": "recorded",
        })

    print("SDOS v1.10 fidelity migration valid: 24 identities retained; 0 added; 0 retired")
    if write:
        write_requirements_document(document)
        print("Wrote canonical EXTREQ shards and compatibility aggregate")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    raise SystemExit(migrate(args.write))


if __name__ == "__main__":
    main()
