# Name: Michael Rojas
# Date: 10/19/2023
# File: main.py
'''
This program creates an interface/menu for managing different functions and options to manipulate weather data.

Functions:
1. Set data filename
2. Add weather data
3. Print daily report
4. Print historical report
9. Exit the program
'''
# Import the weather module
import weather

# Set a default filename to store the JSON data
filename = 'default.json'

# Declare a dictionary to hold the weather data
data = {}

# Implement a menu within a loop 
while True:
    print('      *** TUFFY TITAN WEATHER LOGGER MAIN MENU\n')
    print('1. Set data filename')
    print('2. Add weather data')
    print('3. Print daily report')
    print('4. Print historical report')
    print('9. Exit the program\n')
    choice = input('Enter menu choice: ')
    if choice == '1':
        filename = input('\nEnter data filename: ')
        data = weather.read_data(filename)
    elif choice == '2':
        date = input('\nEnter date (YYYYMMDD): ')
        time = input('Enter time (hhmmss): ')
        temp = int(input('Enter temperature: '))
        humid = int(input('Enter humidity: '))
        rain = float(input('Enter rainfall: '))
        data[date + time] = {'t': temp, 'h': humid, 'r': rain}
        weather.write_data(data, filename)
    elif choice == '3':
        date = input('\nEnter date (YYYYMMDD): ')
        print(weather.report_daily(data, date))
    elif choice == '4':
        print(weather.report_historical(data))
    elif choice == '9':
        break
    else:
        print('\nInvalid choice. Try again.\n')