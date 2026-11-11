"""
Input: a list of single characters, like ["h","e","l","l","o"].

Output: nothing is returned. You change the same list so its characters are in reverse order. After your function runs, the list reads ["o","l","l","e","h"].

Rules:

Do it in place. Don’t create a new list.
Don’t return anything.

Examples:

["h","e","l","l","o"] → the list becomes ["o","l","l","e","h"]
["H","a","n","n","a","h"] → the list becomes ["h","a","n","n","a","H"]

"""
a = ["h","e","l","l","o"]

def reverse_str(a):
    for i in range(len(a)//2):
        
        
        a[i], a[-1-i] = a[-1-i], a[i]
    return a






