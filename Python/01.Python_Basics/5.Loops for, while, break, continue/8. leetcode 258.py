# “Given a non-negative integer num, repeatedly add all its digits until the result has only one digit, and return it.”

# Example: num = 38 → 3 + 8 = 11 → 1 + 1 = 2, so you return 2.

def add_digits(num):
    while num >= 10:

        total = 0
        while num > 0:# after second iteration the condition becomes fales and inner loop stops

            digit = num % 10 # last digit
            total = total + digit
            # first iteration value of digit will be 7
            

            # second iteration value of digit will be 7+8 = 15
        

            # remove the last digit from the number 
            num = num // 10
            # first iteration removes 7 # and value of num will be 8
            # second iteration removes 8  # and value of num will  be 0
        num = total # outer loop will check if digit has 2 value
        # and num's value will be updated with the latest value of total
    return num



assert add_digits(38) == 2
assert add_digits(999) == 9
assert add_digits(55) == 1
assert add_digits(0) == 0
assert add_digits(5) == 5