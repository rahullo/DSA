class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # ans = []
        # i, j = 0, 0
        # while i < m and j < n:
        #     if nums1[i] <= nums2[j]:
        #         ans.append(nums1[i])
        #         i+=1
        #     elif nums1[i] >= nums2[j]:
        #         ans.append(nums2[j])
        #         j+=1
        # nums1 =  ans + nums1[i: m] + nums2[j: n]
        # return nums1

        ans = nums1[:m] + nums2[:n]
        ans.sort()
        nums1 = ans
        
        return nums1


s = Solution()

print(s.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))