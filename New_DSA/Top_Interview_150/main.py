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


# set = []
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

#############################
# 134. Gas Station
def gasStation(gas, cost):
    if sum(gas) < sum(cost): return -1
    tank = idx = 0
    for i in range(len(gas)):
        tank+= gas[i]-cost[i] 
        if tank < 0: tank, idx = 0, i+1
    return idx

# print(gasStation([1,2,3,4,5], [3,4,5,1,2]))

###########################
# 135. Candy

def candy(ratings):
    # candies = 0
    # for i in range(len(rating)):
    #     if i == 0 and rating[i] >= rating[i+1]:
    #         candies +=2
    #     elif i == 0 and rating[i] <= rating[i+1]:
    #        candies +=1
    #     elif i == len(rating)-1 and rating[i] >= rating[i-1]:
    #         candies +=2
    #     elif i == len(rating)-1 and rating[i] <= rating[i-1]:
    #         candies +=1
    #     elif rating[i] >= rating[i-1] or rating[i] >= rating[i+1]:
    #             candies +=2
    #     else:
    #         candies +=1
    # return candies

    n = len(ratings)
    candies = [1]*n
    #Iteration from left to right
    for i in range(1,n):
        if ratings[i]>ratings[i-1] and candies[i]<=candies[i-1]:
            candies[i] = candies[i-1]+1
    #Iteration from right to left
    for i in range(n-2,-1,-1):
        if ratings[i]>ratings[i+1] and candies[i]<=candies[i+1]:
            candies[i] = candies[i+1]+1
    return sum(candies)


# print(candy([1,2,87,87,87,2,1])) #[1, 2, 2, 2, 2, 2, 1]

###############################
# Roman To Integer
def romanToInt(s):
    ans = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000}

    for a, b in zip(s, s[1:]):
        if roman[a] < roman[b]:
            ans -= roman[a]
        else:
            ans += roman[a]

    return ans + roman[s[-1]]

# print(romanToInt("LVIII"))

##############################
# 12. Integer To Roman

def intToRoman(num):
    valueSymbols = [(1000, 'M'), (900, 'CM'),
                (500, 'D'), (400, 'CD'),
                (100, 'C'), (90, 'XC'),
                (50, 'L'), (40, 'XL'),
                (10, 'X'), (9, 'IX'),
                (5, 'V'), (4, 'IV'),
                (1, 'I')]
    
    ans = []

    for value, symbol in valueSymbols:
        if num == 0:
            break
        count, num = divmod(num, value)
        print(count, num)
        ans.append(symbol * count)

    return ''.join(ans)

# print(intToRoman(43))

###########################
# 58. Length of last word
def lengthOfLastWord(s):
    newS = s.strip()
    count = 0

    for i in range(len(newS)-1, -1, -1):
        if newS[i] == " ":
            return count
        else:
            count+=1

    return count

# print(lengthOfLastWord("luffy is still joyboy"))

###############################
# 151. Reverse Words in a String
def reverseWords(s):
    # words = []

    # new_str = s.strip()

    # start = len(new_str)-1

    # for i in range(len(new_str)-1, -1, -1):
    #     if new_str[i] == " ":
    #         words.append(new_str[i+1: start+1])
    #         start = i-1
    #     elif i == 0:
    #         words.append(new_str[i: start+1])
        

    # i = 0
    # while i < len(words):
    #     if words[i] == "":
    #         words.remove("")
    #         i-=1
    #     i+=1

    # return " ".join(words)

    s = s.split()
    s = s[::-1]
    return " ".join(s)

# print(reverseWords("a   good         example "))

######################
# 14. Longest Common Prefix
def longestCommonPrefix(strs) -> str:
    ans=""
    strs=sorted(strs)
    first=strs[0]
    last=strs[-1]
    for i in range(min(len(first),len(last))):
        if(first[i]!=last[i]):
            return ans
        ans+=first[i]
    return ans

# print(longestCommonPrefix(["flower","flow","flowht"]))

##############################
# 28. Find the Index of the First Occurrence in a String

def strStr(haystack, needle):
    m = len(haystack)
    n = len(needle)

    for i in range(m):
        if haystack[i: i+n] == needle:
            return i
    return -1

# print(strStr('leetcode', 'tco'))


##########################
# 239. Sliding Window maximum 
from collections import deque

