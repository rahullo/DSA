from collections import Counter

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
   
    def construct2DArray(self, original, m, n):
        if len(original) != m*n:
            return []
        ans = []
        x = 0
        for i in range(m):
            ans.append([])
            for j in range(n):
                ans[i].append(original[x])
                x+=1
        return ans
    
    def construct2Darr(self, original, m, n):
        if len(original) != m * n:
            return []

        ans = [[0] * n for _ in range(m)]
        print(ans)
        for i, num in enumerate(original):
            print(i, num, "     ", i//n, i%n)
            ans[i // n][i % n] = num

        return ans
    
    def matrixReshape(self, mat, r, c):
        m = len(mat)
        n = len(mat[0])

        if m*n != r*c:
            return mat

        new_mat = []
        for i in range(m):
            for j in range(n):
                new_mat.append(mat[i][j])

        print(new_mat)

        return self.construct2Darr(new_mat, r, c)
    
    def matrixReshape2(self, mat, r, c):
        if mat == [] or r * c != len(mat) * len(mat[0]):
            return mat

        ans = [[0 for j in range(c)] for i in range(r)]
        k = 0

        for row in mat:
            for num in row:
                ans[k // c][k % c] = num
                k += 1

        return ans
    

    def topKFrequent(self, nums, k):
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        print(count)

        for n, c in count.items():
            freq[c].append(n)

        print(freq)

        res = []
        for i in range(len(freq) - 1, 0, -1): #   4,  3,   2,   1
            for n in freq[i]:                   # [], [], [0], [3, 1], []
                res.append(n)
                if len(res) == k:
                    return res
                
        
    def average(self, salary):
        salary.sort()

        n = len(salary)
        sum = 0

        for i in range(1, n-1):
            sum += salary[i]
        
        return sum / (n-2)
    
    def arraySign(self, nums):
        prod = 1

        for item in nums:
            if item == 0:
                return 0
            elif item < 0:
                prod = -prod
        return prod        
    
    def findDifference(self, nums1, nums2):
        # ans = [[],[]]

        # for item in nums1:
        #     if item not in nums2 and item not in ans[0]:
        #         ans[0].append(item)
        
        # for item in nums2:
        #     if item not in nums1 and item not in ans[1]:
        #         ans[1].append(item)
        
        # return ans

        set1 = set(nums1)
        set2 = set(nums2)
        return [set1 - set2, set2 - set1]
    
    def intersection(self, nums):
        count = [0] * 1001

        for A in nums:
            for a in A:
                count[a] += 1

        return [i for i, c in enumerate(count) if c == len(nums)]
    
    def divide(self, dividend, divisor):
        # div = False
        # divi = False
        # ans = 0
        # if dividend < 0:
        #     dividend = -dividend
        #     div = True
        
        # if divisor < 0:
        #     divisor = -divisor
        #     divi = True
        
        # while dividend > 0:
        #     if dividend < divisor:
        #         break
        #     dividend = dividend - divisor
        #     ans +=1
        
        # print(dividend)

        # if div == True and divi == False:
        #     return -ans
        # elif div == False and divi == True:
        #     return -ans
        # elif div == True and divi == True:
        #     return ans
        
        # return ans


        # Optimised approach but not as rule of this question
        # if dividend == -2**31 and divisor == -1:
        #     return 2**31 - 1

        # sign = -1 if (dividend > 0) ^ (divisor > 0) else 1
        # ans = 0
        # dvd = abs(dividend)
        # dvs = abs(divisor)

        # while dvd >= dvs:
        #     k = 1
        #     while k * 2 * dvs <= dvd:
        #         k <<= 1
        #     dvd -= k * dvs
        #     ans += k

        # return sign * ans


        # Another approach 
        
        # Handle division by zero
        if divisor == 0:
            return 2**31 - 1
        
        # Handle overflow case
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        # Get the sign of the result
        sign = 1
        if dividend < 0:
            dividend = -dividend
            sign = -sign
        if divisor < 0:
            divisor = -divisor
            sign = -sign
        
        # Find the largest multiple of the divisor that is less than or equal to the dividend
        multiple = 1
        while dividend >= (divisor << 1):
            divisor <<= 1
            multiple <<= 1
        
        # Perform division using binary search
        quotient = 0
        while multiple > 0:
            if dividend >= divisor:
                dividend -= divisor
                quotient += multiple
            divisor >>= 1
            multiple >>= 1
        
        # Apply the sign to the result
        return sign * quotient

    def threeSumClosest(self, nums, target):
        ans = nums[0] + nums[1] + nums[2]
        nums.sort()
        print(nums)
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            summ = 0
            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                if summ == target:
                    return summ
                if abs(summ - target) < abs(ans - target):
                    ans = summ
                if summ < target:
                    l += 1
                else:
                    r -= 1
            print(i, summ)
        return ans
    
    # 59 Spiral Matrix 2 (Leetcode)
    def generateMatrix(self, n):
        ans = [[0] * n for _ in range(n)]
        count = 1

        for min in range(n // 2):
            max = n - min - 1
            print(min, max)
            for i in range(min, max):
                ans[min][i] = count
                count += 1
            for i in range(min, max):
                ans[i][max] = count
                count += 1
            for i in range(max, min, -1):
                ans[max][i] = count
                count += 1
            for i in range(max, min, -1):
                ans[i][min] = count
                count += 1
            print(ans)

        if n & 1:
            ans[n // 2][n // 2] = count

        return ans      

    def getConcatenation(self, nums):
        return nums + nums

        # Other solution
        # ans = []
        # for i in range(2):
        #     for n in nums:
        #         ans.append(n)
        # return ans

    def replaceElements(self, arr):
        ### Brute force approach
        # for i in range (len(arr)-1):
        #     maxi = arr[i+1]

        #     for j in range(i+1, len(arr)):
        #         maxi = max(maxi, arr[j])

        #     arr[i] = maxi
        
        # arr[-1] = -1

        # return arr

        ###Optimized opproach

        maxi = -1

        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = maxi
            maxi = max(maxi, temp)

        return arr

    # 1. Two sum
    def twoSum(self, nums, target):
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

    def pascalTriangle(self, rows):
        ans = []
        for i in range(1, rows+1):
            ans.append([1]*i)
        
        for i in range(2, rows):
            for j in range(1, i):
                ans[i][j] = ans[i-1][j-1] + ans[i-1][j]

        return ans
    

    def removeElement(self, nums, val):
        for i in range(nums.count(val)):
            nums.remove(val)
        return len(nums)
    
    def canPlaceFlowers(self, flowerbed, n):
        emptySpace = 0

        if flowerbed[0] == 0 and flowerbed[1] == 0:
            emptySpace += 1
            flowerbed[0] = 1

        for i in range(len(flowerbed)-1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                emptySpace += 1
                flowerbed[i] = 1
        
        print(flowerbed)
        return emptySpace == n

    def majorityElement(self, nums):
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
            
        return res



array = Solution()

print(array.majorityElement([6,5,5]))


