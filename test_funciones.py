from functions import sumar,isitPrime,restar

def test_sumar():
    assert sumar(2,4)==6
    assert sumar(-2,2)==0
    assert sumar(2,2)==4
    
def test_restar():
    assert restar(4,2)==2
    assert restar(2,2)==0
    assert restar(6,3)==3

def test_isitprime():
    assert isitPrime(7) is True
    assert isitPrime(4) is False