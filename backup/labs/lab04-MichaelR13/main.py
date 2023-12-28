# Name: Michael Rojas
# Date: 9/28/2023
# File Purpose: Main module that will contain the main function and user I/O loop.

from contacts import *

def main():
    # Initialize an empty dictionary
    contactDictionary = dict()

    while True:
        print('      *** TUFFY TITAN CONTACT MAIN MENU\n')
        print('1. Add contact')
        print('2. Modify contact')
        print('3. Delete contact')
        print('4. Print contact list')
        print('5. Find contact')
        print('6. Exit the program\n')
        choice = input('Enter menu choice: ')
        print()

        if choice == '1':
            id = input('Enter phone number: ')
            first_name = input('Enter first name: ')
            last_name = input('Enter last name: ')
            result = add_contact(contactDictionary, id, first_name, last_name)
            if result == 'error':   # if error is returned, display error message
                print('Phone number already exists.\n')
            else:
                print(f'Added: {first_name} {last_name}.\n')    # if successful, display success message

        elif choice == '2':
            id = input('Enter phone number: ')
            first_name = input('Enter first name: ')
            last_name = input('Enter last name: ')
            result = modify_contact(contactDictionary, id, first_name, last_name)
            if result == 'error':   # if error is returned, display error message
                print('Phone number does not exist.\n')
            else:
                print(f'Modified: {first_name} {last_name}.\n')   # if successful, display success message
        elif choice == '3':
            id = input('Enter phone number: ')
            result = delete_contact(contactDictionary, id)
            if result == 'error':   # if error is returned, display error message
                print('Invalid phone number.\n')
            else:
                print(f'Deleted: {first_name} {last_name}.\n')  # if successful, display success message
                
        elif choice == '4':
            print('==================== CONTACT LIST ====================')
            print('Last Name             First Name            Phone')
            print('====================  ====================  ==========') 
            sorted_contacts = sort_contacts(contactDictionary)
            for key, value in sorted_contacts.items():  
                print(f'{value[1]:<22}{value[0]:<22}{key}') # print sorted contacts (last name, first name, phone)
            print ('')
            
        elif choice == '5':
            find = input('Enter search string: ')
            found_contacts = find_contact(contactDictionary, find)
            print('================== FOUND CONTACT(S) ==================')
            print('Last Name             First Name            Phone')
            print('====================  ====================  ==========')
            for key, value in found_contacts.items():   
                print(f'{value[1]:<22}{value[0]:<22}{key}') # print found contacts (last name, first name, phone)
            print('')

        elif choice == '6':
            break
        else:
            print('Invalid choice; chose 1-6\n')

# Call the main function
main()