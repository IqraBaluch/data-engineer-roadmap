
"""

Mini project 2: Contact Book

Goal: a program that stores contacts and lets the user add, search, delete, and list them from a text menu.

Data: one dictionary, contacts. Each key is a name, and each value is a dictionary with phone, email, and address.

Functions, each with its own asserts:

add_contacts(contacts, name, data) adds a person.
search_contact(contacts, name) returns that person's details, or None if the name isn't there.
delete_contact(contacts, name) removes the person, and does nothing (no crash) if the name isn't there.
list_contacts(contacts) prints every person: name and details.

Menu loop:

Shows the options: add, search, delete, list, quit
Uses input() to read the user's choice and details
Repeats until the user chooses quit

Edge cases to handle:

Adding a name that already exists (decide: replace it, or refuse)
Searching or deleting a name that doesn't exist
Listing an empty book

Rules:

Use made-up data only, because the project goes on public GitHub.
Test the functions with asserts before you build the menu.
Push to GitHub when it works.

"""

contacts = {}


def add_contacts(contacts, name, data):
    contacts[name] = data


def search_contact(contacts, name):
    return contacts.get(name)


def delete_contact(contacts, name):
    return contacts.pop(name, None)


def list_contacts(contacts):
    if len(contacts) == 0:
        print("no contacts available")
        return

    for name, data in contacts.items():
        print(name, ":", data)


# ---- my tests ----

# add
add_contacts(contacts, "Iramm", {"phone": 97458, "email": "irammm@gmail.com"})
assert "Iramm" in contacts
assert len(contacts) == 1

add_contacts(contacts, "Iqra", {"phone": 7463900, "email": "iqra@gmail.com"})
assert len(contacts) == 2
assert contacts["Iqra"]["email"] == "iqra@gmail.com"

# search
print(search_contact(contacts, "Iqra"))
print(search_contact(contacts, "ISRA"))

# delete
delete_contact(contacts, "Iramm")
assert "Iramm" not in contacts
assert len(contacts) == 1

assert delete_contact(contacts, "Zzz") == None
assert len(contacts) == 1

# list
list_contacts({})
list_contacts(contacts)
