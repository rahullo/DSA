def moveZeroes(nums):
    left = 0

    for right in range(len(nums)):
        if nums[right] != 0:
            nums[right], nums[left] = nums[left], nums[right]
            left += 1
    return nums


print(moveZeroes([0, 2, 1, 0, 4, 3]))