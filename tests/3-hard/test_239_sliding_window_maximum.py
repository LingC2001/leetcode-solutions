import importlib.util
import sys
from pathlib import Path

import pytest

solution_path = Path(__file__).parent.parent.parent / 'problems/3-hard/239-Sliding-Window-Maximum/solution.py'
spec = importlib.util.spec_from_file_location('sliding_window_maximum_solution', solution_path)
mod = importlib.util.module_from_spec(spec)
sys.modules['sliding_window_maximum_solution'] = mod
spec.loader.exec_module(mod)

TEST_CASES = [
    ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
    ([1], 1, [1]),
    ([9, 11], 2, [11]),
    ([4, -2], 2, [4]),
    ([7, 2, 4], 2, [7, 4]),
    ([1, 3, 1, 2, 0, 5], 3, [3, 3, 2, 5]),
    ([1, 3, 1, 2, 0, 5], 1, [1, 3, 1, 2, 0, 5]),
    ([1, 3, 1, 2, 0, 5], 6, [5]),
    ([1, 2, 3, 4, 5, 6], 2, [2, 3, 4, 5, 6]),
    ([6, 5, 4, 3, 2, 1], 2, [6, 5, 4, 3, 2]),
    ([1, 2, 3, 4, 5, 6], 3, [3, 4, 5, 6]),
    ([6, 5, 4, 3, 2, 1], 3, [6, 5, 4, 3]),
    ([1, 2], 2, [2]),
    ([1, 2], 1, [1, 2]),
]


@pytest.mark.parametrize("nums, k, expected", TEST_CASES)
def test_max_sliding_window(nums, k, expected):
    result = mod.maxSlidingWindow(nums, k)
    assert result == expected
