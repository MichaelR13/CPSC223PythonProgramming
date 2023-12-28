"""
This module provides some basic functions for performing calculations on lists of numbers.

Functions:
- sum_values(list): Calculate the sum of all the values in a list.
- average(list): Calculate the average of all the values in a list.
"""

# Initialize the __all__ variable to the whoami and series modules.
__all__ = ['whoami', 'series']

# Create a function named sum_values which receives a keyword parameter list and returns the sum of all the values in the list.
def sum(list):
    sum = 0
    for i in list:
        sum += i    # add each value in the list to the sum variable
    return sum

# Create a function named average which receives a keyword parameter list and returns the average of all the values in the list.
def average(list):
    sum = 0
    for i in list:
        sum += i    # add each value in the list to the sum variable
    return sum / len(list)  # divide the sum by the number of values in the list