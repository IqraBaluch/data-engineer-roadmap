


#containsDuplicate

# a = [1,2,3,4,5,1,3,4,5,6]
# seen = set()

# for i in a:
#     if i not in seen:
#         seen.add(i)
#     else:
#         print("Duplicate", i)
#         break

def containsDuplicate(a):
    seen = set()

    for i in a:
        if i not in seen:
            seen.add(i)
            
        else:
            return True 
    return False

assert containsDuplicate([1, 2, 3, 1]) == True
assert containsDuplicate([1, 2, 3, 4]) == False
assert containsDuplicate([]) == False
assert containsDuplicate([5, 5]) == True