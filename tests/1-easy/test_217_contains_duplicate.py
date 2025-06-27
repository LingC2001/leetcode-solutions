import importlib.util
import sys
from pathlib import Path

solution_path = Path(__file__).parent.parent.parent / 'problems/1-easy/217-Contains-Duplicate/solution.py'
spec = importlib.util.spec_from_file_location('contains_duplicate_solution', solution_path)
mod = importlib.util.module_from_spec(spec)
sys.modules['contains_duplicate_solution'] = mod
spec.loader.exec_module(mod)

def test_contains_duplicate():
    assert mod.containsDuplicate([1,2,3,1]) is True
    assert mod.containsDuplicate([1,2,3,4]) is False
    assert mod.containsDuplicate([1,1,1,3,3,4,3,2,4,2]) is True
