class Solution:

    # Maximum and Minimum Element in an Array
    def findSum(self,A): 
        #code here
        maxi = A[0]
        mini = A[0]

        for item in A:
            if item > maxi:
                maxi = item
            elif item < mini:
                mini = item
        return maxi+mini
    
    # Reverse an array or string
    def reverseWord(self,s):
        # My solution
        arr = []
        for i in range(len(s)-1, -1, -1):
            arr.append(s[i])
        
        return ''.join(arr)

        # Other solution(Best)
        # return s[::-1]
    
array = Solution()

print(array.reverseWord('Rahul'))