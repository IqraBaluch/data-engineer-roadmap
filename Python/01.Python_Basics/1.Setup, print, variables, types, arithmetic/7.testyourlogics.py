"""
Do these in order. Predict the answer before you run each one:

Print your name and age on two lines.
Convert 36.6 Celsius to Fahrenheit. The formula is c * 9 / 5 + 32.
A rectangle with width 7 and height 4: print its area and perimeter.
Get the last digit and the tens digit of 8472. Hint: the last digit uses % 10. For the tens digit, use // 10 first, then % 10.
Predict, then check: 7 // 2, -7 // 2, -7 % 3, 2 ** 10, 10 / 4, 10 // 4.

"""

#1. Print your name and age on two lines.
name = 'Ali'
age = 18
print("My name is ", name, ".")
print("I am ", age, " years old.")

# 2. Convert 36.6 Celsius to Fahrenheit. The formula is c * 9 / 5 + 32.
celsius = 36.6 
Fahrenheit = celsius * 9 / 5 + 32

print("Fahrenheit is: ",Fahrenheit)

# 3. A rectangle with width 7 and height 4: print its area and perimeter.

w = 7
h = 4
a = w*h
p = 2*(w+h)
print("The area of the rectanle is: ", a)
print("The perimeter of the rectanle is: ", p)

"""
Get the last digit and the tens digit of 8472.
Hint: the last digit uses % 10. For the tens digit, use // 10 first, then % 10.

"""

print(8472 % 10)

print(8472 // 10)

tense = 8472 //10
print("Tense: ",tense%10)



# Predict, then check: 7 // 2, -7 // 2, -7 % 3, 2 ** 10, 10 / 4, 10 // 4.
print(7//2) # 3
print(-7//2) # -4
print(-7%3) # 2
print(2**10) # 1024
print(10/4) # 2.5
print(10//4) # 2
print(-10 % 3)

print("TEST THE BELOW")
print(-7 // 2)
print(-7 % 3)
print(-10 // 3)
print(-10 % 3)
print(2 + 3 * 4 ** 2)
x = 29 
print(x // 10, x % 10)