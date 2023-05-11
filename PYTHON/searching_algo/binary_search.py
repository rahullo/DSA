# def binarySearch(nums, num):
#     low = 0
#     high = len(nums)-1
#     i = 0
#     while i < len(nums)// 2:
#         mid = (low + high) //2
#         if nums[mid] == num:
#             return True
#         elif num < nums[mid]:
#             high = mid-1
#         else:
#             low = mid+1
#         i+=1
#     return False

def binarySearchRecursion(nums, num, low, high):
    if low > high:
        return False
    else:
        mid = (low + high)//2
        if nums[mid] == num:
            return True
        elif num < nums[mid]:
            return binarySearchRecursion(nums, num, low, mid-1)
        else:
            return binarySearchRecursion(nums, num, mid+1, high)

print(binarySearchRecursion([1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 0, 8))
