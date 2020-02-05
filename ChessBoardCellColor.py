"""
Given two cells on the standard chess board, determine whether they have the same color or not.

Example

For cell1 = "A1" and cell2 = "C3", the output should be
chessBoardCellColor(cell1, cell2) = true.

For cell1 = "A1" and cell2 = "H3", the output should be
chessBoardCellColor(cell1, cell2) = false.
"""
def chessBoardCellColor(cell1, cell2):
    def get_color(c1):
        boxes = "#ABCDEFGH"
        i,i1 = boxes.index(c1[0])%2, int(c1[1])%2
        retval = "Black" if ((i==1 and i1==1) or (i==0 and i1==0) ) else "White"
        return retval
        
    return get_color(cell1)==get_color(cell2)
