import pytest
import random
from numb3rs import validate

n = []
w = []
for i in range(20):
    n.append(random.randint(1,255))
    w.append(random.randint(256,1000))



def test_validate():
    assert validate(f"{n[0]}.{n[1]}.{n[2]}.{n[3]}") == True
    assert validate(f"{w[0]}.{w[1]}.{w[2]}.{w[3]}") == False

def test_validate_B1():
    assert validate(f"{w[4]}.{n[4]}.{n[5]}.{n[6]}") ==  False
    assert validate(f"{n[7]}.{w[5]}.{w[6]}.{w[7]}") == False

def test_validate_B2():
    assert validate(f"{n[8]}.{w[8]}.{n[9]}.{n[10]}") ==  False
    assert validate(f"{w[9]}.{n[11]}.{w[10]}.{w[11]}") == False

def test_validate_B3():
    assert validate(f"{n[12]}.{n[13]}.{w[12]}.{n[14]}") ==  False
    assert validate(f"{w[13]}.{w[14]}.{n[15]}.{w[15]}") == False

def test_validate_B4():
    assert validate(f"{n[16]}.{n[17]}.{n[18]}.{w[16]}") ==  False
    assert validate(f"{w[17]}.{w[18]}.{w[19]}.{n[19]}") == False


