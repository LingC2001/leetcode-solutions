import importlib.util
import sys
from pathlib import Path

import pytest

solution_path = (
    Path(__file__).parent.parent.parent
    / "problems/2-medium/74-Search-A-2D-Matrix/solution.py"
)
spec = importlib.util.spec_from_file_location("search_a_2d_matrix_solution", solution_path)
mod = importlib.util.module_from_spec(spec)
sys.modules["search_a_2d_matrix_solution"] = mod
spec.loader.exec_module(mod)

TEST_CASES = [
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
    ([[1]], 1, True),
    ([[1]], 2, False),
    ([[1, 3]], 3, True),
    ([[1, 3]], 2, False),
    ([[1], [3]], 3, True),
    ([[1], [3]], 2, False),
    ([[1, 2, 3, 4, 5]], 4, True),
    ([[1, 2, 3, 4, 5]], 6, False),
    ([[1], [3], [5]], 5, True),
    ([[1], [3], [5]], 0, False),
]


@pytest.mark.parametrize("matrix, target, expected", TEST_CASES)
def test_search_matrix(matrix, target, expected):
    result = mod.searchMatrix(matrix, target)
    assert result == expected
