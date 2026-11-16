# sort vs sorted

# .sort(): sorts the list ITSELF, returns None
x = [5, 2, 9]
z = x.sort()
print("x after sort:", x)      # [2, 5, 9]
print("z:", z)                 # None

# sorted(): makes a NEW sorted list, original stays the same
a = [5, 2, 9]
b = sorted(a)
print("a:", a)                 # [5, 2, 9]
print("b:", b)                 # [2, 5, 9]

# biggest first: reverse=True (capital T)
c = sorted(a, reverse=True)
print("c:", c)                 # [9, 5, 2]

# Rule: .sort() changes the list. sorted() gives a new list.


a = [1, 2, 3, 6]
total = 0
val = 0
above_avg = 0
below_avg = 0

for num in a:
    total = total + num
    val = val + 1
    avrg = total//val
    print(num < avrg)
    if num < avrg:
        below_avg = below_avg + 1




        
# print("AVERAGE:",avrg)
# print("ABOVE AVG:", above_avg)
print("BELOW AVG:", below_avg)




