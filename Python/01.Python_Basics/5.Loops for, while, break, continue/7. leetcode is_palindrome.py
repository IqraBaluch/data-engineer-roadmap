"""
A nested loop is a loop inside another loop. For every single round of the outer loop, 
the inner loop runs completely.

The clock analogy: the minute hand goes round fully (0 to 59) for every one step of the hour hand.
Hours are the outer loop and minutes are the inner loop.

A small example:

for i in range(1, 4):          # outer: 1, 2, 3
    for j in range(1, 3):      # inner: 1, 2
        print(i, j)


"""

# example: 1

for i in range(1,4): # 1,2,3
    #for j in range(1,3):# 1,2
        print(i)
for j in range(1,3):
     print(j)
# 1,1,2
# 2, 1,2
# 3,1,2

def star_triangle_nested(rows):
    for i in range(rows):
        for j in range(i):
            print("*", end = " ")
        print()
star_triangle_nested(4)


# Improved version

# rows = 5
# for i in range(rows): # ist iteration = 1 || second iteration = 2
#     #print("*"*i)
#     for j in range(i): #1st iteration = 1,2 || second iteration = do not run
#         print("*", end = "")
#     print("")

def star_triangle_nested(rows):
    for i in range(1,rows+1):
        for j in range(i):
            print("*", end= "")
        print()
star_triangle_nested(4)     # 4 rows: 1, 2, 3, 4 stars, no blank line on top
star_triangle_nested(1)     # one *
star_triangle_nested(0)     # nothing


# time complexity = linear O(n square) bcs of the nested loop, 
# # space complexity = O(1) bcs  we are just printing and not storing anything

# problem 2: “Find the first number between 1 and 100 that is divisible by both 7 and 5.”

for num in range(1,101):
     if num % 7 == 0 and num % 5 == 0:
          print("Divisible by 7 and 5:",num)
          break

def first_multiple(a):

     for i in range(1, a+1):
          if i % 7 == 0 and i % 5 == 0:
               return i


assert first_multiple(100) == 35
assert first_multiple(34) == None      # none in 1..34


# “Given an integer, return True if it reads the same forwards and backwards, and False otherwise.”

# a = '121'
# if a[::-1] == a:
#      print(True)
# else:
#      print(False)

def is_palindrome(a):
     a = str(a)
     if a[::-1] == a:
          return True
     else:
          return False

print(is_palindrome(121))
assert is_palindrome(121) == True
assert is_palindrome(123) == False
assert is_palindrome(-121) == False
assert is_palindrome(10) == False
          