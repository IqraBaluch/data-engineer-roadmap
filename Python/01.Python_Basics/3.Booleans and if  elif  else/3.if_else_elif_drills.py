# Drill 1: Even or odd
# Take a number and print Even or Odd. Test: 4, 7, 0.

num = 0

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Drill 2: Grade
#Print the grade from a score: A for 90 and above,
# B for 75–89, C for 60–74, otherwise F. Test: 95, 75, 60, 59, 90.

score = 95
if score >= 90:
    print("A")
elif score >= 75:
    print("B")
elif score >= 60:
    print("C")
else:
    print("F")


# Drill 3: Ticket price
"""Print the price by age:

under 13 → child, 5
13 to 64 → adult, 10
65 and above → senior, 6"""

age = 14
child = 5
adult = 10
senior = 6
if age >= 65:
    print("Ticket price for senior is: ", senior)
elif age >= 13:
    print("Ticket price for adult's is: ",adult)
else:
    print("Ticket price for child is: ", child)


#Drill 4: Largest of three
#Given three numbers, a, b and c, 
# print the largest. Don’t use max(). 
# Test: (3, 9, 5), (9, 3, 5), (5, 3, 9), (4, 4, 2).

a = 4
b = 4
c = 2

# if a > b and a > c:
#     print(a," is largest!")
# elif b > a and b > c:
#     print(b, " is largest!")
# elif a == b and b == a and a > c and b > c:
#     print("a: ", a, " b: ", b, " are equals and are greater thn c: ", c)
# else:
#     print(c, " is largest")

if a >= b and a >= c:
    print("a",a)
elif b >= c:
    print("b",b)
else:
    print("c",c)