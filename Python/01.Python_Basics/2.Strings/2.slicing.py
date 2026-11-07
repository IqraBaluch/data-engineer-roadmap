# Slicing picks a piece with [start:stop]. 
# It includes start but stops before stop: 

word = "Python"

# pyt   (positions 0, 1, 2)
print(word[0:3])

# ytho
print(word[1:5])

# py
print(word[0:2])

# thon
print(word[2:5])

# hon 
print(word[3:6])

#  nohtyp , reverse the string using slicing
print(word[::-1])


# YOUR TEST 

"""
Quick check (no running code)
python
s = "data"
s[1]
s[-1]
s[1:3]
s[::-1]
len("data engineer") (the space counts)
"""