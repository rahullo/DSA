class Solution:
    def removeElement(self, nums, val):
        i = 0
        count = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
                count+=1
                i-=1
            i+=1
        for i in range(count):
            nums.append('_')
        print(nums)
        return len(nums) - count
    
s = Solution()

print(s.removeElement([0,1,2,2,3,0,4,2], 2))