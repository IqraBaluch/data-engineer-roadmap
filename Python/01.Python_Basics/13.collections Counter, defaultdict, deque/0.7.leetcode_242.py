# 242. Valid Anagram
# Idea (my words): ______
# Time: O(n) because the more letters the string has, the more the loop has to go through.
# Space: O(1) because once a key is added it only gets updated, and there are only 26 letters.
# Level 3: solved alone, no hints. Accepted 56/56 on 22 Nov 2026 (manual version).
# My own test cases are the asserts at the bottom.

# ====== version 1 ======
def isAnagram(s,t):
    a_dic = {}
    b_dic = {}
    for i in range(len(s)):
        a_dic[s[i]] = a_dic.get(s[i],0)+1

    for j in range(len(t)):
        b_dic[t[j]] = b_dic.get(t[j], 0)+1

    return a_dic == b_dic



# === version 2 ====

from collections import Counter
def isAnagram(s, t):
    if type(s) != str or type(t) != str:
        return -1
    if Counter(s) == Counter(t):
        return True
    else:
        return False

assert isAnagram("silent", "listen") == True
assert isAnagram("silent", "silen") == False
assert isAnagram("", "") == True
assert isAnagram("rat", "car") == False
assert isAnagram(123, 333) == -1
assert isAnagram("123", "231") == True
assert isAnagram("aba", "aab") == True
assert isAnagram("aab", "bba") == False
