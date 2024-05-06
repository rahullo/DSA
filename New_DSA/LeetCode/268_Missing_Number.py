class Solution:
    def missingNumber(self, nums):
        total = 0
        for num in nums:
            total += num
        m = len(nums)
        missing = abs(total - ((m*(m+1))//2))
        return missing

s = Solution()

print(s.missingNumber([ 0, 1]))