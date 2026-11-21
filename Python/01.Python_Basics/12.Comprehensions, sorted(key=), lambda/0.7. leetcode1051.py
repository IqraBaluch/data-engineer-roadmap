

# sorted_heights = sorted(heights)

# print(sorted_heights)


def heightChecker(heights):
    counter = 0
    s = [x for x in heights]
    s=sorted(s)
    for h,s in zip(heights,s):
        if h != s:
            counter +=1
    return counter
print(heightChecker([1, 1, 4, 2, 1, 3]))

assert heightChecker([1, 1, 4, 2, 1, 3]) == 3
assert heightChecker([5, 1, 2, 3, 4]) == 5
assert heightChecker([1, 2, 3, 4, 5]) == 0
assert heightChecker([1]) == 0