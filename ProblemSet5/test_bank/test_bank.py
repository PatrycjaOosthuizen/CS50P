import pytest
from bank import value

def main():
    # Call tests functions
     test_hello()
     test_h()

# Test starts with hello return 0
def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("hElLo") == 0
    assert value("Hello, Newman") == 0

# Test starts with h return 20
def test_h():
    assert value("hey") == 20
    assert value("Hi") == 20
    assert value("How you doing?") == 20

# Test other greetings return 100
def test_other():
    assert value("What's happening?") == 100
    assert value("good day") == 100

if __name__ == "__main__":
    main()
