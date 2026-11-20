"""a = [7,5,2,6,7,8]

def twosum(a,target):
    twosum_dictionary = {}

    for i in range(len(a)):
        value = target - a[i]
        if value in twosum_dictionary:
            return [twosum_dictionary[value],i]
            
        twosum_dictionary[a[i]] = i
    #print(twosum_dictionary)
   
assert twosum([2, 7, 11, 15], 9) == [0, 1]
assert twosum([3, 2, 4], 6) == [1, 2]
assert twosum([3, 3], 6) == [0, 1]
assert twosum([-1, 5, 8], 7) == [0, 2]




# two sum"""

a = [2,7,8,99]
target = 9
def twoSum(a,target):
    seen = {}
    for i in range(len(a)):

        partner_val = target - a[i]
        if partner_val not in seen:
            seen[a[i]] = i
        else:
            return [seen[partner_val],i]
        
assert twoSum([2, 7, 11, 15], 9) == [0, 1]
assert twoSum([3, 2, 4], 6) == [1, 2]
assert twoSum([3, 3], 6) == [0, 1]
assert twoSum([-1, 5, 8], 7) == [0, 2]


s = 'MCMXCIV'
value = {
    "I": 1, "V": 5, "X": 10, "L": 50,
    "C": 100, "D": 500, "M": 1000
}
total = 0
for i in range(len(s)):

    if i+ 1 < len(s) and value[s[i]] < value[s[i+1]]:
        total -= value[s[i]] 
    else:
        total += value[s[i]] 
print(total)


s = "anagram"
t = "nagaram"


         

# data = {}
# def isAnagram(s,t):

#     for i in s and t:
#         for j in s and t:
#             return True
#         else:
#             return False

# assert isAnagram("anagram", "nagaram") == True
# assert isAnagram("rat", "car") == False
# assert isAnagram("listen", "silent") == True
# assert isAnagram("aab", "aba") == True
# assert isAnagram("aab", "abb") == False
# assert isAnagram("ab", "a") == False
# assert isAnagram("a", "a") == True
# assert isAnagram("abc", "cba") == True

# print("All tests passed!")

# a = "anagram"
# b = "nagaram"



