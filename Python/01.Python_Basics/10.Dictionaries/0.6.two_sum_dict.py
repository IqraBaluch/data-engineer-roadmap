nums = [2, 7, 11, 15]
target = 9




# for num in range(len(nums)):
#     partner = target - nums[num]
#     if partner in seen:
#         print(partner,num)
#     else:
#         seen[nums[num]] = num
#     # if nums[num] == partner:

# print(seen)



def twosum(nums,target):
    seen = {}
    for num in range(len(nums)):
        partner = target - nums[num]
        if partner not in seen:
            seen[nums[num]] = num
            
        else:
            return [seen[partner], num]
            
        # if nums[num] == partner:

    
assert twosum([2, 7, 11, 15], 9) == [0, 1]
assert twosum([3, 2, 4], 6) == [1, 2]
assert twosum([3, 3], 6) == [0, 1]
assert twosum([-1, 5, 8], 7) == [0, 2]
print("all passed")
print(twosum( [2, 7, 11, 15],9))