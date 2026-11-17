# LeetCode 1: Two Sum (brute force with pairs)
#
# Idea: try every pair of positions (i, j). The inner loop starts at i + 1,
# so no item is used twice and no pair is checked twice.
#
# Time:  O(n^2), because nested loops check every possible pair of numbers.
#        There are about n * n / 2 pairs and each check costs O(1).
# Space: O(1), because only i and j exist; nothing grows with the input.


def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


assert twoSum([2, 7, 11, 15], 9) == [0, 1]
assert twoSum([3, 2, 4], 6) == [1, 2]
assert twoSum([3, 3], 6) == [0, 1]
assert twoSum([1, 5, 3, 7], 10) == [2, 3]
assert twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]
assert twoSum([0, 4, 3, 0], 0) == [0, 3]
