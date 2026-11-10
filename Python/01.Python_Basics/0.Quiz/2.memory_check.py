# “Write a function that returns the sum of the numbers from 1 to n.”

"""Time complexity = O(n) bcs the bigger the number the more iteration would accure
 and space compexity = O(1) bcs only returning 1 value and its constant"""

def sum_n(n):
    # initialize totals = 0 to keep adding value with every iteration
    totals = 0
    # for loop for the number times loop will execute
    for i in range(1,n+1):
        # add the new i valuye in totals variable
        totals += i
    #return total
    return totals

print(sum_n(4))

    

"""Time complexity = O(n) bcs the bigger the number the more iteration would accure
 and space compexity = O(1) bcs only returning 1 value and its constant"""

#“Write a function that returns how many vowels are in a string.”

def vowels_counter(word):
    # assigned vowels to a varible to compare with input
    vowels = 'aeiouAEIOU'
    # to keep count of how many vowels we got
    counter = 0
    # loop to iterate through charcters in word
    for i in word:
        # check if character is vowel
        if i in vowels:
            # if a vowel is found add +1 to counter
            counter += 1
        # return counter
    return counter

print(vowels_counter("education and learning"))

assert sum_n(4) == 10
assert sum_n(0) == 0
assert vowels_counter("education") == 5
assert vowels_counter("xyz") == 0