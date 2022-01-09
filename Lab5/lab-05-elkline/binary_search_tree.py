from queue_array import Queue


class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:

    def __init__(self):  # Returns empty BST
        self.root = None

    def is_empty(self):  # returns True if tree is empty, else False
        if self.root is None:
            return True
        else:
            return False

    def search(self, key):  # returns True if key is in a node of the tree, else False

        # BST is empty
        if self.is_empty():
            return False

        else:
            t = self.root
            return search_helper(t, key)

    def insert(self, key, data=None):  # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data

        x = self.root
        # Create a new Node containing
        new_node = TreeNode(key, data)

        if self.is_empty():
            self.root = new_node

        elif self.search(key):

            key_location = find_key(x, key)
            key_location.data = data

        else:
            # Pointer y maintains the trailing
            # pointer of x
            y = None

            while x is not None:
                y = x
                if key < x.key:
                    x = x.left
                else:
                    x = x.right

            # If the new key is less then the leaf node key
            # Assign the new node to be its left child
            if key < y.key:
                y.left = new_node

            # else assign the new node its
            # right child
            else:
                y.right = new_node

    def find_min(self):  # returns a tuple with min key and data in the BST
        # returns None if the tree is empty

        if self.is_empty():
            return None
        else:
            t = self.root
            min_key = ()
            while t is not None:  # traces left side of tree until it hits None
                min_key = (t.key, t.data)
                t = t.left
            return min_key

    def find_max(self):  # returns a tuple with max key and data in the BST
        # returns None if the tree is empty

        if self.is_empty():
            return None
        else:
            t = self.root
            max_key = ()
            while t is not None:  # traces right side of tree until it hits None
                max_key = (t.key, t.data)
                t = t.right
            return max_key

    def tree_height(self):  # return the height of the tree
        # returns None if tree is empty

        if self.is_empty():
            return None
        else:
            t = self.root
            return height_helper(t)

    def inorder_list(self):  # return Python list of BST keys representing in-order traversal of BST

        t = self.root
        return inorder_helper(t)

    def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST

        t = self.root
        return preorder_helper(t)

    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        q = Queue(25000)  # Don't change this!
        queue = []

        root = self.root

        if root is None:
            return []

        # Enqueue Root and initialize height
        q.enqueue(root)

        while q.size() > 0:

            # remove front of queue and add it to []
            node = q.dequeue()
            if node is not None:
                queue.append(node.key)

            # Enqueue left child
            if node.left is not None:
                q.enqueue(node.left)

            # Enqueue right child
            if node.right is not None:
                q.enqueue(node.right)
        return queue


def search_helper(root, key):
    # Base Cases: root is None or key is at the root
    if root is None:
        return False

    if root.key == key:
        return True

    # Key is greater than root's key
    if root.key < key:
        return search_helper(root.right, key)

    # Key is smaller than root's key
    return search_helper(root.left, key)


def find_key(root, key):
    x = root
    while x is not None:
        if x.key == key:
            return x
        elif key < x.key:
            x = x.left
        else:
            x = x.right


def height_helper(root):
    if root is None:
        return -1

    else:
        # Computing the depth of each subtree
        left_depth = height_helper(root.left) + 1
        right_depth = height_helper(root.right) + 1

        # Use the larger one
        if left_depth > right_depth:
            return left_depth
        else:
            return right_depth


def inorder_helper(root):
    elements = []
    if root.left:  # Traverses left
        elements += inorder_helper(root.left)

    elements.append(root.key)  # visits root node

    if root.right:  # Traverses right
        elements += inorder_helper(root.right)
    return elements


def preorder_helper(root):
    elements = [root.key]

    if root.left:
        elements += preorder_helper(root.left)
    if root.right:
        elements += preorder_helper(root.right)
    return elements


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10, 'stuff')
    print(bst.search(10))
    bst.insert(10, 'other')
    print(bst.find_max())
    print(bst.inorder_list())
