#1. A while loop runs as long as a condition is True: 
# 
# ptint a table using while loop

table = int(input("Enter a number: "))

i = 1
while i < 11:
    print(table, "*", i, "=", table*i)
    i+=1

# 2. n = 3

n = 3


while n > 0:
    print(n)
    n -= 1
    """
    The key line is n -= 1, which changes n so that the condition eventually becomes False. 
    Without it, n stays 3 and the loop never stops. That’s an infinite loop.
    
    """
    # 3
    # 2
    # 1
    # 0
print("Go!")