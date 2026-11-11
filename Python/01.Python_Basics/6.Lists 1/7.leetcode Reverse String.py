
 #344 Reverse String: reverse the list of characters in place, so no new list, and return nothing.
#["h","e","l","l","o"] → ["o","l","l","e","h"].


def reverseString(n):
    for i in range(len(n)//2):
        n[i], n[-1 -i] = n[-1 -i], n[i]

n = ["h","e","l","l","o"]
reverseString(n)
print(n)