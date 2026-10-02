import copy
import importlib.util
from pathlib import Path
import sys
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "vigil" / "scripts"
SCRIPT = SCRIPTS / "validate-external-requirement-fidelity.py"
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location("validate_external_requirement_fidelity", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


class ExternalRequirementFidelityTests(unittest.TestCase):
    def test_migration_packages_are_independent(self):
        canonical = {"retained-parent", "already-migrated-child"}
        self.assertEqual(module.migration_state({"retained-parent"}, {"future-child"}, canonical), "pre-migration")
        self.assertEqual(module.migration_state({"retired-parent"}, {"already-migrated-child"}, canonical), "migrated")

    def test_migration_rejects_partial_children_and_parent_reuse(self):
        self.assertEqual(module.migration_state({"parent"}, {"a", "b"}, {"a"}), "partial-or-invalid")
        self.assertEqual(module.migration_state({"parent"}, {"a", "b"}, {"parent", "a", "b"}), "partial-or-invalid")
        self.assertEqual(module.migration_state({"parent"}, {"parent"}, {"parent"}), "partial-or-invalid")

    def test_current_fidelity_ledger_is_structurally_valid(self):
        errors, warnings, summary = module.validate()
        self.assertEqual(errors, [])
        scope = module.load(module.SCOPE_PATH)
        fidelity = module.load(module.FIDELITY_PATH)
        assured = {module.source_key(entry) for entry in fidelity["entries"] if entry["fidelity_status"] == "assured"}
        complete = {module.source_key(entry) for entry in scope["entries"] if entry["extraction_status"] == "complete"}
        self.assertEqual(summary["fidelity_assured_effective_complete_sources"], len(complete & assured))
        self.assertEqual(summary["effective_partial_due_fidelity"], len(complete - assured))
        self.assertEqual(len(warnings), len(complete - assured))
        self.assertTrue(all(warning.startswith("effective downgrade:") for warning in warnings))

    def test_nonassured_historical_completion_is_not_effective_completion(self):
        fidelity = copy.deepcopy(module.load(module.FIDELITY_PATH))
        scope = module.load(module.SCOPE_PATH)
        complete_keys = {
            module.source_key(entry) for entry in scope["entries"]
            if entry["extraction_status"] == "complete"
        }
        target = next(
            entry for entry in fidelity["entries"]
            if module.source_key(entry) in complete_keys
        )
        target["fidelity_status"] = "provisional"
        target["effective_extraction_status"] = "complete"
        original_load = module.load
        with mock.patch.object(
            module, "load",
            side_effect=lambda path: fidelity if path == module.FIDELITY_PATH else original_load(path),
        ):
            errors, _, _ = module.validate()
        self.assertTrue(any(
            "non-assured source cannot remain effectively complete" in error
            for error in errors
        ))


if __name__ == "__main__":
    unittest.main()
