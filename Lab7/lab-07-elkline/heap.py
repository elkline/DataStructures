
class MaxHeap:

    def __init__(self, capacity=50):
        '''Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created.'''

        self.heapList = [0]
        self.currentSize = 0
        self.capacity = capacity

    def swap(self, index1, index2):
        self.heapList[index1], self.heapList[index2] = self.heapList[index2], self.heapList[index1]

    def enqueue(self, item):
        '''inserts "item" into the heap, returns true if successful, false if there is no room in the heap
           "item" can be any primitive or ***object*** that can be compared with other
           items using the < operator'''

        if self.is_full():
            return False
        else:
            # self.heapList.append(item)
            # self.currentSize = self.currentSize + 1
            # self.build_heap(self.heapList)
            # self.perc_up(self.currentSize)  ##
            # return True

            self.heapList.append(item)
            self.perc_up(len(self.heapList) - 1)  # furthest left node
            self.currentSize += 1
            return True

    def peek(self):
        '''returns max without changing the heap, returns None if the heap is empty'''

        return self.heapList[0]

    def dequeue(self):
        '''returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty'''

        n = len(self.heapList) - 1
        self.swap(0, n)
        max = self.heapList.pop(len(self.heapList) - 1)
        self.perc_down(0)
        self.currentSize -= 1
        return max

    def contents(self):
        '''returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)'''

        return self.heapList

    def build_heap(self, alist):
        '''Discards all items in the current heap and builds a heap from
        the items in alist using the bottom-up construction method.
        If the capacity of the current heap is less than the number of
        items in alist, the capacity of the heap will be increased to accommodate the items in alist'''

        self.heapList = alist

        if len(alist) > self.capacity:
            self.capacity = len(alist)

        self.currentSize = len(alist)

        n = len(self.heapList) - 1
        # start at last parent and go left one node at a time
        for i in range(n // 2, -1, -1):
            self.perc_down(i)
        return

    def is_empty(self):
        '''returns True if the heap is empty, false otherwise'''

        if self.currentSize == 0:
            return True
        else:
            return False

    def is_full(self):
        '''returns True if the heap is full, false otherwise'''

        if self.capacity == self.currentSize:
            return True
        else:
            return False

    def get_capacity(self):
        '''this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold'''

        return self.capacity

    def get_size(self):
        '''the actual number of elements in the heap, not the capacity'''

        return self.currentSize

    def perc_down(self, i):
        '''where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''

        # pass

        child = 2 * i + 1
        # base case, stop recursing when we hit the end of the heap
        if child > len(self.heapList) - 1:
            return
        # check that second child exists; if so find max
        if (child + 1 <= len(self.heapList) - 1) and (self.heapList[child + 1] > self.heapList[child]):
            child += 1
        # preserves heap structure
        if self.heapList[i] < self.heapList[child]:
            self.swap(i, child)
            self.perc_down(child)
        else:
            return

    def perc_up(self, i):
        '''where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''

        try:
            self.heapList[i]
        except:
            return
        # pass

        # parent = (i - 1) // 2
        #
        # # base case; we've reached the top of the heap
        # if parent <= 0:
        #     return
        # if i < len(self.heapList) and self.heapList[parent] < self.heapList[i]:
        #     self.swap(i, parent)
        # else:
        #     self.perc_up(parent)

        parent = (i - 1) // 2
        while (i - 1) // 2 >= 0:
            if self.heapList[i] > self.heapList[(i - 1) // 2]:
                self.swap(i, ((i - 1) // 2))

            i = (i - 1) // 2

    def heap_sort_ascending(self, alist):
        '''perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order'''

        new_list = alist.sort()

    def max_child(self, child1, child2):
        '''returns the minimum child'''

        if self.heapList[child1] > self.heapList[child2]:
            return child1
        else:
            return child2

if __name__ == "__main__":
    # test_heap = MaxHeap(7)
    # test_heap.build_heap([2, 9, 7, 6, 5, 8])
    # print(test_heap.contents())
    # insert = test_heap.enqueue(10)
    #
    # print(test_heap.contents())

    q = MaxHeap()
    words = ['hello', 'this', 'is', 'a', 'list', 'of', 'strings']
    q.build_heap(words)
    words.sort(reverse=True)

    print(q.contents())

    for i in range(len(words)):
        print(q.peek())