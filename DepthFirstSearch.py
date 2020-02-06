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
    