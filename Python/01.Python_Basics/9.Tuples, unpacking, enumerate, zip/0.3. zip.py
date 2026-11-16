# zip pairs items from two lists that go together

names = ["ali", "sara", "omar"]
marks = [70, 85, 60]

for name, mark in zip(names,marks):
    print(name,mark)

for n,m in zip(names, marks):
    if m > 65:
        print(n,m)

# a function can return a tuple. You can return two values at once, and unpack them when you call it:
def min_max(a):
    return min(a), max(a)

result = min_max([4, 9, 1])
print(result)         # (1, 9)
print(type(result))   # <class 'tuple'>

"""
write first_last(a) that returns the first and last items of a list. Call it on [7, 8, 9],
unpack into two variables, and print both with labels,
 like First: 7. Send me the code and the output.

"""
# a = [7,8,9]
def first_last(a):
    First = a[0]
    Last = a[-1] 
    return First, Last
First, Last = first_last([7,8,9])
print("First:",First, "Last:",Last)