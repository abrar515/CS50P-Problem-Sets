from plates import is_valid


#"vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters."
def test_is_valid_2_6():
    assert is_valid("CS50") == True
    assert is_valid("CS") == True
    assert is_valid("CS5050") == True
    assert is_valid("C") == False
    assert is_valid("CS505050") == False

#All vanity plates must start with at least two letters
def test_is_valid_2L():
    assert is_valid("CS50") == True
    assert is_valid("C500") == False
    assert is_valid("5050") == False


#No periods, spaces, or punctuation marks are allowed.
def test_is_valid_punc():
    assert is_valid("CS 50") == False
    assert is_valid("CS,00") == False
    assert is_valid("CS.50") == False

#Numbers cannot be used in the middle of a plate"
def test_is_valid_num_in_mid():
    assert is_valid("CS50CS") == False

#first num cant be zero
def test_is_valid_num_0():
    assert is_valid("CS050") == False


