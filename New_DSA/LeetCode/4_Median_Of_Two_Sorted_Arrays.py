class Solution:
    def mergeArrays(self, nums1, nums2):
        new_Arr = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                new_Arr.append(nums1[i])
                i+=1
            elif nums1[i] > nums2[j]:
                new_Arr.append(nums2[j])
                j+=1
        new_Arr = new_Arr + nums1[i:] + nums2[j:]
        return new_Arr

    def findMedianSortedArrays(self, nums1, nums2):
        mergedArray = self.mergeArrays(nums1, nums2)
        l = len(mergedArray)
        if l % 2 == 0:
            m = l//2
            return ((mergedArray[m-1] + mergedArray[m])/2)
        else:
            return mergedArray[l//2]
        
s = Solution()
print(s.findMedianSortedArrays([1, 2], [3, 4]))