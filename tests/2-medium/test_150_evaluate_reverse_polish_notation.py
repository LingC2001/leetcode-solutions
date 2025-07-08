import importlib.util
import sys
from pathlib import Path

import pytest

solution_path = (
    Path(__file__).parent.parent.parent / "problems/2-medium/150-Evaluate-Reverse-Polish-Notation/solution.py"
)
spec = importlib.util.spec_from_file_location("evaluate_reverse_polish_notation_solution", solution_path)
mod = importlib.util.module_from_spec(spec)
sys.modules["evaluate_reverse_polish_notation_solution"] = mod
spec.loader.exec_module(mod)

TEST_CASES = [
    (["2", "1", "+", "3", "*"], 9),
    (["4", "13", "5", "/", "+"], 6),
    (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    (["3", "-4", "+"], -1),
    (["5", "1", "2", "+", "4", "*", "+", "3", "-"], 14),
    (["2", "3", "/"], 0),
    (["7", "2", "/"], 3),
    (["0", "3", "/"], 0),
    (["3", "0", "+"], 3),
    (["-2", "3", "/"], 0),
]


@pytest.mark.parametrize("tokens, expected", TEST_CASES)
def test_eval_rpn(tokens, expected):
    result = mod.evalRPN(tokens)
    assert result == expected
