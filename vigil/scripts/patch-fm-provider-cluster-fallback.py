#!/usr/bin/env python3
"""One-shot patch: finalize bounded FM record-context fallback semantics."""

from pathlib import Path

PATH = Path(__file__).with_name("reconcile-fm-system-context.py")
text = PATH.read_text(encoding="utf-8")

# Generic uncertainty text must never become a model/runtime identity.
if '    "not specified",\n' not in text:
    marker = '    "none",\n'
    if marker not in text:
        raise SystemExit("placeholder marker not found")
    text = text.replace(marker, marker + '    "not specified",\n', 1)

# Preserve a bounded record-level provider cluster when source-level affected-system
# fields are incomplete. This is intentionally independent of source_platform.
if "declared_providers: list[str] = []" not in text:
    old_platform = '''    platform = context.get("platform_or_vendor")

    high_products = products_from_text(specific)
'''
    new_platform = '''    platform = context.get("platform_or_vendor")

    declared_providers: list[str] = []
    for field in ("primary_evidenced_vendors", "vendor_cluster"):
        values = context.get(field)
        if isinstance(values, list):
            for value in values:
                if value in CONCRETE_LEGACY_PROVIDERS:
                    add_unique(declared_providers, str(value))

    high_products = products_from_text(specific)
'''
    if old_platform not in text:
        raise SystemExit("context provider marker not found")
    text = text.replace(old_platform, new_platform, 1)

if "extend_unique(providers, declared_providers)" not in text:
    old_lists = '''    providers: list[str] = []
    products: list[str] = []

    if high_providers:
'''
    new_lists = '''    providers: list[str] = []
    products: list[str] = []
    extend_unique(providers, declared_providers)

    if high_providers:
'''
    if old_lists not in text:
        raise SystemExit("context provider-list marker not found")
    text = text.replace(old_lists, new_lists, 1)

# A record-context fallback is provenance from the historical FM classification,
# not from whichever external source happens to be first in source_records.
if "def record_context_fallback_entry(" not in text:
    insertion_marker = '''def project_system_context(
'''
    helper = '''def record_context_fallback_entry(
    record_id: str,
    providers: list[str],
    products: list[str],
    models: list[str],
) -> dict[str, Any]:
    return {
        "providers_or_vendors": providers,
        "products_or_services": products,
        "models_or_runtimes": models,
        "projection_basis": "record-system-context-fallback",
        "source_title": f"{record_id} historical system_context",
    }


'''
    if insertion_marker not in text:
        raise SystemExit("project_system_context marker not found")
    text = text.replace(insertion_marker, helper + insertion_marker, 1)

old_fallback = '''            evidenced_systems.append(
                projection_entry(
                    eligible_sources[0],
                    missing_vendors,
                    missing_products,
                    missing_models,
                    "record-system-context-fallback",
                )
            )
'''
new_fallback = '''            evidenced_systems.append(
                record_context_fallback_entry(
                    str(record.get("id", "VIGIL failure mode")),
                    missing_vendors,
                    missing_products,
                    missing_models,
                )
            )
'''
if old_fallback in text:
    text = text.replace(old_fallback, new_fallback, 1)
elif "record_context_fallback_entry(" not in text[text.index("def project_system_context("):]:
    raise SystemExit("record-context fallback call not found")

PATH.write_text(text, encoding="utf-8")
print("Finalized FM record-context fallback semantics.")
