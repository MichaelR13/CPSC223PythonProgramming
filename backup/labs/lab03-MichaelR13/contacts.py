# Name: Michael Rojas
# Date: 9/14/2023
# File Purpose: contacts module that will contain the functions that will be used in main.py

def print_list(contacts):
    '''
    Function will format and print out the list of contacts. Contacts are in ([first_name], [last_name]) format.
    '''
    print('================== CONTACT LIST ==================')
    print('Index   First Name            Last Name')
    print('======  ====================  ====================')

    for i in range(len(contacts)):
        print(f'{str(i):8}{contacts[i][0]:22}{contacts[i][1]:22}')
    print('')
    return contacts

def add_contact(contacts, first_name, last_name):
    '''
    Function will add a new contact to the contact list. This is done by asking the user to input a first and last name,
    and appending it to the contact list.
    '''
    contacts.append([first_name, last_name])
    print('')
    return contacts

def modify_contact(contacts, index, first_name, last_name):
    '''
    Function will modify an existing contact in the contact list. This is done by asking the user to input an index number,
    and then asking the user to input a first and last name to replace the existing contact at the index.
    If no contact exists at the index, the function will return False.
    '''
    if index < len(contacts):
        contacts[index] = [first_name, last_name]
        print('')
        return True
    else :
        print('Invalid index number.')
        return False

def delete_contact(contacts, index):
    '''
    Function will delete an existing contact in the contact list. The user is asked to input an index number to delete.
    If no contact exists at the index, the function will return False.
    '''
    if index < len(contacts):
        contacts.pop(index)
        print('')
        return True
    else :
        print('Invalid index number.')
        return False

def sort_contacts (contacts, column = 0):
    '''
    Function will sort the contact list based on the value of the column. If the user wants to sort by first name, the column
    value is set to 0. If the user wants to sort by last name, the column value is set to 1. If an invalid column number is
    assigned, the function will return False.
    '''
    if column == 0:
        contacts.sort(key=lambda x: x[0])    # sorts the first index of the contact list (first name) in alphabetical order
        return contacts
    elif column == 1:
        contacts.sort(key=lambda x: x[1])    # sorts the second index of the contact list (last name) in alphabetical order
        return contacts
    else:
        print('Invalid column number.')
        return False
