import unittest
from heap import *
import random
import math


class TestHeap(unittest.TestCase):

    def test_01_enqueue(self):
        test_heap = MaxHeap(7)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        insert = test_heap.enqueue(10)
        self.assertTrue(insert)
        self.assertEqual(test_heap.contents(), [10, 6, 9, 2, 5, 7, 8])

    def test_02_dequeue(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.dequeue(), 9)
        self.assertEqual(test_heap.get_size(), 5)
        self.assertEqual(test_heap.contents(), [8, 6, 7, 2, 5])

    def test_03_heap_contents(self):
        test_heap = MaxHeap(8)
        test_heap.build_heap([1, 2, 3])
        self.assertEqual(test_heap.contents(), [3, 2, 1])

    def test_04_build_heap(self):
        test_heap = MaxHeap(10)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

    def test_05_is_empty(self):
        test_heap = MaxHeap(5)
        self.assertTrue(test_heap.is_empty())

    def test_06_is_full(self):
        test_heap = MaxHeap(2)
        built = test_heap.build_heap([1, 2, 3, 4, 5])
        self.assertTrue(test_heap.is_full())

    def test_07_get_heap_cap(self):
        test_heap = MaxHeap(7)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        insert = test_heap.enqueue(10)
        self.assertEqual(test_heap.get_capacity(), 7)

    def test_08_get_size(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.get_size(), 6)

    def test_09_perc_down(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 8, 6, 5, 7])
        test_heap.perc_down(1)
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

    def test_10_perc_up(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 8, 6, 5, 7])
        test_heap.perc_up(6)
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

    def test_11_heap_sort_ascending(self):
        test_heap = MaxHeap()
        list1 = [2, 9, 7, 6, 5, 8]
        test_heap.heap_sort_ascending(list1)
        self.assertEqual(list1, [2, 5, 6, 7, 8, 9])


# tests from log

    def test_01_peek_and_dequeue_1_item(self):
        test_heap = MaxHeap(10)
        test_heap.enqueue(25)
        self.assertEqual(test_heap.peek(), 25)

    def test_02_dequeue_2_item(self):
        test_heap = MaxHeap(10)
        test_heap.enqueue(25)
        test_heap.enqueue(5)
        self.assertEqual(test_heap.dequeue(), 25)

    def test_03_enqueue1(self):
        test_heap = MaxHeap(7)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertTrue(test_heap.enqueue(10))

    def test_05_insert3(self):
        test_heap = MaxHeap()
        test_heap.build_heap([3, 4, 5, 6, 7, 10, 8, 1, 2])
        self.assertTrue(test_heap.enqueue(15))

    def test_06_find_max1(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        test_heap.enqueue(10)
        self.assertEqual(test_heap.dequeue(), 10)

    def test_08_del_max1(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.dequeue(), 9)

    def test_09_del_max2(self):
        test_heap = MaxHeap()
        test_heap.build_heap([3, 4, 5, 6, 7, 10, 8, 1, 2])
        insert = test_heap.enqueue(15)
        self.assertEqual(test_heap.dequeue(), 15)

    def test_10_heap_contents1(self):
        test_heap = MaxHeap(8)
        test_heap.build_heap([1, 2, 3])
        self.assertEqual(test_heap.contents(), [3, 2, 1])

    def test_11_heap_contents2(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

    def test_12_build_heap1(self):
        test_heap = MaxHeap(8)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

    def test_13_build_heap2(self):
        test_heap = MaxHeap(3)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

    def test_14_build_heap3(self):
        test_heap = MaxHeap()
        test_heap.build_heap([3, 4, 5, 6, 7, 10, 8, 1, 2])
        self.assertEqual(test_heap.contents(), [10, 7, 8, 6, 4, 5, 3, 1, 2])

    def test_15_is_empty1(self):
        test_heap = MaxHeap(5)
        self.assertTrue(test_heap.is_empty())

    def test_16_is_full1(self):
        test_heap = MaxHeap(5)
        test_heap.build_heap([1, 2, 3, 4, 5])
        self.assertTrue(test_heap.is_full())

    def test_17_get_heap_cap1(self):
        test_heap = MaxHeap(7)
        self.assertEqual(test_heap.get_capacity(), 7)

    def test_18_get_heap_size1(self):
        test_heap = MaxHeap()
        self.assertEqual(test_heap.get_size(), 0)

    def test_19_perc_down_and_up(self):
        '''No real way to test these, but should have no affect on heap'''
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 8, 6, 5, 7])
        test_heap.perc_down(1)
        test_heap.perc_down(2)
        test_heap.perc_down(3)
        test_heap.perc_down(4)
        test_heap.perc_down(5)
        test_heap.perc_down(6)
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

    def test_20_heap_sort_increase1(self):
        test_heap = MaxHeap()
        list1 = [2, 9, 7, 6, 5, 8]
        test_heap.heap_sort_ascending(list1)
        self.assertEqual(list1, [2, 5, 6, 7, 8, 9])

    def test_21_heap_sort_increase2(self):
        test_heap = MaxHeap()
        list1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        test_heap.heap_sort_ascending(list1)
        self.assertEqual(list1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_22_duplicate_keys(self):
        test_heap = MaxHeap()
        list1 = [28, 41, 41]
        test_heap.build_heap(list1)
        contents = test_heap.contents()
        self.assertTrue(contents == [41, 28, 41] or contents == [41, 41, 28])

    def test_23_negative_keys(self):
        q = MaxHeap()
        q.enqueue(-937)
        self.assertEqual(1, q.get_size())

    def test_24_string_keys(self):
        q = MaxHeap()
        words = ['hello', 'this', 'is', 'a', 'list', 'of', 'strings']
        q.build_heap(words)
        words.sort(reverse=True)
        for i in range(len(words)):
            self.assertEqual(q.peek(), words[i])

    def test_25_object_keys(self):
        q = MaxHeap()
        vals = [TestVal(45), TestVal(4.5), TestVal(1.45), TestVal(5), TestVal(4), TestVal(0), TestVal(2.34)]
        q.build_heap(vals)
        vals.sort(reverse=True)
        for i in range(len(vals)):
            self.assertEqual(q.peek(), vals[i])

    def test_01_big_Oh(self):
        sizes = [100, 1000, 10000]
        random.seed(1234)

        for size in sizes:
            log_2_size = int(math.floor(math.log(size, 2)))
            test_heap = MaxHeap(size)
            randoms = random.sample(range(1000000), size)
            for i in range(size):
                test_heap.enqueue(randoms[i])
            randoms.sort(reverse=True)
            for i in range(size):
                for j in range(log_2_size):
                    self.assertEqual(test_heap.peek(), randoms[i])


if __name__ == "__main__":
    unittest.main()
