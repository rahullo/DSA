class Solution:
    def intersection(self, nums1, nums2):
        ans = []
        for num in nums1:
            if num in nums2 and num not in ans:
                ans.append(num)
            
        return ans
    
    def intersection2(self, nums1, nums2):
        return {*nums1} & {*nums2}
    
s = Solution()

print(s.intersection2(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))