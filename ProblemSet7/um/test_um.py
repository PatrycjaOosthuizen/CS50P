from um import count

def main():
    test_lower_upper_cases()
    test_um_in_word()
    test_um_surrounded_by_space()

def test_lower_upper_cases():
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2


def test_um_in_word():
    assert count("drums") == 0

def test_um_surrounded_by_space():
    assert count(" um ") == 1
    assert count ("thanks, um ") == 1


if __name__ == "__main__":
    main()
