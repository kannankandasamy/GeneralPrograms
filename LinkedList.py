"""
Create linked list and add operations like push, reverse, get elements from linked list
"""

class Node(object):
    
    def __init__(self,val):
        self.value = val
        self.next = None
        

class LinkedList(object):
    def __init__(self):
        self.head = None
        
    def push(self,val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        
    def printList(self):
        tmp = self.head
        while tmp:
            print(tmp.value)
            tmp = tmp.next
            
    def reverse(self):
        prev, nxt = None, None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev
