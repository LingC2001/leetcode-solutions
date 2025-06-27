import importlib.util
import sys
from pathlib import Path

solution_path = Path(__file__).parent.parent.parent / 'problems/2-medium/238-Product-Of-Array-Except-Self/solution.py'
spec = importlib.util.spec_from_file_location('product_of_array_except_self_solution', solution_path)
mod = importlib.util.module_from_spec(spec)
sys.modules['product_of_array_except_self_solution'] = mod
spec.loader.exec_module(mod)

def test_product_of_array_except_self():
    assert mod.productExceptSelf([1,2,3,4]) == [24,12,8,6]
    assert mod.productExceptSelf([0,0]) == [0,0]
    assert mod.productExceptSelf([2,3,4,5]) == [60,40,30,24]
