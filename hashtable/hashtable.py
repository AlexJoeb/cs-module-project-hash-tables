# Import the LinkedList functionality.
from linkedlist import LinkedList

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # `Capacity` will be initial size of given storage.
        self.capacity = capacity
        # `Storage` will be our mock hashtable. Initalize with a bunch of empty LinkedLists for future mutalation.
        self.storage = [LinkedList()] * capacity
        # `Count` will be the amount of active records in the entire Hashtable.
        self.count = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.count / self.capacity


    def djb2(self, key):
        hash = 5381
        for ltr in key:
            hash = ((hash << 5) + hash) + ord(ltr)

        return hash


    def hash_index(self, key):
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        # Find the appropriate index for the item to be stored at, given it's hash value.
        index = self.hash_index(key)

        # The first node instance in the LinkedList at the given index in self.storage.
        linkedlist = self.storage[index]
        node = self.storage[index].head

        # Create instance of HashTableEntry.
        entry = HashTableEntry(key, value)

        if node == None:
            # LinkedList is empty.
            linkedlist.append_to_head(entry)
            self.count += 1
        else:
            item = linkedlist.contains(key)

            if item is None:
                # Item does not exist in LinkedList yet. Append it.
                linkedlist.append_to_head(entry) 
                self.count += 1
            else:
                # Item does exist in the LinkedList. Modify it.
                item.value = value

    def delete(self, key):
        index = self.hash_index(key)
        list = self.storage[index]

        # Check to see if the key is in the list.
        node = list.contains(key)

        if node is None:
            # Key is not in the list.
            return
        else:
            # Key is in the list.
            if list.head is node and node.next is None:
                # Node is the only item in the list.
                list.head = None
                self.count -= 1
            elif list.head is node and node.next is not None:
                # Node is head and not the only item in the list.
                list.head = node.next
                node.next = None
                self.count -= 1
            elif list.head is not node and node.next is None:
                # Node is at the end of the list.
                before = list.head
                while before is not node:
                    if before.next is node:
                        break
                    before = before.next
                before.next = None
                self.count -= 1
            else:
                # Node is somewhere in the middle.
                before = list.head
                while before is not node:
                    if before.next is node:
                        break
                    before = before.next
                before.next = node.next
                node.next = None
                self.count -= 1

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)

        node = self.storage[index].head # Points to a reference of a LinkedList node.
        
        while node:
            if node.key == key:
                return node.value
            else: node = node.next

        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        self.capacity = new_capacity
        old_storage = self.storage
        self.storage = [LinkedList()] * new_capacity
        
        for item in old_storage:
            node = item.head
            while node:
                self.put(node.key, node.value)
                node = node.next

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
