import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack
    

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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
    def contains(self, target, current_tree = None):
        # if target == self.value, return it
        # keeping track of current tree for comparison
        current = current_tree or self

        # if target is found return True
        if current.value == target:
            return True

        # go left if smaller
        elif current.value >= target:

            if current.left is not None:
                current = current.left
                return self.contains(target, current)
            else:
                return False

        # go right if smaller
        elif current.value <= target:

            if current.right is not None:
                current = current.right
                return self.contains(target, current)
            else:
                return False
        
       




    # Return the maximum value found in the tree
    def get_max(self):
        current = self

        # if right exists, go right
        while current.right is not None:
            current = current.right

        max_val = current.value

        return max_val


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach


    def for_each(self, cb):

        if self.right is None and self.left is None:
            return cb(self.value)

        if self.left is not None:
            self.left.for_each(cb)
            
        if self.right is not None:
            self.right.for_each(cb)
        
        cb(self.value)

        


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

# print(bst.contains(10))

# print(bst.left.right.value)
# print(bst.right.left.value)
# print(bst.value)

    
def display_node(val):
    print(val)

print(bst.for_each(display_node))