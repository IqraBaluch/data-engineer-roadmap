
# Kilometres to miles: miles = km × 0.621371
# Kilograms to pounds: pounds = kg × 2.20462
# Celsius to Fahrenheit: °F = °C × 9/5 + 32


print("====== Unit Conversion =========")
print("---- Find the manue below ----")
print(" Press 1 to convert Kilometres to miles\n Press 2 to convert Kilograms_to_pounds \n Press 3 to convert Celsius to Fahrenheit ")

units = int(input(""))


if units == 1:
    km= int(input("Enter the value: "))
    Kilometres_to_miles = km * 0.621371
    print(Kilometres_to_miles)

elif units == 2:
    kg= int(input("Enter the value: "))
    Kilograms_to_pounds =  kg * 2.20462
    print(Kilograms_to_pounds)


elif units == 3:
    C= int(input("Enter the value: "))
    Celsius_to_Fahrenheit = C * 9/5 + 32
    print(Celsius_to_Fahrenheit)

else:
    print("Pls enter a valid input.")


# Clauds code

def km_to_miles(km):
    return km * 0.621371

def kg_to_pounds(kg):
    return kg * 2.20462

def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

# tests
assert km_to_miles(0) == 0
assert round(km_to_miles(100), 2) == 62.14
assert round(kg_to_pounds(10), 4) == 22.0462
assert celsius_to_fahrenheit(0) == 32
assert celsius_to_fahrenheit(100) == 212

print("====== Unit Converter ======")
while True:
    print("\n1) Kilometres to miles")
    print("2) Kilograms to pounds")
    print("3) Celsius to Fahrenheit")
    print("4) Quit")
    choice = int(input("Choose an option: "))

    if choice == 4:
        print("Goodbye!")
        break
    elif choice == 1:
        value = float(input("Enter kilometres: "))
        print(km_to_miles(value))
    elif choice == 2:
        value = float(input("Enter kilograms: "))
        print(kg_to_pounds(value))
    elif choice == 3:
        value = float(input("Enter degrees Celsius: "))
        print(celsius_to_fahrenheit(value))
    else:
        print("Please enter 1, 2, 3 or 4.")