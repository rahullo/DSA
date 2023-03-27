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
    
    # Reverse an string
    def reverseWord(self,s):
        # My solution
        arr = []
        for i in range(len(s)-1, -1, -1):
            arr.append(s[i])
        
        return ''.join(arr)

        # Other solution(Best)
        # return s[::-1]

    # Reverse an array
    def reverseArray(self,arr):
        n = len(arr)
        for i in range(n//2):
            print(arr[n-1-i], arr[i])
            arr[n-1-i], arr[i] = arr[i], arr[n-1-i]

        return arr
    
    # Maximum Subarray in given array
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
    # Contains Duplicate
    def containsDuplicate(self, nums) -> bool:
        dic = set(nums)
        return len(dic) != len(nums)
    
    def chocolateDistribution(self, nums, m):
        nums.sort()
        min_diff = nums[len(nums)-1]
        for i in range(len(nums)-m+1):
            if nums[i+m-1] - nums[i] < min_diff:
                min_diff = nums[i+m-1] - nums[i]
            
        return min_diff
    
    # Search in Rotated Sorted Array
    def reverseSearch(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:  # nums[l..m] are sorted
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:  # nums[m..n - 1] are sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1

array = Solution()

print(array.reverseSearch([4,5,6,7,0,1,2], 3))
