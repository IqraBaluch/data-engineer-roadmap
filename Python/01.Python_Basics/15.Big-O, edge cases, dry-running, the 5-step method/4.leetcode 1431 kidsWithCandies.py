# LeetCode 1431: Kids With the Greatest Number of Candies
# Idea: find the greatest once; for each kid, candies + extra >= the greatest gives True.
# Time: O(n), max() is one pass and the loop is one pass (they add)
# Space: O(n), the result list has one True or False per kid

a = [1,5,2]
extra = 3
maximum = max(a)


result = []

for i in a:
    data  = i + extra
    # print(i,data, maximum)
    # print()
    if data > maximum:
        result.append(True)
    else:
        result.append(False)
print(result)

def kidsWithCandies(a,extra):
    if len(a) == 0:
        return []
    result = []
    maximum = max(a)


    for i in a:
        if i + extra >= maximum:
            result.append(True)
        else:
            result.append(False)
    return result

print(kidsWithCandies([2,3,5,1,3],3))
assert kidsWithCandies([2,3,5,1,3],3) == [True, True, True, False, True]
assert kidsWithCandies([1],3) == [True]
assert kidsWithCandies([],3) == []