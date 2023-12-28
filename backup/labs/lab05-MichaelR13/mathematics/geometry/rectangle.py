"""
This module provides the basic functions for rectangle calculations.

Functions:
- perimeter(length, width): Calculate the perimeter of a rectangle.
- area(length, width): Calculate the area of a rectangle.
"""

# Create a function named perimeter which receives a keyword parameters length and width and returns (2l + 2h).
def perimeter(length, width):
    return (2 * length) + (2 * width)

# Create a function named area which receives a keyword parameters length and width and returns (l * h).
def area(length, width):
    return length * width