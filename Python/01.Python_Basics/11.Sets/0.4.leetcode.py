def singleNumber(num):

    counts = {}

    for i in num:
        counts[i] = counts.get(i,0)+1

    for key,value in counts.items():
        if value ==1:
            return key


assert singleNumber([2, 2, 1]) == 1
assert singleNumber([4, 1, 2, 1, 2]) == 4
assert singleNumber([1]) == 1