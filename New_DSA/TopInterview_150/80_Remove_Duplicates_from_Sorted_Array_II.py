# 80. Remove Duplicates from Sorted Array II
class Solution:
    def removeDuplicates(self, nums):
        hashMap = {}
        i = 0
        while i < len(nums):
            if not hashMap[i]:
                hashMap[i] = 1
                i+=1
                continue
            elif hashMap[i] and hashMap[i] < 2:
                hashMap[i] +=1
                i+=1
                continue
            if hashMap[i] == 2:
                del nums[i]

        return nums
        

s = Solution()

print(s.removeDuplicates([1, 1, 2, 3, 3, 4]))