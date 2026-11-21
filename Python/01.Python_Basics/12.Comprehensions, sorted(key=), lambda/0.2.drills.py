a = [3, 8, 5, 12, 7]
words = ["sun", "moon", "sky", "star"]

double = [x * 2 for x in a]
print("doubled:", double)

odds = [x for x in a if x % 2 != 0]
print("odds:", odds)

lengths = [len(w) for w in words if len(w) > 3]
print("lengths:", lengths)


a  = [-7, -3, 2, 3, 11] # [0, 1, 9, 16, 100]
data = []
for i in a:
    b = i**2
    data.append(b)

print(sorted(data))



def sortedSquares(a):
    sots = [x**2 for x in a]  
    return sorted(sots)

assert sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
assert sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
assert sortedSquares([5]) == [25]