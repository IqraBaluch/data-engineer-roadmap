#1480 Running Sum of 1d Array:

"""Given an array nums, return an array where each item is the sum of all items up to and 
including that position. [1,2,3,4] → [1,3,6,10]."""
numbers = [1,2,3,4]
sum_of_all = []
total = 0
for num in numbers:
    total =  num + total
    sum_of_all.append(total)
print(sum_of_all)


def add_all(numbers):
    sum_of_nums = []
    total = 0
    for num in numbers:
        total = num + total
        sum_of_nums.append(total)
    return sum_of_nums
print(add_all([1,2,3,4]))

