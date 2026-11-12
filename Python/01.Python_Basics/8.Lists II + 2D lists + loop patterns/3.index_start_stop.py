
"""slices (taking a piece).
names[start:stop] takes boxes from start up to, but not including, stop:
"""
names = ["Sara"  "Ali"  "Noor"  "Zain"]
names[1:3]    # ["Ali", "Noor"]       positions 1 and 2 (3 is excluded)
names[0:2]    # ["Sara", "Ali"]
names[2:]     # ["Noor", "Zain"]      from position 2 to the end
names[:2]     # ["Sara", "Ali"]       from the start up to (not including) 2


# A slice gives a new list. The original stays the same.
names[0:3] # ["Sara", "Ali", "Noor"]
names[1:] # ["Ali", "Noor", "Zain"]
names[:1] # ["Sara"] (a list holding one name)
names[1:2] # ["Ali"] (also a list)