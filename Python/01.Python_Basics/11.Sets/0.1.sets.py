"""
SET: a set is a collection with no duplicates.

"""
# SETS: notes as code

# 1. A set keeps only unique items (duplicates disappear)
a = [1, 2, 2, 3, 3, 3]
print("set of a:", set(a))
print("length of the set:", len(set(a)))

# 2. add() puts in a new item; adding an item that is already there changes nothing
s = {1, 2, 3}
s.add(2)
s.add(5)
print("after add:", s)

# 3. in checks if an item is there (about 1 step, like a dictionary key)
print("2 in s:", 2 in s)
print("9 in s:", 9 in s)

# 4. remove() deletes an item on purpose
s.remove(2)
print("after remove:", s)

# 5. A set has no positions, so s[0] gives TypeError (do not run it)
# print(s[0])

# 6. Order does not matter: same items means equal sets
print("equal sets:", {1, 2, 3} == {3, 2, 1, 1})

# 7. A list can have duplicates, a set can't: compare the lengths
b = [3, 1, 3, 2, 1]
print("has a duplicate:", len(set(b)) != len(b))

# 8. An empty set is set(); {} would be an empty dictionary
empty = set()
print("empty set:", empty, "| empty dict:", {})