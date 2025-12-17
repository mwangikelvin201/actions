from src.math_operations import add,sub

def test_add():
    assert add(2,3) == 5
    assert add(8,5) == 13
    assert add(10,1) == 11

def test_sub():
    assert sub (3,2) == 1
    assert sub (-5,4) == -9