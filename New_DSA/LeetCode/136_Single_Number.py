class Solution:
    def singleNumber(self, nums):
        nums.sort()
        for i in range(len(nums)):
            if i == 0:
                if nums[i] == nums[i+1]:
                    continue
                elif nums[i] != nums[i+1]:
                    return nums[i]
            elif 1 <= i <= len(nums)-2:
                if nums[i] != nums[i+1] and nums[i] != nums[i-1]:
                    return nums[i]
            elif nums[-1] != nums[-2]:
                return nums[-1]
            

    def singleNumber2(self, nums):
        # Initialize the result variable
        result = 0
        
        # XOR all elements in the array
        for num in nums:
            result ^= num
        
        return result

s = Solution()
print(s.singleNumber([2,1,2]))