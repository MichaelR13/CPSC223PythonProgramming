# Name: Michael Rojas
# Date: 10/26/2023
# File: contacts.py
'''
This contactss module provides functions that add, modify, and delete different contacts data.

This module includes functions to manipulate data in the JSON format, using classes and objects.

Functions:
- __init__(): Initializes the Contacts object.
- add_contact(): Adds a contact to the data dictionary.
- modify_contact(): Modifies a contact in the data dictionary.
- delete_contact(): Deletes a contact from the data dictionary.
'''
# Import the json module.
import json

class Contacts:
    # Take a self as a positional parameter, filename as a keyword parameter.
    def __init__(self, filename):
        self.filename = filename    # Set a member variable equal to the filename
        self.data = {}  # Set a member varialbe equal to an empty data dictionary
        # Open the filename and load the JSON decoded contents to the empty data dictionary.
        try:
            with open(self.filename) as f:
                self.data = json.load(f)
        except FileNotFoundError:
            pass
        
    # Take a self as a positional parameter, id/first_name/last_name as a keyword parameter.
    def add_contact(self, id, first_name, last_name):
        # If the id exists in the data dictionary, return the string error.
        if id in self.data:
            return "error"
        # Set key:value pair to the data dictionary.
        self.data[id] = [first_name, last_name]
        # Sort the data dictionary in ascending order by last name, and then by first name, ignoring case.
        self.data = dict(sorted(self.data.items(), key=lambda x: (x[1][1].lower(), x[1][0].lower())))
        # Write the contents of the data dictionary to the filename that was set to the member variable.
        with open(self.filename, "w") as f:
            json.dump(self.data, f)
            return {id: [first_name, last_name]}
    
    # Take a self as a positional parameter.
    # Take a id/first_name/last_name as a keyword parameter.
    def modify_contact(self, id, first_name, last_name):
        # If the id does not exists in the dictionary, return the string error.
        if id not in self.data:
            return "error"
        # Set key:value pair to the contact dictionary.
        self.data[id] = [first_name, last_name]
        # Sort the data dictionary in ascending order by last name, and then by first name, ignoring case.
        self.data = dict(sorted(self.data.items(), key=lambda x: (x[1][1].lower(), x[1][0].lower())))
        # Write the contents of the data dictionary to the filename that was set to the member variable.
        with open(self.filename, "w") as f:
            json.dump(self.data, f)
            return {id: [first_name, last_name]}
    
    # Take a self as a positional parameter, id as a keyword parameter.
    def delete_contact(self, id):
        # If the id does not exists in the dictionary, return the string error.
        exists = id in self.data
        if not exists:
            return "error"
        exists = self.data.pop(id)  # Remove key:value pair with key = id
        # Write the contents of the data dictionary to the filename that was set to the member variable.
        with open(self.filename, "w") as f:
            json.dump(self.data, f)
            return exists