class Solution:
    def summaryRanges(self, nums):
        start = 0
        end = 0
        ans = []
        for i in range(1, len(nums)):
            if nums[end]+1 == nums[i]:
                print('continue')
                end = i
            # elif nums[end] == nums[i]:
            #     ans.append(f'{nums[i]}')
            elif nums[end] != nums[i] + 1:
                print('break')
                ans.append(f'{nums[start]} -> {nums[end]}')
                start = i
                end = i+1
        return ans
    
    def findRanges(self, nums):
        if not nums:
            return []

        ranges = []
        start = end = nums[0]

        for num in nums[1:]:
            if num == end + 1:
                end = num
            else:
                if start == end:
                    ranges.append(str(start))
                else:
                    ranges.append(f"{start}->{end}")
                start = end = num

        if start == end:
            ranges.append(str(start))
        else:
            ranges.append(f"{start}->{end}")

        return ranges

# Test cases
nums1 = [0, 1, 2, 4, 5, 7]
nums2 = [0, 2, 3, 4, 6, 8, 9]

  # Output: ["0", "2->4", "6", "8->9"]

    
s = Solution()

# print(s.summaryRanges([0,1,2,4,5,7]))

print(s.findRanges(nums1))
print(s.findRanges(nums2))