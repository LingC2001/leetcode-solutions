import importlib.util
import sys
from pathlib import Path

solution_path = Path(__file__).parent.parent.parent / "problems/2-medium/128-Longest-Consecutive-Sequence/solution.py"
spec = importlib.util.spec_from_file_location("longest_consecutive_sequence_solution", solution_path)
mod = importlib.util.module_from_spec(spec)
sys.modules["longest_consecutive_sequence_solution"] = mod
spec.loader.exec_module(mod)


def test_longest_consecutive_sequence():
    assert mod.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert mod.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert mod.longestConsecutive([]) == 0
