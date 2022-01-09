import unittest
from sorts import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        '''Given test'''
        nums = [23, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

    def test_selection_01(self):
        '''Testing slightly larger list'''
        nums = [23, 7, 13, 5]
        comps = selection_sort(nums)
        self.assertEqual(comps, 6)
        self.assertEqual(nums, [5, 7, 13, 23])

    def test_selection_02(self):
        '''Testing list with duplicate numbers'''
        nums = [1, 2, 2, 1, 0, 0, 15, 15]
        comps = selection_sort(nums)
        self.assertEqual(comps, 28)
        self.assertEqual(nums, [0, 0, 1, 1, 2, 2, 15, 15])

    def test_selection_03(self):
        '''Testing empty list and list with one integer'''
        nums = []
        comps = selection_sort(nums)
        self.assertEqual(comps, 0)
        self.assertEqual(nums, [])

        nums = [1]
        comps = selection_sort(nums)
        self.assertEqual(comps, 0)
        self.assertEqual(nums, [1])

    def test_simple2(self):
        '''simple test for insertion'''
        nums = [23, 10]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 3)
        self.assertEqual(nums, [10, 23])

    def test_insertion_01(self):
        '''Testing slightly larger list'''
        nums = [23, 7, 13, 5]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 9)
        self.assertEqual(nums, [5, 7, 13, 23])

    def test_insertion_02(self):
        '''Testing list with duplicate numbers'''
        nums = [1, 2, 2, 1, 0, 0, 15, 15]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 18)
        self.assertEqual(nums, [0, 0, 1, 1, 2, 2, 15, 15])

    def test_insertion_03(self):
        '''Testing empty list and list with one integer'''
        nums = []
        comps = insertion_sort(nums)
        self.assertEqual(comps, 0)
        self.assertEqual(nums, [])

        nums = [1]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [1])

    def test_worst_cases(self):
        '''The worst case for both insertion and selection sort is when the list is in decreasing order'''
        nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        comps = selection_sort(nums)
        self.assertEqual(comps, 45)
        self.assertEqual(nums, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 55)
        self.assertEqual(nums, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])



if __name__ == '__main__': 
    unittest.main()
