import math

def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

def testsquare():
   num = 7
   assert 7*7 == 40 ## this is false assertion

# This will not be executed, because the name doesn't match the pattern test*.
def tesequality():
   assert 10 == 11