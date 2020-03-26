from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        if value <= self.value:
            if self.left is not None:
                self.left.insert(value)

            else:
                new_tree = BinarySearchTree(value)
                self.left = new_tree

        elif value > self.value:
            if self.right is not None:
                self.right.insert(value)
            
            else:
                new_tree = BinarySearchTree(value)
                self.right = new_tree
            
        
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):

        if self.value == target:
            return True
        
        elif target < self.value:
            if self.left is None:
                return False
            
            return self.left.contains(target)

        elif target > self.value:
            if self.right is None:
                return False
            
            return self.right.contains(target)

       
    # Return the maximum value found in the tree
    def get_max(self):
        current = self

        max_val = current.value

        while current.right is not None:
            max_val = current.right.value
            current = current.right

        return max_val


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):

        if self.left is None and self.right is None:
            return cb(self.value)

        if self.left is not None:
            self.left.for_each(cb)
        
        cb(self.value)
        
        if self.right is not None:
            self.right.for_each(cb)
        

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, tree):

        if self.left is None and self.right is None:
            print(self.value)
            return 

        if self.left is not None:
            self.left.in_order_print(tree)

        print(self.value)

        if self.right is not None:
            self.right.in_order_print(tree)
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # initialize queue
        queue = Queue()

        # add node to queue for our while loop
        queue.enqueue(node)

        while queue.size > 0:
            
            # grab next item from queue
            item = queue.dequeue()

            print(item.value)

            # if there is a node to the left then add to the queue
            if item.left is not None:
                queue.enqueue(item.left)
            
            # if there is a node to the right the add to the queue
            if item.right is not None: 
                queue.enqueue(item.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # ! Stacks - FILO - first in last out - last in first out
        stack = Stack()
        
        # pushing onto stack
        stack.push(node)

        while stack.size > 0:

            # grabbing node from the stack
            item = stack.pop()

            print(item.value)
            # if there is a node on the left then add
            if item.left:
                stack.push(item.left)
            
            # if there is a node to the right then add to the stack
            if item.right:
                stack.push(item.right)


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

bst = BinarySearchTree(5)
bst.insert(2)
bst.insert(3)
bst.insert(7)
bst.insert(10)
bst.insert(6)


print(bst.dft_print(bst))
