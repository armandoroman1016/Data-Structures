from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.storage = DoublyLinkedList()
        self.limit = limit
        self.cache = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
# TODO SET CACHE TO HOLD A DICTIONARY WITH KEY AS KEYNAME: AND VALUE AS NODE'S KEY VALUE PAIRS
# ? node = (key, value)
# ? inside cache = (node[0], node) 

    def get(self, key):

        if key in self.cache:
            target_node = self.storage.get_node(key)
            if target_node is not None:
                self.storage.move_to_front(target_node)
                return self.cache[key]

        else:
            return None
            
            
    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):


        new_node = (key, value)

        if key in self.cache:
            target_node = self.storage.get_node(key)

            if target_node is not None:
                self.storage.move_to_front(target_node)
            else:
                self.storage.add_to_head(new_node)

            self.cache[key] = value

            return

        if self.storage.length < self.limit:
            self.storage.add_to_head(new_node)
            self.cache[key] = value

        elif self.storage.length == self.limit:
            self.storage.remove_from_tail()
            self.storage.add_to_head(new_node)
            self.cache[key] = value
        
