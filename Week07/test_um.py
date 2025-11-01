from um import count
import pytest

def test_count_true():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2

def test_count_false():
    assert count("This is CS50!") == 0
    assert count("jump pump drum umea") == 0
    assert count("jump, pump, drum, umea") == 0


