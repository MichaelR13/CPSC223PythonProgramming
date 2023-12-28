'''
This module provides some basic functions for circle calculations.

Functions:
- circumference(radius): Calculate the circumference of a circle.
- area(radius): Calculate the area of a circle.
'''
import math

# Initialize the __all__ variable to the whoami, circle, and cube modules.
__all__ = ['whoami', 'circle', 'cube']

# Create a function named circumference which receives the keyword parameter radius and returns (2 * pi * r).
def circumference(r):
    return 2 * math.pi * r

# Create a function named area which receives the keyword parameter radius and returns (pi * r * r).
def area(r):
    return math.pi * r * r