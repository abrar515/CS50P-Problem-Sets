from fuel import convert, gauge
import pytest

def test_convert_format():
    assert convert("1/4") == 25
    with pytest.raises(ValueError):
        convert("14")

def test_convert_positive_int():
    with pytest.raises(ValueError):
        convert("-1/4")
    with pytest.raises(ValueError):
        convert("1/-4")

def test_convert_not_int():
    with pytest.raises(ValueError):
        convert("1.5/4")
    with pytest.raises(ValueError):
        convert("1/3.5")

def test_convert_x_greater():
    with pytest.raises(ValueError):
        convert("5/4")

def test_convert_y_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge_E():
    #"E" if that int is less than or equal to 1,
    assert gauge(1) == "E"
    assert gauge(0) == "E"

def test_gauge_F():
    #"F" if that int is greater than or equal to 99,
    assert gauge(100) == "F"
    assert gauge(99) == "F"


def test_gauge_Z():
    #and "Z%" otherwise, wherein Z is that same int.
    assert gauge(55) == "55%"
