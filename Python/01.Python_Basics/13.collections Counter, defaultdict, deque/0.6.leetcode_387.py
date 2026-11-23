# 387. First Unique Character in a String
# Time: O(n) because Counter reads the string once and the loop goes through the dictionary once.
# Space: O(1) because once a key is added a repeat only updates its value,
#   and there are only 26 lowercase letters, so at most 26 keys.
# Level 3: logic was mine, final polish (Counter + s.index) came with a small hint.

# ====== version 1: my own logic (passes all my asserts) ======
from collections import Counter

def count(a):
    return Counter(a)

def firstUniqChar(s):
    if s == "":
        return -1
    s = list(s)

    first_unique = count(s)

    for i, j in first_unique.items():
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


# ====== version 2: LeetCode Accepted (107/107, 22 Nov 2026) ======
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)

        for letter, n in counts.items():
            if n == 1:
                return s.index(letter)
        return -1
