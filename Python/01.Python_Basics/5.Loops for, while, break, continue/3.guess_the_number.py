import random

    #generate a random number
num = random.randint(1,10)
guess = int(input("Guess the number: "))

counter = 1
while guess != num:

    if guess < num:
        print("Wrong! Guess higher")
    else:
        print("Lower!")

    guess = int(input("Guess the number: "))
    counter+=1

else:
    print("Correct Guess! ")
    print("Total Attempts",counter)
