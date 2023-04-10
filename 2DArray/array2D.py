
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
    
            # Get count of elements in this line.
            # The count of elements is equal to
            # minimum of line number, COL-start_col and ROW
            count = min(line, (COL - start_col), ROW)
    
            # Print elements of this line
            for j in range(0, count):
                print(matrix[min(ROW, line) - j - 1][start_col + j], end="\t")
    
            print()
        
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        target = []
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    target.append([i,j])
        
        for item in target:
            for i in range(rows):
                matrix[i][item[1]] = 0
            for j in range(cols):
                matrix[item[0]][j] = 0
        print(matrix)

    def spiralOrder(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        left, top = 0, 0
        right = cols-1
        bottom = rows - 1
        ans = []

        for i in range(right+1):
            ans.append(matrix[top][i])
        top+=1
        for i in range(bottom+1):
            ans.append(matrix[top][i])
        right-=1
        for i in range(right+1):
            ans.append(matrix[top][i])
        top+=1
        for i in range(right+1):
            ans.append(matrix[top][i])
        top+=1




sol = Array2D()
m1 = [[1,2,3],[4,5,6],[7,8,9]] #[1,2,3,6,9,8,7,4,5]
m2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]  #[1,2,3,4,8,12,11,10,9,5,6,7]
sol.setZeroes(m2)