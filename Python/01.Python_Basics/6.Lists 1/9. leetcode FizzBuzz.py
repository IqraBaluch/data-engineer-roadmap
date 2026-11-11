"""

write a function that takes a number n and returns a list of strings, 
one for each number from 1 to n.

If the number is divisible by 3, the string is "Fizz".
If it’s divisible by 5, the string is "Buzz".
If it’s divisible by both, the string is "FizzBuzz".
Otherwise, the string is the number itself, as text.

For n = 5, I’d expect ["1","2","Fizz","4","Buzz"].

"""
n = 20

data = []
for num in range(1,n):
    if num % 3 == 0 and num % 5 == 0:
        data.append("FizzBuzz")
    elif num % 5 == 0:
        data.append("Buzz")
    elif num % 3 == 0:
        data.append("Fizz")
    else:
        data.append(num)
print(data)

# convert it to function
def fizzBuzz(n):
    data = []
    for num in range(1,n+1):
        if num % 3 == 0 and num % 5 == 0:
            data.append("FizzBuzz")
        elif num % 5 == 0:
            data.append("Buzz")
        elif num % 3 == 0:
            data.append("Fizz")
        
        else:
            data.append(str(num))
    return data


print(fizzBuzz(5))

assert fizzBuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]