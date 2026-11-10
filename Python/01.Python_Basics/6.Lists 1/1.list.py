# A list holds several values in one variable, in order:
fruits = ["apple", "banana", "cherry"]
"""

index	 index 0       index 1   	index 2
fruits	“apple”	       “banana”	    “cherry”

"""

print(fruits[0])
print(fruits[-1])
print(fruits[2])
print(fruits[1])
print(len(fruits))

"""
These work exactly like string indexing and slicing, which you already know
 The only thing that’s new is that a list can be changed in place:

"""

fruits[1] = 'Mango'

print(fruits)