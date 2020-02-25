
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
