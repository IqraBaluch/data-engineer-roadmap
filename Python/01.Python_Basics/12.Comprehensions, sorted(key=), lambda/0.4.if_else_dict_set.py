# COMPREHENSIONS, part 2: if/else, dictionary, set
# Pattern: [ what to give back  for item in list  if which to keep ]

# 1. A filter if goes at the END: it keeps SOME items (the list gets shorter)
nums = [1, 2, 3, 4]
print("kept (>2):", [x for x in nums if x > 2])

# 2. An if/else goes at the START: it changes EVERY item (same length)
#    [ A if condition else B  for item in list ]
print("labels:", ["big" if x > 2 else "small" for x in nums])
print("even/odd:", ["even" if x % 2 == 0 else "odd" for x in nums])

# 3. Change AND filter together: the if decides who stays, the expression changes who stays
print("even squares:", [x * x for x in [1, 2, 3, 4, 5, 6] if x % 2 == 0])

# 4. Dictionary comprehension: { key: value for item in list }  (it has a colon)
words = ["sun", "moon", "sky"]
print("word -> length:", {w: len(w) for w in words})

# 5. Set comprehension: { value for item in list }  (no colon, removes duplicates)
print("unique lengths:", {len(w) for w in ["ab", "cd", "efg", "hi"]})

# 6. Mistakes I made (so I do not repeat them):
#    - name before brackets:  doubled[x * 2 for x in a]   -> needs  doubled = [x * 2 for x in a]
#    - using x in the expression but w in the loop       -> use the SAME name
#    - giving back w when the task asked for len(w)
#    - x % 3 == 0 is "divisible by 3", odd is x % 2 != 0
#    - {len(w) for ...} has no colon, so it is a SET, not a dictionary

# MY OWN: a comprehension is ______.
