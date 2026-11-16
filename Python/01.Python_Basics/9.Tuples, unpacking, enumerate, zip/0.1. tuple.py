# tuples are like lists but are immutable

t = (4, 5, 6)
print(t[1])
print(len(t))
#t[0] = 9 # gives typeerror

# Step 2: unpacking. A tuple can be split into separate variables in one line:
point = (5,6)
x,y = 5,6
print(x)
print(y)
print(point)