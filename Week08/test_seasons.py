import pytest
from datetime import date
from seasons import convert_to_date


def test_convert_to_date():
    assert convert_to_date("2000-01-01") == date(2000,1,1)
    with pytest.raises(ValueError):
        assert convert_to_date("January 1, 1999")
