#start a new dictionary
phonebook = {}

def add_contact():
    name  = input("Enter the contact name: ")
    if name in phonebook:
        print("Contact already exists")
    else:
        number = input("Enter the phone number: ")
        phonebook[name] = number
        print("Contact added successfully.")

add_contact()

#search for a contact
def search_for_a_contact():
    name = input("Enter the contact name to search: ")
    if name in phonebook:
        number = phonebook[name]
        print(name,":", number)
    else:
        print("Contact not found")

search_for_a_contact()

