# Use sorted with key=lambda. Predict first (no running), and fill in each blank:


words = ["pear", "fig", "banana", "kiwi"]

f = lambda w: len(w)
print(f("iqra"))

print(f('hy my name is iqra'))

#It sorts by length, 
print(sorted(words,key=lambda w: len(w))) # ['fig', 'pear', 'kiwi', 'banana']

# solve below 
words = ["pear", "fig", "banana", "kiwi"]
nums = [10, -3, 7, -20]
pairs = [("ali", 25), ("sara", 21), ("omer", 30)]

#1. #sort by length
print(sorted(words, key=lambda w:len(w)))

 # 2. by size, ignore the sign
print(sorted(nums, key=lambda x:abs(x)))


# 3. by age 
print(sorted(pairs, key=lambda p:p[1]))