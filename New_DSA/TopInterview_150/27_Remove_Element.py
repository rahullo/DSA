class Solution:
    def removeElement(self, nums, val):
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                del nums[i]
                n-=1
                i-=1
            i+=1
        return nums

s = Solution()
print(s.removeElement([1, 3, 5, 0, 0, 0, 0], 0))