## JUST A RANDOM quiz

### Rotate
a = [1,2,3,4]

def rotate(a):

    d = []
    for num in range(len(a)):
        d.insert(-1,a[num])
    return d

assert rotate([1, 2, 3, 4]) == [2, 3, 4, 1]
assert rotate([5]) == [5]
assert rotate([]) == []

# merg_2_lists

a = [1,2]
b = [1,3]
c = []

c.append(a)
c.append(b)
print("append",c)

def merg_2_lists(a,b):
    d = []
    for num in a:
        d.append(num)
    for num in b:
        d.append(num)
    return d

print(merg_2_lists([1,2,3,4,5,],[3,4,5,6,88]))

assert merg_2_lists([1,2],[3,4]) ==[1,2,3,4]
assert merg_2_lists([1,11],[22,2]) == [1,11,22,2]
assert merg_2_lists([],[1,2,3]) == [1,2,3]