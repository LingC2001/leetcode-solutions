import importlib.util
import sys
from pathlib import Path

solution_path = (
    Path(__file__).parent.parent.parent / "problems/2-medium/167-Two-Sum-II-Input-Array-Is-Sorted/solution.py"
)
spec = importlib.util.spec_from_file_location("two_sum_ii_solution", solution_path)
mod = importlib.util.module_from_spec(spec)
sys.modules["two_sum_ii_solution"] = mod
spec.loader.exec_module(mod)


def test_two_sum_ii():
    assert mod.twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert mod.twoSum([2, 3, 4], 6) == [1, 3]
    assert mod.twoSum([-1, 0], -1) == [1, 2]
