# loops work directly on lists

# example 1: print whatver is in the list without one by one printing the items

num = [1,4,6,7]

for i in num:
    print(i)

# Example2: print index and values using loop
for i in range(len(num)):
    print("index",i, "Value",num[i])


# example 3: Aliasing: copying lists

a = [1,2,3,4]
b = a # # b is NOT a copy: both names point to the SAME list
b.append(5)

print(a) #[1, 2, 3, 4, 5]
print(b) # [1, 2, 3, 4, 5]
"""
b = a doesn’t copy the list. 
It gives the same list a second name. Change it through either name, and both see the change.

"""

# example 4: make a real, independent copy
a = [1,2,3,4]
b = a[:] # slicing and including everything a has
print(b) # [1, 2, 3, 4]
b.append(9) 
print(b)#[1, 2, 3, 4, 5]
print(a) # #[1, 2, 3, 4]

# list method: list.copy(): (a.copy() does the same thing.)

c = b.copy()
print(c) # [1, 2, 3, 4, 9]
c.append(77)
print(c) # [1, 2, 3, 4, 9, 77]