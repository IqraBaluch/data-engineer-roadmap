# Break and continue: These two give you control inside a loop.

# 1: break stops the loop immediately:

for i in range(5):
    if i ==3:
        break
    print(i)

for i in range(1,10):
    if i == 4:
        # Output: 1, 2, 3. When i reaches 4, the loop ends, and 4 isn’t printed.
        break
    print(i)