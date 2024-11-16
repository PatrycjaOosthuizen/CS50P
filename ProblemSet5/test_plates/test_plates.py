import pytest
from plates import is_valid

def main():
    # Call tests functions
    test_max_and_min_characters()
    test_starts_with_two_letters()
    test_zero()
    test_middle()
    test_punctuations()

# Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
def test_max_and_min_characters():
    assert is_valid("AA") == True
    assert is_valid("A") == False
    assert is_valid("AAA222") == True
    assert is_valid("AAA222B") == False

# Vanity plates must start with at least two letters
def test_starts_with_two_letters():
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("2B") == False
    assert is_valid("22") == False

# The first number used cannot be a zero
def test_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

# Numbers cannot be used in the middle of the vanity plates: they must be at the end
def test_middle():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22B") == False
    assert is_valid("CS50P") == False

# No periods, spaces, or punctuation marks are allowed.
def test_punctuations():
     assert is_valid("PI314") == True
     assert is_valid("PI3 14") == False
     assert is_valid("PI3.14") == False
     assert is_valid("PI3?14") == False

if __name__ == "__main__":
    main()

