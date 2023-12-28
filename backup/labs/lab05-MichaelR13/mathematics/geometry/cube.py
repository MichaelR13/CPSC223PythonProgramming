"""
This module provides the basic functions for cube calculations.

Functions:
- surface_area(side): Calculate the surface area of a cube.
- volume(side): Calculate the volume of a cube.
"""

# Initialize the __all__ variable to the whoami, circle, and cube modules.
__all__ = ['whoami', 'circle', 'cube']

# Create a function named surface_area which receives the keyword parameter side and returns (s * s * 6).
def surface_area(side):
    return side * side * 6

# Create a function named volume which receives the keyword parameter side and returns (s * s * s).
def volume(side):
    return side * side * side