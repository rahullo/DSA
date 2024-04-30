class Solution:
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums)  -  1
        mid = (l + r)//2
        while l <= r:
            mid = (l + r)// 2 
            c = mid
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                r = mid-1
            else:
                l = mid + 1
        if nums[mid] < target:
            return mid + 1
        else: return mid
    
    def searchInsert2(self, nums, target):
        if target in nums:
            return nums.index(target)
        
        nums.append(target)
        nums.sort()
        return nums.index(target)

s = Solution()
arr1 = [1, 3, 5, 7, 9]
arr2 = [1, 2, 4, 6, 7, 9, 10, 12]
print(s.searchInsert2(arr2, 8))