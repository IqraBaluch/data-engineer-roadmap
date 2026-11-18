# loop over a dictionary

ages = {"ali": 21, "sara": 25, "omar": 30}

#only prints keys
for names in ages:
    print(names)


#only values
for name in ages.values():
    print(name)

#both key and valu
for names, age in ages.items():
    print(names,age)

for key,value in ages.items():
    print(key,value)


"""
write loop, so that it prints:
ali is 21
sara is 25
omar is 30

"""
for n,a in ages.items():
    print(f"{n} is {a}")