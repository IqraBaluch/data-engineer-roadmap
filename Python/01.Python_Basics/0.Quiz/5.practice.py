"""#Task 1: largest number in list

number = [2,3,4,6,1,26,4,5,89]
largest = number[0]

for num in range(len(number)):
    if number[num] > largest:
        largest = number[num] 
print(largest)

numbers = [8, 3, 12, -2, 5]

smallest = numbers[0]

for i in range(len(numbers)):
    if numbers[i] < smallest:
        smallest = numbers[i]
print(smallest)

# second largest nymber
numbers =  [5, 5, 3, 2]

largest = numbers[0]
second_largest = numbers[-1]

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
 

    if num < largest and num > second_largest:
        second_largest =  num
    
    
print(largest)
print(second_largest)


n = 8472
last_digit = n % 10
print("Last digit",last_digit)

remove_last = n//10
second_last = remove_last%10
print("Tens digit",second_last)

time = 500

print("Hour:",time//60)
print("Min: ",time%60)

print(7//2)
print(-7//2)
print(-7%3)
print(2**10)
print(10/4)
print(10//4)

# 7. Swap two variables using a third. Start with a = 5 and 
# b = 9, finish with a = 9 and b = 5. Print both before and after.

a = 9
print("A:", a)

b = 5
print("B",b)

temp = a
a = b
b = temp

print(a,b)

# 8. Cause a NameError, a TypeError and a SyntaxError on purpose, one tiny line each. 
# Write one plain sentence on what each means.

print(a)

# 
# # "programming" reversed with [::-1].
# # Is "data" inside "I love data engineering"? Print True or False."""""

# word = 'programming'
# print(len(word)//2)
# print(word[0],word[5],word[-1])

# print(word[::-1])

# print('data' in "I love engineering")

# data = "learn data engineering"
# data = data.replace(" ", "-")
# print(data.title())
# sentence = "I love data engineering"
# print(sentence.split()[2])
# print("data analyst".count('a'))


# [9, 5, 2] from x = [5, 2, 9]

# x = [5, 2, 9] 
# y = sorted(x, reverse=True)
# print(y)

# """
# """Part 2, programs 7 to 9:

# 7. Take " ali ", strip the spaces, and print with an f-string: Hello, Ali!
# 8. Predict first, then run: 'abc'*2, 'hello'[1:4], 'hello'[-3:], 'a,b,c'.split(',')
# 9. Name cleaner: turn ' aLi rAZA ' into 'Ali Raza'"""

"""

a = " ali "
b  = a.strip().title()
print(f"Hello, {b}!")

print("abc"*2) #abcabc

print("hello"[1:4]) #hell

print("hello"[-3:]) # llo

print("a,b,c".split(',')) # str to list

def name_cleaner(name = '  iQrA    baLoch        '):

    name = name.strip().title()
    name = name.split()
    name = name[0]+ " "+name[1]
    return name

print(name_cleaner())

# name = "   iQrA   anWar   "
# name = name.strip().title()
# name = name.split()
# name = name[0]+ " "+name[1]
# print(name)


"""
# b) ount_above_average(a) with two passes, and test it on [1, 2, 4] (expect 1).

# (c) Aliasing, one line: a = [1, 2, 3], c = a[:], c.append(99). What is a, and why?

# Start with (a) whenever you’re ready.

"""

def count_above_average(a):
    counter = 0
    total = sum(a)
    above_avg = 0
    for num in a:
        counter += 1
        avg = total /counter
    for num in a:
        if num > avg:
            above_avg += 1
    return above_avg
        
print(count_above_average([4, 1, 2]))



def sum_of_all(a):
    total = 0
    for num in a:
        for i in num:
            total = total + i
    return total

print(sum_of_all([[1, 2, 3], [4, 5, 6]]))

assert sum_of_all([[1, 2, 3], [4, 5, 6]]) == 21
assert sum_of_all([[7]]) == 7
assert sum_of_all([]) == 0
assert sum_of_all([[1, 2], [], [3]]) == 6


"""
# def duplicates(nums):
#     if len(nums) ==1 or len(nums) ==0:
#         return False
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i] == nums[j]:
#                 return True
#     return False
# print(duplicates([1, 2, 3, 1]))
# # Test cases
# assert duplicates([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
# assert duplicates([1, 2, 3, 4]) == False
# assert duplicates([5, 5]) == True
# assert duplicates([7]) == False
# assert duplicates([]) == False
# assert duplicates([1, 2, 3, 1]) == True
# assert duplicates([0, -1, -1, 2]) == True
# assert duplicates([0, -1, 2, 3]) == False

# print("All tests passed!")

# nums = [1, 3, 4, 2]
# def dups(nums):
#     seen = set()
#     for num in nums:
#         if num in seen:
#             return True
#         num = seen.add(num)
#     return False

# print(dups(nums))


# def twosums(nums,target):
#     # nums = [11, 7, 15,2]
#     # target = 9
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i,j] 
#     return "no match"
# print(twosums([11, 7, 15,2],9))
# print(twosums([3, 2, 4], 6))
# print(twosums([1, 2, 3], 10))
# # Expected: no match


# nums = [2, 7, 15,11]
# target = 9
# def twosums(nums,target):

#     dict_seen = {}

#     for i in range(len(nums)):
#             # nums = [2, 7, 15,11]
#             val = target - nums[i]
#             #print(val) 7
#             if val in dict_seen:   
#                 return [dict_seen[val], i]

#             dict_seen[nums[i]]=i
#     return f"no values found that sum to {target}"

# print(twosums([13, 4, 5], 9))
        # else:
        #     dict_seen[nums[i]] = i
        #     print(dict_seen.keys())
        #     previous_val = dict_seen[nums[i]]
        #     print(previous_val)




# def find_max(a):
#     best = 0
#     largest = a[0]
#     for i in range(1, len(a)):
#         if a[i] > largest:
#             best = largest
#             largest = a[i]
#             return a[i], i
          
          
     




#a_list = [3,1,2,3,5,7]

def find_max(a_list):
    largest = a_list[0]
    best_index = 0
    for i in range(1,len(a_list)):
        if len(a_list) == 1:
            print(largest,i)
    
        if a_list[i] > largest:
            best_index = i
            largest = a_list[i]

    return largest, best_index


assert find_max([3, 8, 5, 8, 1]) == (8, 1)
assert find_max([5]) == (5, 0)
assert find_max([1, 2, 3]) == (3, 2)
assert find_max([-5, -2, -9]) == (-2, 1)
                             

def max_and_count(a_list):
    # pass 1: find the biggest
    largest = a_list[0]
    for x in a_list:
        if x > largest:
            largest = x

    # pass 2: count how many times it appears
    counter = 0
    for x in a_list:
        if x ==largest:
            counter += 1

    return largest, counter
assert max_and_count([3, 8, 5, 8, 1]) == (8, 2)
assert max_and_count([5]) == (5, 1)
assert max_and_count([1, 2, 3]) == (3, 1)
assert max_and_count([-5, -2, -2]) == (-2, 2)


