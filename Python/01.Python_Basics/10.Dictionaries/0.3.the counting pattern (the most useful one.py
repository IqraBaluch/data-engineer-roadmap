# the counting pattern (the most useful one)
# This is where .get(key, 0) becomes powerful. We want to count how many times each item appears:

letters = ["a", "b", "a", "c", "a"]

counts = {}

for x in letters:
    counts[x] =  counts.get(x,0) + 1
print(counts)


# convert it into funciton
# def count_items(a):
#     counter = {}
#     for x in a:
#         counter[x] = counter.get(x,0) + 1
#     return counter
a = [1,2,1,3,4,1,3,5,2,1]


def count_items(a):

    counter = {}
    for x in a:
        if x in counter:
            counter[x] = counter[x] + 1
        else:
            counter[x] = 1
    return counter

assert count_items(["a", "b", "a"]) == {"a": 2, "b": 1}
assert count_items([5]) == {5: 1}
assert count_items([]) == {}
assert count_items([1, 1, 1]) == {1: 3}

seen = {2: 0, 7: 1, 11: 2}
print(7 in seen)
print(9 in seen)
print(seen[7])


seen = {}
partner = 0
number = [2,7,4,6,8,9]
target = 9

def twoSum(nums, target):
    seen = {}
    for i in range(len(nums)):
        number = nums[i]
        partner = target - number
        if partner in seen:
            return [seen[partner], i]
        seen[number] = i