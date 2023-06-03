import pytest

## test math multiple function 
@pytest.mark.parametrize("a, b, expected", [(2,3,6),(-3,3,-9),(3,4,12),(-5,-3,15),(6,3,18),(7,"3",21)])
def test_mul(a, b, expected):
    assert a*b == expected

## test math minus function
@pytest.mark.parametrize("a, b, expected", [(2,3,-1),(-3,3,-6),(3,4,-1),(-5,-3,-2),(6,3,3),(7,"3",4)])
def minustest(a, b, expected):
    assert a-b == expected

