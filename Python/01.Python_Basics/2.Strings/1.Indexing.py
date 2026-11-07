# A string is a row of character, and each one has a position. 
# Positions start at 0, not 1.
word = "python"
#       p  y  t  h  o  n
#       0  1  2  3  4  5      ← forward positions
#      -6 -5 -4 -3 -2 -1      ← backward positions

print(word[1])
print(word[0])
print(word[2])
print(word[-1])
print("Length of word is: ",len(word))