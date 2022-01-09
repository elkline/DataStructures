import unittest
from ordered_list import *


class TestLab4(unittest.TestCase):

    def test_simple(self):
        '''Given Tests'''
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)

    def test_01(self):
        '''Testing a longer list'''
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(20)
        t_list.add(30)
        self.assertEqual(t_list.python_list(), [10, 20, 30])
        self.assertEqual(t_list.size(), 3)
        self.assertEqual(t_list.index(20), 1)
        self.assertFalse(t_list.is_empty())
        self.assertTrue(t_list.remove(20))
        self.assertFalse(t_list.add(10))
        self.assertEqual(t_list.pop(0), 10)

    def test_03(self):
        '''Testing that the elements are added in order'''
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(30)
        t_list.add(20)
        self.assertEqual(t_list.python_list(), [10, 20, 30])
        self.assertEqual(t_list.size(), 3)
        self.assertEqual(t_list.index(20), 1)
        self.assertEqual(t_list.python_list_reversed(), [30, 20, 10])

    def test_04(self):
        '''Testing IndexError in pop'''
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(30)
        t_list.add(20)
        self.assertRaises(IndexError, t_list.pop, 3)
        self.assertRaises(IndexError, t_list.pop, -1)

        t_list2 = OrderedList()
        self.assertRaises(IndexError, t_list2.pop, 0)


