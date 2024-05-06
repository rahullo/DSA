class Solution:
    def containsNearbyDuplicate(self, nums, k):

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j] and abs(i-j) <= k:
        #             return True
        # return False

        for i in range(len(nums)-k):
            for j in range(i+1, i+k+1):
                # print(i,j)
                if nums[i] == nums[j] and abs(i-j) <= k:
                    return True
        return False


s = Solution()      

print(s.containsNearbyDuplicate([1, 2, 3, 1], 3))
print(s.containsNearbyDuplicate([1, 0, 1, 1], 1))
print(s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))