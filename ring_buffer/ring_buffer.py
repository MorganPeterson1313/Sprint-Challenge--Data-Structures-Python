from doubly_linked_list import DoublyLinkedList
from queue import Queue



class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None] *capacity
    

    def append(self, item):
         # if current index is less than the capacity 
    # change the value at the index to the item
        if self.current < self.capacity:
            self.storage[self.current] = item
            self.current += 1
        else:
        # if the index reaches the capacity
        # reset to 0 and replace the first
        # item in the list
            self.current = 0
            self.storage[self.current] = item
            self.current += 1
        
       

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        for i in range(len(self.storage)):
            if self.storage[i] is not None:
                list_buffer_contents.append(self.storage[i])
    
             
        # list_buffer_contents = []
        # current = self.storage
        # while current:
            
        #     list_buffer_contents += current.value
        #     current = current.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
