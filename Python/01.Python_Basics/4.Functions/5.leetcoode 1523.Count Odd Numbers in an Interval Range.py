"""
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).


Example 1:

Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].

Example 2:
Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].
 

"""

def countOdds(low,high):
    low = ((low-1)+1)//2
    high = (high+1)//2

    return high - low
#     # count of odd number btwn low and high (3,7) = 3
#     if low % 3 == 0:

# high = 10
# low = 8
# print((high+1)//2)
# #((low - 1) + 1) // 2
# print(((low-1) +1)//2)
print(countOdds(3,7))

