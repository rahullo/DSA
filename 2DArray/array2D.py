
m1 = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

class Array2D:
    def diagonalOrder(self, matrix):
        ROW = len(matrix)
        COL = len(matrix[0])
        print(ROW, COL)
        # There will be ROW+COL-1 lines in the output
        for line in range(1, (ROW + COL)):
            # Get column index of the first element
            # in this line of output. The index is 0
            # for first ROW lines and line - ROW for
            # remaining lines
            start_col = max(0, line - ROW)
            # print(start_col, 0, line - ROW)
    
            # Get count of elements in this line.
            # The count of elements is equal to
            # minimum of line number, COL-start_col and ROW
            count = min(line, (COL - start_col), ROW)
    
            # Print elements of this line
            for j in range(0, count):
                print(matrix[min(ROW, line) - j - 1]
                            [start_col + j], end="\t")
    
            print()

sol = Array2D()
sol.diagonalOrder(m1)