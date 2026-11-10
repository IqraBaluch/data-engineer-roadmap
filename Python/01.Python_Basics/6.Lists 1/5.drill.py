# Question 1: “Write a function that returns the largest number in a list, without using max.”
"""
Examples:

[3, 9, 2] → 9
[-5, -1, -8] → -1"""

num = [3, 9, 2] 
max = 0
for i in (num):
    #
    if i > max:
        max = i
print(max)

# covert it into function
def max_val(n):
    max = n[0]
    for i in n:
        if i > max:
            max = i
    return max



print(max_val([-12,-56,-105]))

assert max_val([1,2,3]) == 3
assert max_val([11,202,3]) == 202
assert max_val([-11,-202,-3]) == -3


# Drill 2: “Write a function that returns how many even numbers are in a list.”

# Examples: [1, 2, 3, 4] → 2, and [] → 0.

n = [2,3,4,5,6,7,8,9,10]

for num in n:
    #print(num)
    even_count = 0
    if num % 2== 0:
        #print(num)
        even_count +=1
print(even_count)


m = [2,4]
counter = 0
for num in m:
    if num % 2 == 0:
        #print(num)
        counter+=1
print("Total evens in list:",counter)

def count_evens(m):
    counter = 0
    for num in m:
        if num % 2 ==0:
            counter += 1
    return counter

assert count_evens([1, 2, 3, 4]) == 2
assert count_evens([]) == 0
assert count_evens([-4, -3, 0]) == 2

# Drill 3: “Write a function that returns a reversed copy of a list, 
# without using reverse or slicing.”

#Example: [1, 2, 3] → [3, 2, 1].

# reverse = [10,20,30] 
# new_list = []
# for num in range(len(reverse)):

#     new_list.insert(0, reverse[num])
#     print("reverse[num]",reverse[num])
#     print(new_list)

# print(new_list)

# function 
def reverse_list(input):
    new_list = []
    for num in range(len(input)):
        new_list.insert(0, input[num])

    return new_list
print(reverse_list([1,2,3]))


assert reverse_list([1, 2, 3]) == [3, 2, 1]
assert reverse_list([]) == []
assert reverse_list([5]) == [5]


# Drill 4: “Write a function that returns the second largest number in a list.”

#Examples: [3, 9, 2] → 3, and 

# num = [5, 5, 1]
# num = sorted(num, reverse=True)
# print(num)
# if num[0] == num[1]:
#     print(num[2])
# else:
#     print(num[1])

def second_largest(number):
    ordered = sorted(number, reverse=True)
    largest = ordered[0]
    for num in ordered:
        if num != largest:
            return num
print(second_largest([5, 5, 5, 4]))

assert second_largest([3, 9, 2]) == 3
assert second_largest([5, 5, 1]) == 1
assert second_largest([5, 5, 5, 1]) == 1



# Drill 5: “Write a function that removes duplicates from a list, keeping the original order.”

#Example: [3, 1, 3, 2, 1] → [3, 1, 2]

number = [3, 1, 3, 2, 1]
dedups = []
for val in number:
    if val not in dedups:
        dedups.append(val)

print(dedups)

def deduplicates(number):
    dedup = []
    for val in number:
        if val not in dedup:
            dedup.append(val)
    return dedup
assert deduplicates([3, 1, 3, 2, 1]) == [3, 1, 2]
assert deduplicates([]) == []
assert deduplicates([5, 5, 5]) == [5]


# Drill 6:

#“Write a function that merges two lists into one, without using +.”

#Example: [1, 2] and [3, 4] → [1, 2, 3, 4].

list1 = [1,2]
list2 = [2,3]

list3 = []
for num in list1:
    list3.append(num)
for num in list2:
    list3.append(num)
    
print("NEW LIST",list3)

def merg_2_lists(a,b):
    list3 = []
    for num in a:
        list3.append(num)
    for num in b:
        list3.append(num)
        
    return list3
print(merg_2_lists([1,15],[44,99]))

# Drill 7:

# “Write a function that rotates a list one position to the left.”

# Example: [1, 2, 3, 4] → [2, 3, 4, 1].


list_1 = [1, 2, 3, 4] 
rotated_list = []
for num in range(len(list_1)):
    rotated_list.insert(-1,list_1[num])
print("rotated_list",rotated_list)

def rotate(list_1):
    rotated_list = []
    for num in range(len(list_1)):
        rotated_list.insert(-1,list_1[num])
    return rotated_list

assert rotate([1, 2, 3, 4]) == [2, 3, 4, 1]
assert rotate([5]) == [5]
assert rotate([]) == []

# Drill: 8
# Write a function that returns the sum and the average of a list, without using sum().

s = [1,2,3]

def sum_and_average(s):
    total = 0
    div = len(s)
    if len(s) == 0:
        return "There must be an item in the list"
    for num in s:

        #print(num)
        total = num + total
    
    return total, total / div
print(sum_and_average([]))
#assert sum_and_average([1, 2, 3]) == (6, 2.0)

