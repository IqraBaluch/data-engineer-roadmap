# An if runs code only when a condition is True:

"""
Two rules you must follow:

1: A colon : ends the if, elif and else lines.
2: The code inside is indented by 4 spaces.
That indentation tells Python what belongs to the if. There are no { } as in other languages.

"""


# example 1: if

"""
Read it as a sentence: if age is at least 18, print “You can vote”.

The comparison age >= 18 gives True or False.
If it’s True, the indented line runs.
If it’s False, Python skips it and prints nothing.


Notice two details:

- The if line ends with a colon.
- The print line is indented by 4 spaces. You can press Tab in VS Code.

"""


age = 15

if age >= 18:
    print("You meet the age criteria")


# example 2: else

# What if you want something to print when the condition is False? Use else:


age = 18

if age >= 18:
    print("You can vote")
else:
    print("Too young to vote")


"""

elif means “else, if this other thing is true”. 
Python checks conditions from top to bottom and runs only the first one that is True:

"""

# example 3: elif
"""
Order matters. If you put score >= 60 first, 
then 95 would print C, because that condition is true and Python
stops there. Check the strictest condition first.

"""
score = 75
if score >= 90:
    print("A")
elif score >= 75:
    print("B")
elif score >= 60:
    print("C")
else:
    print("D")

# example 4: : Combine conditions with and / or

"""

and: both sides must be True.
or: at least one side must be True.
not: flips True ↔ False.

"""

age = 20
has_ticket = True


if age >= 18 and has_ticket:
    print("Enter")
else:
    print("Stop")


# example 5: ==

"""
Common mistake: day == "Saturday" or "Sunday" looks right, 
but it doesn’t work.
Write the full comparison on each side of or.

"""
day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("Weekend")

# example 6: login page

email = 'iqra12@gmail.com'
pw = "1234"

e = input("Enter your email to log in to the system")
p = input("Enter your password")

if e == email and p == pw:
    print("Succesfully Logged in...")
elif e == email and p != pw:
    print("Incorrecte pass word. Try again...")
    p = input("Enter your password again")
    if p == pw:
        print("Succesfully Logged in...")
    else:
        print("Incorrect pw again...")
else:
    print("Incorrect credentials!")

