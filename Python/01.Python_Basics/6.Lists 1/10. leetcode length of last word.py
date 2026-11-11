"""
return the length of the last word. A word is a run of characters with no spaces in it.

For example:

"Hello World" → 5
" fly me to the moon " → 4
"luffy is still joyboy" → 6

"""

#words = "   fly me   to   the moon  "

def lengthOfLastWord(n):

    list_of_words = n.split()
    
    return len(list_of_words[-1])

print(lengthOfLastWord("my name is iqra and i am data engineer"))


assert lengthOfLastWord("Hello World") == 5
assert lengthOfLastWord("   fly me   to   the moon  ") == 4
assert lengthOfLastWord("luffy is still joyboy") == 6


