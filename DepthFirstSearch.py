"""
This program is to do graph traversal using Depth First Search algorithmic approach.
It uses Stack data structure.
"""

#Converts edges list to adjacency list
def convertToAdjacencyList(graph, nodes):
    al = {n:[] for n in nodes}
    for edge in graph:
        al[edge[0]].append(edge[1])
        al[edge[1]].append(edge[0])
    return al
    
#Does Depth First Search using Stack and returns visited nodes or the path of traversal
def depthFirstSearch(al, node):
    visited = {n:False for n in al.keys()}
    path = []
    stk = Stack()
    stk.push(node)
    visited[node] = True
    while not stk.isEmpty():
        cur = stk.pop()
        path.append(cur)
        for n in al[cur]:
            if not visited[n]:
                stk.push(n)
                visited[n] = True
    return visited
    #return path #To return path based on requirement

#Return True if there is a path from s to d
def hasPath(s,d,alist):
    visited, path = {n:False for n in alist.keys()}, []
    stk = Stack()
    stk.push(s)
    visited[s] = True
    while not stk.isEmpty():
        t = stk.pop()
        path.append(t)
        if t==d:
            return True
            #return path --If we want to look at the exact path of traversal using Depth First Search
        for n in alist[t]:
            if not visited[n]:
                stk.push(n)
                visited[n] = True
    return False
    
#Return True if there is a cycle in Graph. This approach traverses whole graph and finds cycle, it will not stop if it found a cycle
from collections import Counter as c
def hasCycle(s,alist):
    visited, path = {n:False for n in alist.keys()}, []
    stk = Stack()
    stk.push(s)
    visited[s] = True
    while not stk.isEmpty():
        cur = stk.pop()
        for n in alist[cur]:
            if not visited[n]:
                stk.push(n)
        visited[cur] = True
        path.append(cur)
    for item in c(path).items():
        if item[1]>1:
            return True
    return False

class Stack:
    def __init__(self):
        self.l = []
        self.count = 0
        
    def push(self, val):
        self.l.append(val)
        self.count += 1
    
    def pop(self):
        self.count -= 1
        t = self.l.pop()
        return t
    
    def isEmpty(self):
        return self.count==0
    
    def printStack(self):
        return self.l
    
