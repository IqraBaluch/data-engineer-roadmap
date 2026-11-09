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

# def hours_and_minutes_counter(n):

#     for num in n:
#         minutes = num%60
#         hours = minutes - n
#     return minutes, hours % 60
# print(hours_and_minutes_counter(500))

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
# def name_initials(name='   iqra Anwar baloch   '):
#     # title will conver
#     name_t = name.title()
#     #converts string into list so taht we can use indezing to get initials
#     name_t = name_t.split()
#     print(len(name_t))
#     if len(name) == 3:
#         # indexing to get 1st and second words 1st chatacters 
#         name_t = name_t[0][0] + name_t[1][0]  + name_t[2][0]
#         print(name_t)
#         return name_t
  
    # else:
    #     print(" name can be only first name and first and last name and first middle and last name.")

#     return name_t
# print(name_initials())


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