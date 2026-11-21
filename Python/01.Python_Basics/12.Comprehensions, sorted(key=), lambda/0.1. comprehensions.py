# COMPREHENSIONS: notes as code
# Pattern: [ what to give back  for item in list  if which to keep ]
# A comprehension builds a new list in one line.

# 1. The long loop and the one-liner give the same result
squares = []
for n in [1, 2, 3, 4]:
    squares.append(n * n)
print("loop:", squares)
print("one line:", [n * n for n in [1, 2, 3, 4]])

# 2. Change every item
a = [1, 2, 3]
print("doubled:", [x * 2 for x in a])

# 3. Any expression works, e.g. the length of each word
print("lengths:", [len(w) for w in ["ab", "cde", "f"]])

# 4. Add an if to keep only some items
print("even:", [x for x in [1, 2, 3, 4, 5, 6] if x % 2 == 0])

# 5. When NOT to use one: if the loop needs break or an early return
#    (Two Sum, #14), keep it as a loop

# MY OWN: a comprehension is __

# 6. if / else INSIDE the expression (it goes BEFORE the for)
#    [ A if condition else B  for item in list ]
nums = [1, 2, 3, 4]
print("labels:", ["even" if x % 2 == 0 else "odd" for x in nums])

# 7. Comprehension over range
print("squares 0 to 4:", [i * i for i in range(5)])

# 8. Comprehension over a string
print("letters upper:", [c.upper() for c in "abc"])

# 9. Dictionary comprehension: { key: value for item in list }
words = ["sun", "moon", "sky"]
print("lengths:", {w: len(w) for w in words})

# 10. Set comprehension: { expression for item in list }
print("unique lengths:", {len(w) for w in ["ab", "cd", "efg"]})

# 11. The filter if goes at the END, the if/else goes at the START