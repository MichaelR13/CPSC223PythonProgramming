# Main.py that will test the SimpleMatrix class and each function.

import simplematrix

# Create an instance of the SimpleMatrix class.
sm = simplematrix.SimpleMatrix()

# Test the setA function on a 2x2 matrix (valid).
    # EX: 
    # input a valid matrix (numbers only, from top left to bottom right, separated by spaces): 5 2 8 7
    # result: True, it is a valid matrix

# Test the setA function on a 3x3 matrix (valid).
    # EX:
    # valid matrix: numbers only, from top left to bottom right, separated by spaces: 9 5 2 8 2 7 6 3 1
    # result: True, it is a valid matrix

# Test the setA function on a 2x3 matrix (invalid).
    # EX:
    # invalid matrix: numbers only, from top left to bottom right, separated by spaces: 9 5 2 8 2 7
    # result: False, it is not a valid matrix

# Test the setB function on a 2x2 matrix (valid).
    # EX:
    # valid matrix: numbers only, from top left to bottom right, separated by space: 5 2 8 7
    # result: True, it is a valid matrix

# Test the setB function on a 3x3 matrix (valid).
    # EX:
    # valid matrix: numbers only, from top left to bottom right, separated by spaces: 9 5 2 8 2 7 6 3 1
    # result: True, it is a valid matrix

# Test the setB function on a 2x3 matrix (invalid).
    # EX:
    # invalid matrix: numbers only, from top left to bottom right, separated by spaces: 9 5 2 8 2 7
    # result: False, it is not a valid matrix

# Test the addMatrices function on two 2x2 matrices (valid).
    # EX:
    # valid matrix: numbers only, from top left to bottom right, separated by spaces: 5 2 8 7
    # valid matrix: numbers only, from top left to bottom right, separated by spaces: 3 1 6 4
    # result: [[8, 3], [14, 11]]

# Test the addMatrices function on two 3x3 matrices (valid).
    # EX:
    # valid matrix: numbers only, from top left to bottom right, separated by spaces: 9 5 2 8 2 7 6 3 1
    # valid matrix: (numbers only, from top left to bottom right, separated by spaces: 2 3 1 6 9 4 5 2 0
    # result: [[11, 8, 3], [14, 11, 11], [11, 5, 1]]

# Test the addMatrices function on a 2x2 matrix and a 3x3 matrix (invalid).
    # EX:
    # valid matrix: numbers only, from top left to bottom right, separated by spaces: 5 2 8 7
    # invalid matrix 2: (numbers only, from top left to bottom right, separated by spaces: 9 5 2 8 2 7 6 3 1
    # result: False, the matrices are not the same size

# Test the subtractMatrices function on two 2x2 matrices (valid).
    # EX:
    # valid matrix: numbers only, from top left to bottom right, separated by spaces: 5 2 8 7
    # valid matrix 2: numbers only, from top left to bottom right, separated by spaces: 3 1 6 4
    # result: [[2, 1], [2, 3]]

# Test the subtractMatrices function on two 3x3 matrices (valid).
    # EX:
    # valid matrix: numbers only, from top left to bottom right, separated by spaces: 9 5 2 8 2 7 6 3 1
    # valid matrix 2: numbers only, from top left to bottom right, separated by spaces: 2 3 1 6 9 4 5 2 0
    # result: [[7, 2, 1], [2, -7, 3], [1, 1, 1]]

# Test the subtractMatrices function on a 2x2 matrix and a 3x3 matrix (invalid).
    # EX:
    # valid matrix: numbers only, from top left to bottom right, separated by spaces: 5 2 8 7
    # invalid matrix 2: numbers only, from top left to bottom right, separated by spaces: 9 5 2 8 2 7 6 3 1
    # result: False, the matrices are not the same size

# Write an end message to the user.
print("Thank you for using the SimpleMatrix program!")