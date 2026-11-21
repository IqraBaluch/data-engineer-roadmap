# LeetCode 1051: Height Checker (Easy)
# Students should stand shortest to tallest. Count how many stand in the wrong place:
# the height differs from the height at the same position in the sorted line.
# Plan: sort a copy; walk both lists together with zip; if the two heights differ, count it; return the count.
# Time O(n log n) (sorted costs n log n, the zip loop is n); space O(n) (the sorted copy).

def heightChecker(heights):
    counter = 0
    sorted_h = sorted(heights)
    for h, s in zip(heights, sorted_h):
        if h != s:
            counter += 1
    return counter

assert heightChecker([1, 1, 4, 2, 1, 3]) == 3
assert heightChecker([5, 1, 2, 3, 4]) == 5
assert heightChecker([1, 2, 3, 4, 5]) == 0
assert heightChecker([1]) == 0
print("all passed")
