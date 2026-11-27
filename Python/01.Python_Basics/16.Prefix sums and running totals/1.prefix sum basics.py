a = [1,2,3,4,5,6,7]

total = 0

prefix = []

for x in a:
    total = total + x
    prefix.append(total)

print(prefix) # [1, 3, 6, 10, 15, 21, 28] # Days [1,2,3,4,5,6,7]

# sum of the numbers at positions 2 to 5

# Days 1 to 4:

answer = prefix[3] #0-3 is day 4 
# if starting day is 1, so answer will come through right -1( where starting day is left
#  and ending day is right) so here right is 4 and 4-1 = 3 thats why answer = prefix[3] 
answer = prefix[3]
print("Day 1 to 4: ",answer)

# in other all cases prefix [right -1] - prefix[left-2]
answer = prefix[5] - prefix[3-2]
print("Day 3 to 6: ",answer)



answer = prefix[-1] - prefix[3] 
print("Day 5 to 7: ",answer)



# range_sum: takes 3 input,  list to convert to prefix, and left right values for days

def range_sum(prefix, left, right):
    if left == 1:
        return prefix[right-1]
    else:
        return prefix[right-1]-prefix[left-2]
print(range_sum(prefix, 1,4))

assert range_sum(prefix, 1, 4) == 10
assert range_sum(prefix, 3, 6) == 18
assert range_sum(prefix, 5, 7) == 18
assert range_sum(prefix, 4, 4) ==  4

# [3, 1, 4, 1, 5]

b = [3, 1, 4, 1, 5]

total = 0
pref = []

for x in b:
    total = total + x
    pref.append(total)

print(pref) # [3, 4, 8, 9, 14]

"""Days 1 to 3
Days 2 to 5
Days 1 to 5
Days 4 to 4
Days 3 to 5"""

day1_3 = pref[3-1]
print("Days 1 to 3: ",day1_3)

day2_5 = pref[5-1] - pref[2-2] 
print("Days 2 to 5: ",day2_5)

day1_5 = pref[5-1]
print("Days 1 to 5: ",day1_5)

day4_4 = pref[4-1]-pref[4-2]
print("Days 4 to 4: ", day4_4)

day3_5 = pref[5-1]-pref[3-2]
print("Days 3 to 5: ",day3_5)


nums = [1, -1, 2, -2, 3, -3]

total = 0
count = 0

for x in nums:
    total = total + x
    if total == 0:
        count +=1

print(count)