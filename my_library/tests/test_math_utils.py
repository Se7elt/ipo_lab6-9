import pytest

from my_library.my_library.math_utils import calculate_mean, factorial


def test_calculate_mean():
    """Check arithmetic mean calculation for a simple list."""
    assert calculate_mean([1, 2, 3]) == 2


def test_factorial():
    """Check factorial calculation for a positive integer."""
    assert factorial(5) == 120


def test_factorial_zero():
    """Check factorial edge case for zero."""
    assert factorial(0) == 1


def test_negative_factorial_raises_error():
    """Check that factorial raises ValueError for negative input."""
    with pytest.raises(ValueError):
        factorial(-1)
