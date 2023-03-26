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
    
    def reverseArray(self,arr):
        n = len(arr)
        for i in range(n//2):
            print(arr[n-1-i], arr[i])
            arr[n-1-i], arr[i] = arr[i], arr[n-1-i]

        return arr
    
    def maxSubArray(self, nums):
        maximum = 0
        if len(nums) <2:
            return nums[0]
        for i in range(len(nums)):
            cum_sum = 0
            for j in range(i, len(nums)):
                cum_sum += nums[j]
                maximum = max( maximum, cum_sum)
        return maximum
    
array = Solution()

print(array.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))