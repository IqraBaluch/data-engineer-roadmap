# Joining, searching, methods

# joining
print("data" + "bricks")
print("iqra" * 3)

#searching
print("data" in "big data engineer")

""" Methods
Methods are built-in actions on a string. 
They return a new string, and the original doesn’t change:
"""

print("============= String Methods ===========")
word = " Hello! , world "
print("without Strip method")
print(word)
# Mehod 1: Strip (removes spaces at both ends)
print("With method!")
print(word.strip())

# Method 2: lower() : 
print(word.strip().lower())

# Method 3: upper()
print(word.strip().upper())

# Method 4: replace()
print("Hello world".replace("world", "Iqra!"))

# Method 5: split() -> (string → list)
print("a,b,c".split(","))

# Method 6: join() -> (list → string)
print(",".join(['a', 'b', 'c']))
print(type(",".join(['a', 'b', 'c'])))

# Method 7: count() 
print('banana'.count('a'))
print("data engineer".count('e'))

# Method 8: find() -> (position of the first match; -1 if not found)
print("data engineer".find('r'))
print("data engineer".find('y'))

# Method 9: startswith() / endswith() -> True/False
print("helo".startswith('he')) #True
print("helo".endswith('he')) # False
print("helo".endswith('o')) #True

# Method 10: isalpha/isdigit -> True/False
print("123".isdigit())
print("123".isalpha())
print("abcd".isalpha())