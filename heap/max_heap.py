import math
import random
#       15
#    5      10 
#  20

class Heap:
    def __init__(self):
        self.storage = []
        self.size = 0

    def insert(self, value):
        self.storage.append(value)
        self.size += 1
        
        #  if only single element return
        # ! single element is a heap
        if self.size == 1:
            return

        parent_index = math.floor(self.size / 2) - 1 

        new_val_index = self.size - 1

        while True:
            # preventing comparisons of invalid indexes
            if parent_index < 0 or new_val_index < 0:
                break

            # ? return if the element is less then its parent, its already in correct position 
            if self.storage[new_val_index] <= self.storage[parent_index]:
                break
            
            
            # ? swap if child is greater then its parent
            self.storage[new_val_index], self.storage[parent_index] = self.storage[parent_index], self.storage[new_val_index]

            # updating indexes for next comparison
            new_val_index = parent_index
            parent_index = math.floor((new_val_index / 2))

        return

    def delete(self):

        max_el = self.get_max()

        # get index of last head item 
        # swap first and last item in heap
        self.storage[self.size - 1], self.storage[0] = self.storage[0], self.storage[self.size - 1]


        self.size -= 1

        if self.size < 0:
            return max_el

        curr_idx = 1

        left_child_idx = 2

        right_child_idx = 3

        while True:
            
            # ? preventing out of bounds errors
            if right_child_idx > self.size or left_child_idx > self.size:

                if right_child_idx > self.size and left_child_idx > self.size:
                    break

                elif self.storage[left_child_idx - 1] > self.storage[curr_idx - 1]:
                    self.storage[curr_idx - 1], self.storage[left_child_idx - 1] = self.storage[left_child_idx - 1], self.storage[curr_idx - 1]
                    break


            # compare both children and store greater value
            greater_child = left_child_idx if self.storage[left_child_idx - 1] > self.storage[right_child_idx - 1] else right_child_idx
    
            # if parent is greater then the child return 
            if self.storage[curr_idx - 1] >= self.storage[greater_child - 1]:
                break

            # else swap the values
            else:
                self.storage[curr_idx - 1], self.storage[greater_child - 1] = self.storage[greater_child - 1], self.storage[curr_idx - 1]

            # update current idx with child index
            curr_idx = greater_child

            # update children index with formula
            left_child_idx = 2 * greater_child
            right_child_idx = (2 * greater_child) + 1

        return max_el

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return self.size

    def get_heap(self):
        return self.storage[0 : self.size]

    def _bubble_up(self, index):
        pass

    def _sift_down(self, index):
        pass


# x = Heap()

# for i in range(5):
#     x.insert(random.randint(0, 100))

# while x.get_size() > 0:
#     x.delete()


# # for i in range(100000):
# #     x.insert(random.randint(0, 1000000))

# # while x.get_size() > 0:
# #     x.delete()

# print(x.storage)




