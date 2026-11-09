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
counter = 0
def count_vowels(text):
    vowels = 'aeiouAEIOU'
    for i in count_vowels(text):
        print(i)
        if i in vowels:
            print(i)
            counter +=1
    return counter
print(count_vowels("education"))
num = 0            
def sum_to_n(n=4):
    for i in range(1,n+1):
        num+= 1
        i = i +num
sum_to_n()
n = 4
num = 0
for i in range(1,n+1):
        print(i)
        num += i
        i = num + i
print("num",num)


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

n = 123

while n ==  0:
    
          

