import pytest 
from my_library.my_library.math_utils import calculate_mean, factorial 
 
def test_calculate_mean(): 
    assert calculate_mean([1, 2, 3]) == 2 
 
def test_factorial(): 
    assert factorial(5) == 120 
 
def test_factorial_zero(): 
    assert factorial(0) == 1 
 
def test_negative_factorial_raises_error(): 
    with pytest.raises(ValueError): 
        factorial(-1) 
