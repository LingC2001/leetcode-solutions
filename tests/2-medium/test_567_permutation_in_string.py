import importlib.util
import sys
from pathlib import Path

import pytest

solution_path = Path(__file__).parent.parent.parent / 'problems/2-medium/567-Permutation-in-String/solution.py'
spec = importlib.util.spec_from_file_location('permutation_in_string_solution', solution_path)
mod = importlib.util.module_from_spec(spec)
sys.modules['permutation_in_string_solution'] = mod
spec.loader.exec_module(mod)

TEST_CASES = [
    ("ab", "eidbaooo", True),
    ("ab", "eidboaoo", False),
    ("adc", "dcda", True),
    ("hello", "ooolleoooleh", False),
    ("a", "a", True),
    ("a", "b", False),
    ("abc", "ccccbbbbaaaa", False),
    ("abc", "bbbca", True),
    ("xyz", "afdgzyxksldfm", True),
    ("xyz", "afdgzyksldfm", False),
    ("", "anything", True),
    ("a", "", False),
]


@pytest.mark.parametrize("s1, s2, expected", TEST_CASES)
def test_check_inclusion(s1, s2, expected):
    sol = mod.Solution()
    result = sol.checkInclusion(s1, s2)
    assert result == expected
