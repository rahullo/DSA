arr1, arr2 = [1,2,3,0,0,0], [2, 5, 6]
from collections import Counter

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

# removeDuplicates([1,2,2,3,4,4,5])

# "80. Remove Duplicates from Sorted Array II"

def removeDuplicatesSorted(nums):

    #With Time Complexity in mind
    # i = 0
    # n = len(nums)

    # hashMap = {}

    # while i < n:
    #     if  nums[i] not in hashMap:
    #         hashMap[nums[i]] = 1
    #     elif nums[i] in hashMap:
    #         hashMap[nums[i]] +=1
        
    #     if hashMap[nums[i]] > 2:
    #         del nums[i]
    #         i -= 1
    #         n -= 1

    #     i +=1

    # return len(nums)

    # With Space complexity in mind
    print(nums)

    i = 0

    for num in nums:
      if i < 2 or num != nums[i - 2]:
        nums[i] = num
        i += 1
    return i

# print(removeDuplicatesSorted([0,0,1,1,1,1,2,3,3]))


#################################
# "169. Majority Element"
def majorityElement(nums) -> int:
    # count = {}
    # res, maxCount = 0, 0

    # for n in nums:
    #     count[n] = 1 + count.get(n, 0)
    #     res = n if count[n] > maxCount else res

    #     maxCount = max(count[n], maxCount)

    # return res

    ans = None
    count = 0

    for num in nums:
        if count == 0:
            ans = num
        count += (1 if num == ans else -1)

    return ans
            



print(majorityElement([2,2,1,1,1,2,2]))