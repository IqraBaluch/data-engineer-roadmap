# Two tools with similar names, and a trap:

a = [2,3,5,1]
b = sorted(a)
print(b) # [1, 2, 3, 5]
print(a) #  [2,3,5,1]

x = [4, 2, 9]
y = sorted(x)
x.sort(reverse=True)
z = x.sort()

# print(x)
# print(y)
# print(z)


# the largest number

nums =  [4, 9, 2, 7]


nums = [4, 9, 2, 7]

best = nums[0]
best_index = 0          # position of the first item

for i in range(len(nums)):
    if nums[i] > best:
        best = nums[i]
        best_index = i  # remember the position too

print("Value", best, "index", best_index)