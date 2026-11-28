# a = [1,2,3,1,1,1]
# # for i in range(len(a)):
# #     leftsum = sum(a[:i])
# #     # print(leftsum)
# #     rightsum = sum(a[i+1:])
# # print(i)

"""
===== COMPEXITY ======

Time: sum slices inside the loop is O(n squared) for time
Space: space complexity is O(1) as it stays constant and we are only returning index value of -1
"""
    
class Solution:

    def pivotIndex(self, nums):

        for i in range(len(nums)):
            leftsum = sum(nums[:i])
            rightsum = sum(nums[i+1:])

            if leftsum == rightsum:
                return i 
        return -1

print(Solution().pivotIndex(([1,2,3,1,1,1])))
assert Solution().pivotIndex([1,2,3,1,1,1]) == 2
assert Solution().pivotIndex([]) == -1
assert Solution().pivotIndex([2,2,2]) == 1
assert Solution().pivotIndex([2,2,2,2]) == -1