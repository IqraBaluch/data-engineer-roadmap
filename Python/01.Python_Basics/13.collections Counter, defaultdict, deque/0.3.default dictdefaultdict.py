from collections import defaultdict

d = defaultdict(int)

d['a'] +=1
d['a'] +=1
d['b'] +=1
d['c'] +=1
d['b'] +=1

print(d)
print(d["z"])
print(d)
