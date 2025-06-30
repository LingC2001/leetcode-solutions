import importlib.util
import sys
from pathlib import Path

import pytest

solution_path = Path(__file__).parent.parent.parent / 'problems/1-easy/121-Best-Time-To-Buy-And-Sell-Stock/solution.py'
spec = importlib.util.spec_from_file_location('best_time_to_buy_and_sell_stock_solution', solution_path)
mod = importlib.util.module_from_spec(spec)
sys.modules['best_time_to_buy_and_sell_stock_solution'] = mod
spec.loader.exec_module(mod)

TEST_CASES = [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
    ([1, 2], 1),
    ([2, 4, 1], 2),
    ([3, 3, 5, 0, 0, 3, 1, 4], 4),
    ([1], 0),
    ([2, 1, 2, 1, 0, 1, 2], 2),
    ([2, 1, 4], 3),
    ([1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9], 9),
    ([2, 4, 1, 7], 6),
]


@pytest.mark.parametrize("prices, expected", TEST_CASES)
def test_max_profit(prices, expected):
    result = mod.maxProfit(prices)
    assert result == expected