# tests from log

    def test_02a_add(self):
        t_list = OrderedList()
        self.assertTrue(t_list.add(10))
        self.assertFalse(t_list.add(10))
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertFalse(t_list.is_empty())
        self.assertTrue(t_list.add(20))
        self.assertFalse(t_list.add(20))
        self.assertEqual(t_list.python_list(), [10, 20])
        self.assertEqual(t_list.python_list_reversed(), [20, 10])
        self.assertEqual(t_list.size(), 2)

    def test_02a_add2(self):
        t_list = OrderedList()
        self.assertTrue(t_list.add(10))
        self.assertFalse(t_list.add(10))
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertFalse(t_list.is_empty())
        self.assertTrue(t_list.add(20))
        self.assertFalse(t_list.add(20))
        self.assertEqual(t_list.python_list(), [10, 20])
        self.assertEqual(t_list.python_list_reversed(), [20, 10])
        self.assertEqual(t_list.size(), 2)
        self.assertTrue(t_list.add(30))
        self.assertFalse(t_list.add(30))
        self.assertEqual(t_list.python_list(), [10, 20, 30])
        self.assertEqual(t_list.size(), 3)
        self.assertTrue(t_list.add(5))
        self.assertFalse(t_list.add(5))
        self.assertEqual(t_list.python_list(), [5, 10, 20, 30])
        self.assertEqual(t_list.size(), 4)
        self.assertTrue(t_list.add(15))
        self.assertFalse(t_list.add(15))
        self.assertEqual(t_list.python_list(), [5, 10, 15, 20, 30])
        self.assertEqual(t_list.python_list_reversed(), [30, 20, 15, 10, 5])
        self.assertEqual(t_list.size(), 5)

    def test_02a_add_HuffmanNodes(self):
            t_list = OrderedList()
            self.assertTrue(t_list.add(HuffmanNode('a', 10)))
            self.assertFalse(t_list.add(HuffmanNode('a', 10)))
            self.assertEqual(t_list.python_list(), [HuffmanNode('a', 10)])
            self.assertEqual(t_list.size(), 1)
            self.assertFalse(t_list.is_empty())
            self.assertTrue(t_list.add(HuffmanNode('b', 10)))
            self.assertFalse(t_list.add(HuffmanNode('b', 10)))
            self.assertEqual(t_list.python_list(), [HuffmanNode('a', 10), HuffmanNode('b', 10)])
            self.assertEqual(t_list.python_list_reversed(), [HuffmanNode('b', 10), HuffmanNode('a', 10)])
            self.assertEqual(t_list.size(), 2)

    def test_02a_add_HuffmanNodes2(self):
        t_list = OrderedList()
        self.assertTrue(t_list.add(HuffmanNode('a', 10)))
        self.assertFalse(t_list.add(HuffmanNode('a', 10)))
        self.assertEqual(t_list.python_list(), [HuffmanNode('a', 10)])
        self.assertEqual(t_list.size(), 1)
        self.assertFalse(t_list.is_empty())
        self.assertTrue(t_list.add(HuffmanNode('b', 10)))
        self.assertFalse(t_list.add(HuffmanNode('b', 10)))
        self.assertEqual(t_list.python_list(), [HuffmanNode('a', 10), HuffmanNode('b', 10)])
        self.assertEqual(t_list.python_list_reversed(), [HuffmanNode('b', 10), HuffmanNode('a', 10)])
        self.assertEqual(t_list.size(), 2)
        self.assertTrue(t_list.add(HuffmanNode('c', 30)))
        self.assertFalse(t_list.add(HuffmanNode('c', 30)))
        self.assertEqual(t_list.python_list(), [HuffmanNode('a', 10), HuffmanNode('b', 10), HuffmanNode('c', 30)])
        self.assertEqual(t_list.size(), 3)
        self.assertTrue(t_list.add(HuffmanNode('d', 5)))
        self.assertFalse(t_list.add(HuffmanNode('d', 5)))
        self.assertEqual(t_list.python_list(),
                         [HuffmanNode('d', 5), HuffmanNode('a', 10), HuffmanNode('b', 10), HuffmanNode('c', 30)])
        self.assertEqual(t_list.size(), 4)
        self.assertTrue(t_list.add(HuffmanNode('e', 15)))
        self.assertTrue(t_list.add(HuffmanNode('f', 15)))
        self.assertEqual(t_list.python_list(),
                         [HuffmanNode('d', 5), HuffmanNode('a', 10), HuffmanNode('b', 10), HuffmanNode('e', 15),
                          HuffmanNode('f', 15), HuffmanNode('c', 30)])
        self.assertEqual(t_list.python_list_reversed(),
                         [HuffmanNode('c', 30), HuffmanNode('f', 15), HuffmanNode('e', 15), HuffmanNode('b', 10),
                          HuffmanNode('a', 10), HuffmanNode('d', 5)])
        self.assertEqual(t_list.size(), 6)



    def test_03_remove(self):
        t_list = OrderedList()
        self.assertFalse(t_list.remove(5))
        self.assertEqual(t_list.size(), 0)
        t_list.add(10)
        t_list.add(20)
        t_list.add(30)
        t_list.add(40)
        t_list.add(50)
        self.assertFalse(t_list.remove(5))

    def test_03a_remove_HuffmanNodes(self):
        t_list = OrderedList()
        self.assertFalse(t_list.remove(5))
        self.assertEqual(t_list.size(), 0)
        t_list.add(HuffmanNode('a', 10))
        t_list.add(HuffmanNode('b', 10))
        t_list.add(HuffmanNode('e', 15))
        t_list.add(HuffmanNode('f', 15))
        t_list.add(HuffmanNode('c', 30))
        self.assertFalse(t_list.remove(HuffmanNode('c', 5)))

    def test_04_index(self):
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(20)
        t_list.add(30)
        t_list.add(40)
        t_list.add(50)
        self.assertEqual(t_list.index(10), 0)

    def test_04a_index_HuffmanNodes(self):
        t_list = OrderedList()
        t_list.add(HuffmanNode('a', 10))
        t_list.add(HuffmanNode('b', 10))
        t_list.add(HuffmanNode('e', 15))
        t_list.add(HuffmanNode('f', 15))
        t_list.add(HuffmanNode('c', 30))
        self.assertEqual(t_list.index(HuffmanNode('a', 10)), 0)

    def test_05_pop(self):
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(20)
        t_list.add(30)
        t_list.add(40)
        t_list.add(50)
        self.assertRaises(IndexError, t_list.pop, -1)
        self.assertEqual(t_list.size(), 5)
        self.assertRaises(IndexError, t_list.pop, 5)
        self.assertEqual(t_list.size(), 5)
        self.assertEqual(t_list.pop(0), 10)
        self.assertEqual(t_list.python_list(), [20, 30, 40, 50])

    def test_07_python_list(self):
        t_list = OrderedList()
        self.assertEqual(t_list.python_list(), [])
        self.assertEqual(t_list.python_list_reversed(), [])
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.python_list_reversed(), [10])
        t_list.add(20)
        self.assertEqual(t_list.python_list(), [10, 20])
        self.assertEqual(t_list.python_list_reversed(), [20, 10])
        t_list.add(30)
        t_list.add(40)
        t_list.add(50)
        self.assertEqual(t_list.python_list(), [10, 20, 30, 40, 50])

    def test_08_size_is_empty(self):
        t_list = OrderedList()
        self.assertEqual(t_list.size(), 0)
        self.assertTrue(t_list.is_empty())
        t_list.add(10)
        self.assertEqual(t_list.size(), 1)
        self.assertFalse(t_list.is_empty())
        t_list.add(20)
        self.assertEqual(t_list.size(), 2)
        self.assertFalse(t_list.is_empty())
        t_list.remove(20)
        self.assertEqual(t_list.size(), 1)

    def test_09_add_remove_all_add(self):
        t_list = OrderedList()
        for val in range(200):
            t_list.add(val)
        for val in range(200):
            self.assertTrue(t_list.remove(val))

    def test_10_add_pop_all_add(self):
        t_list = OrderedList()
        for val in range(200):
            t_list.add(val)
        for val in range(199, -1, -1):
            self.assertEqual(t_list.pop(val), val)
            # self.assertTrue(t_list.is_empty())

    def test_11_add_pop_remove(self):
        t_list = OrderedList()
        for val in range(200):
            t_list.add(val)
        for val in range(100):
            self.assertEqual(t_list.pop(0), val)


if __name__ == '__main__':
    unittest.main()
