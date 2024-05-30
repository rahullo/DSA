class Solution:
    def merge(self, nums1, m, nums2, n):
        last = m + n -1
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -=1
            else:
                nums1[last] = nums2[n-1]
                n-=1
            last-=1
        while n > 0:
            nums1[last] = nums2[n]
            n-=1
            last-=1
        return nums1
    
    def merge2(self, nums1, m, nums2, n):
        i = m - 1  # nums1's index (the actual nums)
        j = n - 1  # nums2's index
        k = m + n - 1  # nums1's index (the next filled position)

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1

s = Solution()
print(s.merge([1, 3, 5, 0, 0, 0, 0], 3, [2, 4, 6, 8], 4))