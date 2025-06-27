import importlib.util
import sys
from pathlib import Path

solution_path = Path(__file__).parent.parent.parent / 'problems/1-easy/242-Valid-Anagram/solution.py'
spec = importlib.util.spec_from_file_location('valid_anagram_solution', solution_path)
mod = importlib.util.module_from_spec(spec)
sys.modules['valid_anagram_solution'] = mod
spec.loader.exec_module(mod)

def test_valid_anagram():
    assert mod.isAnagram(None, "anagram", "nagaram") is True
    assert mod.isAnagram(None, "rat", "car") is False
    assert mod.isAnagram(None, "", "") is True
