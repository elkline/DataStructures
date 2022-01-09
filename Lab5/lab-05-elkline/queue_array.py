class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''

        self.num_items = 0
        self.capacity = capacity

        # initializing queue with none
        self.queue = [None for i in range(capacity)]
        self.front = 0
        self.rear = 0


    def is_empty(self): # fix this
        '''Returns True if the Queue is empty, and False otherwise
           MUST have O(1) performance'''

        if self.num_items == 0:
            return True
        # if self.front == -1:  # condition for empty queue
        #     return True
        else:
            return False

    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise
           MUST have O(1) performance'''

        if self.num_items == self.capacity:
            return True

        # if (self.rear + 1) % self.num_items == self.front:
        #     return True

        else:
            return False

    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError
           MUST have O(1) performance'''

        # condition if queue is full
        if self.is_full():
            raise IndexError

        # condition for empty queue
        elif self.is_empty():
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = item
            self.num_items += 1

        else:
            # next position of rear
            self.rear += 1
            # self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item
            self.num_items += 1

    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError
           MUST have O(1) performance'''

        if self.is_empty():  # condition for empty queue
            raise IndexError

            # condition for only one element
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.queue[self.front] = None
            self.rear = 0
            self.num_items = 0
            self.front = 0
            return temp

        else:
            temp = self.queue[self.front]
            # self.front = (self.front + 1) % self.size
            self.queue[self.front] = None
            self.front += self.front
            self.num_items -= 1
            return temp

    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity
           MUST have O(1) performance'''

        return self.num_items
