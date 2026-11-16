"""

Given a list nums, return the smallest index i such that i % 10 == nums[i].
If there is no such index, return -1.

🔎 Examples
Input	Output	Why
[0, 1, 2]	0	index 0: 0 % 10 = 0, equals nums[0]
[4, 3, 2, 1]	2	index 2: 2 % 10 = 2, equals nums[2]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	-1	no index matches
"""


# def smallestEqual(nums):

#     for i,num in enumerate(nums):
#         if (num % 10) == num:
#             return i

# print(smallestEqual([4, 3, 2, 1]))



def smallestEqual(num):
    for i,n in enumerate(num):
        if (i%10)==n:
            return i
    return -1
print(smallestEqual([5]))
assert smallestEqual([0, 1, 2]) == 0
assert smallestEqual([4, 3, 2, 1]) == 2
assert smallestEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == -1
assert smallestEqual([1, 7, 2]) == 2
assert smallestEqual([0]) == 0
assert smallestEqual([5]) == -1


"""

🟢 LEETCODE Q2 : #905

Title: Sort Array By Parity
Difficulty: Easy
Tools: loop, if, list append

📋 The question

Given a list nums of integers, put all the even numbers first, then all the odd numbers. 
Return any list that works.

🔎 Examples
Input	A valid output
[3, 1, 2, 4]	[2, 4, 3, 1] ([4, 2, 1, 3] is valid too)
[0]	[0]

📏 Constraints
1 to 5000 items
each item is 0 to 5000

"""



# 2 % == 0 [append even_odds list]
# if num 

def sortArrayByParity(numbers):
    even = []
    odd = []
    for num in numbers:
        # even = []
        # odd = []
        if num % 2 == 0:
            even.append(num)
        if num % 2 !=0:
            odd.append(num)

    return even+odd

print(sortArrayByParity([0]))

assert sortArrayByParity([3, 1, 2, 4]) == [2, 4, 3, 1]
assert sortArrayByParity([0]) == [0]
assert sortArrayByParity([2, 4, 6]) == [2, 4, 6]
assert sortArrayByParity([1, 3, 5]) == [1, 3, 5]
assert sortArrayByParity([1, 2]) == [2, 1]
assert sortArrayByParity([2, 1]) == [2, 1]
assert sortArrayByParity([5, 2, 7, 4]) == [2, 4, 5, 7]