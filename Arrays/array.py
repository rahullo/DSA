class Solution:

    # Maximum and Minimum Element in an Array
    def findSum(self,A,N): 
        #code here
        maxi = A[0]
        mini = A[0]

        for item in A:
            if item > maxi:
                maxi = item
            elif item < mini:
                mini = item
        return maxi+mini
    
array = Solution()

print(array.findSum([ 1, 4, 1, 3], 5))