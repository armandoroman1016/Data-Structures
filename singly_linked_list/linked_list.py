class SLL:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = head
        self.count = 0


    def add_to_head(self, val):
        if self.count == 0:
            self.head = self.tail = Node(val)
        else:
            node = Node(val, self.head)
            self.head = node
        self.count += 1
        

    def find_middle(self):
            hare = self.head
            tortise = self.head
            while hare is not None:
                hare = hare.next.next
                tortise = tortise.next

            return tortise.value

    #  ? 1 => 2 => 3 => 4 => 5 => None

    #  ? None <= 1 <= 2 <= 3

    def reverse(self):
        prev = None
        curr = self.head
        nxt = self.head.next
    
        while curr is not None:

            curr.next = prev

            prev = curr

            curr = curr.next
        
        self.head = prev

        return

        

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    def add(self, value):
        self.next = Node(value)


linked_list = SLL()

linked_list.add_to_head(4)
linked_list.add_to_head(3)
linked_list.add_to_head(5)
linked_list.add_to_head(9)
linked_list.add_to_head(10)
linked_list.add_to_head(43)


linked_list.reverse()

print(linked_list.head.value)
print(linked_list.head.next.value)
print(linked_list.head.next.next.value)




