import importlib.util
import sys
from pathlib import Path

import pytest

solution_path = Path(__file__).parent.parent.parent / "problems/2-medium/853-Car-Fleet/solution.py"
spec = importlib.util.spec_from_file_location("car_fleet_solution", solution_path)
mod = importlib.util.module_from_spec(spec)
sys.modules["car_fleet_solution"] = mod
spec.loader.exec_module(mod)

TEST_CASES = [
    (12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3], 3),
    (10, [6, 8], [3, 2], 2),
    (100, [0, 2, 4], [4, 2, 1], 1),
    (10, [0, 4, 2], [2, 1, 3], 1),
    (10, [0, 2, 4], [2, 2, 2], 3),
    (10, [0, 2, 4], [1, 1, 1], 3),
    (10, [0, 2, 4], [3, 2, 1], 1),
    (0, [], [], 0),
    (10, [0], [1], 1),
    (10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10),
]


@pytest.mark.parametrize("target, position, speed, expected", TEST_CASES)
def test_car_fleet(target, position, speed, expected):
    result = mod.carFleet(target, position, speed)
    assert result == expected
