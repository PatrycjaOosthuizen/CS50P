import pytest
from fuel import convert,gauge

def mani():
    # Call the tests functions
    test_correct_input()
    test_value_error()
    test_zero_division_error()

# Test correct input by user
def test_correct_input():
    assert convert("3/4") == 75 and gauge(75) == "75%"
    assert convert("1/4") == 25 and gauge(25) == "25%"
    assert convert("1/100") == 1 and gauge(1) == "E"
    assert convert("99/100") == 99 and gauge(99) == "F"

# Test ValueError
def test_value_error():
    with pytest.raises(ValueError):
        convert("three/four")

# Test ZeroDivisionError
def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

if __name__ == "__main__":
    main()
