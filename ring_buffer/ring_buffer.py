from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.size = 0

    def append(self, item):
        
        # for s in item:
        #     self.storage.add_to_head(s)
        # return item
        # self.current = item
    
        self.storage.add_to_head(item)
        self.size+= 1
        if self.size == self.capacity:
            max = self.storage.get_max()
            self.storage.delete(max)
            self.size -= 1
        # elif item is in list_buffer_contents:
            # return self.current

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current = self.storage.head
        while current:
            
            list_buffer_contents += current.value
            current = current.next
        # return s
        # list_buffer_contents.append(s)
        # TODO: Your code here
        
             
        
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
