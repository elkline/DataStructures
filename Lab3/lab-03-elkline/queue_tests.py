import unittest


from queue_array import Queue

# from queue_linked import Queue
# from queue_linked import Node


class TestLab1(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        q.dequeue()
        q.size()

    def test_queue_01(self):
        '''Testing size function'''
        q = Queue(5)
        q.enqueue('thing')
        self.assertEqual(q.size(), 1)

        q.dequeue()
        self.assertEqual(q.size(), 0)
        self.assertEqual(q.is_empty(), True)

    def test_queue_02(self):
        '''Testing is_empty and is_full'''
        q = Queue(2)
        q.enqueue('thing')
        self.assertEqual(q.is_full(), False)
        self.assertEqual(q.is_empty(), False)

        q.enqueue('thing2')
        self.assertEqual(q.is_full(), True)

        q.dequeue()
        q.dequeue()
        self.assertEqual(q.is_empty(), True)

    def test_queue_03(self):
        '''Testing that dequeue and enqueue return and add the correct values'''
        q = Queue(5)
        q.enqueue('thing1')
        q.enqueue('thing2')

        self.assertEqual(q.dequeue(), 'thing1')
        self.assertEqual(q.dequeue(), 'thing2')

    def test_queue_04(self):
        '''Testing IndexError within dequeue and enqueue'''
        q = Queue(2)
        q.enqueue('thing')
        q.enqueue('thing2')
        self.assertRaises(IndexError, q.enqueue, 'thing3')

        q.dequeue()
        q.dequeue()
        self.assertRaises(IndexError, q.dequeue)


# tests from log

    def test_everything_and_big_O(self):
        size = 50000
        q = Queue(size)
        for i in range(size):
            q.enqueue(i)
        for i in range(size):
            self.assertEqual(q.dequeue(), i)
            q.enqueue(i)

    def test_queue_fill_to_capacity(self):
        q = Queue(5)
        q.enqueue(None)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(None)
        self.assertTrue(q.is_full())
        self.assertEqual(q.size(), 5)
        self.assertEqual(q.dequeue(), None)
        self.assertEqual(q.dequeue(), 2)

    def test_queue_fill_to_capacity_and_dequeue_all(self):
        q = Queue(5)
        q.enqueue(1)
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.size(), 0)
        self.assertRaises(IndexError, q.dequeue)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)
        self.assertRaises(IndexError, q.enqueue, 6)
        self.assertEqual(q.size(), 5)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)

    def test_queue_simple(self):
        q = Queue(5)
        q.enqueue(1)
        self.assertEqual(q.size(), 1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)
        self.assertEqual(q.size(), 5)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)


if __name__ == '__main__':
    unittest.main()
