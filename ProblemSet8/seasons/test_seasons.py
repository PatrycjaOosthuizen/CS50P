import pytest
from seasons import minutes_lived

def main():
    test_1()
    test_2()

def test_1():
    assert minutes_lived(2000, 5, 30) == "Twelve million, seven hundred ninety-four thousand, four hundred minutes"
    assert minutes_lived(1999, 1, 1) == "Thirteen million, five hundred thirty-six thousand minutes"

def test_2():
    assert minutes_lived(23, 1, 2000) == "Invalid date"

if __name__ == "__main__":
    main()
