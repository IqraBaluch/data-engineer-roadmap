# Prefix sum template
# Use it when you must answer many range-sum queries on the same list.
# Build the prefix list once, then each query is two lookups.

# Build the prefix list: prefix[i] = sum of the first i + 1 numbers.
"""
==== COMPLEXITY ====
Time: O(n) because the loop runs n times
Space: O(n) because we create a list and store n running totals in it
"""
def build_prefix(nums):
    prefix = []
    b = 0
    for x in nums:
        b = b + x
        prefix.append(b)
    return prefix


# Range sum of days left to right (days count from 1).
"""
==== COMPLEXITY ====
Time: O(1) because a lookup by position is O(1): two lookups and one subtraction
Space: O(1) because nothing is created, only a number is returned
"""
def range_sum(prefix, left, right):
    if left == 1:
        return prefix[right - 1]
    else:
        return prefix[right - 1] - prefix[left - 2]


print(range_sum(build_prefix([5, 6, 7]), 2, 3))  # 13