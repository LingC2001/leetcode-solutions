import importlib.util
import sys
from pathlib import Path

import pytest

solution_path = Path(__file__).parent.parent.parent / 'problems/2-medium/3-Longest-Substring-Without-Repeating-Characters/solution.py'
spec = importlib.util.spec_from_file_location('longest_substring_without_repeating_characters_solution', solution_path)
mod = importlib.util.module_from_spec(spec)
sys.modules['longest_substring_without_repeating_characters_solution'] = mod
spec.loader.exec_module(mod)

TEST_CASES = [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("", 0),
    ("au", 2),
    ("dvdf", 3),
    ("abba", 2),
    ("tmmzuxt", 5),
    ("aab", 2),
    ("abcdeafbdgcbb", 7),
    ("anviaj", 5),
]


@pytest.mark.parametrize("s, expected", TEST_CASES)
def test_length_of_longest_substring(s, expected):
    class Dummy:
        pass
    result = mod.lengthOfLongestSubstring(Dummy(), s)
    assert result == expected
