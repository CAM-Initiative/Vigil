#!/usr/bin/env python3
"""One-shot patch: preserve declared provider clusters in FM context fallback."""

from pathlib import Path

PATH = Path(__file__).with_name("reconcile-fm-system-context.py")
text = PATH.read_text(encoding="utf-8")

old_placeholder = '    "none",\n    "as described by the incident record",'
new_placeholder = '    "none",\n    "not limited to a single model or runtime",\n    "as described by the incident record",'
if old_placeholder in text:
    text = text.replace(old_placeholder, new_placeholder, 1)

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

PATH.write_text(text, encoding="utf-8")
print("Patched FM provider-cluster fallback.")
