# Name: Michael Rojas
# Date: 10/19/2023
# File: weather.py
'''
The weather module provides functions that read, write, and analyze different weather data.

This module includes functions to read and write weather data in JSON format, as well as functions to analyze and report daily and historical weather data.

Functions:
- read_data(filename)
- write_data(data, filename)
- max_temperature(data, date)
- min_temperature(data, date)
- max_humidity(data, date)
- min_humidity(data, date)
- tot_rain(data, date)
- report_daily(data, date)
- report_historical(data)
'''
# weather module

# import modules
import json
import calendar

# Create a function named read_data which receives a keyword parameter filename.
def read_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)  # Decode the JSON data into a dictionary
            return data # Return the dictionary
    except FileNotFoundError:
        return {}
    
# Create a function named write_data which receives a keyword parameter data and filename
def write_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)   # Write the dictionary data to the file encoded as JSON
    
# Create a function named max_temperature which receives a keyword parameter data and date
def max_temperature(data, date):
    max_temp = 0    # Initialize max_temp
    for key in data:
        if key.startswith(date):    # Check if the key starts with the date (Key contains the date as YYYYMMDD)
            if data[key]['t'] > max_temp:
                max_temp = data[key]['t']   # Update max_temp if the current temperature is greater than max_temp
    return max_temp

# Create a function named min_temperature which receives a keyword parameter data and date
def min_temperature(data, date):
    min_temp = 100  # Initialize min_temp
    for key in data:
        if key.startswith(date):    # Check if the key starts with the date
            if data[key]['t'] < min_temp:
                min_temp = data[key]['t']   # Update min_temp if the current temperature is less than min_temp
    return min_temp

# Create a function named max_humidity which receives a keyword parameter data and date
def max_humidity(data, date):
    max_hum = 0    # Initialize max_hum
    for key in data:
        if key.startswith(date):    # Check if the key starts with the date
            if data[key]['h'] > max_hum:
                max_hum = data[key]['h']    # Update max_hum if the current humidity is greater than max_hum
    return max_hum

# Create a function named min_humidity which receives a keyword parameter data and date
def min_humidity(data, date):
    min_hum = 100   # Initialize min_hum
    for key in data:
        if key.startswith(date):    # Check if the key starts with the date
            if data[key]['h'] < min_hum:
                min_hum = data[key]['h']    # Update min_hum if the current humidity is less than min_hum
    return min_hum

# Create a function named tot_rain which receives a keyword parameter data and date
def tot_rain(data, date):
    total_rain = 0  # Initialize total_rain
    for key in data:
        if key.startswith(date):    # Check if the key starts with the date
            total_rain += data[key]['r']    # Add the current rainfall to total_rain
    return total_rain 

# Create a function named report_daily which receives a keyword parameter data and date
def report_daily(data, date):
    # Format JSON data
    year = date[:4]
    month = date[4:6]
    day = str(int(date[6:]))  # Convert day to an integer and then back to a string to remove leading zeros
    month_name = calendar.month_name[int(month)]    # Get the month name from the calendar module

    # Header
    report = f'========================= DAILY REPORT ========================\n'
    report += f'Date                      Time  Temperature  Humidity  Rainfall\n'
    report += f'====================  ========  ===========  ========  ========\n'

    # Loop through the data
    for key in data:
        if key.startswith(date):    # Check if the key starts with the date
            time = key[8:10] + ':' + key[10:12] + ':' + key[12:]    # Format the time
            temp = data[key]['t']   # Get the temperature
            hum = data[key]['h']
            rain = data[key]['r']
            rain_str = f'{rain:.2f}'  # Format the rain variable with 2 decimal places
            report += f'{month_name} {day}, {year}      {time}           {temp}        {hum}      {rain_str}\n' # Append data to report
    return report


# Create a function named report_historical which receives a keyword parameter data
def report_historical(data):
    # Create a dictionary to group data by date
    grouped_data = {}

    # Loop through the data
    for date, readings in data.items(): # readings is a dictionary containing the temperature, humidity, and rainfall
        date_part = date[:8]    # Extract the date part (YYYYMMDD)

        if date_part in grouped_data: 
            grouped_data[date_part].append(readings)    # Append the readings dictionary to the list
        else:
            grouped_data[date_part] = [readings]    # Create a new list with the readings dictionary

    # Header
    report = f'============================== HISTORICAL REPORT ===========================\n'
    report += f'                          Minimum      Maximum   Minumum   Maximum     Total\n'
    report += f'Date                  Temperature  Temperature  Humidity  Humidity  Rainfall\n'
    report += f'====================  ===========  ===========  ========  ========  ========\n'

    # Loop through the grouped data
    for date, data_list in grouped_data.items():
        # initialize variables
        min_temp, max_temp = float('inf'), -float('inf')
        min_hum, max_hum = float('inf'), -float('inf')
        total_rain = 0.0

        for readings in data_list:  # Loop through the list of readings
            min_temp = min(min_temp, readings['t']) # Update min_temp if the current temperature is less than min_temp
            max_temp = max(max_temp, readings['t'])
            min_hum = min(min_hum, readings['h'])
            max_hum = max(max_hum, readings['h'])
            total_rain += readings['r']

        # Format data
        year = date[:4]
        month = int(date[4:6])
        day = int(date[6:])
        month_name = calendar.month_name[month]
        formatted_date = f'{month_name} {day}, {year}'
        formatted_total_rain = f'{total_rain:.2f}'

        # Append data
        report += f'{formatted_date:<20}{min_temp:>13}{max_temp:>13}{min_hum:>10}{max_hum:>10}{formatted_total_rain:>10}\n'

    return report
