import pytest
import utils

def test_fact():
    # À compléter...
    assert utils.fact(3)==6
    

def test_roots():
    # À compléter...
    assert utils.roots(1,-5,6)==(3,2)

def test_integrate():
    # À compléter...
    assert utils.integrate(lambda x : x, 0, 3)==9/2
    
