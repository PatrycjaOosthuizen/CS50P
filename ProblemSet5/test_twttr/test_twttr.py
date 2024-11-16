import pytest
from twttr import shorten

def main():
    # Call test functions
    test_lower_upper_case()
    test_numbers()
    test_punctuations()

# Test letters lowercase, uppercase and mix
def test_lower_upper_case():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("tWiTTeR") == "tWTTR"

# Test numbers
def test_numbers():
    assert shorten("123") == "123"

# Test punctuations
def test_punctuations():
    assert shorten(",.?!") == ",.?!"


if __name__ == "__main__":
    main()
