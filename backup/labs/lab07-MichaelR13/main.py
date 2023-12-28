# Name: Michael Rojas
# Date: 10/26/2023
# File: main.py
'''
This program creates an interface/menu for managing different functions and options to manipulate contacts data in a dictionary file.

Functions:
1. Add contact data to the dictionary file.
2. Modify contact data in the dictionary file, by phone number.
3. Delete contact data from the dictionary file, by phone number.
4. Print the contact data in the dictionary file.
5. Set the filename of the dictionary file.
6. Exit the program.
'''
# Import the contacts module.
import contacts

# Instantiate a Contacts object with any default filename.
c = contacts.Contacts("contacts.json")

# Implement a menu within a loop
while True:
    print("      *** TUFFY TITAN CONTACT MAIN MENU\n")
    print("1. Add contact")
    print("2. Modify contact")
    print("3. Delete contact")
    print("4. Print contact list")
    print("5. Set contact filename")
    print("6. Exit the program")
    print()
    choice = input("Enter menu choice: ")
    print()
    if choice == "1":
        id = input("Enter phone number: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        if c.add_contact(id, first_name, last_name) == "error":
            print("Phone number already exists.")
        else:
            print("Added: {} {}.".format(first_name, last_name))
        print()
    elif choice == "2":
        id = input("Enter phone number: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        if c.modify_contact(id, first_name, last_name) == "error":
            print("Invalid phone number.")
        else:
            print("Modified: {} {}.".format(first_name, last_name))
        print()
    elif choice == "3":
        id = input("Enter phone number: ")
        if c.delete_contact(id) == "error":
            print("Invalid phone number.")
        else:        
            print("Deleted: {} {}.".format(c.data[id][0], c.data[id][1]))
        print()
    elif choice == "4":
        print("==================== CONTACT LIST ====================")
        print("Last Name             First Name            Phone")
        print("====================  ====================  ==========")
        for key, value in c.data.items():
            print("{:21}{:21}{}".format(value[1], value[0], key))
        print()
    elif choice == "5":
        filename = input("Enter filename: ")
        c = contacts.Contacts(filename)
        print()
    elif choice == "6":
        break