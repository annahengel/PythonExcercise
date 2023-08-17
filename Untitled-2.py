phonebook = {
    "Name": [], 
    "Number": []
}
#Add a contact
def add_a_contact(name, number):
    phonebook["Name"].append(name)
    phonebook["Number"].append(number)
    print(phonebook)
#search by name
def search_contact(name):
    if name in phonebook["Name"]:
        index = phonebook["Name"].index(name)
        number = phonebook["Number"][index]
        print("Contact found")
        print(name,":", number)
    else:
        print("Contact not found")

add_a_contact("Hanna", 123456)
add_a_contact("Adam", 1234321)
add_a_contact("Krysia", 6543212)
search_contact("Hanna")

#delete a contact
def delete_contact(name):
    if name in phonebook["Name"]:
        index = phonebook["Name"].index(name)
        del phonebook["Name"][index]
        del phonebook["Number"][index]
        print(name, "was deleted")
    else:
        print("Contact not found")

delete_contact("Krysia")

def display_all_contacts(phonebook):
    print(phonebook)

display_all_contacts(phonebook)











