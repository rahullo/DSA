class Solution:
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1 ]:
                return True
        return False
    
    def containsDuplicate2(self, nums):
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False


s = Solution()
print(s.containsDuplicate2([1, 2, 3, 1]))
print(s.containsDuplicate2([1, 2, 3, 4]))
print(s.containsDuplicate2([1,1,1,3,3,4,3,2,4,2]))
        