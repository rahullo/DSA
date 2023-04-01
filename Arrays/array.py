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
    
    # The next permutation
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        i = n - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1

        print(i)

        if i >= 0:
            for j in range(n - 1, i, -1):
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
        
        print(nums)

        def reverse(nums, l, r: int) -> None:
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(nums, i + 1, len(nums) - 1)
        return nums
    
    # Best time to buy and sell stock
    def maxProfit(self, prices):
        mini = prices[0]
        profit = 0
        for price in prices:
            cost = price - mini
            profit = max(cost, profit)
            mini = min(mini, price)
        return profit
    
    # Kth largest element in an array
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[(len(nums))-k]

    def productExceptSelf(self, nums):
        ans=[]
        for i in range(len(nums)):
            prod=1
            for j in range(len(nums)):
                if i == j:
                    continue
                prod*=nums[j]
            ans.append(prod)

        return ans
    
    def productExceptSelf2(self, nums):
        n = len(nums)
        prefix = [1] * n  # Prefix product
        suffix = [1] * n  # Suffix product
        print(prefix)
        print(suffix)
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in reversed(range(n - 1)):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        print('\n')
        print(prefix)
        print(suffix)
        print('\n')

        return [prefix[i] * suffix[i] for i in range(n)]
    
    def maxProduct(self, nums):
        ans = nums[0]
        prevMin = nums[0]
        prevMax = nums[0]

        for i in range(1, len(nums)):
            mini = prevMin * nums[i]
            maxi = prevMax * nums[i]
            prevMin = min(nums[i], mini, maxi)
            prevMax = max(nums[i], mini, maxi)
            ans = max(ans, prevMax)

        return ans

    def maximumProduct(self, nums):
        nums.sort()
        return max(nums[0]* nums[1]* nums[-1], nums[-1]* nums[-2]* nums[-3])
   

array = Solution()

print(array.maximumProduct([-100,-98,-1,2,3,4]))
# print(array.maximumProduct([-2, 0, -1]))

