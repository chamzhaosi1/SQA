from calculator import Calculator
import pytest

calc = Calculator()

# test math add in class Calculator
@pytest.mark.parametrize("x, y, expected", [(2,3,-5),(-3,3,0),(3,4,7),(-5,-3,-8),(6,3,9),(7,"3",10)])
def test_add(x, y, expected):
    assert calc.add(x, y) == expected

# test math sub in class Calculator
@pytest.mark.parametrize("x, y, expected", [(2,3,-1),(-3,3,-6),(3,4,-1),(-5,-3,-2),(6,3,3),(7,"3",4)])
def test_sub(x, y, expected):
    assert calc.sub(x, y) == expected

# test math div in class Calculator
@pytest.mark.parametrize("x, y, expected", [(6,3,2),(-3,3,-1),(12,4,3),(15,-3,-5),(18,3,6),(21,"3",7)])
def test_div(x, y, expected):
    assert calc.div(x, y) == expected

# test math mul in class Calculator
@pytest.mark.parametrize("x, y, expected", [(2,3,6),(3,3,9),(3,4,12),(-5,-3,15),(6,3,18),(7,"3",21)])
def test_mul(x, y, expected):
    assert calc.mul(x, y) == expected
