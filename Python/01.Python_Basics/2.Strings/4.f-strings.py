"""
f-string is a string literal with an f prefix. 
Python evaluates anything inside the curly braces as an expression 
and puts the result into the text. Use them instead of + or .format() 
because they’re shorter, easier to read, 
and you don’t have to convert numbers with str(). 
They also support formatting, like f"{price:.2f}" 
for two decimal places.

Basically: f-strings put values inside text. Write f before the quotes and use {}:

"""

name = "Iqra"
print(f"Hello, {name}")
print("Total:",{3*6})