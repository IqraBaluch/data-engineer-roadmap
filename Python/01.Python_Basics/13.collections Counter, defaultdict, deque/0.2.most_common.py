from collections import Counter

a = Counter(['a','a', 'b', 'a', 'b', 'c', 'd', 'a', 'c', 'd', 'e'])

print(a.most_common(1))
print(a.most_common(2))


from collections import Counter

def singleNumber(nums):
    counts = Counter(nums)
    for key, value in counts.items():
        if value == 1:
            return key