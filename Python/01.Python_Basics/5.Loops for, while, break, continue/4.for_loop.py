# Step 1: why loops?

#Suppose you want to print “Hello” 3 times. You could write:
print("Hello")
print("Hello")
print("Hello")

"""
For 100 times, you’d rather not copy and paste 100 lines, the same way you didn’t 
want to copy the name-cleaning lines on Day 4. A loop repeats code for you:
"""
for i in range(1,4): # 4 is exclusive
    print(i)
    print("Hello printing 3 times using loop")

for i in range(3):
    print("iteration number: ", i)
    print("Hy")



"""
The parts:

Part	         Meaning
for     	     “repeat for each item”
i	             a variable that holds the current number (you choose the name)
range(3)	      the numbers 0, 1, 2 (three numbers, starting at 0)
:	              starts the body, like if
indented line	  the code that repeats

"""

# for loop uses a python function range 

for i in range(1,11): 
    """assume we have values from 1-10. 1,2,3,4-----10. and using loop on evey 
    #iteration we are printing 1 value. and range is basically gener
    # ating these numbers
    # and loop is giving it to print and print is displaying it"""
    print(i)

# we can also add a step size or jump
print("print values with ther jump of 2")
for i in range(1,11,2):
    print(i)

# if you need number in decending manner
for i in range(10,0,-1):
    print(i)

# we have already used [in] in string
print("i" in "iqra") #True

# example: current population of area is 10000, and it increases 10% every year. 
# calculate population from

population = 10000


#starting from current year, which will be 10th year, thats why reverse range(10,0,-1)
for year in range(10,0,-1):
    print(year, population)
    population = population - 0.1*population


# population incrase by 10% every year
pop = 4241
for year in range(1,11):
    print(year, pop)
    pop = pop + 0.1*pop


# looping over a string. 
# A for loop can go through the characters of a string directly, with no range at all:

for ch in("Data"):
    print(ch)
# ch takes each character in turn. Now combine it with a counter:
counter = 0

for ch in("Data"):
    print(ch)
    counter += 1
print(counter)
