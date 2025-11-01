from twttr import shorten


def test_shorten_lower():
    assert shorten("alphabeta") == "lphbt"

def test_shorten_Upper():
    assert shorten("Alphabeta") == "lphbt"

def test_shorten_num():
    assert shorten("Alpha1beta2") == "lph1bt2"

def test_shorten_punc():
    assert shorten("Alpha1,beta2") == "lph1,bt2"


