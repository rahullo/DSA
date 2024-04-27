class Solution:
    def twoSum(self, nums, target):
        numToIndex = {}

        for i, num in enumerate(nums):
            if target - num in numToIndex:
                return[numToIndex[target-num], i]
            numToIndex[num] = i

nums = [3,2,4]
target = 6

s = Solution()
print(s.twoSum(nums, target))