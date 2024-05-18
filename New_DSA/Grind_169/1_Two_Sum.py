class Solution:
    # def twoSum(self, nums, target):
    #     numToIndex = {}

    #     for i, num in enumerate(nums):
    #         if target - num in numToIndex:
    #             return numToIndex[target - num], i
    #         numToIndex[num] = i

    def twoSum(self, nums, target):
        hashMap = {}
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in hashMap:
                return [i, hashMap[diff]]
            else:
                hashMap[nums[i]] = i
        print(hashMap)

s = Solution()
print(s.twoSum(nums = [2,7,11,15], target = 9))