def reverse_string(s):
    """Return reversed copy of the input string."""
    return s[::-1]


def count_vowels(s):
    """Count English vowels in the input string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
