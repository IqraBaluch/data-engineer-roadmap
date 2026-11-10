# A method is a function that belongs to an object and is called with a dot

# adding and removing items. These are the methods you’ll use all the time

# 1. list.append(val) : # add to the end  
num =  [10, 20, 30]
num.append(40)
print(num) # [10, 20, 30, 40]


# 2. list.insert(index, value) : Insert at given index
num.insert(1,5) # this will insert 5 at index 1
print(num) # [10, 5, 20, 30, 40]


# 3. list.remove(val) : removes that value/item from listt
num.remove(30)
print(num) # [10, 5, 20, 40]

# 4. list.pop() : # removes the last number/item from list and prints it

print(num.pop()) # 4

"""

Notes:

append, insert and remove change the list in place, and they return nothing (None). 
That’s the same None as in functions that don’t return.
pop() removes the last item and gives it back. pop(0) removes the first.

"""