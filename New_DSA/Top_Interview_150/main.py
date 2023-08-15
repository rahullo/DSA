from collections import Counter
import math


arr1, arr2 = [1,2,3,0,0,0], [2, 5, 6]
# 1) "88. Merge Sorted Array"
def merge(nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = nums1[:m] + nums2[:n]
        nums1.sort()




# " 27. Remove Element "
def removeElement(nums, val) -> int:
    i = 0
    while i<(len(nums)):
        if nums[i] == val:
            count+=1
            del nums[i]
            i-=1
        i+=1
    
    return len(nums)    

# "26. Remove Duplicates from Sorted Array"
def removeDuplicates(nums) -> int:
    # Algorithm which change nums
    # i = 1
    # while i < (len(nums)):
    #     if nums[i] == nums[i-1]:
    #         del nums[i]
    #         i-=1
    #     i+=1

    # Algorithm without changing nums
    i = 0

    for num in nums:
        if i < 1 or num > nums[i - 1]:
            nums[i] = num
            i += 1

    return i

# removeDuplicates([1,2,2,3,4,4,5])

# "80. Remove Duplicates from Sorted Array II"

def removeDuplicatesSorted(nums):

    #With Time Complexity in mind
    # i = 0
    # n = len(nums)

    # hashMap = {}

    # while i < n:
    #     if  nums[i] not in hashMap:
    #         hashMap[nums[i]] = 1
    #     elif nums[i] in hashMap:
    #         hashMap[nums[i]] +=1
        
    #     if hashMap[nums[i]] > 2:
    #         del nums[i]
    #         i -= 1
    #         n -= 1

    #     i +=1

    # return len(nums)

    # With Space complexity in mind
    print(nums)

    i = 0

    for num in nums:
      if i < 2 or num != nums[i - 2]:
        nums[i] = num
        i += 1
    return i

# print(removeDuplicatesSorted([0,0,1,1,1,1,2,3,3]))


#################################
# "169. Majority Element"
def majorityElement(nums) -> int:
    # count = {}
    # res, maxCount = 0, 0

    # for n in nums:
    #     count[n] = 1 + count.get(n, 0)
    #     res = n if count[n] > maxCount else res

    #     maxCount = max(count[n], maxCount)

    # return res

    ans = None
    count = 0

    for num in nums:
        if count == 0:
            ans = num
        count += (1 if num == ans else -1)

    return ans
            

# print(majorityElement([2,2,1,1,1,2,2]))

# 189. Rotate Array

def reverse(nums, l, r) -> None:
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    
def rotate(nums, k):
    #Brute Force
    # for i in range(k):
    #     temp = nums[-1]
    #     for j in range(len(nums)-1, 0, -1):
    #         nums[j] = nums[j-1]
    #     nums[0] = temp

    # return nums

    #Little bit best approach
    # for i in range(k):
    #         last = len(nums)-1
    #         temp = nums[last]
    #         del nums[last]
    #         nums.insert(0, temp)
    # return nums


    #Recursive approach
    # k %= len(nums)
    # reverse(nums, 0, len(nums) - 1)
    # reverse(nums, 0, k - 1)
    # reverse(nums, k, len(nums) - 1)



    #Optimised Solution
    nums[:] = (nums[:-k%len(nums)][::-1] + nums[-k%len(nums):][::-1])[::-1]
    return nums

# print(rotate([-1,-100,3,99], 2))


########################
# 121. Best Time to Buy and Sell Stock
def maxProfit(prices):
    #Brute Force approach
    # profit = 0

    # for i in range(len(prices)):
    #     for j in range(i, len(prices)):
    #         if prices[i] < prices[j]:
    #             currentProfit = prices[j] - prices[i]
    #             profit = max(currentProfit, profit)

    # return profit

    minimum = prices[0]
    profit = 0

    for i in range(len(prices)):
        minimum = min(minimum, prices[i])
        currentProfit = prices[i] - minimum

        profit = max(currentProfit, profit)

    return profit

# print(maxProfit([7,1,5, 11, 0, 3,6,4]))


#######################################
# 122. Best Time to Buy and Sell Stock II
def maxProfit2(prices):
    #Brute force
    # minimum = prices[0]
    # profit = 0
    # stock = prices[0]
    # res = 0

    # for price in prices:
    #     minimum = min(price, minimum)
    #     stock = minimum
    #     currentProfit = price - minimum

    #     profit = max(currentProfit, profit)

    #     if stock < price:
    #         stock = price
    #         res += profit
    #         profit = 0
    #         minimum = price

    # return profit + res

    #Optimised solution
    sell = 0
    hold = -math.inf
    print(sell, hold)
    for price in prices:
        sell = max(sell, hold + price)
        hold = max(hold, sell - price)
        print(sell, hold)

    return sell

# print(maxProfit2([7,1,5,3,6,4]))


####################
# 55. Jump Game
def canJump(nums):
    i = 0
    reach = 0

    while i < len(nums) and i <= reach:
      reach = max(reach, i + nums[i])
      print(reach)
      i += 1

    return i == len(nums)

# print(canJump([2,3,1,1,4]))


def canJump2(nums):
    res = 0
    r = l = 0

    while r < len(nums) - 1:
        farthest = 0
        for i in range(l, r+1):
            farthest = max(farthest, i + nums[i])
        
        l = r+1
        r = farthest
        res +=1
    return res


# print(canJump2([2,3,1,1,4]))

#  ###################
# 274. H-Index
def hIndex(citations):
    citations.sort(reverse= True)

    if len(citations) == 1 and citations[0] > 0:
        return 1
    
    if citations[-1] > len(citations):
        return len(citations)
    
    for i in range(len(citations)):
        if citations[i] < i+1:
            return i
    
    return 0

# print(hIndex([7,7,7,7,7,7,7]))

#####################
#
def productExceptSelf(nums):
        n = len(nums)
        prefix = [1] * n  
        suffix = [1] * n 


        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]


        for i in reversed(range(n - 1)):
            suffix[i] = suffix[i + 1] * nums[i + 1]


        return [prefix[i] * suffix[i] for i in range(n)]

# print(productExceptSelf([1,2,3,4]))


set = []
import random
class RandomizedSet:

    def __init__(self):
        self.set = []

    def insert(self, val: int) -> bool:
        if val in set:
            return False
        set.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in set:
            set.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        randomNum = random.randint(0, len(set)-1)
        return set[randomNum]
    
# obj = RandomizedSet()
# print(obj.insert(2))
# print(obj.insert(3))
# print(obj.insert(4))
# # print(obj.remove(2))
# print(obj.getRandom())