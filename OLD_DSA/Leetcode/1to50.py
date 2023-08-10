###################
#### 3 #######

# def longestword(string):
#     list1 = {}
#     maxi = 0
#     count = 0
#     for item in string:
#         if item in list1:
#             list1.clear()
#             count = 0
#             list1[item] = True
#             count +=1

#         if item not in list1:
#             list1[item] = True
#             count +=1
#         maxi = max(maxi, count)
#     return maxi

    
# # print(longestword('dvdf'))


# def convert(s, numRows):
#     rows = [''] * numRows
#     k = 0
#     direction = (numRows == 1) - 1

#     for c in s:
#       rows[k] += c
#       if k == 0 or k == numRows - 1:
#         direction *= -1
#       k += direction
#       print(rows, k, direction)

#     return ''.join(rows)

# print(convert("PAYPALISHIRING", 4))

# import math
# class Solution:
#     def maxProfit(self, prices):
#         sellOne = 0
#         holdOne = -math.inf

#         for price in prices:
#             print(sellOne, holdOne)
#             sellOne = max(sellOne, holdOne + price)
#             holdOne = max(holdOne, -price)

#         return sellOne
    
#     def maxProfit2(self, prices):
#         mini = prices[0]
#         profit = 0
#         for price in prices:
#             cost = price - mini
#             profit = max(profit, cost)
#             mini = min(mini, price)
#         return profit

  
# s1 = Solution()

# print(s1.maxProfit2([7, 1, 5, 3, 6, 4]))

# def isBadVersion(m):
#     badVersion = 1702766719
#     if m == badVersion:
#         print("true")
#         return True
#     else:
#         return False

# def firstBadVersion(n):
#     print("1")
#     l = 1
#     r = n
#     print("2")

#     while l < r:
#         print("3")
#         m = (l + r) >> 1
#         print(l, r, (l + r) >> 1)
#         if isBadVersion(m):
#             print("4")
#             r = m
#         else:
#             l = m + 1

#     return l

    # yes = n

    # while not isBadVersion(yes):
    #     yes -=1
    # return yes

# print(firstBadVersion(2126753390))

# print(32 >> 2)
# print(2 << 5)

# def searchInsert(nums, target): #Search insert Position
#     left = 0
#     right = len(nums) - 1
#     mid = (left+right)  // 2
#     while left <= right:
#         mid = (left+right)  // 2
#         if nums[mid] == target:
#             return mid
#         elif target < nums[mid]:
#             right = mid - 1
#         else:
#             left = mid + 1
#     if nums[mid] < target:
#         return mid +1
#     else:
#         return mid
        

# print(searchInsert([1, 3, 5, 6], ))

# def twoSum(nums, target):
#     l = 0
#     r = len(nums) -1 
#     ans = []
#     while l < r:
#         sum = nums[l] + nums[r]
#         if sum == target:
#             ans.append([l + 1, r + 1])
#             l+=1
#             r-=1
#         elif sum < target:
#             l+=1
#         else:
#             r -=1
#     return ans
    
#     l = 0
#     r = len(nums) -1 
#     while l < r:
#         sum = nums[l] + nums[r]
#         if sum == target:
#             return [l + 1, r + 1]
#         elif sum < target:
#             l+=1
#         else:
#             r -=1
        
# print(twoSum([1, 2, 3, 4, 5, 6, 7], 6))

# def reverseString(s):
#     l = 0
#     r = len(s)
#     while l<r:
#         s[l], s[r-1] = s[r-1], s[l]
#         l+=1
#         r-=1
    
#     return s

# print(reverseString(["H","a","n","n","a","h"]))

# def reverseWords(s):
#     return " ".join([word[::-1]for word in s.split()])
     

# print(reverseWords("Let's take LeetCode contest"))

# def reverseStr(s, k):
#     arr =[]
#     for item in s:
#         arr.append(item)

    

# print(reverseStr("Rahul", 3))