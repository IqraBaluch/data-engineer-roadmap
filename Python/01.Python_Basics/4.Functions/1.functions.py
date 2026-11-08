"""What is a function?

A function is a reusable block of code with a name that does one specific job.

Without a function, you copy the same lines every time. With one, you write them once 
and call the name whenever you need them.

Think of a coffee machine. You press the button (call it) and 
get coffee (the result). You don’t rebuild the machine each time.

"""

# 1. Defining and calling

def greet():
    print("Hello! wellcome to python.")

greet() # Hello! wellcome to python.
greet() # Hello! wellcome to python.
"""

Part      	Meaning
def     	“I’m defining a function”
greet	    the name you choose
()	        brackets for inputs (empty here)
:	        starts the body

indented lines	the code that belongs to the function

Defining only saves the function. It runs when you call it with greet()

"""

# 2. Parameters: giving it inputs 

def greet(name):
    # name is the parameter, the empty slot in the definition.
    print("Hello!",name)

# "Iqra" is the argument, the actual value you put in when calling.
greet("Iqra")


# 3. Multiple parameters

def add(a,b):
    result = a + b
    print(result)

#The arguments go in order: a gets 10 and b gets 20.
add(10,20)

# 4. return: the important one

"""print() shows something on the screen. return hands 
the value back to the code that called the function, so you can use it again."""

def add_number(a,b):
    # print = show it to me. 
    # return = give it back so I can keep working with it.
    return a + b
total = add_number(3,6)
## we can keep using it
final = total * 2
print(final)

# A function that only prints can’t be reused in later calculations, 
# but one that returns can. Most real data functions return.

# 5. A data example

def calculate_average(prices_list):
    total = sum(prices_list)
    average = total / len(prices_list)
    return average
avg = calculate_average([150, 250])
print(avg)


def adds(a,b):
    print(a+b)

print("check",adds(5,4))


#5 calculate total

def calculate_total(a,b):
    return a + b
sum =  calculate_total(150, 250)
print(sum)

#6 square(n): returns n times n. Call it with 7.

def square(n):
    return n * n
square = square(7)
print(square)

# 7 is_even(n): returns True if n is even 
# and False otherwise. Call it with 10 and 7.

def is_even(n):
    return n % 2 == 0

a = is_even(10)
b = is_even(7)
print(a)
print(b)


#8 clean_name(name): returns the name after strip, 
# lower and title. Call it with " iQRA anWAR ".

def clean_name(name):
    stripped = name.strip()
    return stripped.title()

n = clean_name(" iQRA anWAR ")
print(n)

#9 default parameters

def greet(name = "friend"):
    return "Hello! "+ name

name = greet("Iqra")
print(name) # Hello! Iqra
#A default value is what the parameter gets when you don’t pass one.
print(greet()) # Hello! friend


# 10
# Drills. Use return, with no print inside the functions.

#greet_user(name, greeting="Hello") returns something like "Hello, Iqra!". 
# Call it with just a name, then with "Welcome" as the second argument.

def greet_user(name, greeting = "Hello"):
    return greeting + ", " + name

print(greet_user("Iqra"))

print(greet_user("Wellcome!"))

# 11 get_initials(full_name) returns the initials in capitals. 
# "iqra anwar" gives "IA". You did this on Day 2, so now it’s a function.

def initials_generator(name="iqra anwar"):
    name = name.upper()
    name = name.split()
    return name[0][0] + name[1][0]

print(initials_generator())

# 12 get_discount_price(price, discount=10) returns the price after a percentage discount. 
# With 200 and the default 10%, it gives 180.0. Call it with the default and with 25.

def get_discount_price(price, discoun=10):
    discount_amount = price * discoun / 100
    return price - discount_amount

print(get_discount_price(200))
print(get_discount_price(200,25))

# 13 grade(score) returns "A" for 90 or above, "B" for 70 or above, and "C" otherwise. 
# Call it with 95, 75 and 40. This is Day 3 inside a function, and remember the order.

def grade(score):
    if score >= 90:
        return "A"
    elif score >= 70:
        return "B"
    else:
        return "C"
print(grade(95))
print(grade(75))
print(grade(40))

def get_discount_price(price, discount=10):
    return price - price * discount / 100

print(get_discount_price(200, 25))            # by position
print(get_discount_price(price=200, discount=25))   # by keyword
print(get_discount_price(discount=25, price=200))   # order doesn't matter now



"""

Rule of thumb:

A function can read outer variables.
Assigning to a name inside a function creates a local variable.
Local variables disappear when the function ends.

"""

def show():
    print(y)

y = 5
show()

def make_local():
    z = 7

make_local()
print(z)