"""Create 3.drills.py in 2.Strings. Write each one yourself, run it, and send me the file.

For word = "programming", print the first, last and middle character.
Reverse a string with [::-1].
Check whether "data" is inside a sentence and print True or False.
Replace the spaces in a sentence with -, then print it in title case (.title()).
Split a sentence and print its 3rd word.
Count how many times "a" appears, using .count().
Take " hello ", strip it, and print it with an f-string as Hello, <name>! (capitalise it with .capitalize()).
Predict first, then run to check: "abc" * 2, "hello"[1:4], "hello"[-3:], "a,b,c".split(","). Write your prediction in a # comment above each line."""

# 1: For word = "programming", print the first, last and middle character.
word = "programming"
mid_len = len(word) // 2
print(word[0],word[mid_len], word[-1])

# 2: Reverse a string
print(word[::-1])

# 3: Check whether "data" is inside a sentence and print True or False.
print("data" in "my name is Iqra and I am a data engineer")

# 4: Replace the spaces in a sentence with -, then print it in title case (.title()).
print("My name is Iqra".replace(" ", "-").title())

# 5: Split a sentence and print its 3rd word.
a = "My name is Iqra and im a data data engieer".split()
print("Third word is: ",a[2])


# 6: Count how many times "a" appears, using .count().
print("what a life it is to be able to do what you want to to do".count('a'))
# 7: Take " hello ", strip it, 
# and print it with an f-string as Hello, <name>! (capitalise it with .capitalize()).

name = " aLi "
name = name.strip().capitalize()
print(" hello,".strip().capitalize(), f"{name}!")

# 8: Predict first, then run to check: "abc" * 2, "hello"[1:4], "hello"[-3:]
#  "a,b,c".split(","). Write your prediction in a # comment above each line.

# 8.1: "abc" * 2 
print("abc"*2) ## abcabc

# 8.2: "0h1e2l3l4o"[1:4]
print("hello"[1:4]) #ell

# 8.3: hello"[-3:]
print("hello"[-3:]) #llo

# 8.4: "a,b,c".split(",")
print("a,b,c".split(",")) # ["a", "b", "c"]