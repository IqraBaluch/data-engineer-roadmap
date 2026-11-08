"""
ssert tests

An assert checks that something is True. If it’s False, Python stops with an AssertionError.

"""

def is_even(a):
    return a % 2 == 0

assert is_even(2) == True
assert is_even(10) == True     # passes, nothing happens
assert is_even(7) == False     # passes
#assert is_even(3) == True      # fails -> AssertionError
assert is_even(-4) == True 

def grade(a):
    if a >= 90:
        return "A"
    elif a >= 70:
        return "B"
    else:
        return "C"

assert grade(90) == "A"
#assert grade(50) == "B"

def calculate_total(a,b):
    return a + b
assert calculate_total(150,250) == 400
assert calculate_total(0,0) == 0 
assert calculate_total(-5,5) == 0
