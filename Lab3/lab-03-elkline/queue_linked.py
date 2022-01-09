class Node:
    def __init__(self, item):
        self.data = item
        self.next = None  # pointer to next Node

    def __repr__(self):
        return ("Node({!r}, {!r})".format(self.data, self.next))

    def __eq__(self, other):
        return ((type(other) == Node) and self.data == other.data and self.next == other.next)


class Queue:
    '''Implements an link-based ,efficient first-in first-out Abstract Data Type'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''

        self.front = None
        self.rear = None
        self.capacity = capacity
        self.num_items = 0

    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise
           MUST have O(1) performance'''

        return self.num_items == 0

    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise
           MUST have O(1) performance'''

        return self.num_items == self.capacity

    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError
           MUST have O(1) performance'''

        temp = Node(item)

        if self.is_full():
            raise IndexError

        if self.num_items == 0:
            self.front = temp
            self.rear = temp

        else:
            self.rear.next = temp
            self.rear = temp

        self.num_items += 1



    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError
           MUST have O(1) performance'''

        if self.is_empty():
            raise IndexError

        if self.front == None:
            self.rear = None

        # temp = self.front
        # self.front = temp.next
        # self.num_items -= 1

        temp = self.front
        self.front = temp.next
        self.num_items -= 1

        return temp.data

    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity
           MUST have O(1) performance'''

        return self.num_items
