
## create a dictionary using for loop to store the contact numbers of family members (at least 10)


def family():
    contact_numbers = {}
    while input("Do you want to enter another contact number? y/n") == "y":
        name = input("Enter their name: ")
        contact = input("Enter contact number: ")
        contact_numbers.__setitem__(name,contact)
    return contact_numbers
print(family())