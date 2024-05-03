class Solution:
    def getRow(self, rowIndex):
        triangle = [[1]*x for x in range(1, rowIndex+2)]
        print(triangle)
        for i in range(2, len(triangle)):
            for j in range(1, len(triangle[i]) - 1):
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
        return triangle[-1]
    
    def getRow2(self, rowIndex):
        ans = [1] * (rowIndex+1)
        print(ans)
        for i in range(2, rowIndex+1):
            for j in range(1, i):
                ans[i-j] += ans[i-j-1]
                
        return ans
    
s = Solution()

print(s.getRow2(3))
        