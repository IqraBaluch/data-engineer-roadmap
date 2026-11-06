# Always read the last line first, then look at the line number above it.

# print(name) 

"""
Traceback (most recent call last):
  File "hello.py", line 3, in <module>
    print(name)
NameError: name 'name' is not defined

"""

"""
Types of error

1. NameError: you used a name/variable you never created (or misspelled it).
2. TypeError: you mixed types that don’t go together.
3. SyntaxError: something is written wrongly: a missing quote or bracket, or a typo.

Errors are normal and useful. They tell you exactly where the problem is.
"""


#TypeError: 
#print("5" + 5)

"""
Traceback (most recent call last):
  File "C:\Users\Iqraa\OneDrive\Documents\Data Engineer\Python\Basic\5.error_reading.py", line 25, in <module>
    print("5" + 5)
          ~~~~^~~
TypeError: can only concatenate str (not "int") to str

"""

# SyntaxError:

"""print("hello)

      print("hello)
          ^
SyntaxError: unterminated string literal (detected at line 38)"""