import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def test_active_rights_contract():
    path = ROOT / "vigil" / "scripts" / "validate-vigil-rights.py"
    spec = importlib.util.spec_from_file_location("validate_vigil_rights", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert module.find_errors() == []
