class Node:
    def __init__(self, value):
        self.next = None # Next node in chain.
        self.value = value # Current node's value.

class LinkedList:
    def __init__(self):
        # Initialize the list as empty by setting the head to none.
        self.head = None
    
    def append_to_head(self, node):
        # Make node's next -> self.head
        node.next = self.head

        # Make self's head into node.
        self.head = node

    def contains(self, key):
        node = self.head
        while node:
            if node.key == key:
                return node
            
            node = node.next
        return None