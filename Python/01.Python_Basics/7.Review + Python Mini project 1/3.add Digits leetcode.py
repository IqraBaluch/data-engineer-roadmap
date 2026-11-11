"""I’ll give you a non-negative whole number, num. 
Take its digits and add them together.
If the result still has more than one digit, 
do the same thing again with the result. Keep going until you have a single digit. Return that digit.

Example 1: num = 38

Digits 3 and 8: 3 + 8 = 11
11 has two digits, so repeat: 1 + 1 = 2
2 is a single digit, so the answer is 2.

Example 2: num = 9875

9 + 8 + 7 + 5 = 29
2 + 9 = 11
1 + 1 = 2
The answer is 2.

Example 3: num = 0 → the answer is 0.
Example 4: num = 7 → already a single digit, so the answer is 7.

Method name: addDigits(self, num)."""

num = 67


while num >= 10:
    add_digits = 0
    #print("add_digits", add_digits)

    while num > 0:
        digit = num % 10
        add_digits = add_digits + digit
        num  = num // 10
    num = add_digits
    
print(add_digits)
   
        
        


 
  
