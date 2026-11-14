"""
LeetCode #1672 Richest Customer Wealth. accounts[i][j] is the money customer i has in bank j. Return the wealth of the richest customer, where wealth = the sum of that customer’s money across all banks.

[[1, 2, 3], [3, 2, 1]] → 6
[[1, 5], [7, 3], [3, 5]] → 10

"""

f = [[1, 5, 3], [3, 2, 1]]
#print(f[1])


def the_rich(k):

    richer = 0
    for customer in k:
        wealth = sum(customer)
        if wealth > richer:
            richer = wealth
    return richer

print(the_rich([[1, 2, 3], [3, 2, 1]]))

print(the_rich([[1, 5], [7, 3], [3, 5]]))


"""
Given a list of integers nums, return how many of them have an even number of digits.

[12, 345, 2, 6, 7896] → 2 (12 and 7896)
[555, 901, 482, 1771] → 1 (only 1771)

"""

a = [12, 345, 2, 6, 7896]

a = [12, 345, 2, 6, 7896]

# Using map()
result = list(map(str, a))

# Or using list comprehension
result = [str(x) for x in a]
print(result)
# Output: ['12', '345', '2', '6', '7896']

print(type(result))

for val in result:
    if len(val) % 2 ==0:
        print(val)


def anynegativenumber(a):
    flag = False
    for num in a:
        if num < 0:
            flag = True
            break
    return flag

print(anynegativenumber([1,3,4,5,6,5]))

"""

LeetCode #485 Max Consecutive Ones. Given a list nums of 0s and 1s, return the longest run of consecutive 1s.

[1, 1, 0, 1, 1, 1] → 3
[1, 0, 1, 1, 0, 1] → 2
"""


def consecutive(lis):
    current = 0
    max_consec = 0
    for num in lis:

        if num == 1:
            current += 1
            if current > max_consec:
                max_consec = current
        if num <1:
            current = 0

        
    return max_consec

print(consecutive([1, 1, 1]))
print(consecutive([1, 1, 1, 0, 1, 0, 1]))
print(consecutive([0,1,1,1,1,0,1,1,1,1,1,1,1,1,1]))
print(consecutive([0,0,0]))
       

"""LeetCode #66 Plus One. A non-negative integer is stored as a list of digits, most significant digit first. Add one to it and return the digits as a list.

[1, 2, 3] → [1, 2, 4]
[9] → [1, 0]
[1, 9, 9] → [2, 0, 0]

"""
b =  [1, 2, 11]
# for b[-1] in b:
#     print(b[-1])

#print(b[-1]+1) # 4
b =  [1, 2, 9]

def plusOne(digit):
    for i in range(len(digit)-1, -1, -1):
        if digit[i] < 9:
            digit[i] = digit[i] +1
            break
        else:
            digit[i] = 0
    else:
        digit.insert(0,1)
    return(digit)
print("PLUS ONE")
print(plusOne([9,9,9]))
print(plusOne([1, 2, 3]))
print(plusOne([1, 0]))
print(plusOne([1, 9, 9]))