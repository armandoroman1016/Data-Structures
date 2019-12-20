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
    def insert(self, value):
        # If inserting we must already have a tree/root

        # if value is less than self.value go left, make a new tree/node if empty, otherwise
        # keep going (recursion)
        if value < self.value:

            if self.left is None:
                new_tree = BinarySearchTree(value)
                self.left = new_tree

            else:
                self.left.insert(value)
            
        # if greater than or equal to then go right, make a new tree/node if empty, otherwise
        # keep going.
        elif value >= self.value:

            if self.right is None:
                new_tree = BinarySearchTree(value)
                self.right = new_tree
 
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target == self.value, return it
        # keeping track of current tree for comparison

        # if target is found return True
        if self.value == target:
            return True

        # go left if smaller
        elif self.value >= target:

            if self.left is not None:
                return self.left.contains(target)

            else:
                return False

        # go right if smaller
        elif self.value <= target:

            if self.right is not None:
                return self.right.contains(target)

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
        
        cb(self.value)

        if self.right is None and self.left is None and self.value is not None:
            return

        if self.left is not None:
            self.left.for_each(cb)
            
        if self.right is not None:
            self.right.for_each(cb)


        
    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):

        # print(f'self.value: {self.value}, node.value: {node.value}')
        
        # if self.left is None:
        # # if cant go left return self.value
        #     return self.value
            
        # # if can go left recurse
        # if self.left is not None:
        #     return self.left.in_order_print(self.left)

        # # if can go right go right 
        # if self.right is not None:
        #     return self.right.in_order_print(self.right)

        # return self.value
        if node is None:
            return
        # print(f'self.value: {self.value} node.value:{node.value}')

        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):

        queue = Queue()
        queue.enqueue(node)

        while queue.len() > 0:

            node = queue.dequeue()

            print(node.value)

            if node.left is not None:
                queue.enqueue(node.left)

            if node.right is not None:
                queue.enqueue(node.right)




    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):

        stack = Stack()

        stack.push(node)

        while stack.len() > 0:

            node = stack.pop()

            print(node.value)

            if node.left is not None:
                stack.push(node.left)
            
            if node.right is not None:
                stack.push(node.right)
        
        

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

bst = BinarySearchTree(5)
bst.insert(4)
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

# print(bst.in_order_print(bst))
# print(bst.bft_print(bst))
print(bst.dft_print(bst))


# print(bst.for_each(display_node))