class Node:
    '''Node for use with doubly-linked list'''

    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

    def __repr__(self):
        return "({!r}, {!r})".format(self.item, self.next)


class HuffmanNode:
    def __init__(self, char, freq, tree_left=None, tree_right=None, parent=None):
        self.char = char  # stored as an integer - the ASCII character code value
        self.freq = freq  # the frequency associated with the node
        self.left = None  # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right
        self.tree_left = tree_left
        self.tree_right = tree_right
        self.parent = parent
        self.huff = ''

    def __eq__(self, other):
        '''Needed in order to be inserted into OrderedList'''

        if self is None or other is None:
            return False
        if self.char == other.char and self.freq == other.freq:
            return True
        else:
            return False

    def __lt__(self, other):
        '''Needed in order to be inserted into OrderedList'''
        '''Returns True is self should come before other'''

        if self.freq < other.freq:
            return True
        if self.freq == other.freq:
            if self.char < other.char:
                return True
        return False

    def __repr__(self):
        return "Node({!r}, {!r})".format(self.char, self.freq)


class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''

    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           DO NOT have an attribute to keep track of size'''
        # purpose: to hold the head (in prev) and tail of the list (next)

        self.dummy = Node(None)
        # the pointer to the head and tail of the list is stored in this Node
        # self.dummy.prev, self.dummy.next

    def is_empty(self):
        '''Returns True if OrderedList is empty
            MUST have O(1) performance'''
        if self.dummy.prev is None:
            return True
        else:
            return False

    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list) and returns True.
           If the item is already in the list, do not add it again and return False.
           MUST have O(n) average-case performance'''

        if item is HuffmanNode:

            if self.is_empty():  # if the DLL is empty
                self.dummy.left = item
                self.dummy.right = item
                return True
            else:
                index = 0
                n = self.dummy.left
                while n is not None:
                    if item.__lt__(n) and index == 0:  # goes in the front of the OrderedList
                        temp = n

                        item.right = n
                        self.dummy.left = item
                        n.left = item
                        item.left = self.dummy
                        return True

                    if item.__lt__(n):  # if item is less then the current item (goes before)
                        temp = n

                        n.left.right = item
                        item.left = n.left
                        n.left = item
                        item.right = temp
                        return True

                    n = n.right
                    index += 1

                # item must be greater than all the elements, so added to the back of the list
                last_node = self.dummy.right
                last_node.right = item
                item.left = last_node
                self.dummy.right = item
                return True

        else:
            new_node = Node(item)
            if self.is_empty():  # if the DLL is empty
                self.dummy.prev = new_node
                self.dummy.next = new_node
                return True
            else:
                n = self.dummy.prev
                while n is not None:
                    if item == n.item:  # if item is already in the list
                        return False
                    elif item < n.item:  # if item is less then the current item
                        temp = n

                        n.prev.next = new_node  #
                        new_node.prev = n.prev
                        n.prev = new_node
                        new_node.next = temp
                        return True

                    n = n.next

                # item must be greater than all the elements, so added to the back of the list
                last_node = self.dummy.next
                last_node.next = new_node
                new_node.prev = last_node
                self.dummy.next = new_node
                return True

    def remove(self, item):
        '''Removes the first occurrence of an item from OrderedList. If item is removed (was in the list) 
          returns True.  If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        if self.is_empty():
            return False
        else:
            n = self.dummy.prev
            index_of_item = self.index(item)
            while n is not None:  # and n.next is not None:
                if item == n.item:

                    temp = n.next

                    if index_of_item == 0:  # if first element
                        if temp is None:  # if only element in the list
                            self.dummy = Node(None)
                        else:
                            self.dummy.prev = temp
                            temp.prev = self.dummy

                    elif temp is None:  # item is at the end of the list
                        n.prev.next = None
                        self.dummy.next = n.prev

                    else:
                        n.prev.next = temp
                        temp.prev = n.prev

                    # n.prev.next = n.next
                    # n.next.prev = n.prev
                    return True
                n = n.next
            return False

    def index(self, item):
        '''Returns index of the first occurrence of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''

        if self.is_empty():
            return None
        else:
            index = 0
            n = self.dummy.prev
            while n is not None:  # and n.next is not None:
                if item == n.item:
                    return index
                n = n.next
                index += 1
            if index == -1:
                return None
            else:
                return None

    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''

        if self.is_empty():
            raise IndexError
        if index < 0 or index >= self.size():
            raise IndexError
        else:
            start_index = 0
            n = self.dummy.prev
            while n is not None:
                if start_index == index:
                    temp = n.item
                    self.remove(n.item)
                    return temp
                n = n.next
                start_index += 1

            # n = self.dummy.prev
            # temp_index = -1
            # while n is not None:
            #     temp_index += 1
            #     if temp_index == index:
            #         temp = n.item
            #         n.prev.next = n.next
            #         n.next.prev = n.prev
            #         return temp
            #         index += 1
            #     n = n.next

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''

        n = self.dummy.prev
        return search_recur(n, item)

    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''

        new_list = []
        n = self.dummy.prev
        while n is not None:
            new_list.append(n.item)
            n = n.next
        # print(new_list)
        return new_list

    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''

        n = self.dummy.next
        # reversed_list = reverse_list_recur(n)

        start_list = self.python_list()
        return reverse_list_recur(start_list)

        # new_list = []
        # n = reversed_list
        # while n is not None:
        #     new_list.append(n.item)
        #     n = n.next

        # return reversed_list

    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''

        # needs to go through list and count how many non-None nodes there are
        # recursive part - keeps calling next on the node

        # n = self.dummy.prev
        # num_items = size_recur(n)
        # return num_items

        list_form = self.python_list()
        # print(list_form)
        size = size_recur2(list_form)
        return size


