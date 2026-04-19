def calculate_mean(numbers):
    """Return arithmetic mean for a non-empty numeric iterable."""
    return sum(numbers) / len(numbers)


def factorial(n):
    """Return factorial for a non-negative integer."""
    if n < 0:
        raise ValueError("Факториал определён только для неотрицательных чисел.")
    if n == 0:
        return 1
    return n * factorial(n - 1)
