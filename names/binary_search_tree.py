import sys
# sys.path.append('C:\Users\MorganPeterson\Documents\CODE PROJECTS\Data-Structures\queue_and_stack\dll_queue.py')
# sys.path.append('C:\Users\MorganPeterson\Documents\CODE PROJECTS\Data-Structures\queue_and_stack\dll_stack.py')
sys.path.append('../ring_buffer')
from queue import Queue
from stack import Stack

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None




   
    

    # Insert the given value into the tree
    def insert(self, value):
        if not self.value:
            self = BinarySearchTree(value)
        if value is self.value:
            #  self.value = BinarySearchTree(value)
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        # item = BinarySearchTree.value.contains(value)
        elif value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        
        else: #value >= self.left: #value >= node go right
            if not self.right:
                self.right = BinarySearchTree(value)
        
            else:
                self.right.insert(value)
        
        
        # if self.right is None and self.left is None:
        #     return self.storage.enqueue(value)
        # if value > self.storage:
        #     self.right.enqueue(value)
        #     return
        # elif value < self.storage:
        #     self.left.enqueue(value)
        #     return
    

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        elif target >= self.value:
            if not self.right:
                return False
            else:
                return self.right.contains(target)
        elif target != self.value:
            return False
    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()
           
        

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    #same structure as a depth first traversal
    def for_each(self, cb):
        # if self.value:
        #     cb(self)
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
            # BinarySearchTree(self.left).for_each(cb)
        if self.right:
            # BinarySearchTree(self.right).for_each(cb)
             self.right.for_each(cb)
    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        
        if node is None:
            return

        self.in_order_print(node.left)
        print(node.value)
    
        self.in_order_print(node.right)
    

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)
    
        while len(q) != 0:
            node = q.dequeue()
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)
            print(node.value)
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):

        s = Stack()
        s.push(node)
        #as long as teh stack is not empty
        while len(s) != 0:
            node = s.pop()
            print(node.value)
            if node.left is not None:
                s.push(node.left)
            if node.right is not None:
                s.push(node.right)
    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node is None:
            return
        print(node.value)
        
        self.pre_order_dft(node.left)
            
    
        self.pre_order_dft(node.right)
            
    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node is None:
            return
        
        self.post_order_dft(node.left)
            
        
        self.post_order_dft(node.right)
        print(node.value)