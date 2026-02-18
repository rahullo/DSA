def containsDuplicate(nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False

def containsDuplicate(nums):
    newArr = set(nums)

    return len(newArr) != len(nums)

