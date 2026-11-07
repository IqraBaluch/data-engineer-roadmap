"""
Goal: turn a full name into initials.

"Iqra Anwar" → I.A.

"""

name = "iqra anwar"

# upper case or title both will work
name = name.upper()

#split so that string converts to list
words = name.split()
print(words)

# indexing to fetch the 1st later of first word
a =words[0][0]

# indexing to fetch the 1st later of second word
i = words[1][0]

#print using f string
print(f"{a}.{i}.")
