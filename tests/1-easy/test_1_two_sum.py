import importlib.util
import sys
from pathlib import Path

solution_path = Path(__file__).parent.parent.parent / 'problems/1-easy/1-Two-Sum/solution.py'
spec = importlib.util.spec_from_file_location('two_sum_solution', solution_path)
mod = importlib.util.module_from_spec(spec)
sys.modules['two_sum_solution'] = mod
spec.loader.exec_module(mod)

def test_two_sum():
    assert set(mod.twoSum([2,7,11,15], 9)) == set([0,1])
    assert set(mod.twoSum([3,2,4], 6)) == set([1,2])
    assert set(mod.twoSum([3,3], 6)) == set([0,1])
