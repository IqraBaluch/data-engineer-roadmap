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


# lc # 14

def longestCommonPrefix(strs):
    """
for i in range(len(strs[0])): go through each position of the first word (0, 1, 2, ...). The first word is our guide, because the prefix has to be inside it.
for word in strs: at each position, look at every word, one at a time.
if i == len(word) or word[i] != strs[0][i]: stop if this word has run out of letters (so it can’t match), or if this word’s letter at position i is different from the guide’s letter.
return word[:i]: when we stop at position i, the positions before it all matched, so the answer is the letters before i.
return strs[0]: if the loops finish and nothing ever differed, the whole first word is the common prefix.

Trace for ["flower", "flow", "flight"]:

i = 0: all three have f, so no stop. i = 1: all have l, so no stop.
i = 2: flower has o and flow has o, but flight has i, which is different. So it returns "flight"[:2], which is "fl".
      
        """
    for i in range(len(strs[0])):
        for word in strs:
            if i == len(word) or word[i] != strs[0][i]:
                return word[:i]
    return strs[0]

assert longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
assert longestCommonPrefix(["dog", "racecar", "car"]) == ""
assert longestCommonPrefix(["dog"]) == "dog"
assert longestCommonPrefix(["flower", "flow"]) == "flow"




def twoSum(nums,targer):

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == targer:
                return [i,j]
print(twoSum([3, 2, 4], 6))



assert twoSum([2, 7, 11, 15], 9) == [0, 1]
assert twoSum([3, 2, 4], 6) == [1, 2]
assert twoSum([3, 3], 6) == [0, 1]
assert twoSum([1, 5, 3, 7], 10) == [2, 3]
assert twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]
assert twoSum([0, 4, 3, 0], 0) == [0, 3]