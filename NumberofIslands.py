Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by 
connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3"""
"""

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

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def move(p, direction):
            if direction == 0:
                return (p[0]+steps[0][0],p[1]+steps[0][1])
            elif direction == 1:
                return (p[0]+steps[1][0],p[1]+steps[1][1])
            elif direction == 2:
                return (p[0]+steps[2][0],p[1]+steps[2][1])
            elif direction == 3:
                return (p[0]+steps[3][0],p[1]+steps[3][1])

        # (0,-1) -> left, (0,1) ->right, (-1,0) -> up, (1,0) -> down
        steps = [(0,-1),(0,1),(-1,0),(1,0)] 
        
        visited = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    visited[(i,j)] = False
        
        if visited:
            first = list(visited)[0]
        else:
            return 0
        
        path, ctr = [], 1
        stk = Stack()
        stk.push(first)
        while True:
            cur = stk.pop()
            for i,d in enumerate(steps):
                p = move(cur,i)
                if p in visited and not visited[p]:
                    if grid[p[0]][p[1]] == "1":
                        stk.push(p)
            visited[cur] = True
            path.append(cur)
            if all(visited.values()):
                return ctr
            else:
                if stk.isEmpty():
                    ctr += 1
                    p1 = [k for k,v in visited.items() if not v][0]
                    stk.push(p1)
        return ctr                       
       
