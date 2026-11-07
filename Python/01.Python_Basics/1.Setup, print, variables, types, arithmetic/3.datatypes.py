"""
Every value has a type:

Type	Example	        Meaning
int	       42 	        whole number
float     3.14	        decimal number
str	     "hello"	    text
bool	 True, False	yes or no

"""

print(type(42))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("42"))      # <class 'str'>  (quotes make it text!)


#"42" and 42 are different things. The first is text and the second is a number.

# Converting:
print("--------Converting between types--------")
a = int("42")      # 42
b = str(42)        # "42"
c = float("3.5")   # 3.5
d = int(7.9)       # 7  (cuts off the decimal, does not round)


print(a, type(a), b, type(b), c, type(c), d, type(d))

# A very common first error:


print("Age: " +25) #  TypeError: can't join text and a number

print("Age: "+str(25)) #works