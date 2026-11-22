from collections import defaultdict

words = ["apple", "avocado", "banana", "blueberry", "cherry"]
groups = defaultdict(list)

for w in words:
    groups[w[0]].append(w)

print(groups)


nums = [1, 2, 3, 4, 5, 6, 7]
groups = defaultdict(list)

for i in nums:
    key = 'even' if i % 2 == 0 else 'odd'
    groups[key].append(i)
print(groups)
