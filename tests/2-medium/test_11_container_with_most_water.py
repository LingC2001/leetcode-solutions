import importlib.util
import sys
from pathlib import Path

import pytest

solution_path = Path(__file__).parent.parent.parent / "problems/2-medium/11-Container-With-Most-Water/solution.py"
spec = importlib.util.spec_from_file_location("container_with_most_water_solution", solution_path)
mod = importlib.util.module_from_spec(spec)
sys.modules["container_with_most_water_solution"] = mod
spec.loader.exec_module(mod)

TEST_CASES = [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1),
    ([4, 3, 2, 1, 4], 16),
    ([1, 2, 1], 2),
    ([2, 3, 10, 5, 7, 8, 9], 36),
    ([1, 2, 4, 3], 4),
    ([1, 3, 2, 5, 25, 24, 5], 24),
    ([1, 2, 3, 4, 5, 25, 24, 3, 4], 24),
    ([1, 2], 1),
    ([1, 1000, 1000, 6, 2, 5, 4, 8, 3, 7], 1000),
]


@pytest.mark.parametrize("height, expected", TEST_CASES)
def test_max_area(height, expected):
    class Dummy:
        pass

    result = mod.maxArea(Dummy(), height)
    assert result == expected
