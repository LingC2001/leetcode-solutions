import importlib.util
import sys
from pathlib import Path

solution_path = Path(__file__).parent.parent.parent / "problems/1-easy/20-Valid-Parentheses/solution.py"
spec = importlib.util.spec_from_file_location("valid_parentheses_solution", solution_path)
if spec is None or spec.loader is None:
    raise ImportError(f"Could not load spec for {solution_path}")
mod = importlib.util.module_from_spec(spec)
sys.modules["valid_parentheses_solution"] = mod
spec.loader.exec_module(mod)


def test_valid_parentheses():
    assert mod.isValid("()") is True
    assert mod.isValid("()[]{}") is True
    assert mod.isValid("(]") is False
    assert mod.isValid("([)]") is False
    assert mod.isValid("{") is False
    assert mod.isValid("") is True
    assert mod.isValid("([])") is True
    assert mod.isValid("([{}])") is True
    assert mod.isValid("(((())))") is True
    assert mod.isValid("(()") is False
