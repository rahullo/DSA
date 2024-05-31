class Solution:
    def removeDuplicates(self, nums):
        # i = 1
        # count = 0
        # while i < len(nums):
        #     if nums[i] == nums[i-1]:
        #         del nums[i]
        #         count +=1
        #         i-=1
        #     i+=1

        # for i in range(count):
        #     nums.append('_')
        # return nums
        new = list(set(nums))
        return new
s = Solution()

print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(s.removeDuplicates([1,1,2]))