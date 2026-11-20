a = 'baa'
b = 'bab'

def isAnagram(s,t):
    a_dic = {}
    b_dic = {}
    for i in range(len(s)):
        a_dic[s[i]] = a_dic.get(s[i],0)+1

    for j in range(len(t)):
        b_dic[t[j]] = b_dic.get(t[j], 0)+1

    return a_dic == b_dic


# print(a_dic)
# print(b_dic)
# print(a_dic==b_dic)

assert isAnagram("anagram", "nagaram") == True
assert isAnagram("rat", "car") == False
assert isAnagram("listen", "silent") == True
assert isAnagram("aab", "aba") == True
assert isAnagram("aab", "abb") == False
assert isAnagram("ab", "a") == False
assert isAnagram("a", "a") == True
assert isAnagram("abc", "cba") == True

print("All tests passed!")