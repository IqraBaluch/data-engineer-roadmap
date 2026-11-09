"""
1: Sum 1 to n
Write a function sum_to_n(n) that returns the sum of the numbers 1 to n.

sum_to_n(4) gives 10
sum_to_n(1) gives 1

"""
a = []
def sum_to_n(n):
    for i in range(1,n+1):
        #print(i)
        a.append(i)

       
sum_to_n(4)
#sum_to_n(1)
#print("list", a)
print(sum(a))


def sum_to_n(n):
    for i in range(1,n+1):
        i = i + i
    return i
# Drill 2: Multiplication table

#Print the 7 times table from 7 × 1 to 7 × 10, one line each, like 7 x 1 = 7.
print("While loop method")
i = 1
while i != 11:
    print(7, "x", i , "=", 7*i)
    i+=1

print("For loop mathod")
for i in range(1,11):
    print(7, "x", i , "=", 7*i)
    

# Drill 3: Count vowels
"""Write count_vowels(text) that returns the number of vowels in a string.

count_vowels("education") gives 5
count_vowels("xyz") gives 0"""
# counter = 0
# def count_vowels(text):
#     vowels = 'aeiouAEIOU'
#     for i in count_vowels(text):
#         print(i)
#         if i in vowels:
#             print(i)
#             counter +=1
#     return counter
# print(count_vowels("education"))
# num = 0            
# def sum_to_n(n=4):
#     for i in range(1,n+1):
#         num+= 1
#         i = i +num
# sum_to_n()
# n = 4
# num = 0
# for i in range(1,n+1):
#         print(i)
#         num += i
#         i = num + i
# print("num",num)


# num = 0
def sum_to_n(n):
        num = 0
        for i in range(1,n+1):
                num += i

        return num
print(sum_to_n(4))
print(sum_to_n(1))

#using assert we test to see if function works the way we are expecting
assert sum_to_n(4) == 10
assert sum_to_n(1) == 1

# 2. count wovels
counter = 0
a = "aeiouAEIOU"
word = "education"
for i in word:
    if i in a:
            print(i)
            counter += 1
print(counter)

# def count_vowels(word):
#        counter = 0
#        wovels = 'aeiouAEIOU'
#        for i in word:
#               if i in wovels:
#                     counter += 1
#         return counter
# print("check",count_vowels("Education"))



def vowel_counter(word):

    vowel = 'aeiouAEIOU'
    counter = 0
    for char in word:
          if char in vowel:
                counter += 1
    return counter

                      
assert vowel_counter("Education") == 5
assert vowel_counter("xyz") == 0

# Drill 3: Fictorial 
n = 5
factorial = 1
for i in range(1, n+1):
      factorial *= i
      
print("factorial",factorial)

def factorial(n):
    fact = 1
    for i in range(1, n+1):
          fact *= i
    return fact

assert factorial(3) == 6
assert factorial(4) == 24

# Drill 4: “Write a function that takes a number and returns the sum of its digits.”

def sum_of_digits(m):
    num1 = m % 10
    #print("first iteration:",num1)

    val1 = m // 10
    #print("value 1:", val1)

    num2 =  val1 % 10
    #print("second iteration:", num2)

    val2 = val1 // 10
    #print("value 2:", val2)

    num3 = val2 % 10
    #print("third iteration:",num3)

    val3 = val2 //10
    #print("value 3:", val3)

    num4 = val3 % 10
    #print("forth iteration:", num4)

    val4 = val3 // 10
    #print("value 4:", val4)

    return num1+num2+num3+num4

# lets do the same more efficiently using loop


n = 2
while n > 0:
     print(n)
     n -= 1


def sum_of_digits(m):
    total = 0
    while m > 0:

        digit = m % 10
        total += digit
        m = m // 10
    return total
     

    
assert sum_of_digits(12) == 3
assert sum_of_digits(12345) == 15
assert sum_of_digits(0) == 0



# Drill 5: “Write a program that prints the numbers from 1 to 30. For multiples of 3 print ‘Fizz’, 
# for multiples of 5 print ‘Buzz’, and for multiples of both print ‘FizzBuzz’.”

def FizzBuzz(i):
    for i in range(1,31):
        if i % 3 == 0 and i % 5 == 0:
            #print("FizzBuzz")
            return "FizzBuzz"
        elif i % 3 == 0:
            #print("Fizz")
            return "Fizz"
        elif i % 5 == 0:
            #print("Buzz")
            return "Buzz"
        else:
            return i
    
# Drill 6: “Write a function that checks whether a number is prime.”

# n = 9
# for num in range(2,n):
#     if n % num == 0:
#         print("Not prime")
#     else:
#         print("Prime")
    
def is_prime(a):
    if a < 2:
         return False
        
    for num in range(2,a):
        if a % num == 0:
            return False
    
    return True

#print(is_prime(3))

assert is_prime(7) == True
assert is_prime(9) == False
assert is_prime(2) == True
assert is_prime(1) == False
assert is_prime(0) == False

# Drill 7: “Write a program that prints a triangle of stars with 4 rows:
#  one star on the first row, two on the second, and so on.”
# def star_triangle(n=4):
#     for i in range(1,n):
#         print("printing star:",i)
#         return ("*"*i)

    
# print(star_triangle(4))
def star_triangle(times):
    for i in range(times+1):
        print("*"*i)
star_triangle(0)



