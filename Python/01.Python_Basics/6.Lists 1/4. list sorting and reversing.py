"""
The two ways to sort:

nums.sort() changes the list and returns None. (Like append: don’t write nums = nums.sort().)
sorted(nums) returns a new sorted list and leaves nums alone.

"""

num = [44,76,23,8,1,45,89,2,3]

print(sorted(num)) # [1, 2, 3, 8, 23, 44, 45, 76, 89]
print(num.sort()) # None

b = num.sort()
print(b) # None

# reverse the list

reverse_sort = sorted(num, reverse=True)
print(reverse_sort) # [89, 76, 45, 44, 23, 8, 3, 2, 1]