"""

"""
#1. Dictionary basic

ages = {"ali": 20, "sara": 25}
print(ages["ali"]) # 20
print(ages["sara"]) # 25
print(len(ages)) # 2

#2. change a dictionary

    # add a new key
ages['omar'] = 33

print(ages)

#3. change an existing key's value" ali = 25
ages["ali"]=25

print(ages)

#4. check key is in dictionary

print("sara" in ages) #True

print("iqra" in ages) # False

#print(ages["zoya"])    # what happens? (key error, bcs key is missing)

#4. ask safely with .get

"""

A crash for a missing key is annoying. 
.get asks the dictionary without crashing,
and lets you choose what to get back if the key isn’t there:

"""

print(ages.get("ali")) # prints value if available
print(ages.get("zoya")) # prints None if no value available
print(ages.get("iqra",0)) #prints 0 as default if no value available, else will print the value of key



