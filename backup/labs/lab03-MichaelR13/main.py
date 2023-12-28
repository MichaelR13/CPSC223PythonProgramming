# Name: Michael Rojas
# Date: 9/14/2023
# File Purpose: Main module that will contain the main function for contact list which contains a list of contacts that can be modified or deleted.

# import functions from contacts.py
from contacts import print_list, add_contact, modify_contact, delete_contact, sort_contacts

# main function
def main():
    # initialize variables
    contacts = []

    while True:
        print('      *** TUFFY TITAN CONTACT MAIN MENU\n')
        print('1. Print list')
        print('2. Add contact')
        print('3. Modify contact')
        print('4. Delete contact')
        print('5. Sort list by first name')
        print('6. Sort list by last name')
        print('7. Exit the program\n')
        choice = int(input('Enter menu choice: '))
        print()

        if choice == 1:
            print_list(contacts)
        
        elif choice == 2:
            first_name = input('Enter first name: ')
            last_name = input('Enter last name: ')
            add_contact(contacts, first_name, last_name)
        
        elif choice == 3:
            index = int(input('Enter the index number: '))
            first_name = input('Enter first name: ')
            last_name = input('Enter last name: ')           
            modify_contact(contacts, index, first_name, last_name)

        elif choice == 4:
            index = int(input('Enter the index number: '))
            delete_contact(contacts, index)

        elif choice == 5:
            sort_contacts(contacts, 0)   # column 0 = sort by first name
        
        elif choice == 6:
            sort_contacts(contacts, 1)   # column 1 = sort by last name
        
        elif choice == 7:
            break
        
        else:
            print('Invalid choice; chose 1-7\n')

# call main function
main()  