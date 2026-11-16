"""
enumerate: for ["a", "b", "c"], print each item as 0: a, 1: b, 2: c.
zip: for names = ["ali", "sara"] and ages = [20, 25], print ali is 20, sara is 25.
Function min_max(a) that returns the smallest and largest.
Unpack the result for [4, 9, 1] and print Min: 1, Max: 9. No min() or max(): use a loop.

"""

alpha = ["a", "b", "c"]

for i, char in enumerate(alpha):
    print(f"{i}: {char}")

names = ["ali", "sara"]
ages = [20, 25]

for n,a in zip(names, ages):
    print(f"{n} is {a}")


c = [4, 9, 1]
# min = 0
# max = 0
# for num in c:
#     if num > min and num > max:
#         max = num
#     elif num > min and num < max:
#         min = num
# print(min,max)




def min_max(c):
    if len(c) == 0:
        return None, None
    min_num = c[0]
    max_num = c[0]
    for num in c:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
        

    return min_num,max_num
min_num,max_num = min_max([2,3])
print("Min:",min_num,"Max:",max_num)
assert min_max([4, 9, 1]) == (1, 9)
assert min_max([5]) == (5, 5)
assert min_max([3, 3, 3]) == (3, 3)
assert min_max([-2, -7, 0]) == (-7, 0)
assert min_max([9, 4, 1]) == (1, 9)
assert min_max([1, 4, 9]) == (1, 9)
assert min_max([]) == (None, None)

"""
enumerate: for [3, 9, 4], find the index of the largest item.
Print Index: 1. No max() or .index(): use a loop with enumerate.

zip: for names = ["ali", "sara"] and scores = [70, 85], build a list of pairs: [("ali", 70), ("sara", 85)]. Use a loop and append, then print the list.


Unpack in a loop: with pairs = [("ali", 70), ("sara", 85)], write for name, score in pairs: and print ali scored 70, sara scored 85."""


# index or largest number

# num_list =  [3, 9, 4]
# max_num = num_list[0]
# for i,n in enumerate(num_list):
#     if n > max_num:
#         max_num = n
# print(i)

# build a list of pairs
data = []
names = ["ali", "sara"]
scores = [70, 85]

for n,s in zip(names,scores):
    data.append((n,s))

print(data)

# unpacking

pairs = [("ali", 70), ("sara", 85)]

for std_name, std_marks in pairs:
    print(std_name,"scored", std_marks)



num_list =  [4, 3, 2, 1]
max_num = num_list[0]
for num in num_list:
    if num > max_num:
        max_num = num
for i,nums in enumerate(num_list):
    if nums == max_num:
        print(i)

"""

zip to compare two lists

📋 The question

Write a function count_matches(a, b) that counts how many positions have the same value in both lists. 
Use zip. Return the count (don’t print inside).

"""

# a1 = [1, 5, 3]	
# b1 = [1, 2, 3]

# def count_matches(a1, b1):
#     counter = 0
#     for a,b in zip(a1,b1):
#         if a != b:
#             return 0
#         if a == b:
#             counter += 1
#     return counter

# print(count_matches([1, 5, 3], [1, 5, 4]))

# assert count_matches([1, 5, 3], [1, 2, 3]) == 2
# assert count_matches([4, 4], [5, 6]) == 0
# assert count_matches([7], [7]) == 1
# assert count_matches([], []) == 0

a1 = [1, 5, 3]
b1 = [1, 5, 4]

def count_matches(a1,b1):
    counter = 0
    for a,b in zip(a1,b1):
        if a == b:
            counter += 1

    return counter
print(count_matches([1, 5, 3], [1, 2, 3]))
assert count_matches([1, 5, 3], [1, 2, 3]) == 2
assert count_matches([4, 4], [5, 6]) == 0
assert count_matches([7], [7]) == 1
assert count_matches([], []) == 0