def maxSlidingWindow(nums, k):
    # i = 0
    # j = len(nums) if len(nums) % 2 != 0 else len(nums) - 1
    
    # fArr = []
    # bArr = []

    # while i + k != j:
    #     print(i, j)
    #     print(nums[i: i+k], nums[j-k: j])
    #     fArr.append(max(nums[i: i+k]))
    #     bArr.insert(0, max(nums[j-k: j+1]))

    #     i+=1
    #     j-=1
    
    # fArr.append(max(nums[i:j]))
    # print(nums[i:j])

    # return fArr+bArr

    
    result = [] 
    window = deque()  
    for i in range(len(nums)):
        print(window, result)
        while window and window[0] < i - k + 1:
            window.popleft()
        
        while window and nums[i] >= nums[window[-1]]:
            window.pop()
        
        window.append(i)
        
        if i >= k - 1:
            result.append(nums[window[0]])
    
    return result

# print(maxSlidingWindow([1], 1))
# print(maxSlidingWindow([1,3,-1,-3,5,3,6, 7], 3))

###################
# 42. Trapping Rain Water
def trap(height):
    # Array preprocessing approach
    # preffix = [0] * len(height)
    # suffix = [0] * len(height)

    # current_max = 0
    # for i in range(len(height)):
    #     if height[i] > current_max:
    #         current_max = height[i]
    #         preffix[i] = current_max
    #     else:
    #         preffix[i] = current_max
    
    # current_max = 0
    # for i in range(len(height)-1, -1, -1): 
    #     if current_max < height[i]:  #[0, 0, 0, 0, 0, 0] = [0, 1, 1, 3, 2, 1]
    #         current_max = height[i]
    #         suffix[i] = current_max
    #     else:
    #         suffix[i] = current_max
    # res = 0
    # for i in range(len(height)):
    #     res += min(preffix[i], suffix[i]) -height[i]

    # return res

    # Two pointer approach
    n = len(height)
    res = 0

    l = 0
    r = n-1
    maxL = maxR = 0

    while l <= r:
        if height[l] <= height[r]:
            if height[l] > maxL:
                maxL = height[l]
            else: res += maxL - height[l]

            l+=1
        else:
            if height[r] > maxR:
                maxR = height[r]
            else:
                res+= maxR - height[r]

            r-=1
    return res

# print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
# print(trap([0,6,1,3,2,1]))

###############################
# 6. Zigzag Conversion
def convert(s, numRows):

    if numRows == 1: return s

    res = ""

    for r in range(numRows):
        increment = 2*(numRows-1)
        for i in range(r, len(s), increment):
            res += s[i]
            if (r > 0 and r < numRows -1 and 
                i+increment-2*r< len(s)):
                res += s[i+increment-2*r]

    return res

    # optimized approach
    # rows = [''] * numRows
    # k = 0
    # direction = (numRows == 1) -1
    # print(direction)
    # for c in s:
    #     rows[k] += c
    #     if k == 0 or k == numRows-1:
    #         direction *= -1
    #     k += direction
    #     print(rows)
        
    # return ''.join(rows)


# print(convert("PAYPALISHIRING", 3))

################################3
# 125. Valid Palindrome
def isPalindrome(s) -> bool:
    i = 0
    j = len(s)-1

    while i <= j:
        while i < j and not s[i].isalnum():
            i+=1
        while i < j and not s[j].isalnum():
            j-=1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True


# print(isPalindrome("A man, a plan, a canal: Panama"))

#################
# 392. Is Subsequence
def isSubsequence(s, t) -> bool:
    # seq = 0
    # for char in s:
    #     for i in range(len(t)):
    #         if char not in t:
    #             return False
    #         elif t[i] == char and i < seq:
    #             return False
    #         elif t[i] == char and i >= seq:
    #             seq = i
    # return True
    for c in s:
        i = t.find(c)
        if i == -1:    return False
        else:   t = t[i+1:]
    return True



# print(isSubsequence('abc', 'ahbgdc'))

############################
# 167. Two Sum II - Input Array Is Sorted
def twoSum(numbers, target):
    l = 0
    r = len(numbers)-1

    while l <= r:
        sum = numbers[l] + numbers[r]

        if sum == target:
            return [l+1, r+1]
        elif sum > target:
            r -= 1
        else:
            l += 1
        

# print(twoSum([2, 7, 11, 15], 13))

############################################
# 11. Container With Most Water
def maxArea(height):
    l = 0
    r = len(height) - 1
    ans = 0

    while l < r:
        minHeight = min(height[l], height[r])
        ans = max(ans, minHeight * (r-l))
        if height[l] < height[r]:
            l+=1
        else:
            r-=1
    return ans

