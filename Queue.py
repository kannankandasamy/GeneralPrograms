"""
Implement Queue data structure with enequeue and dequeue methods
"""
class Queue(object):
    def __init__(self):
        self.q = []
        self.n = 0
        
    def enqueue(self, item):
        self.q.append(item)
        self.n += 1
        
    def dequeue(self):
        if self.n == 0:
            return -1
        else:
            rv = self.q[0]
            del self.q[0]
            self.n -= 1
            return rv
        
    def is_empty(self):
        return True if self.n==0 else False
    
    def size(self):
        return self.n
