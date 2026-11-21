# LeetCode 977: Squares of a Sorted Array (Easy)
# Given a list sorted smallest to biggest (it can have negatives), return the squares, also sorted.
# Why sort again: squaring changes the order (-4 -> 16 is bigger than 3 -> 9).
# Plan: square every number with a comprehension, then sort.
# Time O(n log n) (sorted costs n log n, the comprehension is n); space O(n) (a new list of n items).

def sortedSquares(a):
    sots = [x**2 for x in a]
    return sorted(sots)

assert sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
assert sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
assert sortedSquares([5]) == [25]
print("all passed")
