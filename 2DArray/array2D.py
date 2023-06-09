
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
        n = len(matrix)
        m = len(matrix[0])
        left, top = 0, 0
        right = m-1
        bottom = n - 1
        ans = []

        while top <= bottom and left <= right:

            for i in range(left, right+1):
                ans.append(matrix[top][i])
            top+=1

            for i in range(top, bottom+1):
                ans.append(matrix[i][right])
            right-=1
            if top <= bottom:
                for i in range( right, left-1, -1):
                    ans.append(matrix[bottom][i])
                bottom-=1
            if left <= right:
                for i in range(bottom, top-1, -1):
                    ans.append(matrix[i][left])
                left+=1
            
        return ans
    
    def spiralOrder2(self, matrix):
        if not matrix:
            return []

        m = len(matrix)
        n = len(matrix[0])
        ans = []
        r1 = 0
        c1 = 0
        r2 = m - 1
        c2 = n - 1

        # Repeatedly add matrix[r1..r2][c1..c2] to ans
        while len(ans) < m * n:
            j = c1
            while j <= c2 and len(ans) < m * n:
                ans.append(matrix[r1][j])
                j += 1
            i = r1 + 1
            while i <= r2 - 1 and len(ans) < m * n:
                ans.append(matrix[i][c2])
                i += 1
            j = c2
            while j >= c1 and len(ans) < m * n:
                ans.append(matrix[r2][j])
                j -= 1
            i = r2 - 1
            while i >= r1 + 1 and len(ans) < m * n:
                ans.append(matrix[i][c1])
                i -= 1
            r1 += 1
            c1 += 1
            r2 -= 1
            c2 -= 1

        return ans

    def rotate(self, matrix):
        matrix.reverse()
        print(matrix)
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        return matrix

    def exist(self, board, word):
        m = len(board)
        n = len(board[0])

        def dfs(i: int, j: int, s: int) -> bool:
            if i < 0 or i == m or j < 0 or j == n:
                return False
            if board[i][j] != word[s] or board[i][j] == '*':
                return False
            if s == len(word) - 1:
                return True

            cache = board[i][j]
            board[i][j] = '*'
            isExist = \
                dfs(i + 1, j, s + 1) or \
                dfs(i - 1, j, s + 1) or \
                dfs(i, j + 1, s + 1) or \
                dfs(i, j - 1, s + 1)
            board[i][j] = cache
            print(board)
            return isExist

        return any(dfs(i, j, 0) for i in range(m) for j in range(n))


sol = Array2D()
m1 = [[1,2,3],[4,5,6],[7,8,9]] # [[7,4,1],[8,5,2],[9,6,3]]
m2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]  # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCC"))