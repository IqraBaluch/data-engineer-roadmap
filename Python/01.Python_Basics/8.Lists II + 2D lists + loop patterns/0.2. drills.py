#3 rows and 4 columns, where every cell is 0

l = []

for a in range(3):
    row = []
    for b in range(4):
        row.append(0)
    l.append(row)
        
print(l)
# short cut

bad = [[0]*4]*3
print(bad)

# change one cell
bad[0][0] = 5
print(bad)

# 

l = []

for a in range(3):
    row = []
    for b in range(4):
        row.append(0)
    l.append(row)
l[0][0] =5
        
print(l)