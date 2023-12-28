# Name: Michael Rojas
# Date: 9/19/2023
# File Purpose: main program file for Tuffy Titan Aircraft Manifest, which uses functions from manifest.py

import manifest

# nested list = [seat(str), first_name(str), last_name(str), checked_in(bool), no_bags(int), boarded(bool)],

m = [
['1A', '', '', False, 0, False],
['1B', '', '', False, 0, False],
['1C', '', '', False, 0, False],
['2A', 'Richard', 'Stallman', True, 0, True],
['2B', 'john', 'stallman', True, 0, True],
['2C', '', '', False, 0, False],
['3A', '', '', False, 0, False],
['3B', '', '', False, 0, False],
['3C', 'Becky', 'Evans', False, 0, False],
['4A', '', '', False, 0, False],
['4B', 'Jane', 'Doe', True, 2, False],
['4C', '', '', False, 0, False],
['5A', '', '', False, 0, False],
['5B', '', '', False, 0, False],
['5C', '', '', False, 0, False],
['6A', 'Bob', 'Eckart', True, 1, False],
['6B', 'Steve', 'Jobs', True, 2, False],
['6C', 'Todd', 'McEntee', True, 1, False],
['7A', '', '', False, 0, False],
['7B', 'Bill', 'Gates', False, 0, False],
['7C', '', '', False, 0, False],
['8A', 'Becky', 'Simpson', True, 1, True],
['8B', '', '', False, 0, False],
['8C', 'George', 'Mason', True, 1, True],
['9A', '', '', False, 0, False],
['9B', '', '', False, 0, False],
['9C', '', '', False, 0, False],
]

while True:
    print()
    print("      *** TUFFY TITAN AIRCRAFT MANIFEST")
    print()
    print("1. Print Seating Chart")
    print("2. Print Passenger Manifest")
    print("3. Purchase Ticket")
    print("4. Cancel Ticket")
    print("5. Check In")
    print("6. Check Bags")
    print("7. Board Aircraft")
    print("8. Exit")
    print()
    choice = input("Enter menu choice: ")
    if choice.isnumeric():
        choice = int(choice)
    else:
        print()
        continue
    print()

    # PRINT SEATING CHART
    if choice == 1:
        print('** SEATING CHART **')
        print('      A  B  C')
        print('     ========')
        for seat in m:
            row = seat[0][0]
            seat_assigned = 'x'
            if seat[1] == '':
                seat_assigned = '-'
            if 'A' in seat[0]:
                print(f'  {row:2}| {seat_assigned:1}  ',end='')
            if 'B' in seat[0]:
                print(f'{seat_assigned:1}  ',end='')
            if 'C' in seat[0]:
                print(f'{seat_assigned:1}')

    # PRINT PASSENGER MANIFEST
    elif choice == 2:
        r = manifest.get_passenger_manifest(manifest=m)
        print('** PASSENGER MANIFEST **')
        print('Last Name   First Name   Seat   Checked-In   No. Bags   Boarded')
        print('=========   ==========   ====   ==========   ========   =======')
        for x in r:
            checked_in = ''
            if x[3] == True:
                checked_in = 'Yes'
            boarded = ''
            if x[5] == True:
                boarded = 'Yes'
            print(f'{x[0]:12}{x[1]:14}{x[2]:9}{checked_in:5}{x[4]:10}        {boarded:10}')

    # PURCHASE TICKET
    elif choice == 3:
        fn = input("Enter first name: ")
        ln = input("Enter last name: ")
        s = input("Enter seat: ")
        r = manifest.purchase_ticket(manifest=m, first_name=fn, last_name=ln, seat=s)
        if r is True:
            print('Success')
        else:
            print("Fail")

    # CANCEL TICKET
    elif choice == 4:
        s = input("Enter seat: ")
        r = manifest.cancel_ticket(manifest=m, seat=s)
        if r is True:
            print('Success')
        else:
            print("Fail")

    # CHECK IN
    elif choice == 5:
        s = input("Enter seat: ")
        r = manifest.check_in(manifest=m, seat=s)
        if r is True:
            print('Success')
        else:
            print("Fail")


    # CHECK BAGS
    elif choice == 6:
        s = input("Enter seat: ")
        n = int(input("Number of bags: "))
        r = manifest.check_bags(manifest=m, seat=s, no_bags=n)
        if r is True:
            print('Success')
        else:
            print("Fail")


    # BOARD AIRCRAFT
    elif choice == 7:
        s = input("Enter seat: ")
        r = manifest.board_aircraft(manifest=m, seat=s)
        if r is True:
            print('Success')
        else:
            print("Fail")

    # EXIT PROGRAM
    elif choice == 8:
        break
