import random




# generate = random.randint(1,100)
# counter = 0
# for num in range(3):
#     number = int(input("Guess a number! "))
#     counter+=1
#     if number == generate:
#         print("Congrates! you guessed it right!")
#         break
#     elif counter == 3:
#         print(f" YOU LOST:( and the number was {generate}")
#     elif number >= generate:
#         print("Lower")
#     elif number <= generate:
#         print("Higher")

# print("Attempts:",counter)

def play_game():
    generate = random.randint(1,10)
    counter = 0
    
    for num in range(3):
        number = int(input("Guess a number! "))
        counter+=1
        if number == generate:
            print("Congrats! you guessed it right!")
            break
        elif counter == 3:
            print(f" YOU LOST:( and the number was {generate}")
        elif number >= generate:
            print("Lower")
        elif number <= generate:
            print("Higher")

    return "Attempts:",counter
print(play_game())
