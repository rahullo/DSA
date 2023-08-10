# 1) "88. Merge Sorted Array"

def merge(nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = nums1[:m] + nums2[:n]
        nums1.sort()


arr1, arr2 = [1,2,3,0,0,0], [2, 5, 6]

print(arr1)
print(merge(arr1, 3, arr2, 3))
print(arr1)