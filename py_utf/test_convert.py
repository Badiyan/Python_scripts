import convert


def test_empty_string():
    assert convert.utf_len(b"") == 0


def test_latin_and_punctuation():
    assert convert.utf_len(b"Hello!") == 6


def test_cyrillic():
    assert convert.utf_len("Привіт!".encode('utf-8')) == 7


def test_japanese():
    assert convert.utf_len("こんにちは".encode('utf-8')) == 5


def test_mixed():
    assert convert.utf_len("Hello! Привіт! こんにちは".encode('utf-8')) == 20