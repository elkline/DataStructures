class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # pointer to next Node

        # replaces 'mt', Node acts as a Pair from in class examples
        # Node(1, Node(2....


class Stack:
    '''Implements an efficient last-in first-out Abstract Data Type using a Linked List'''

    def __init__(self, capacity):
        '''Creates and empty stack with a capacity'''
        self.capacity = capacity
        self.head = None
        self.num_items = 0

    def is_empty(self):
        '''Returns True if the stack is empty, and False otherwise
           MUST have O(1) performance'''

        return self.head is None

    def is_full(self):
        '''Returns True if the stack is full, and False otherwise
           MUST have O(1) performance'''

        return self.num_items == self.capacity

    def push(self, item):
        '''If stack is not full, pushes item on stack. 
           If stack is full when push is attempted, raises IndexError
           MUST have O(1) performance'''

        # When we want to add any Node at the front, we must make the head point to it.
        # And the Next pointer of the newly added Node, must point to the previous Head, whether it be NULL(in case of new List) or the pointer to the first Node of the List.
        # The previous Head Node is now the second Node of Linked List, because the new Node is added at the front.

        # # allocate a new node for the stack
        # node = Node(item)

        # check if stack (heap) is full. Then inserting an element would
        # lead to stack overflow
        if self.is_full():
            raise IndexError
        else:
            # set data in the allocated node
            node = Node(item)

            # set the `.next` pointer of the new node to point to the current
            # top node of the list
            node.next = self.head

            # update top pointer
            self.head = node
            # self.head = Node(item)

            #incrementing num_items
            self.num_items += 1


    def pop(self):
        '''If stack is not empty, pops item from stack and returns item.
           If stack is empty when pop is attempted, raises IndexError
           MUST have O(1) performance'''

        if self.is_empty():
            raise IndexError
        else:
            popped = self.head.data
            self.head = self.head.next

            # decrementing num_items
            self.num_items -= 1

            return popped

    def peek(self):
        '''If stack is not empty, returns next item to be popped (but does not pop the item)
           If stack is empty, raises IndexError
           MUST have O(1) performance'''

        if self.is_empty():
            raise IndexError
        else:
            return self.head.data

    def size(self):
        '''Returns the number of elements currently in the stack, not the capacity
           MUST have O(1) performance'''

        return self.num_items
