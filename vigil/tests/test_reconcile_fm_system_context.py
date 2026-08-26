#!/usr/bin/env python3
"""Focused tests for evidence-backed FM system-context reconciliation."""

from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "vigil" / "scripts" / "reconcile-fm-system-context.py"
SPEC = importlib.util.spec_from_file_location("reconcile_fm_system_context", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def source(
    platform: str,
    system: str = "",
    model: str = "",
    *,
    title: str = "Source",
    url: str = "https://example.invalid/source",
    context: str = "",
    role: str = "incident-evidence",
) -> dict:
    return {
        "source_residence": "external",
        "source_role": role,
        "source_platform": platform,
        "system_or_product": system,
        "model_or_algorithm": model,
        "deployment_context": context,
        "source_title": title,
        "source_url": url,
    }


def base_record(
    sources: list[dict],
    context: dict | None = None,
    *,
    created: str = "2026-08-15",
) -> dict:
    return {
        "id": "VIGIL-2026-FM-9999",
        "record_type": "failure_mode",
        "date_recorded": created,
        "record_identity": {"created": created},
        "source_records": sources,
        "system_context": context or {
            "platform_or_vendor": "Multi Vendor",
            "product_or_service": "Other",
            "specific_model_or_runtime": "Unknown",
            "model_or_product": "Unknown",
            "interface_surface": "Multiple surfaces",
        },
    }


def test_multi_provider_rollup_uses_affected_system_fields() -> None:
    record = base_record([
        source("OpenAI Help Center", "OpenAI account access / ChatGPT / Codex / OpenAI API"),
        source("Business Insider", "Claude / Claude Code / Claude API", "Claude / Claude Code"),
    ])
    projected = MODULE.project_system_context(record)
    assert projected["evidence_scope"] == "multi-provider"
    assert projected["evidenced_vendors"] == ["OpenAI", "Anthropic"]
    assert "ChatGPT" in projected["evidenced_products_or_services"]
    assert "Codex" in projected["evidenced_products_or_services"]
    assert "Claude Code" in projected["evidenced_products_or_services"]
    assert projected["evidenced_models_or_runtimes"] == ["Claude", "Claude Code"]
    assert projected["platform_or_vendor"] == "Multi Vendor"
    assert projected["evidence_projection"]["method"] == "structured source affected-system roll-up with record system-context fallback"


def test_evidence_host_is_not_affected_vendor() -> None:
    record = base_record(
        [source("TikTok", title="TikTok observation")],
        context={
            "platform_or_vendor": "OpenAI",
            "product_or_service": "ChatGPT",
            "specific_model_or_runtime": "ChatGPT Advanced Voice Mode",
            "model_or_product": "ChatGPT",
            "interface_surface": "voice | multi-device",
        },
    )
    projected = MODULE.project_system_context(record)
    assert projected["evidenced_vendors"] == ["OpenAI"]
    assert projected["evidenced_products_or_services"] == ["ChatGPT"]
    assert projected["evidenced_models_or_runtimes"] == ["ChatGPT Advanced Voice Mode"]
    assert projected["platform_or_vendor"] == "OpenAI"
    assert projected["product_or_service"] == "ChatGPT"
    assert "TikTok" not in projected["evidenced_vendors"]
    assert "TikTok" not in projected["evidenced_products_or_services"]
    assert projected["evidenced_systems"][0]["projection_basis"] == "record-system-context-fallback"
    assert projected["evidenced_systems"][0]["source_title"] == "VIGIL-2026-FM-9999 historical system_context"
    assert "evidence_source_platform" not in projected["evidenced_systems"][0]


def test_publisher_and_narrative_are_not_mined() -> None:
    record = base_record([
        source("Reuters", "", "", context="OpenAI ChatGPT and Anthropic Claude are discussed here.")
    ])
    projected = MODULE.project_system_context(record)
    assert projected["evidenced_vendors"] == []
    assert projected["evidenced_products_or_services"] == []
    assert projected["evidence_scope"] == "system-unresolved"


def test_x_affected_system_can_use_record_context_fallback() -> None:
    record = base_record(
        [source("X Help Center")],
        context={
            "platform_or_vendor": "xAI",
            "product_or_service": "X",
            "specific_model_or_runtime": "Not applicable",
            "model_or_product": "X Premium / X verification / X recommender affordances",
            "interface_surface": "X profile",
        },
    )
    projected = MODULE.project_system_context(record)
    assert projected["evidenced_vendors"] == ["xAI"]
    assert "X" in projected["evidenced_products_or_services"]
    assert "X Premium" in projected["evidenced_products_or_services"]
    assert projected["platform_or_vendor"] == "xAI"


def test_specific_model_beats_polluted_host_compatibility_fields() -> None:
    record = base_record(
        [source("TikTok")],
        context={
            "platform_or_vendor": "TikTok",
            "product_or_service": "TikTok",
            "specific_model_or_runtime": "ChatGPT Advanced Voice Mode",
            "model_or_product": "TikTok",
            "interface_surface": "voice | multi-device",
        },
    )
    projected = MODULE.project_system_context(record)
    assert projected["evidenced_vendors"] == ["OpenAI"]
    assert projected["evidenced_products_or_services"] == ["ChatGPT"]
    assert projected["platform_or_vendor"] == "OpenAI"
    assert projected["product_or_service"] == "ChatGPT"


def test_uncertainty_is_not_a_model_and_provider_cluster_survives() -> None:
    record = base_record(
        [source("OpenAI Status", "ChatGPT and OpenAI APIs", "not specified")],
        context={
            "platform_or_vendor": "Multi Vendor",
            "vendor_cluster": ["OpenAI", "Anthropic"],
            "primary_evidenced_vendors": ["OpenAI", "Anthropic"],
            "product_or_service": "Other",
            "specific_model_or_runtime": "Not limited to a single model or runtime",
            "model_or_product": "OpenAI and Anthropic frontier AI platform services",
            "interface_surface": "multiple access surfaces",
        },
    )
    projected = MODULE.project_system_context(record)
    assert projected["evidence_scope"] == "multi-provider"
    assert projected["evidenced_vendors"] == ["OpenAI", "Anthropic"]
    assert projected["evidenced_models_or_runtimes"] == []
    fallback = [
        item for item in projected["evidenced_systems"]
        if item["projection_basis"] == "record-system-context-fallback"
    ]
    assert len(fallback) == 1
    assert fallback[0]["providers_or_vendors"] == ["Anthropic"]
    assert fallback[0]["source_title"] == "VIGIL-2026-FM-9999 historical system_context"
    assert "evidence_source_platform" not in fallback[0]


def test_qwen_maps_to_alibaba_without_expanding_closed_compatibility_enums() -> None:
    record = base_record([source("Research paper", "Qwen models", "Qwen3 235B")])
    projected = MODULE.project_system_context(record)
    assert projected["evidenced_vendors"] == ["Alibaba"]
    assert projected["evidenced_products_or_services"] == ["Qwen"]
    assert projected["evidenced_models_or_runtimes"] == ["Qwen3 235B"]
    assert projected["platform_or_vendor"] == "Other"
    assert projected["product_or_service"] == "Other"


def test_contextual_background_does_not_enter_affected_system_rollup() -> None:
    primary = source("Nature Communications", "ChatGPT", "GPT-4o", title="Primary", role="research-evidence")
    contextual = source(
        "OpenAI",
        "OpenAI API safety systems and Private Safety Processing",
        "Private Safety Processing",
        title="Contextual provider material",
        role="contextual-background",
    )
    projected = MODULE.project_system_context(base_record([primary, contextual]))
    assert projected["evidenced_vendors"] == ["OpenAI"]
    assert projected["evidenced_models_or_runtimes"] == ["GPT-4o"]
    assert [item["source_title"] for item in projected["evidenced_systems"]] == ["Primary"]


def test_target_model_list_remains_open_ended_and_traceable() -> None:
    targets = (
        "GPT-4o; DeepSeek-V3; Llama 3.1 70B; Llama 4 Maverik; o4-mini; "
        "Claude 4 Sonnet; Gemini 2.5 Flash; Grok 3; Qwen3 30B"
    )
    record = base_record([
        source(
            "Nature Communications",
            "Nine target language models evaluated against autonomous adversarial LRM attacks",
            targets,
            role="research-evidence",
        )
    ], created="2026-08-25")
    projected = MODULE.project_system_context(record)
    assert projected["evidence_scope"] == "multi-provider"
    assert projected["evidenced_vendors"] == ["OpenAI", "Anthropic", "Google", "Meta", "xAI", "DeepSeek", "Alibaba"]
    assert projected["evidenced_models_or_runtimes"] == targets.split("; ")
    assert "Qwen" in projected["evidenced_products_or_services"]
    assert projected["platform_or_vendor"] == "Multi Vendor"
    assert projected["product_or_service"] == "Other"


def test_reconciliation_date_does_not_predate_record_creation() -> None:
    old = base_record([source("Vendor documentation", "ChatGPT", "GPT-5")], created="2026-07-01")
    new = base_record([source("Vendor documentation", "ChatGPT", "GPT-5")], created="2026-08-25")
    assert MODULE.project_system_context(old)["evidence_projection"]["reconciled_on"] == "2026-08-15"
    assert MODULE.project_system_context(new)["evidence_projection"]["reconciled_on"] == "2026-08-25"


def test_reconciliation_is_idempotent() -> None:
    record = base_record([source("Vendor documentation", "ChatGPT", "GPT-5")])
    assert MODULE.reconcile_record(record) is True
    assert MODULE.reconcile_record(record) is False


def main() -> int:
    test_multi_provider_rollup_uses_affected_system_fields()
    test_evidence_host_is_not_affected_vendor()
    test_publisher_and_narrative_are_not_mined()
    test_x_affected_system_can_use_record_context_fallback()
    test_specific_model_beats_polluted_host_compatibility_fields()
    test_uncertainty_is_not_a_model_and_provider_cluster_survives()
    test_qwen_maps_to_alibaba_without_expanding_closed_compatibility_enums()
    test_contextual_background_does_not_enter_affected_system_rollup()
    test_target_model_list_remains_open_ended_and_traceable()
    test_reconciliation_date_does_not_predate_record_creation()
    test_reconciliation_is_idempotent()
    print("FM system-context reconciliation tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
