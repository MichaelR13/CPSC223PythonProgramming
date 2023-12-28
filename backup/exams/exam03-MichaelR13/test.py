import unittest
#from unittest.mock import patch
from simplematrix import *


class Test01_SetA_Valid(unittest.TestCase):
    def test_list_int(self):
        sm = SimpleMatrix()
        r = sm.setA([[1,2],[3,4]])
        self.assertEqual(r, True)

class Test02_SetA_NotSquare(unittest.TestCase):
    def test_list_int(self):
        sm = SimpleMatrix()
        r = sm.setA([[1,2],[3,4,5]])
        self.assertEqual(r, False)

class Test03_SetA_NotIntegers(unittest.TestCase):
    def test_list_int(self):
        sm = SimpleMatrix()
        r = sm.setA([[1,2],[3.1,4]])
        self.assertEqual(r, False)

class Test04_SetB_Valid(unittest.TestCase):
    def test_list_int(self):
        sm = SimpleMatrix()
        r = sm.setB([[1,2],[3,4]])
        self.assertEqual(r, True)

class Test05_SetB_NotSquare(unittest.TestCase):
    def test_list_int(self):
        sm = SimpleMatrix()
        r = sm.setB([[1,2],[3,4,5]])
        self.assertEqual(r, False)

class Test06_SetB_NotIntegers(unittest.TestCase):
    def test_list_int(self):
        sm = SimpleMatrix()
        r = sm.setB([[1,2],[3.1,4]])
        self.assertEqual(r, False)

class Test07_AddMatrices_Valid2x2(unittest.TestCase):
    def test_list_int(self):
        sm = SimpleMatrix()
        sm.setA([[5,2],[8,7]])
        sm.setB([[3,1],[6,4]])
        r = sm.addMatrices()
        self.assertEqual(r, [[8, 3], [14, 11]])

class Test08_AddMatrices_Valid3x3(unittest.TestCase):
    def test_list_int(self):
        sm = SimpleMatrix()
        sm.setA([[9,5,2],[8,2,7],[6,3,1]])
        sm.setB([[2,3,1],[6,9,4],[5,2,0]])
        r = sm.addMatrices()
        self.assertEqual(r, [[11, 8, 3], [14, 11, 11], [11, 5, 1]])

class Test09_AddMatrices_InvalidNotSameSizes(unittest.TestCase):
    def test_list_int(self):
        sm = SimpleMatrix()
        sm.setA([[5,2],[8,7]])
        sm.setB([[2,3,1],[6,9,4],[5,2,0]])
        r = sm.addMatrices()
        self.assertEqual(r, False)

class Test10_SubtractMatrices_Valid2x2(unittest.TestCase):
    def test_list_int(self):
        sm = SimpleMatrix()
        sm.setA([[5,2],[8,7]])
        sm.setB([[3,1],[6,4]])
        r = sm.subtractMatrices()
        self.assertEqual(r, [[2, 1], [2, 3]])

class Test11_SubtractMatrices_Valid3x3(unittest.TestCase):
    def test_list_int(self):
        sm = SimpleMatrix()
        sm.setA([[9,5,2],[8,2,7],[6,3,1]])
        sm.setB([[2,3,1],[6,9,4],[5,2,0]])
        r = sm.subtractMatrices()
        self.assertEqual(r, [[7, 2, 1], [2, -7, 3], [1, 1, 1]])

class Test12_SubtractMatrices_InvalidNotSameSizes(unittest.TestCase):
    def test_list_int(self):
        sm = SimpleMatrix()
        sm.setA([[5,2],[8,7]])
        sm.setB([[2,3,1],[6,9,4],[5,2,0]])
        r = sm.subtractMatrices()
        self.assertEqual(r, False)

if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
