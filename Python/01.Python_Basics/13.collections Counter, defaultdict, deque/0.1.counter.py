from collections import Counter

a = ['a','a', 'b', 'a', 'b', 'c', 'd', 'a', 'c', 'd', 'e']

c = Counter(a)
print(c)

print(c['a'])
print(c['z'])

def count(a):
    return Counter(a)

print(count(['a','a', 'b', 'a', 'b', 'c', 'd', 'a', 'c', 'd', 'e']))


# def firstUniqChar(s):
    
#     s = list(s)

#     first_unique = count(s)

#     for i in range(len(first_unique)):
#         print(i)
#         if j == 1:
#             return i
# print(firstUniqChar("leetcode"))

# assert firstUniqChar("leetcode") == 0
# assert firstUniqChar("loveleetcode") == 2
# assert firstUniqChar("aabb") == -1
# assert firstUniqChar("z") == 0
# assert firstUniqChar("") == -1


s = 'leetcode'
def firstUniqChar(s):
    if s == "":
        return -1
    # s = list(s)

    # first_unique = count(s)
    # print(first_unique)

    for i,j in s.items():
        print(i,j)
        if j == 1:
            val = i
            for i in range(len(s)):
                if s[i] == val:
                    return i
    return -1



assert firstUniqChar("leetcode") == 0
assert firstUniqChar("loveleetcode") == 2
assert firstUniqChar("aabb") == -1
assert firstUniqChar("z") == 0
assert firstUniqChar("") == -1