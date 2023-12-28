# Name: Michael Rojas
# Date: 9/28/2023
# File Purpose: Contacts module that will contain functions for adding, modifying, deleting, sorting/printing, and finding contacts.

def add_contact(contactDictionary, id, first_name, last_name):
    if id in contactDictionary:
        return 'error'  # unsuccessful add if phone number already exists
    else:
        contactDictionary[id] = [first_name, last_name] # add pair to dictionary
        return {id: [first_name, last_name]}

def modify_contact(contactDictionary, id, first_name, last_name):
    if id not in contactDictionary:
        return 'error'  # unsuccessful modify if phone number does not exist
    else:
        contactDictionary[id] = [first_name, last_name] # modify pair in dictionary
        return {id: [first_name, last_name]}
    
def delete_contact(contactDictionary, id):
    if id not in contactDictionary:
        return 'error'  # unsuccessful delete if phone number does not exist
    else:
        popped = contactDictionary.pop(id)  # delete pair from dictionary
        return popped

def sort_contacts(contactDictionary):
    sorted_list = dict(sorted(contactDictionary.items(), key=lambda x: (x[1][1].lower(), x[1][0].lower())))  # Sort by last name, then by first name
    return sorted_list

def find_contact(contactDictionary, find):
    # Create an empty dictionary to store the found contacts
    found_contacts = {}

    # First convert find to a string
    find_str = str(find)

    # If find is a phone number and is in the dictionary, add the key-value pair to the created dictionary.
    if find_str.isdigit():
        for key in contactDictionary: 
            if find_str in str(key):    
                found_contacts[key] = contactDictionary[key]

    # If find is in a first/last name and is in the dictionary, add the key-value pair to the created dictionary.
    for key, value in contactDictionary.items():
        if find_str.lower() in value[0].lower() or find_str.lower() in value[1].lower() or find_str == str(key):
            found_contacts[key] = value

    # Sort created dictionary by last name, then by first name
    sorted_found = dict(sorted(found_contacts.items(), key=lambda x: (x[1][1].lower(), x[1][0].lower())))
    return sorted_found