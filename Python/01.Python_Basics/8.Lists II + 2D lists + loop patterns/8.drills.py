
"""

Given a 2D list, return the sum of all its items. Don’t use sum().

[[1, 2, 3], [4, 5, 6]] → 21
[[7]] → 7
[] → 0

"""
# a = [[2, 2, 3], [4, 5, 6]] 
a = [[]]
# add = 0
# for num in range(len(a)):
#     b = a[num]
#     for i in b:
#         add = add + i
# print(add)

def sumofall(a):
    adds = 0
    for num in range(len(a)):
        b = a[num]
        for i in b:
            adds = adds + i
    return adds
#print(sumofall(a))


"""
Given a square 2D list, return the sum of the main diagonal (top-left to bottom-right).

[[1, 2, 3], [4, 5, 6], [7, 8, 9]] → 15
[[7]] → 7

"""

b = [[1, 2], [3, 4]]
def totals(a):
    total = 0
    for i in range(len(a)):
        values = a[i][i]
        total = values + total
    return total

print(totals(b))

"""

Given a 2D list, return a new flat list with all items in order.

[[1, 2, 3], [4, 5, 6]] → [1, 2, 3, 4, 5, 6]
[[7], [8, 9]] → [7, 8, 9]
[] → []
"""

dc =[]

def list_merg(m):

    all_values = []
    for num in range(len(m)):

        vals = m[num]

        for j in vals:
            all_values.append(j)
    return all_values

print(list_merg(dc))


"""
Given a non-empty 2D list, print the largest value and its row and column.

[[3, 9, 2], [4, 1, 8]] → Value 9 row 0 col 1
[[5]] → Value 5 row 0 col 0

"""


h = [[5]]



def find_value_row_col(a):
    great = a[0][0]
    best_row = 0
    best_col = 0

    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] > great:
                great = a[i][j]
                best_row = i
                best_col = j

    return great, best_row, best_col


h = [[3, 9, 2], [4, 1, 8]]
val, row, col = find_value_row_col(h)
print("Value", val, "row", row, "col", col)


"""

Given a 1D list of numbers, return True if it’s sorted in increasing order (equal neighbors are allowed), 
otherwise False. Don’t use sorted() or sort().

[1, 2, 2, 5] → True
[3, 1, 2] → False
[7] → True
[] → True

"""



lst = [1,2,0,4]
is_sorted = True
for i in range(len(lst) - 1):

    if lst[i] > lst[i + 1]:
        is_sorted = False
        print(is_sorted)
        break
else:
    print(True)


def sort_list_or_unsorted(j):
    is_sorted = True
    for i in range(len(j)- 1):
        if j[i] > j[i+1]:
            is_sorted = False
            break
 
    return is_sorted

    

print(sort_list_or_unsorted([]))


# g = [[1, 2, 3], [4, 5, 6]]
# s = []
# for i in range(len(g)):
#     s.append(g[i][0])

# print(s)    


print("----===000=-=0=")

g = [[1, 2, 3], [4, 5, 6]]
result = []

for j in range(len(g[0])):
    s = []
    for i in range(len(g)):
        s.append(g[i][j])
    result.append(s)

print("check",result)

w = [[1, 2, 3], [4, 5, 6]]

def transpose(g):
    results = []

    for j in range(len(g[0])):
        s = []

        for i in range(len(g)):
            s.append(g[i][j])
        results.append(s)
    return results
print(transpose([[7]]))
        
