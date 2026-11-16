"""
enumerate:
    Sometimes you need both the index and the value while looping. 
    Before, you wrote for i in range(len(a)) and then a[i]. 
    enumerate gives you both at once, using the unpacking you just learned:
"""

names = ['iqra', 'hajo', 'anu', 'sabiha']
for i, name in enumerate(names):
    print(i,name)


# write a loop with enumerate over [5, 8, 2] that
#  prints only the index of any number bigger than 4.
num = [5, 8, 2] 

for i, n in enumerate(num):
    if n > 4:
        print(i)