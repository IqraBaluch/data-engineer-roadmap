# 383. Ransom Note
# Idea (my words): ______
# Rule: if the magazine has LESS than the note needs, return False.
#   Return True only AFTER the loop, when no letter said "no".
# Time: O(n) because each Counter reads its string once; the loop goes through
#   the different letters of the note and each lookup is about 1 step.
# Space: O(1) because a Counter holds one key per different letter (a repeat only
#   updates the count) and there are only 26 lowercase letters.
# Level 2 to 3: solved with hints on the direction of the if and on return True after the loop.
#   Accepted 131/131 on 23 Nov 2026. Redo from blank on 26 Nov.
# Edge cases I thought about: empty note gives True (it needs no letters);
#   letter missing from the magazine gives 0 with Counter, so the check says False.

from collections import Counter


def canConstruct(ransom, magazine):
    ransom_note = Counter(ransom)
    magazine_data = Counter(magazine)

    for letter, need in ransom_note.items():
        if magazine_data[letter] < need:
            return False
    return True


assert canConstruct("aabbaa", "aaba") == False
assert canConstruct("", "aaba") == True
assert canConstruct("aba", "aab") == True
assert canConstruct("aaab", "ab") == False
assert canConstruct("hi", "hyi") == True


# LeetCode form (same logic)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_count = Counter(ransomNote)
        magazine_data = Counter(magazine)

        for letter, need in note_count.items():
            if magazine_data[letter] < need:
                return False
        return True