# print(maxArea([1,8,6,2,5,4,8,3,7]))

###############################
# 15. 3Sum
from collections import defaultdict
def threeSum(nums):
    negative = defaultdict(int)
    positive = defaultdict(int)
    zeros = 0
    for num in nums:
        if num < 0:
            negative[num] += 1
        elif num > 0:
            positive[num] += 1
        else:
            zeros += 1
    
    result = []
    if zeros:
        for n in negative:
            if -n in positive:
                result.append((0, n, -n))       
        if zeros > 2:
            result.append((0,0,0))

    for set1, set2 in ((negative, positive), (positive, negative)):
        set1Items = list(set1.items())
        for i, (j, k) in enumerate(set1Items):
            for j2, k2 in set1Items[i:]:
                if j != j2 or (j == j2 and k > 1):
                    if -j-j2 in set2:
                        result.append((j, j2, -j-j2))
    return result

# print(threeSum([-1,0,1,2,-1,-4]))

######################################
# 209. Minimum Size Subarray Sum
def minSubArrayLen(target, nums):
    # nums.sort(reverse= True)
    # print(nums)
    # ans = 0
    # sums = 0

    # for i in range(len(nums)):
    #     sums += nums[i]
    #     print(sums, nums[i])
    #     ans += 1

    #     if sums >= target:
    #         return ans

    # return 0

    
    minlen = float('inf')
    l,sum =0,0
    for r in range(len(nums)):
        sum += nums[r]
        while sum >= target:
            minlen = min(minlen, r-l+1)
            sum -= nums[l]
            l += 1
    return minlen if minlen<=len(nums) else 0

# print(minSubArrayLen(213, [12,28,83,4,25,26,25,2,25,25,25,12]))

#################################3
# 3. Longest Substring Without Repeating Characters
from collections import Counter
def lengthOfLongestSubstring(s):
    ans = 0
    count = Counter()
    print(count)
    l = 0
    for r, c in enumerate(s):
        count[c] += 1
        print(count)
        while count[c] > 1:
            count[s[l]] -= 1
            l += 1
        ans = max(ans, r - l + 1)

    return ans

# print(lengthOfLongestSubstring('abcabccbb'))

##############################
# 54. Spiral Matrix
def spiralOrder( matrix ):
    if not matrix:
        return []

    m = len(matrix)
    n = len(matrix[0])
    ans = []
    r1 = 0
    c1 = 0
    r2 = m - 1
    c2 = n - 1

    # Repeatedly add matrix[r1..r2][c1..c2] to ans
    while len(ans) < m * n:
        j = c1
        while j <= c2 and len(ans) < m * n:
            ans.append(matrix[r1][j])
            j += 1
        i = r1 + 1
        while i <= r2 - 1 and len(ans) < m * n:
            ans.append(matrix[i][c2])
            i += 1
        j = c2
        while j >= c1 and len(ans) < m * n:
            ans.append(matrix[r2][j])
            j -= 1
        i = r2 - 1
        while i >= r1 + 1 and len(ans) < m * n:
            ans.append(matrix[i][c1])
            i -= 1
        r1 += 1
        c1 += 1
        r2 -= 1
        c2 -= 1

    return ans

# print(spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))

