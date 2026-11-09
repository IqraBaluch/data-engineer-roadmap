"""

Restate it in your own words. This buys thinking time.
Clarify. Ask 1 or 2 questions (edge cases, input type).
Plan out loud before any code: “I’ll use X, then Y.”
Code, saying what each line does as you write.
Test with an example out loud, including an edge case.
State complexity (time and space), once we’ve covered it.

"""

# Question 1 “Someone gives you a number of minutes, like 500. Write a function that returns 
# how many hours and minutes that is. For 500 it should give 8 hours and 20 minutes.”

def hours_and_minutes_counter(n):
    # gives the left over minutes
    minutes = n % 60
    # calculates the whole hours
    hours = n // 60   
    return hours, minutes

print(f"Total whole hours and minutes: {hours_and_minutes_counter(5000000)}")

assert hours_and_minutes_counter(0) == (0, 0)
assert hours_and_minutes_counter(500) == (8, 20)
assert hours_and_minutes_counter(60) == (1, 0)
assert hours_and_minutes_counter(59) == (0, 59)


# Question 2:

# “A user types their age into a form, so the program receives it as the text '25'. 
# Write a function that takes that text and returns the age next year, as a number.”
def age_next_year(age="0"):
    # conver age into integer
    age = int(age)

    #check type to confirm
    # -- print(type(age))
    # add 1 to current age to tell age next year
    age = age + 1
    #return age
    return age
# call funciton to see what age will you be next year
print(f"your age next year: {age_next_year()}")

assert age_next_year("25") == 26
assert age_next_year("51") == 52


# Question 3: 
# “Write a function that takes a full name like ' iqra ANWAR ' 
# and returns the initials in capitals, like 'IA'.”


def name_initializer(name= 'anwar '):
    

    # title will conver
    capital = name.title()
    #print(capital)
    #converts string into list so taht we can use indezing to get initials
    to_list = capital.split()
    
    if len(to_list) == 3:
        # indexing to get 1st and second words 1st chatacters 
        indexing = to_list[0][0] + to_list[1][0]  + to_list[2][0]
        #retun indexing
    elif len(to_list) == 2:
        # indexing to get 1st and second words 1st chatacters 
        indexing = to_list[0][0] + to_list[1][0]  
        #print(indexing)
    elif len(to_list) == 1:
        # indexing to get 1st and second words 1st chatacters 
        indexing = to_list[0][0]   
        #print(indexing)
    else:
        print(" name can be only first name Or first and last name Or first middle and last name. so make sure you add your name correctly")

    return indexing
print(name_initializer())

assert name_initializer("Iqra") == 'I'
assert name_initializer("Anwar Baloch") == 'AB'
assert name_initializer('tell me whats') == 'TMW'


# list and for loop with string function title() 
names = ["iQra", "anwar", "baloch"]

letters = ""
for name in names:
    letters +=name[0].title()
print(letters)


# list and for loop with string function upper()
names = ["iQra", "anwar", "baloch"]

letters = ""
for name in names:
    letters +=name[0]
print(letters.upper())

def name_initals(name):
    letter = ""
    names = name.split()
    for name in names:
        letter += name[0]
    return letter.upper()


print(name_initals("iqra anwar baloch data engineer"))
# checking if function works accordingly
assert name_initals('iqra Anwar') == 'IA'
assert name_initals("Iqra") == "I"
assert name_initals("Anwar Baloch") == "AB"
assert name_initals("tell me whats") == "TMW"
assert name_initals("Ali Hassan Raza Khan") == "AHRK"
assert name_initals("") == ""

# Question 4 

# “Write a function that tells me whether a year is a leap year.”
# year = 2021
# if (year % 4 == 0 or year % 100 == 0) or(year % 400 == 0):
#     print("leap")
# else:
#     print("not leap")

def leap_year(year):

    if (year % 4 ==0 and year % 100 !=0) or (year % 400 == 0):
        return True
    else:
        return False

print(leap_year(1900))

assert leap_year(1900) == False
assert leap_year(2024) == True
assert leap_year(2029) == False
assert leap_year(2024) == True
assert leap_year(2023) == False
assert leap_year(1900) == False
assert leap_year(2000) == True