# sorted() with key, and lambda

# 1. sorted() returns a NEW list; the original does not change
words = ["banana", "fig", "apple", "kiwi"]
print("alphabetical:", sorted(words))

# 2. key=len sorts by the LENGTH of each item (smallest first)
print("by length:", sorted(words, key=len))
print("longest first:", sorted(words, key=len, reverse=True))

# 3. lambda = a tiny function: input before the colon, output after it (no return)
f = lambda x: x * 2
print("f(5):", f(5), "| f(10):", f(10))

# 4. key=lambda: sort by what the lambda gives back; the list keeps the ORIGINAL items
print("by last letter:", sorted(words, key=lambda w: w[-1]))

# 5. key=abs sorts by size, ignoring the sign
nums = [-5, 3, -1, 4]
print("by value:", sorted(nums))
print("by size:", sorted(nums, key=abs))     # -5 is last: its size (5) is the biggest

# 6. Only ONE key= allowed in a call (two give a SyntaxError)
# 7. abs(-3) is 3: abs drops the minus sign (distance from zero)
print("abs:", abs(-3), abs(7), abs(0))
