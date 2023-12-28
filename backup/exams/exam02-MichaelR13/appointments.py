# Name: Michael Rojas
# Date: 10/31/2023
# File: appointments.py

#import modules
import json
import datetime

class Appointments:

    def __init__(self, filename):
        self.filename = filename    # member variable = filename
        self.data = {}  # member variable = empty data dictionary
        try:
            with open(self.filename, 'r') as f:
                self.data = json.load(f)    # load the JSON decoded contents into the empty data dictionary
        except FileNotFoundError:   # if the filename does not exist
            pass
    
    def add_appointment(self, phone, first, last, appt_datetime):
        if len(phone) != 10 or not phone.isdigit():    # if phone number != 10 digits or not all digits
            return False
        if phone in self.data:  # if phone number exists in the data dictionary
            return False
        # If the appointment date and time is invalid the function should return a False.
        try:
            appointment_time = datetime.datetime.strptime(appt_datetime, '%Y-%m-%d %H:%M')  # convert appt_datetime to datetime object
        except ValueError:
            return False
        self.data[phone] = [first, last, appt_datetime]    # add data to the member variable data dictionary
        with open(self.filename, 'w') as f:
            json.dump(self.data, f) # write the JSON encoded contents of the member variable data dictionary to filename
        return True

    def delete_appointment(self, phone):
        if len(phone) != 10 or not phone.isdigit():    # if phone number != 10 digits or not all digits
            return False
        if phone not in self.data:  # if phone number does not exist in the data dictionary
            return False
        self.data.pop(phone)    # remove the phone number dictionary element from the member variable data dictionary
        with open(self.filename, 'w') as f:
            json.dump(self.data, f) # write the JSON encoded contents of the member variable data dictionary to filename
        return True
    
    def get_appointments(self, appt_date):
        appt_list = []  # this will return an empty list if there are no appointments on the appointment date

        # If the supplied appointment date is invalid the function should return an empty list.
        if len(appt_date) != 10 or not appt_date[0:4].isdigit() or not appt_date[5:7].isdigit() or not appt_date[8:10].isdigit():
            return appt_list
        # Return a list of appointments for all appointments in the member variable data dictionary that match the supplied date
        for phone, data in self.data.items():
            appt_date2 = data[2][0:10]  # date from data dictionary
            appt_time = data[2][11:16]  # time from data dictionary

            if appt_date2 == appt_date:
                # format the date
                month, day, year = appt_date2.split('-')
                format_date = datetime.datetime.strptime(appt_date2, '%Y-%m-%d').strftime('%B %d, %Y')  # convert appt_date2 to datetime object
                # format the time
                time_parts = appt_time.split(':')
                hour, minute = int(time_parts[0]), int(time_parts[1])
                am_pm = 'am' if hour < 12 else 'pm'
                if hour == 0:
                    hour = 12
                elif hour > 12:
                    hour -= 12
                format_time = f'{hour}:{minute:02d} {am_pm}'
                # format the phone number
                format_phone = f'({phone[:3]}){phone[3:6]}-{phone[6:]}'
                # format the name
                format_name = f'{data[0]} {data[1]}'
                # append the list
                appt_list.append([format_date, format_time, format_phone, format_name])
        return appt_list