'''
This file includes test cases for the SimpleInteger class in the si module.

These tests cover various scenarios for the add, subtract, multiply, isequal, and isgreaterthan methods.

Test01_add_valid_data: int + int = int
Test02_add_invalid_data: float + int (Invalid)
Test03_subtract_valid_data: int - int = int
Test04_subtract_invalid_data: float - int (Invalid)
Test05_multiply_valid_data: int * int = int
Test06_multiply_invalid_data: float * int (Invalid)
Test07_isequal_valid_true_data: int == int (True)
Test08_isequal_valid_false_data: int == int (False)
Test09_isequal_invalid_data: float == int (Invalid)
Test10_isgreaterthan_valid_true_data: int > int (True)
Test11_isgreaterthan_valid_false_data: int > int (False)
Test12_isgreaterthan_invalid_data: float > int (Invalid)

The module also includes code at the bottom that will run the tests and write the results to a 'test.txt' file.
'''
# Import modules
import unittest
import io
import si

class Test01_add_valid_data(unittest.TestCase):
    def test_list_int(self):
        obj = si.SimpleInteger()
        result = obj.add(1,2)   # int + int
        self.assertEqual(3, result)
    
class Test02_add_invalid_data(unittest.TestCase):
    def test_list_int(self):
        obj = si.SimpleInteger()
        result = obj.add(1.5,2) # float + int
        self.assertEqual(None, result)

class Test03_subtract_valid_data(unittest.TestCase):
    def test_list_int(self):
        obj = si.SimpleInteger()
        result = obj.subtract(3,7)  # int - int
        self.assertEqual(-4, result)

class Test04_subtract_invalid_data(unittest.TestCase):
    def test_list_int(self):
        obj = si.SimpleInteger()
        result = obj.subtract(3.5,7) # float - int
        self.assertEqual(None, result)
    
class Test05_multiply_valid_data(unittest.TestCase):
    def test_list_int(self):
        obj = si.SimpleInteger()
        result = obj.multiply(5,3)  # int * int
        self.assertEqual(15, result)

class Test06_multiply_invalid_data(unittest.TestCase):
    def test_list_int(self):
        obj = si.SimpleInteger()
        result = obj.multiply(5.5,3)    # float * int
        self.assertEqual(None, result)

class Test07_isequal_valid_true_data(unittest.TestCase):
    def test_list_int(self):
        obj = si.SimpleInteger()
        result = obj.isequal(7,7)   # int == int
        self.assertEqual(True, result)
    
class Test08_isequal_valid_false_data(unittest.TestCase):
    def test_list_int(self):
        obj = si.SimpleInteger()
        result = obj.isequal(7,8)   # int == int
        self.assertEqual(False, result) # int != int

class Test09_isequal_invalid_data(unittest.TestCase):
    def test_list_int(self):
        obj = si.SimpleInteger()
        result = obj.isequal(7.5,7) # float == int
        self.assertEqual(None, result)

class Test10_isgreaterthan_valid_true_data(unittest.TestCase):
    def test_list_int(self):
        obj = si.SimpleInteger()
        result = obj.isgreaterthan(10,6)    # int > int
        self.assertEqual(True, result)
    
class Test11_isgreaterthan_valid_false_data(unittest.TestCase):
    def test_list_int(self):
        obj = si.SimpleInteger()
        result = obj.isgreaterthan(10,10)   # int > int
        self.assertEqual(False, result) # int !> int
    
class Test12_isgreaterthan_invalid_data(unittest.TestCase):
    def test_list_int(self):
        obj = si.SimpleInteger() 
        result = obj.isgreaterthan(10.5,6)  # float > int
        self.assertEqual(None, result)

# Include the following code at the bottom of the module file:
if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)