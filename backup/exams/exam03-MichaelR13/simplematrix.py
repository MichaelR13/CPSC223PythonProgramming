class SimpleMatrix:
    def setA(self, a):  
        # Accept a matrix as a list positional parameter.
        self.a = a
        # If the list does not represent a square matrix (i.e. 2x2 or 3x3) or any of the elements of the list are not integers, return a False.
        if not all(isinstance(row, list) and len(row) == len(a) and all(isinstance(item, int) for item in row) for row in a):   
            # checks if each row is a list, and if the length is the same as the length of the list (also checks for data type)
            return False
        # Otherwise store the list for future adds or subtracts and return a True.
        else:
            return True
    
    def setB(self, b):
        # Accept a matrix as a list positional parameter.
        self.b = b
        # If the list does not represent a square matrix (i.e. 2x2 or 3x3) or any of the elements of the list are not integers, return a False.
        if not all(isinstance(row, list) and len(row) == len(b) and all(isinstance(item, int) for item in row) for row in b):   
            # checks if each row is a list, and if the length is the same as the length of the list (also checks for data type)
            return False
        # Otherwise store the list for future adds or subtracts and return a True.
        else:
            return True
       
    def addMatrices(self):
        # If the lists stored from setA and setB do not represent the same size matrices then return a False.
        if len(self.a) != len(self.b):
            return False
        # Otherwise create and return a new list that represents the matrix from setA plus the matrix from setB.
        else:
            self.c = [] # Create a new list to store the result.
            for i in range(len(self.a)):
                row = []
                for j in range(len(self.a[0])):
                    row.append(self.a[i][j] + self.b[i][j]) # Add the two values and append the result to the row.
                self.c.append(row)
            return self.c
        
    def subtractMatrices(self):
        # If the lists stored from setA and setB do not represent the same size matrices then return a False.
        if len(self.a) != len(self.b):
            return False
        # Otherwise create and return a new list that represents the matrix from setA minus the matrix from setB.
        else:
            self.c = [] # Create a new list to store the result.
            for i in range(len(self.a)):
                row = []
                for j in range(len(self.a[0])):
                    row.append(self.a[i][j] - self.b[i][j]) # Subtract the two values and append the result to the row.
                self.c.append(row)
            return self.c