import pytest

# def testadd():
#     assert add(2, 3) == 5
#     assert add(3, 3) == 6
#     assert add(4, 3) == 7
#     assert add(5, 3) == 8
#     assert add(6, 3) == 9
#     assert add(7, 3) == 10

# def add(a, b):
#     return a+b

@pytest.mark.parametrize("a, b, expected", [(2,3,-5),(-3,3,0),(3,4,7),(-5,-3,-8),(6,3,9),(7,"3",10)])
def test_add(a, b, expected):
   assert add(a, b) == expected
   
def add(a, b):
    return a+b

