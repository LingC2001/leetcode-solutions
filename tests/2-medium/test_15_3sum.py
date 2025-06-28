import importlib.util
import sys
from pathlib import Path
import pytest

solution_path = Path(__file__).parent.parent.parent / 'problems/2-medium/15-3Sum/solution.py'
spec = importlib.util.spec_from_file_location('three_sum_solution', solution_path)
mod = importlib.util.module_from_spec(spec)
sys.modules['three_sum_solution'] = mod
spec.loader.exec_module(mod)

TEST_CASES = [
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ([], []),
    ([0], []),
    ([0, 0, 0], [[0, 0, 0]]),
    ([1, 2, -2, -1], []),
    ([-2, 0, 1, 1, 2], [[-2, 1, 1], [-2, 0, 2]]),
    ([3, 0, -2, -1, 1, 2], [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]),
    ([0, 0, 0, 0], [[0, 0, 0]]),
    ([-1, 0, 1, 0], [[-1, 0, 1]]),
    ([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6], [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]),
]

@pytest.mark.parametrize("nums, expected", TEST_CASES)
def test_three_sum(nums, expected):
    class Dummy:
        pass
    result = mod.threeSum(Dummy(), nums)
    result_sorted = sorted([sorted(triplet) for triplet in result])
    expected_sorted = sorted([sorted(triplet) for triplet in expected])
    assert result_sorted == expected_sorted
