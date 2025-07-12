import importlib.util
import sys
from pathlib import Path

import pytest

solution_path = Path(__file__).parent.parent.parent / "problems/1-easy/704-Binary-Search/solution.py"
spec = importlib.util.spec_from_file_location("binary_search_solution", solution_path)
mod = importlib.util.module_from_spec(spec)
sys.modules["binary_search_solution"] = mod
spec.loader.exec_module(mod)

TEST_CASES = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 5, 4),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 0),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 8),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 10, -1),
    ([1], 1, 0),
    ([1], 0, -1),
    ([], 1, -1),
    ([2, 4, 6, 8, 10], 6, 2),
    ([2, 4, 6, 8, 10], 2, 0),
    ([2, 4, 6, 8, 10], 10, 4),
    ([2, 4, 6, 8, 10], 5, -1),
]


@pytest.mark.parametrize("nums, target, expected", TEST_CASES)
def test_search(nums, target, expected):
    result = mod.search(nums, target)
    assert result == expected
