class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        count = 0
        while i < len(nums):
            if nums[i] == 0:
                count+=1
                del nums[i]
                i-=1
            i+=1
        
        for i in range(count):
            nums.append(0)

        return nums
    
    def moveZeroes2(self, nums):
        i = len(nums) - 1
        while i >= 0:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
            i-=1
        return nums

s = Solution()
print(s.moveZeroes2([0,1,0,3,12]))