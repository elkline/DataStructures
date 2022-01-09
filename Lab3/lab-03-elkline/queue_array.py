class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''

        self.num_items = 0
        self.capacity = capacity

        # initializing queue with none
        self.queue = [None] * capacity

        self.front = self.rear = -1

    def is_empty(self):  # fix this
        '''Returns True if the Queue is empty, and False otherwise
           MUST have O(1) performance'''

        if self.front == -1:
            return True

        else:
            return False

    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise
           MUST have O(1) performance'''

        if (self.rear + 1) % self.capacity == self.front:
            return True
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
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = item
            self.num_items += 1

        else:
            # next position of rear
            self.rear = (self.rear + 1) % self.capacity
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
            self.front = -1
            self.rear = -1
            self.num_items -= 1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity
            self.num_items -= 1
            return temp

    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity
           MUST have O(1) performance'''

        return self.num_items


if __name__ == '__main__':
    q = Queue(5)
    q.enqueue(1)
    print(q.size())  # 1
    print(q.dequeue())  # 1
    print(q.size())  # 0

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    print(q.queue)

    print(q.size())  # 5
    print(q.dequeue())  # 1
    print(q.dequeue())  # 2
