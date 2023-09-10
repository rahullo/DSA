def longestConsecutive(nums):
    ans = 0
    seen = set(nums)

    for num in nums:
        if num - 1 in seen:
            continue
        length = 0
        while num in seen:
            num += 1
            length += 1
        ans = max(ans, length)

    return ans

print(longestConsecutive([1, 2, 3, 4]))