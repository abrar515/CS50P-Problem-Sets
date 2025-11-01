from bank import value

def test_value_hello():
    assert value("Hello there!") == 0


def test_value_h():
    assert value("Hey there!") == 20

def test_value_noH():
    assert value("Whatsup!") == 100
