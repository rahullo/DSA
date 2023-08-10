arr1, arr2 = [1,2,3,0,0,0], [2, 5, 6]


# 1) "88. Merge Sorted Array"
def merge(nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = nums1[:m] + nums2[:n]
        nums1.sort()




# " 27. Remove Element "
def removeElement(nums, val) -> int:
    i = 0
    while i<(len(nums)):
        if nums[i] == val:
            count+=1
            del nums[i]
            i-=1
        i+=1
    
    return len(nums)    

# "26. Remove Duplicates from Sorted Array"
def removeDuplicates(nums) -> int:
    # Algorithm which change nums
    # i = 1
    # while i < (len(nums)):
    #     if nums[i] == nums[i-1]:
    #         del nums[i]
    #         i-=1
    #     i+=1

    # Algorithm without changing nums
    i = 0

    for num in nums:
        if i < 1 or num > nums[i - 1]:
            nums[i] = num
            i += 1

    return i

removeDuplicates([1,2,2,3,4,4,5])