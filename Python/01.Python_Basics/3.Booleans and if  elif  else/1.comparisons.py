"""
True/False and comparisons

A boolean has only two values: True and False, with a capital first letter. Comparisons produce them:

"""

print(5 > 3)     # True
print(5 < 3)     # False
print(5 == 5)    # True   (equal to)
print(5 != 3)    # True   (not equal to)
print(5 >= 5)    # True   (greater than or equal to)
print(4 <= 3)    # False  (less than or equal to)

"""The most common beginner bug: = vs ==

x = 5 stores 5 in x. It’s an instruction.
x == 5 asks whether x is 5. It’s a question, and the answer is True or False.

"""

# Comparisons work on strings too:

print("data" == "data")   # True
print("Data" == "data")   # False  (capital letters count)

# Combining conditions: and, or and not

age = 20
print(age >= 18 and age < 65)   # True   (BOTH must be true)
print(age < 13 or age > 65)     # False  (AT LEAST ONE must be true)
print(not age > 18)             # False  (flips True/False)

# Divisibility with %
print(10 % 2 == 0)   # True   (nothing left over, so 10 is divisible by 2)
print(9 % 2 == 0)    # False