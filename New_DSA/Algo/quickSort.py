def partion(nums, low, high):
    pivot = high
    i = low -1
    for j in range(low, high):
        if nums[j] < nums[pivot]:
            i+=1
            nums[j], nums[i] = nums[i], nums[j]
    nums[i+1], nums[pivot] = nums[pivot], nums[i+1]
    return i+1

def quickSort(nums, low, high):
    if low < high:
        partitionIndex = partion(nums, low, high)
        quickSort(nums, low, partitionIndex-1)
        quickSort(nums, partitionIndex+1, high)


array = [4, 3, 6, 8, 39, 2, 1]

quickSort(array, 0, 6)
print(array)