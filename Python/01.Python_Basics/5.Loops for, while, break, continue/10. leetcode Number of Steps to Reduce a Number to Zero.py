# Number of Steps to Reduce a Number to Zero
"""
“Given a non-negative integer num, return the number of steps to reduce it to zero. In one step, if the current number is even, you divide it by 2. Otherwise, you subtract 1 from it.”

Example: num = 14 → 14 → 7 → 6 → 3 → 2 → 1 → 0, so the answer is 6.

"""

n = 14
counter = 0
while n > 0:
    if n %  2 == 0:
        n = n //2
        counter = counter + 1
    else:
        n = n -1
        counter += 1
    

print(counter)

# lets turn it into function

def numberOfSteps(num):
    counter = 0
    while num > 0:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num - 1
        counter += 1
    return counter

print(numberOfSteps(15))