"""
Implement a stack using lists
"""
class Stack:
    def __init__(self):
        self.lis = []
        self.n = 0
        
    def push(self,num):
        self.lis.append(num)
        self.n += 1
        
    def pop(self):
        if self.is_empty():
            return -1
        else:
            rv = self.lis[-1]
            del self.lis[-1]
            self.n -= 1
        return rv
    
    def peek(self):
        if self.is_empty():
            return -1
        else:
            rv = self.lis[-1]
        return rv        
    
    def is_empty(self):
        if self.n==0:
            return True
        else:
            return False
        
    def size(self):
        return self.n
