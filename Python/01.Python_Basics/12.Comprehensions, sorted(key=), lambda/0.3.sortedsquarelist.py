a = [-4, -1, 0, 3, 10] # [0, 1, 9, 16, 100]
# data = []
# for i in a:
#     # print(i)
#     b = i**2
#     print(b)
#     data.append(b)


data = [x**2 for x in a]
print(sorted(data))