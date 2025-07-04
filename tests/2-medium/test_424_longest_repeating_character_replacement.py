import importlib.util
import sys
from pathlib import Path

import pytest

solution_path = Path(__file__).parent.parent.parent / 'problems/2-medium/424-Longest-Repeating-Character-Replacement/solution.py'
spec = importlib.util.spec_from_file_location('longest_repeating_character_replacement_solution', solution_path)
mod = importlib.util.module_from_spec(spec)
sys.modules['longest_repeating_character_replacement_solution'] = mod
spec.loader.exec_module(mod)

TEST_CASES = [
    ("ABAB", 2, 4),
    ("AABABBA", 1, 4),
    ("AAAA", 2, 4),
    ("ABCDE", 1, 2),
    ("AABABBA", 2, 5),
    ("BAAAB", 2, 5),
    ("ABBB", 2, 4),
    ("ABAA", 0, 2),
    ("", 2, 0),
    ("A", 0, 1),
    ("A", 1, 1),
    ("AAAB", 0, 3),
    ("AAAB", 1, 4),
]


@pytest.mark.parametrize("s, k, expected", TEST_CASES)
def test_character_replacement(s, k, expected):
    result = mod.characterReplacement(s, k)
    assert result == expected
