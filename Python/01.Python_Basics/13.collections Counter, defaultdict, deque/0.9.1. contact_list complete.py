
contacts = {}

def add_contact(name, data):
    d = contacts[name] =data
    return contacts


# def list_contacts(contacts):
#     if len(contacts) == 0:
#         return "no contacts available"
#     else:
#         for name, data in contacts.items():
#             print("Contact List")
#     return name, data

def list_contacts(contacts):
    if len(contacts) == 0:
        return "no contacts available"

    print("Contact List")
    for name, data in contacts.items():
        print(name, ":", data)
    return ""


def delet_contact(contacts, name):
    if name not in contacts:
        return f"{name} not in contact book"
    if len(contacts) == 0:
        return "No Contacs Available"
    if contacts[name] == contacts.get(name):
        print("Contact deleted")
        return contacts.pop(name)


def search_contact(contacts,name):
    if name not in contacts:
        return f"{name:}  not in the contact book"
    if len(contacts) ==0:
        return "No Contacs Available"
    if contacts[name] == contacts.get(name):
        return contacts.get(name)
        






# print(add_contact("Iqra", {"phone": 97458, "email": "iqra@gmail.com"}))
# print(search_contact(contacts,"Iqra"))



def contact_book():
    

    print("============ CONTACT BOOK ============")
    print("Select a/A to add a contact.")
    print("Select s/S to search a contact by name.")
    print("Select d/D to delet a contact by name.")
    print("Select l/L to list your entire contact.")
    print("Select q/Q to end. ")

    choose =  input("To continue press C to Quit press q: ").lower()
    while choose != "q":
        choose =  input("Enter a character from manu to start! ").lower()
        

        if choose == 'a':
            name = input("Enter the name: ").title()
            data = input(f"Enter remaining data for {name}: ")
            add_contact(name, data)
            print("Contact Saved! ")

        if choose == 'l':
            # print("Contact List")
            print(list_contacts(contacts))

        if choose == 's':
            name = input("Enter a name to find contact details: ").title()
            print(search_contact(contacts, name))


        if choose == 'd':
            name = input("Enter name to delete the contact: ").title()
            print(delet_contact(contacts,name))



    return "Thank you for using Contact Book"
print(contact_book())
