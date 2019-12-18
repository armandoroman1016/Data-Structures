import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack
    

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.current = self

    # Insert the given value into the tree
    def insert(self, value, current_tree = None):
        # If inserting we must already have a tree/root
        current = current_tree or self
        # if value is less than self.value go left, make a new tree/node if empty, otherwise
        # keep going (recursion)
        if value < current.value:

            if current.left is None:
                new_tree = BinarySearchTree(value)
                current.left = new_tree

            else:
                current = self.left
                self.insert(value, current)
            

        # if greater than or equal to then go right, make a new tree/node if empty, otherwise
        # keep going.
        elif value >= current.value:

            if current.right is None:
                new_tree = BinarySearchTree(value)
                current.right = new_tree
 
            else:
                current = self.right
                self.insert(value, current)

        return
            
        


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target == self.value, return it
        # go left or right based on smaller or bigger
        pass



    # Return the maximum value found in the tree
    def get_max(self):
        # if right exists, go right
        # otherwise return self.value
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

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



print(bst.left.right.value)
print(bst.right.left.value)