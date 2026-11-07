print(7 + 2)     # 9
print(7 - 2)     # 5
print(7 * 2)     # 14
print(7 / 2)     # 3.5   always gives a float
print(7 // 2)    # 3     integer division: drops the decimal part and gives integer
print(7 % 2)     # 1     remainder
print(7 ** 2)    # 49    power

"""
The three that matter most:

1. // answers “how many whole times does it fit?” So 17 // 5 is 3. Round off
2. % answers “what is left over?” So 17 % 5 is 2.
3. Together: 17 = 5 * 3 + 2.

"""

print(" ----- Uses you’ll see all the time ----- ")

n = 8472
print(n//10) # evrything except 0
print(n%10) # last digit
print(n%2) # prints 0

print(" ---- Careful with negatives: // rounds toward negative infinity. ----")

print(-7 // 2)    # -4  (not -3)
print(-7 % 3)     # 2   (the result takes the sign of the divisor)

"""
Don’t memorise this. Just run it and see, and trust the result.

Order of operations: ** first, then * / // %, then + -. Brackets override. 2 + 3 * 4 is 14, and (2 + 3) * 4 is 20.

"""

print("Quick check (answer before moving)")

"""What does each print?

print(10 // 3)
print(10 % 3)
print(2 ** 3 + 1)
print("5" + "5")
print(int("5") + int("5"))"""
