import os
import sqlite3  # sqlite3 module used for database access

class Contacts:
    def __init__(self):
        self.DBFile = ""

    def set_database_name(self, database_name):
        self.DBFile = database_name
        # If the file already exists, do nothing
        if os.path.isfile(self.DBFile):
            pass
        # If the file does not exist, connect to the sqlite3 file and create the contacts table and the phones table using the proper SQL CREATE TABLE statement. Use the same field names as those used in the Entity-Relationship diagram above. Use integers for all the id's and text for all the other data.
        else:
            # Connect to the database
            conn = sqlite3.connect(self.DBFile)
            # Create a cursor object
            cursor = conn.cursor()
            # Create the contacts table
            cursor.execute("CREATE TABLE contacts (contact_id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT)")
            # Create the phones table
            cursor.execute("CREATE TABLE phones (phone_id INTEGER PRIMARY KEY, contact_id INTEGER, phone_type TEXT, phone_number TEXT)")
            # Commit the changes
            conn.commit()
            # Close the connection
            conn.close()
            
    
    def get_database_name(self):
        # Return the value of the class variable that stores the database name.
        return self.DBFile
    
    def add_contact(self, first_name, last_name):
        # Insert the first name and last name into the contacts table using the SQL INSERT INTO statement
        conn = sqlite3.connect(self.DBFile)
        cursor = conn.cursor()
        # Insert the first name and last name into the contacts table
        cursor.execute("INSERT INTO contacts (first_name, last_name) VALUES (?, ?)", (first_name, last_name))
        conn.commit()
        conn.close()

    def modify_contact(self, contact_id, first_name, last_name):
        # Update the first name and last name of the cooresponding contact id in the contacts table using the SQL UPDATE statement
        conn = sqlite3.connect(self.DBFile)
        cursor = conn.cursor()
        # Update the first name and last name of the cooresponding contact id in the contacts table
        cursor.execute("UPDATE contacts SET first_name=?, last_name=? WHERE contact_id=?", (first_name, last_name, contact_id))
        conn.commit()
        conn.close()

    def add_phone(self, contact_id, phone_type, phone_number):
        # Insert the contact id, phone type, phone number into the phones table using the SQL INSERT INTO statement
        conn = sqlite3.connect(self.DBFile)
        cursor = conn.cursor()
        # Insert the contact id, phone type, phone number into the phones table
        cursor.execute("INSERT INTO phones (contact_id, phone_type, phone_number) VALUES (?, ?, ?)", (contact_id, phone_type, phone_number))
        conn.commit()
        conn.close()

    def modify_phone(self, phone_id, phone_type, phone_number):
        # Update the phone type and phone number of the cooresponding phone id in the phones table using the SQL UPDATE statement
        conn = sqlite3.connect(self.DBFile)
        cursor = conn.cursor()
        # Update the phone type and phone number of the cooresponding phone id in the phones table
        cursor.execute("UPDATE phones SET phone_type=?, phone_number=? WHERE phone_id=?", (phone_type, phone_number, phone_id))
        conn.commit()
        conn.close()

    def get_contact_phone_list(self):
        conn = sqlite3.connect(self.DBFile)
        cursor = conn.cursor()
        # Create an array from a query on the database using the SQL statement SELECT contacts.*, phones.* FROM contacts LEFT JOIN phones ON contacts.contact_id=phones.contact_id
        cursor.execute("SELECT contacts.*, phones.* FROM contacts LEFT JOIN phones ON contacts.contact_id=phones.contact_id")
        # Create an array from the query
        contact_phone_list = cursor.fetchall()
        conn.close()
        return contact_phone_list