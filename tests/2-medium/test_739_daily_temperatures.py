import importlib.util
import sys
from pathlib import Path

import pytest

solution_path = Path(__file__).parent.parent.parent / "problems/2-medium/739-Daily-Temperatures/solution.py"
spec = importlib.util.spec_from_file_location("daily_temperatures_solution", solution_path)
mod = importlib.util.module_from_spec(spec)
sys.modules["daily_temperatures_solution"] = mod
spec.loader.exec_module(mod)

TEST_CASES = [
    ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
    ([30, 40, 50, 60], [1, 1, 1, 0]),
    ([30, 60, 90], [1, 1, 0]),
    ([90, 80, 70, 60], [0, 0, 0, 0]),
    ([70], [0]),
    ([], []),
    ([70, 70, 70, 70], [0, 0, 0, 0]),
    ([60, 61, 62, 63, 64, 65], [1, 1, 1, 1, 1, 0]),
    ([65, 64, 63, 62, 61, 60], [0, 0, 0, 0, 0, 0]),
    ([73, 72, 71, 70, 69, 68, 67, 66], [0, 0, 0, 0, 0, 0, 0, 0]),
]


@pytest.mark.parametrize("temp, expected", TEST_CASES)
def test_daily_temperatures(temp, expected):
    class Dummy:
        pass

    result = mod.dailyTemperatures(Dummy(), temp)
    assert result == expected
