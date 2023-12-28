import unittest
import io
import sys
from unittest.mock import patch
import manifest
import copy

master = [
['1A', '', '', False, 0, False],
['1B', '', '', False, 0, False],
['1C', '', '', False, 0, False],
['2A', 'Richard', 'Stallman', True, 0, True],
['2B', 'john', 'stallman', True, 0, True],
['2C', '', '', False, 0, False],
['3A', '', '', False, 0, False],
['3B', '', '', False, 0, False],
['3C', 'Becky', 'Evans', False, 0, False],
['4A', '', '', False, 0, False],
['4B', 'Jane', 'Doe', True, 2, False],
['4C', '', '', False, 0, False],
['5A', '', '', False, 0, False],
['5B', '', '', False, 0, False],
['5C', '', '', False, 0, False],
['6A', 'Bob', 'Eckart', True, 1, False],
['6B', 'Steve', 'Jobs', True, 2, False],
['6C', 'Todd', 'McEntee', True, 1, False],
['7A', '', '', False, 0, False],
['7B', 'Bill', 'Gates', False, 0, False],
['7C', '', '', False, 0, False],
['8A', 'Becky', 'Simpson', True, 1, True],
['8B', '', '', False, 0, False],
['8C', 'George', 'Mason', True, 1, True],
['9A', '', '', False, 0, False],
['9B', '', '', False, 0, False],
['9C', '', '', False, 0, False],
]


class Test01_get_passenger_manifest(unittest.TestCase):
    def test_list_int(self):
        m = copy.deepcopy(master)
        r = manifest.get_passenger_manifest(manifest=m)
        t = [['Doe', 'Jane', '4B', True, 2, False], ['Eckart', 'Bob', '6A', True, 1, False], ['Evans', 'Becky', '3C', False, 0, False], ['Gates', 'Bill', '7B', False, 0, False], ['Jobs', 'Steve', '6B', True, 2, False], ['Mason', 'George', '8C', True, 1, True], ['McEntee', 'Todd', '6C', True, 1, False], ['Simpson', 'Becky', '8A', True, 1, True], ['stallman', 'john', '2B', True, 0, True], ['Stallman', 'Richard', '2A', True, 0, True]]
        self.assertEqual(r, t)

class Test02_purchase_ticket_success(unittest.TestCase):
    def test_list_int(self):
        m = copy.deepcopy(master)
        fn = 'Steve'
        ln = 'May'
        s = '1a'
        r = manifest.purchase_ticket(manifest=m, first_name=fn, last_name=ln, seat=s)
        seat1A = m[0]
        t = ['1A', 'Steve', 'May', False, 0, False]
        self.assertEqual(seat1A, t)

class Test03_purchase_ticket_fail_seat_taken(unittest.TestCase):
    def test_list_int(self):
        m = copy.deepcopy(master)
        fn = 'Steve'
        ln = 'May'
        s = '2a'
        r = manifest.purchase_ticket(manifest=m, first_name=fn, last_name=ln, seat=s)
        self.assertEqual(r, False)

class Test04_purchase_ticket_fail_invalid_seat(unittest.TestCase):
    def test_list_int(self):
        m = copy.deepcopy(master)
        fn = 'Steve'
        ln = 'May'
        s = '1d'
        r = manifest.purchase_ticket(manifest=m, first_name=fn, last_name=ln, seat=s)
        self.assertEqual(r, False)

class Test05_cancel_ticket_success(unittest.TestCase):
    def test_list_int(self):
        m = copy.deepcopy(master)
        s = '6c'
        r = manifest.cancel_ticket(manifest=m, seat=s)
        seat6c = m[17]
        t = ['6C', '', '', False, 0, False]
        self.assertEqual(seat6c, t)

class Test06_cancel_ticket_fail_seat_not_assigned(unittest.TestCase):
    def test_list_int(self):
        m = copy.deepcopy(master)
        s = '1a'
        r = manifest.cancel_ticket(manifest=m, seat=s)
        self.assertEqual(r, False)

class Test07_cancel_ticket_fail_invalid_seat(unittest.TestCase):
    def test_list_int(self):
        m = copy.deepcopy(master)
        s = '1d'
        r = manifest.cancel_ticket(manifest=m, seat=s)
        self.assertEqual(r, False)

class Test08_check_in_success(unittest.TestCase):
    def test_list_int(self):
        m = copy.deepcopy(master)
        s = '3c'
        r = manifest.check_in(manifest=m, seat=s)
        seat3c = m[8]
        t = ['3C', 'Becky', 'Evans', True, 0, False]
        self.assertEqual(seat3c, t)

class Test09_check_in_fail_seat_not_assigned(unittest.TestCase):
    def test_list_int(self):
        m = copy.deepcopy(master)
        s = '1a'
        r = manifest.check_in(manifest=m, seat=s)
        self.assertEqual(r, False)

class Test10_check_in_fail_invalid_seat(unittest.TestCase):
    def test_list_int(self):
        m = copy.deepcopy(master)
        s = '1d'
        r = manifest.check_in(manifest=m, seat=s)
        self.assertEqual(r, False)

class Test11_check_bags_success(unittest.TestCase):
    def test_list_int(self):
        m = copy.deepcopy(master)
        s = '2a'
        r = manifest.check_bags(manifest=m, seat=s, no_bags=3)
        seat2a = m[3]
        t = ['2A', 'Richard', 'Stallman', True, 3, True]
        self.assertEqual(seat2a, t)

class Test12_check_bags_fail_seat_not_assigned(unittest.TestCase):
    def test_list_int(self):
        m = copy.deepcopy(master)
        s = '1a'
        r = manifest.check_bags(manifest=m, seat=s, no_bags=3)
        self.assertEqual(r, False)

class Test13_check_bags_fail_invalid_seat(unittest.TestCase):
    def test_list_int(self):
        m = copy.deepcopy(master)
        s = '1d'
        r = manifest.check_bags(manifest=m, seat=s, no_bags=3)
        self.assertEqual(r, False)

class Test14_check_bags_fail_passenger_not_checked_in(unittest.TestCase):
    def test_list_int(self):
        m = copy.deepcopy(master)
        s = '3c'
        r = manifest.check_bags(manifest=m, seat=s, no_bags=3)
        self.assertEqual(r, False)


class Test15_board_aircraft_success(unittest.TestCase):
    def test_list_int(self):
        m = copy.deepcopy(master)
        s = '4b'
        r = manifest.board_aircraft(manifest=m, seat=s)
        seat4b = m[10]
        t = ['4B', 'Jane', 'Doe', True, 2, True]
        self.assertEqual(seat4b, t)

class Test16_board_aircraft_fail_seat_not_assigned(unittest.TestCase):
    def test_list_int(self):
        m = copy.deepcopy(master)
        s = '1a'
        r = manifest.board_aircraft(manifest=m, seat=s)
        self.assertEqual(r, False)

class Test17_board_aircraft_fail_invalid_seat(unittest.TestCase):
    def test_list_int(self):
        m = copy.deepcopy(master)
        s = '1d'
        r = manifest.board_aircraft(manifest=m, seat=s)
        self.assertEqual(r, False)

class Test18_board_aircraft_fail_passenger_not_checked_in(unittest.TestCase):
    def test_list_int(self):
        m = copy.deepcopy(master)
        s = '3c'
        r = manifest.board_aircraft(manifest=m, seat=s)
        self.assertEqual(r, False)

if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
