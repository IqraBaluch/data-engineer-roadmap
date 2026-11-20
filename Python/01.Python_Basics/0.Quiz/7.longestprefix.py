def longestCommonPrefix(a):
    for i in range(len(a[0])):
        for word in a:
            if word[i] != a[0][i]:
                return a[0][:i]
    return a[0]

assert longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
assert longestCommonPrefix(["dog", "racecar", "car"]) == ""
assert longestCommonPrefix(["a"]) == "a"
assert longestCommonPrefix(["ab", "a"]) == "a"