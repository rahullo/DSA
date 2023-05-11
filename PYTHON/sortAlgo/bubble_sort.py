rawArray = [5, 3, 7, 1, 0, 19, -1]



def bubbleSort(nums):
    for i in range(0, len(nums)):
        for j in range(0, len(nums)-i-1):
            if(nums[j] > nums[j+1]):
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

# print(bubbleSort(rawArray))