# Michael Rojas
# Date: 11/2/2023
# File: main.py
'''
This program creates an interface/menu for the user to add faculty and students to a list and print the list.

Functions:
- 1. Add faculty: Adds a new faculty member to the faculty list.
- 2. Print faculty: Prints the faculty list.
- 3. Add student: Adds a new student to the student list.
- 4. Print student: Prints the student list.
- 9. Exit the program: Exits the program.
'''

# Import the Faculty and Student classes from the people module.
from people import Faculty, Student

# Declare a variable to hold a list of faculty
faculty = []
# Declare a variable to hold a list of students
students = []

while True:
    print('      *** TUFFY TITAN STUDENT/FACULTY MAIN MENU\n')
    print('1. Add faculty')
    print('2. Print faculty')
    print('3. Add student')
    print('4. Print student')
    print('9. Exit the program\n')
    choice = input('Enter menu choice: ')
    if choice == '1':
        print()
        firstname = input('Enter first name: ')
        lastname = input('Enter last name: ')
        department = input('Enter department: ')
        faculty.append(Faculty(firstname, lastname, department))    # add a new Faculty object to the faculty list
        print()
    elif choice == '2':
        print('\n======================= FACLUTY =======================')
        print('Record  Name                  Department')
        print('======  ====================  =========================')
        for i in range(len(faculty)):
            print('{:<6}  {:<20}  {:<25}'.format(i, faculty[i].firstname + ' ' + faculty[i].lastname, faculty[i].department))
        print()
    elif choice == '3':
        print()
        firstname = input('Enter first name: ')
        lastname = input('Enter last name: ')
        classyear = input('Enter class year: ')
        major = input('Enter major: ')
        advisor = int(input('Enter faculty advisor: '))
        students.append(Student(firstname, lastname))   # add a new Student object to the students list
        students[-1].set_class(classyear)   # set the class year for the last Student object in the students list
        students[-1].set_major(major)   # set the major for the last Student object in the students list
        students[-1].set_advisor(faculty[advisor])  # set the advisor for the last Student object in the students list
        print()
    elif choice == '4':
        print('\n===================================== STUDENTS ======================================')
        print('Name                  Class      Major                      Advisor')
        print('====================  =========  =========================  =========================')
        for i in range(len(students)):
            print('{:<20}  {:<9}  {:<25}  {:<20}'.format(students[i].firstname + ' ' + students[i].lastname, students[i].classyear, students[i].major, students[i].advisor.firstname + ' ' + students[i].advisor.lastname))
        print()
    elif choice == '9':
        break
    else:
        print('Invalid choice\n')