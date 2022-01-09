import unittest

# Use the imports below to test either your array-based stack
# or your link-based version


from stack_array import Stack
# from stack_linked import Stack

class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())

        # testing size() function
        self.assertEqual(stack.size(), 1)

    def test_pop(self):
        stack = Stack(3)
        stack.push(0)
        stack.push(3)
        stack.push(2)

        # testing is_full() function
        self.assertTrue(stack.is_full())

        # testing that pop() returns correct value and changes the size
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.size(), 2)

    def test_peek(self):
        stack = Stack(3)
        stack.push(0)
        stack.push(3)
        stack.push(2)
        self.assertTrue(stack.is_full())

        # testing that peek function returns correct value but doesn't change size
        self.assertEqual(stack.peek(), 2)
        self.assertTrue(stack.is_full())

# tests from log

    def test_everything(self):
        s = Stack(100)
        for i in range(100):
            s.push(None)

    def test_is_empty_is_full_BigO(self):
        size = 100000
        s = Stack(size)
        for i in range(size):
            self.assertFalse(s.is_full())
            s.push(i)

    def test_is_full(self):
        stack = Stack(5)
        self.assertFalse(stack.is_full())
        stack.push(11)
        stack.push(12)
        stack.push(13)
        stack.push(14)
        stack.push(15)

    def test_peek_size_BigO(self):
        size = 100000
        s = Stack(size)
        for i in range(size):
            self.assertEqual(i, s.size())
            s.push(i)
            self.assertEqual(i, s.peek())

    def test_pop(self):
        stack = Stack(5)
        self.assertRaises(IndexError, stack.pop)
        self.assertEqual(stack.size(), 0)  # Make sure trying to pop on empty stack didn't have an effect
        self.assertTrue(stack.is_empty())
        self.assertFalse(stack.is_full())
        stack.push(11)
        stack.push(12)
        stack.push(13)
        stack.push(14)
        stack.push(15)

    def test_pop_BigO(self):
        size = 100000
        s = Stack(size)
        for i in range(size):
            s.push(i)

    def test_push(self):
        stack = Stack(5)
        stack.push(11)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.peek(), 11)

    def test_size(self):
        stack = Stack(5)
        self.assertEqual(stack.size(), 0)
        stack.push(11)
        self.assertEqual(stack.size(), 1)
        stack.push(12)
        self.assertEqual(stack.size(), 2)
        stack.push(13)
        self.assertEqual(stack.size(), 3)
        stack.push(14)
        self.assertEqual(stack.size(), 4)
        stack.push(15)

    def test_stack_one(self):  # boundary case
        stack = Stack(1)
        self.assertRaises(IndexError, stack.pop)
        self.assertRaises(IndexError, stack.peek)
        self.assertTrue(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(), 0)
        stack.push(11)

    def test_stack_pushPopCombo_with_strings_and_floats_and_Nones(self):
        s = Stack(11)
        s.push('stuff')
        self.assertEqual(1, s.size())
        self.assertEqual('stuff', s.peek())



if __name__ == '__main__':
    unittest.main()
