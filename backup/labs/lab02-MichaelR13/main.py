# Name: Michael Rojas
# Date: 8/31/2023
# File Purpose: Main module that will contain the main function for contact list which contains a list of contacts that can be modified or deleted.

# import functions from contacts.py
from contacts import print_list, add_contact, modify_contact, delete_contact

# main function
def main():
    # initialize contacts list
    contactList = []

    # loop entire menu until user enters 5 to exit the program
    while True:
        print('      *** TUFFY TITAN CONTACT MAIN MENU\n')
        print('1. Print list')
        print('2. Add contact')
        print('3. Modify contact')
        print('4. Delete contact')
        print('5. Exit the program\n')
        choice = int(input('Enter menu choice: '))
        print()

        if choice == 1:
            print_list(contactList)

        elif choice == 2:
            add_contact(contactList)

        elif choice == 3:
            modify_contact(contactList)

        elif choice == 4:
            delete_contact(contactList)

        elif choice == 5:
            break
        else:
            print('Invalid choice; chose 1-5')

# call main function
main()