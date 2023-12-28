# Name: Michael Rojas
# Date: 8/31/2023
# File Purpose: contacts module that will contain the functions that will be used in main.py

def print_list(contactList):
    print('\n================== CONTACT LIST ==================')
    print('Index   First Name            Last Name')
    print('======  ====================  ====================')
    # loop through contacts list and print the index, first name, and last name
    # assuming i is the index
    for i in range(len(contactList)):
        print(f'{str(i):8}{contactList[i][0]:22}{contactList[i][1]:22}')
    print('\n')
    return contactList

def add_contact(contactList):
    firstName = input('Enter first name: ')
    lastName = input('Enter last name: ')
    contactList.append([firstName, lastName])
    print('\n')
    return contactList

def modify_contact(contactList):
    index = int(input('Enter the index number: '))
    # if index does not have a contact, print invalid index, else, modify the contact by asking for first and last name
    if index >= len(contactList):
        print('Invalid index number.')
        print('\n')
    else:
        firstName = input('Enter first name: ')
        lastName = input('Enter last name: ')
        contactList[index] = [firstName, lastName]
        print('\n')
        return contactList

def delete_contact(contactList):
    index = int(input('Enter the index number: '))
    # if index does not have a contact, print invalid index, else, remove the contact
    if index >= len(contactList):
        print('Invalid index number.')
        print('\n')
    else:
        contactList.pop(index)
        print('\n')
    return contactList
