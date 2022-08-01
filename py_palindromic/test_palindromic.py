import palindromic


def test_empty():
    assert palindromic.get_longest_palindrome("") == ""


def test_one_char():
    assert palindromic.get_longest_palindrome("A") == "A"


def test_one_char_in_str():
    assert palindromic.get_longest_palindrome("ABCDEF") == "A"


def test_whole_string():
    assert palindromic.get_longest_palindrome("ABBA") == "ABBA"


def test_banana():
    assert palindromic.get_longest_palindrome("BANANA") == "ANANA"


def test_reversed():
    assert palindromic.get_longest_palindrome("ABCDEBCA") == "A"
