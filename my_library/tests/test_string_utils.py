from my_library.my_library.string_utils import reverse_string, count_vowels


def test_reverse_string():
    """Check that reverse_string returns characters in reverse order."""
    assert reverse_string("hello") == "olleh"


def test_count_vowels():
    """Check vowel counting for a mixed-case English phrase."""
    assert count_vowels("Hello World") == 3
