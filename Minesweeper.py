"""
In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in 
it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want 
to create a Minesweeper game setup.

Example

For

matrix = [[true, false, false],
          [false, true, false],
          [false, false, false]]
the output should be

minesweeper(matrix) = [[1, 2, 1],
                       [2, 1, 1],
                       [1, 1, 1]]
Check out the image below for better understanding:
"""
def minesweeper(matrix):
    def mines(r,c):
        total = 0
        for i in range(r-1,r+2):
            for j in range(c-1,c+2):
                if (i<0 or j<0) or (i>=len(matrix) or j >= len(matrix[0])):
                    pass
                elif matrix[i][j]:
                    if i==r and j==c:
                        pass
                    else:
                        total += 1
        return total

    op = []
    for i in range(len(matrix)):
        tmp = []
        for j in range(len(matrix[0])):
            tmp.append(mines(i,j))
        op.append(tmp)
    
    return op
