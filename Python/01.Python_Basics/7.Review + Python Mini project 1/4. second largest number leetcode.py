"""
Second Largest (Part 6), interviewer style:

“I’ll give you a list of integers. Return the second largest value.

[5, 9, 2, 7] → 7
[4, 4, 3] → 3 (duplicates of the largest don’t count as second)

"""
# a = [5, 9, 2, 7]
# b = sorted(a, reverse= True)



def second_largest(a):
    b = sorted(a, reverse=True)
    c = []
    for num in b:
        if num not in c:
            c.append(num)
    if len(c) <=1:
        return None
    return c[1]

    

print(second_largest([5,6,7,8]))

assert second_largest([5, 9, 2, 7]) == 7
assert second_largest([4, 4, 3]) == 3
assert second_largest([4, 4, 4]) == None
assert second_largest([]) is None
assert second_largest([5]) is None



    

