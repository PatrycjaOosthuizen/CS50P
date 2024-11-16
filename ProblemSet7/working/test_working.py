from working import convert
import pytest

def main():
    test_time_incorrect_format()
    test_time()
    test_incorrect_hour()
    test_incorrect_minute()

def test_time_incorrect_format():
    with pytest.raises(ValueError):
        convert("9 AM - 9 PM")

def test_time():
        assert convert("9 AM to 5 PM") == "09:00 to 17:00"
        assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
        assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"



def test_incorrect_hour():
    with pytest.raises(ValueError):
        convert("17 PM to 21 PM")

def test_incorrect_minute():
     with pytest.raises(ValueError):
        convert("9:60 AM to 9:60 PM")
