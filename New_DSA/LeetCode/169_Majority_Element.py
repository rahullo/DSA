import collections

class Solution:
    def majorityElement(self, nums):
        count = collections.Counter(nums)
        max_count = 0
        num = 0
        for key in count:
            if max_count < count[key]:
                max_count = count[key]
                num = key
        return num

s = Solution()

print(s.majorityElement([2,2,1,1,1,2,2]))