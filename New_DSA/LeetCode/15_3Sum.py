# class Solution:
#     def threeSum2(self, nums):
#         ans = []
#         for i in range(len(nums) - 2):
#             for j in range(i+1, len(nums)-1):
#                 for k in range(j+1, len(nums)):
#                     if nums[i]+nums[j]+nums[k] == 0:
#                         if [nums[i], nums[j], nums[k]] not in ans:
#                             ans.append([nums[i], nums[j], nums[k]])
#         return ans
    
#     def threeSum(self, nums):
#         if len(nums) < 3:
#             return []

#         ans = []

#         nums.sort()

#         for i in range(len(nums) - 2):
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#             l = i + 1
#             r = len(nums) - 1
#             while l < r:
#                 summ = nums[i] + nums[l] + nums[r]
#                 if summ == 0:
#                     ans.append([nums[i], nums[l], nums[r]])
#                     l += 1
#                     r -= 1
#                     while nums[l] == nums[l - 1] and l < r:
#                         l += 1
#                     while nums[r] == nums[r + 1] and l < r:
#                         r -= 1
#                 elif summ < 0:
#                     l += 1
#                 else:
#                     r -= 1

#         return ans

from collections import defaultdict


class Solution:
    def threeSum(self, nums):
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
            print(set1, set2)
            set1Items = list(set1.items())
            for i, (j, k) in enumerate(set1Items):
                for j2, k2 in set1Items[i:]:
                    if j != j2 or (j == j2 and k > 1):
                        if -j-j2 in set2:
                            result.append((j, j2, -j-j2))
        return result

s = Solution()

print(s.threeSum([-1, 0, 1, 2, -1, -4]))