import unittest
from binary_search_tree import *


class TestLab4(unittest.TestCase):

    def test_simple(self):
        '''Given Tests'''
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'stuff')
        self.assertTrue(bst.search(10))
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        bst.insert(10, 'other')
        self.assertEqual(bst.find_max(), (10, 'other'))
        self.assertEqual(bst.tree_height(), 0)
        self.assertEqual(bst.inorder_list(), [10])
        self.assertEqual(bst.preorder_list(), [10])
        self.assertEqual(bst.level_order_list(), [10])

    def test_01(self):
        '''Testing one-sided BST'''
        bst = BinarySearchTree()
        bst.insert(10, 'stuff')
        bst.insert(20, 'other')
        bst.insert(30, 'more')
        self.assertTrue(bst.search(20))
        self.assertEqual(bst.find_max(), (30, 'more'))
        self.assertEqual(bst.tree_height(), 2)
        self.assertEqual(bst.inorder_list(), [10, 20, 30])
        self.assertEqual(bst.preorder_list(), [10, 20, 30])
        self.assertEqual(bst.level_order_list(), [10, 20, 30])

    def test_02(self):
        bst = BinarySearchTree()
        bst.insert(10, 'stuff')
        bst.insert(20, 'other')
        bst.insert(5, 'more')
        bst.insert(15, 'even more')
        bst.insert(30, 'end')
        self.assertEqual(bst.find_max(), (30, 'end'))
        self.assertEqual(bst.tree_height(), 2)
        self.assertEqual(bst.inorder_list(), [5, 10, 15, 20, 30])
        self.assertEqual(bst.preorder_list(), [10, 5, 20, 15, 30])
        self.assertEqual(bst.level_order_list(), [10, 5, 20, 15, 30])


if __name__ == '__main__':
    unittest.main()
