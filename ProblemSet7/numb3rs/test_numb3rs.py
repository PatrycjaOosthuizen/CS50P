from numb3rs import validate

def main():
    test_IP_format()
    test_range()

def test_IP_format():
    assert validate(r"1.2.3.4.5") == False
    assert validate(r"1.2.3.4") == True
    assert validate(r"1.2.3") == False
    assert validate(r"1.2") == False
    assert validate(r"1") == False


def test_range():
    assert validate(r"255.255.255.255") == True
    assert validate(r"127.0.0.1") == True
    assert validate(r"510.0.0.1") == False
    assert validate(r"256.255.255.255") == False
    assert validate(r"64.128.256.512") == False
    assert validate(r"1.2.3.1000") == False
    assert validate(r"cat") == False

if __name__ == "__main__":
    main()
