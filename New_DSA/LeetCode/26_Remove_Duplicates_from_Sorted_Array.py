class Solution:
    def removeDuplicates(self, nums):
        x = len(nums)
        ans = list(set(nums))
        nums = ans
        if len(nums) != x:
            for i in range(x - len(nums)):
                nums.append('_')
        return nums
    
s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))