# Two ways to loop, and they answer different questions

nums = [5, 15, 20, 40]
for a in nums:
    print(a)

for a in range(len(nums)):
    print("index",a, "value",nums[a])

"""
Rule of thumb:

Need only the values (sum, count, max)? → loop by value.
Need the position too (swap, compare neighbours, change items)? → loop by index.

"""

nums = [5, 15, 20, 40]

val = 0
for n in nums:
    val = val+n
print(val)


for a in range(len(nums)):
    nums[a] = nums[a] + nums[a]

print(nums)

