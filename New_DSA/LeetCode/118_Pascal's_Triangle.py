import time

class Solution:
    def generate(self, numRows):
        ans = [[1]*x for x in range(1, numRows+1)]
        for i in range(2, len(ans)):
            for j in range(1, len(ans[i]) - 1):
                ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
        return ans

    def generate2(self, numRows):
        res=[[1]]
        for i in range(numRows-1):
            temp=[0]+res[-1]+[0]
            row=[]
            for j in range(len(res[-1])+1):
                row.append(temp[j]+temp[j+1])
            res.append(row)
        return res

s = Solution()
start = time.time()
print(s.generate(5))
end = time.time()
elapsed_time = (end-start) * 1000 
print(str(elapsed_time) + 'ms')

# print(time.time()/60/60)