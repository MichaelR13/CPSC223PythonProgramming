# Michael Rojas
# Date: 11/2/2023
# File: people.py
'''
This people module provides the Faculty and Student classes,

This module includes functions in each class to create a new object and set member variables

Functions:
- __init__(): Initializes the Person, Faculty, and Student objects.
- set_class(): Sets the class year for the Student object.
- set_major(): Sets the major for the Student object.
- set_advisor(): Sets the advisor for the Student object.
'''

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname  # set member variable firstname = first name parameter
        self.lastname = lastname    # set member variable lastname = last name parameter

class Faculty(Person):
    def __init__(self, firstname, lastname, department):
        Person.__init__(self, firstname, lastname)  # call Person __init__ member function with first and last name parameters
        self.department = department    # set member variable department = department parameter

class Student(Person):
    def __init__(self, firstname, lastname):
        Person.__init__(self, firstname, lastname)  # call Person __init__ member function with first and last name parameters

    def set_class(self, classyear):
        self.classyear = classyear  # set member variable classyear = class year parameter
    
    def set_major(self, major):
        self.major = major  # set member variable major = major parameter

    def set_advisor(self, faculty):
        self.advisor = faculty  # set member variable advisor = faculty parameter