# 36. Valid Sudoku
import collections
def isValidSudoku(board):
    seen = set()

    for i in range(9):
      for j in range(9):
        c = board[i][j]
        if c == '.':
          continue
        if c + '@row ' + str(i) in seen or \
           c + '@col ' + str(j) in seen or \
           c + '@box ' + str(i // 3) + str(j // 3) in seen:
          return False
        seen.add(c + '@row ' + str(i))
        seen.add(c + '@col ' + str(j))
        seen.add(c + '@box ' + str(i // 3) + str(j // 3))

    return True


# print(isValidSudoku([["5","3",".",".","7",".",".",".","."],
#                     ["6",".",".","1","9","5",".",".","."],
#                     [".","9","8",".",".",".",".","6","."],
#                     ["8",".",".",".","6",".",".",".","3"],
#                     ["4",".",".","8",".","3",".",".","1"],
#                     ["7",".",".",".","2",".",".",".","6"],
#                     [".","6",".",".",".",".","2","8","."],
#                     [".",".",".","4","1","9",".",".","5"],
#                     [".",".",".",".","8",".",".","7","9"]]))


################################
# 48. Rotate Image

def rotate(matrix):
    # matrix.reverse()

    # for i in range(len(matrix)):
    #     for j in range(i+1, len(matrix)):
    #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # return matrix
    matrix[:]=list(zip(*matrix[::-1]))

# print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

##############################
# 289. Game of Life
def checkNeighbour(board, i, j):
    survivor = 0
    neighbours = [[i-1, j-1], [i-1, j], [i-1, j+1], [i, j-1], [i, j+1], [i+1, j-1], [i+1, j], [i+1, j+1]]
    for item in neighbours:
        if board[item[0]][item[1]] and board[item[0]][item[1]] == 1:
            survivor +=1

    return survivor


def gameOfLife(board):

    row = len(board)
    col = len(board[0])
    ans = []
    survivor  = checkNeighbour(board, 0, 0)

    print(survivor)

    # for i in range(row):
    #     for j in range(col):
    #         survivor = checkNeighbour(board, i, j)
    #         print(survivor)
    
    return board

# print(gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))

############################
# 383. Ransom Note
import string
def canConstruct(ransomNote, magazine):
    # counter = collections.Counter(magazine)
    # print(counter)
    # for char in ransomNote:
    #     counter[char] -=1

    #     if counter[char] < 0:
    #         return False

    # return True

    count1 = collections.Counter(ransomNote)
    count2 = collections.Counter(magazine)
    return all(count1[c] <= count2[c] for c in string.ascii_lowercase)
    
# print(canConstruct("aab", "baa"))


#################################
# 205. Isomorphic Strings
def isIsomorphic( s, t):
    mapST, mapTS = {}, {}

    for c1, c2 in zip(s, t):
        if ((c1 in mapST and mapST[c1] != c2) or
            (c2 in mapTS and mapTS[c2] != c1)):
            return False

        mapST[c1] = c2
        mapTS[c2] = c1

    return True

# print(isIsomorphic("paper", "title"))

################
# 290. Word Pattern
def wordPattern(pattern, s):
    ls = s.split()
    k, v, p = Counter(pattern), Counter(ls), Counter(zip(pattern, ls))
    print(k, v, p)
    return len(k) == len(v) == len(p) and len(pattern) == len(ls)

# print(wordPattern("abba","dog cat cat dog"))

################################
# 242. Valid Anagram
def isAnagram(s, t):
    # s = ''.join(sorted(s))
    # t = ''.join(sorted(t))

    # return s == t

    dict = collections.Counter(s)

    for c in t:
        dict[c] -=1
        if dict[c] < 0:
            return False
    return True

# print(isAnagram("anagram", "nagaram"))

################################
# 49. Group Anagram
def groupAnagrams(strs):
    dict = collections.defaultdict(list)

    for str in strs:
        key = ''.join(sorted(str))
        dict[key].append(str)

        
    print(dict)
    return dict.values()

# print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

###############################
# 1. two Sum
def twoSum(nums, target):
    dict = {}

    for  i, num in enumerate(nums):
        if target - num in dict:
            return [dict[target-num], i]
        dict[num] = i

# print(twoSum([2, 7, 11, 15], 9))

########################
# 202. Happy Number
def isHappy(n):
    def squaredSum(n: int) -> bool:
      summ = 0
      while n:
        summ += pow(n % 10, 2)
        n //= 10
      return summ

    slow = squaredSum(n)
    fast = squaredSum(squaredSum(n))

    while slow != fast:
      print(slow, fast)
      
      slow = squaredSum(slow)
      fast = squaredSum(squaredSum(fast))

    print(slow, fast)

    return slow == 1
   

# print(isHappy(18))

###################################
# 219. Contain Duplicate II
def containsNearbyDuplicate(nums, k):
    hashSet = {}

    for i, num in enumerate(nums):
        if num in hashSet and i - hashSet[num] <= k:
            return True
        hashSet[num] = i

    return False

    # mySet = set()
    # for r in range(len(nums)):
    #     if nums[r] in mySet:return True
    #     mySet.add(nums[r])
    #     if len(mySet)==k+1:mySet.remove(nums[r-k])
    # return False

# print(containsNearbyDuplicate([1, 0, 1, 1], 1))

#####################################
# 128. Longest Consecutive Sequence
def longestConsecutive(nums):
    ans = 0
    seen = set(nums)

    for num in nums:
        if num - 1 in seen:
            continue
        length = 0
        while num in seen:
            num += 1
            length += 1
        ans = max(ans, length)

    return ans

print(longestConsecutive([1, 2, 3, 4]))
