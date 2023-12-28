#test all the modules and functions in the mathematics package
from mathematics import geometry
from mathematics import numbers
from mathematics.geometry import circle
from mathematics.geometry import cube
from mathematics.geometry import rectangle
from mathematics.numbers import series
from mathematics.numbers import simple

# test out circle.py module
print('Circle circumference of Radius 5:', circle.circumference(5))
print('Circle area of Radius 5:', circle.area(5))
print()

# test out cube.py module
print('Cube surface area of Side 10 :', cube.surface_area(10))
print('Cube volume of Side 10:', cube.volume(10))
print()

# test out rectangle.py module
print('Rectangle perimeter of Length 4 and Width 6:', rectangle.perimeter(4, 6))
print('Rectangle area of Length 4 and Width 6:', rectangle.area(4, 6))
print()

# test out series.py module
print('Sum of values [1, 2, 3, 4, 5]:', series.sum([1, 2, 3, 4, 5]))
print('Average of values [1, 2, 3, 4, 5]:', series.average([1, 2, 3, 4, 5]))
print()

# test out simple.py module
print('Sum of values 1+2:', simple.addition(1, 2))
print('Difference of values 1-2:', simple.subtraction(1, 2))
print('Product of values 1*2:', simple.multiplication(1, 2))
print('Quotient of values 1/2:', simple.division(1, 2))
print()