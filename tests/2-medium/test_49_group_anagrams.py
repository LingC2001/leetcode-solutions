import importlib.util
import sys
from pathlib import Path

solution_path = Path(__file__).parent.parent.parent / "problems/2-medium/49-Group-Anagrams/solution.py"
spec = importlib.util.spec_from_file_location("group_anagrams_solution", solution_path)
mod = importlib.util.module_from_spec(spec)
sys.modules["group_anagrams_solution"] = mod
spec.loader.exec_module(mod)


def test_group_anagrams():
    result = mod.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    # Convert to sets of frozensets for comparison
    assert set(frozenset(group) for group in result) == set(frozenset(group) for group in expected)
    assert mod.groupAnagrams([""]) == [[""]]
    assert mod.groupAnagrams(["a"]) == [["a"]]
