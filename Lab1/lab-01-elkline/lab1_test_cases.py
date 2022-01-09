import unittest
from lab1 import *


# A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """tests that the function raises a ValueError if the list is None"""
        tList = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tList)
        """tests that the function returns the max value if in the middle of the list"""
        tlist = [4, 7, 3, 9, 1, 2, 5]
        self.assertEqual(max_list_iter(tlist), 9)
        """tests that the function returns the max value if on either end of the list"""
        tlist = [4, 7, 3, 5, 1, 2, 9]
        self.assertEqual(max_list_iter(tlist), 9)
        tlist = [9, 7, 3, 4, 1, 2, 5]
        self.assertEqual(max_list_iter(tlist), 9)

    def test_reverse_rec(self):
        """tests that the function raises a ValueError if the list is None"""
        tList = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tList)
        """tests if the function successfully reverses a list"""
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])

        """tests if the function successfully reverses a list that is already reversed"""
        self.assertEqual(reverse_rec([3, 2, 1]), [1, 2, 3])

    def test_bin_search(self):
        """tests the function bin_search as defined in lab1.py"""
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(4, low, high, list_val), 4)


if __name__ == "__main__":
    unittest.main()
