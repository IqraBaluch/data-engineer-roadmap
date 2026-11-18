


# first_repeated

def first_repeated(a):
    seen = {}
    for num in range(len(a)):
        
        if a[num] in seen:
            return a[num]
            
        seen[a[num]]=num

# print(first_repeated([1, 2, 3, 2, 1]))
assert first_repeated([1, 2, 3, 2, 1]) == 2
assert first_repeated(["a", "b", "a"]) == "a"
assert first_repeated([1, 2, 3]) is None
assert first_repeated([]) is None

