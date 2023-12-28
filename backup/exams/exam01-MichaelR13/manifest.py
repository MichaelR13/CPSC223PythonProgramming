# Name: Michael Rojas
# Date: 9/19/2023
# File Purpose: functions for main.py

def get_passenger_manifest(manifest):
    '''
    This function will return a list of passengers in the manifest in a reorganized format.
    From: ['4B', 'Jane', 'Doe', True, 2, False] --> To: ['Doe', 'Jane', '4B', True, 2, False]
    Function will return manifest
    '''
    # Print list in format: [last_name(str), first_name(str), seat(str), checked_in(bool), no_bags(int), boarded(bool)]

    # last_name and first_name can not be empty (filter list with empty last_name or first_name)
    # List should be sorted (case insensitive) by last_name as the primary sort and first_name as the secondary sort.
    #         manifest.sort(key=lambda x: (x[2].lower(), x[1].lower()))
    manifest = [x for x in manifest if x[1] != '' and x[2] != '']
    manifest.sort(key=lambda x: (x[2].lower(), x[1].lower()))

    manifest = [[x[2], x[1], x[0], x[3], x[4], x[5]] for x in manifest]

    return manifest

def purchase_ticket(manifest, first_name, last_name, seat):
    '''
    This function purchases a ticket for a passenger.
    Function will return True if the ticket was purchased successfully, otherwise False.
    '''
    # If seat (case insensitive) is taken (last_name and first_name are not empty) => return False
    # If seat is invalid => return False
    # Otherwise, for the seat in the manifest, set last_name, first_name
    seat = seat.upper()

    if seat not in [x[0] for x in manifest]:    # If seat is invalid => return False
        return False
    
    # If seat is taken (last_name and first_name are not empty) => return False
    if manifest[[x[0] for x in manifest].index(seat)][1] != '' and manifest[[x[0] for x in manifest].index(seat)][2] != '':
        return False
    
    manifest[[x[0] for x in manifest].index(seat)][1] = first_name  # Update first_name in manifest
    manifest[[x[0] for x in manifest].index(seat)][2] = last_name

    return True

def cancel_ticket(manifest, seat):
    '''
    This function cancels a ticket for a passenger.
    Function will return True if the ticket was canceled successfully, otherwise False.
    '''
    # If seat (case insensitive) is not taken (last_name and first_name are empty) => return False
    # If seat is invalid => return False
    # Otherwise, for the seat in the manifest, set last_name, first_name to empty + checked_in and boarded to False + no_bags to 0
    seat = seat.upper()

    if seat not in [x[0] for x in manifest]:
        return False
    
    if manifest[[x[0] for x in manifest].index(seat)][1] == '' and manifest[[x[0] for x in manifest].index(seat)][2] == '':
        return False
    
    manifest[[x[0] for x in manifest].index(seat)][1] = ''
    manifest[[x[0] for x in manifest].index(seat)][2] = ''
    manifest[[x[0] for x in manifest].index(seat)][3] = False
    manifest[[x[0] for x in manifest].index(seat)][4] = 0
    manifest[[x[0] for x in manifest].index(seat)][5] = False

    return True

def check_in(manifest, seat):
    '''
    This function checks in a passenger.
    Function will return True if the passenger was checked in successfully, otherwise False.
    '''
    # If seat (case insensitive) is not taken (last_name and first_name are empty) => return False
    # If seat is invalid => return False
    # Otherwise, for the seat in the manifest, set checked_in to True
    seat = seat.upper()

    if seat not in [x[0] for x in manifest]:
        return False
    
    if manifest[[x[0] for x in manifest].index(seat)][1] == '' and manifest[[x[0] for x in manifest].index(seat)][2] == '':
        return False
    
    manifest[[x[0] for x in manifest].index(seat)][3] = True

    return True


def check_bags(manifest, seat, no_bags):
    '''
    This function updates the number of bags for a passenger.
    Function will return True if the number of bags was updated successfully, otherwise False.
    '''
    # If seat (case insensitive) is not taken (last_name and first_name are empty) => return False
    # If seat is invalid => return False
    # If seat passenger is not checked in => return False
    # Otherwise, for the seat in the manifest, set the no_bags
    seat = seat.upper()

    if seat not in [x[0] for x in manifest]:
        return False
    
    if manifest[[x[0] for x in manifest].index(seat)][1] == '' and manifest[[x[0] for x in manifest].index(seat)][2] == '':
        return False
    
    if manifest[[x[0] for x in manifest].index(seat)][3] == False:
        return False
    
    manifest[[x[0] for x in manifest].index(seat)][4] = no_bags

    return True

def board_aircraft(manifest, seat):
    '''
    This function will update the boarded status for a passenger.
    Function will return True if the passenger was boarded successfully, otherwise False.
    '''
    # If seat (case insensitive) is not taken (last_name and first_name are empty) => return False
    # If seat is invalid => return False
    # If seat passenger is not checked in => return False
    # Otherwise, set boarded to True
    seat = seat.upper()

    if seat not in [x[0] for x in manifest]:
        return False
    
    if manifest[[x[0] for x in manifest].index(seat)][1] == '' and manifest[[x[0] for x in manifest].index(seat)][2] == '':
        return False
    
    if manifest[[x[0] for x in manifest].index(seat)][3] == False:
        return False
    
    manifest[[x[0] for x in manifest].index(seat)][5] = True

    return True