# a = [1,2,3,1,2,3,4]
# b = [2,3,2,3,4,5]

# a =  set(a)
# b = set(b)
# print(a)
# print(b)
# data = set()
# for i in a:
#     for j in b:
#         if i not in data and j not in data:
#             data.add(i)
#             data.add(j)
            

# print(data)


# def intersection(a,b):
#     a =  set(a)
#     b = set(b)
#     # print(a)
#     # print(b)
#     data = []

#     for i in a:
#         for j in b:
#             if (i in b and j in a) and (i not in data and j not in data):
#                 data.append(i)
#     return data
# print(intersection([1, 2, 2, 1], [2, 2]))

def intersection(a, b):
    a = set(a)
    b = set(b)
    data = []
    for i in a:
        if i in b:
            data.append(i)
    return data

assert sorted(intersection([1, 2, 2, 1], [2, 2])) == [2]
assert sorted(intersection([4, 9, 5], [9, 4, 9, 8, 4])) == [4, 9]
assert intersection([1, 2], [3, 4]) == []
assert intersection([], [1]) == []