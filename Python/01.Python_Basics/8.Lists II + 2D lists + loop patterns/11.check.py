

a = [1, 2]
total = 0
val = 0
for num in a:
    total = total + num
    val += 1
    avg = total / val

    above = 0
    for num in a:
        if num > avg:
            above +=1
    below = 0

    for num in a:
        if num < avg:
            below += 1
            

print(total)
print(val)
print(avg)
print(above)
print(below)


def count_above_average(a):
    total = 0
    for num in a:                 # pass 1: build the total
        total += num
    average = total / len(a)      # final average, between the loops

    above = 0
    for num in a:                 # pass 2: compare with the final average
        if num > average:
            above += 1
    return above


print(count_above_average([1, 2, 3, 6]))   # 1
print(count_above_average([2, 4, 6, 8]))   # 2
print(count_above_average([5, 5, 5]))      # 0
print(count_above_average([1, 2, 4]))      # 1


a = [2, 4, 6, 8]

total = 0
for num in a:
    total += num
    avrage = total / len(a)

    above = 0
    for num in a:
        if num > avrage:
            above+=1
    print(above)


