import importlib.util
import sys
from pathlib import Path

solution_path = Path(__file__).parent.parent.parent / 'problems/1-easy/125-Valid-Palindrome/solution.py'
spec = importlib.util.spec_from_file_location('valid_palindrome_solution', solution_path)
mod = importlib.util.module_from_spec(spec)
sys.modules['valid_palindrome_solution'] = mod
spec.loader.exec_module(mod)


def test_valid_palindrome():
    assert mod.isPalindrome("A man, a plan, a canal: Panama") is True
    assert mod.isPalindrome("race a car") is False
    assert mod.isPalindrome("") is True