def size_recur(node):
    if node is None:
        return 1
    else:
        return 1 + size_recur(node.next)


def size_recur2(list):
    if not list:
        return 0
    return 1 + size_recur2(list[1:])


def search_recur(node, item):
    if node is None:
        return False
    if node.item == item:
        return True
    else:
        return search_recur(node.next, item)


def reverse_list_recur(start_list):
    # Base case1
    if len(start_list) == 0:  # If we encounter an empty array, simply return an empty array
        return []

    # Base case2
    elif len(start_list) == 1:  # Inverting an array of size 1 returns the same array
        return start_list

    # Recursive case
    return [start_list[len(start_list) - 1]] + reverse_list_recur(start_list[:len(start_list) - 1])


    # reverse_list = []
    # if node is None:
    #     return reverse_list
    # else:
    #     reverse_list.append(node.item)
    #     reverse_list_recur(node.prev, reverse_list)

    # temp = node.next
    # node.next = node.prev
    # node.prev = temp

    # if not node.prev:
    #     return node
    # return reverse_list_recur(node.prev)


if __name__ == '__main__':
    # t_list = OrderedList()
    # t_list.add(10)
    # t_list.add(20)
    # print(t_list.python_list(), [10])
    # print(t_list.size())
    # self.assertEqual(t_list.size(), 1)
    # self.assertFalse(t_list.is_empty())
    # t_list.add(30)
    # t_list.add(20)
    # print(t_list.python_list())
    # print(t_list.python_list_reversed())  ## need to fix this function
    # print(t_list.size())

    # t_list.remove(20)

    # print(t_list.python_list())
    # t_list.pop(0)
    # print(t_list.python_list())

    # t_list.add(15)
    # print(t_list.python_list())
    # print(t_list.python_list_reversed())
    # print(t_list.size())

    t_list = OrderedList()
    for val in range(200):
        t_list.add(val)

    print(t_list.python_list())

    for val in range(199, -1, -1):
        t_list.pop(val)

    print(t_list.python_list())

    t_list.is_empty()
