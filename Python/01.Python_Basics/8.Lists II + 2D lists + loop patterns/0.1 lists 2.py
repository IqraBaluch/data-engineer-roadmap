marks = [

[50,70,90], 
[67,77,99], # [1][2] == 90
[99,56,88]

]

print(marks[1][2]) # [1][2] == 90

print("rows:",len(marks)) # 3: bcs it has 3 rows

print("COLUMN:",len(marks[0]))
print(len(marks[1]))


# rint row 1 and print column 2
print("ROW 1:", marks[1])

# for row in marks:
#     col = []
#     col.append(row[2])
#     print(col)

col = []
for r in range(len(marks)):
    print(r, marks[r])

"""# loop

for row in marks:
    print(row)

for row in marks:
    for item in row:
        print(item)


for row in marks:
    print("items in this row:", len(row))"""


"""row sums. For each row, print its total:

text
Row 0 sum: 210
Row 1 sum: 243
Row 2 sum: 243"""


for r in range(len(marks)):
    rows = marks[r]
    total = 0
    for data in rows:
        total = total + data
    print("ROWS COUNT:",total)



for c in range(len(marks)):

    total1 =0
    for r in range(len(marks)):
    
        total1 = total1 + marks[r][c]

    print("Col no:",c,"COLUMNS total:", total1)
