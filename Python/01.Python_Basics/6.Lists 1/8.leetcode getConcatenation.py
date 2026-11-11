"""

you are given a list of integers, build and give back a new list 
that contains the original list twice, one copy right after the other.

 [1, 2, 1], you give me back [1, 2, 1, 1, 2, 1].
"""

n =  [1, 2, 1]
m = []
for num in n:
    m.append(num)

print(m+m)

# convert it into function
def getConcatenation(n):
    m = []
    for num in n:
        m.append(num)
    return m+m

assert getConcatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1]
assert getConcatenation([]) == []