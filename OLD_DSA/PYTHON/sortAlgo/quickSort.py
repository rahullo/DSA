rawArr = [4, 3,7, 9, 0, 1, 11, -1]


# def partition(arr, left, right):
#     pivot = right
#     second_index = left-1
#     for i in range(left, right):
#         if arr[i] < arr[pivot]:
#             second_index +=1
#             arr[i], arr[second_index] = arr[second_index], arr[i]
#     arr[second_index+1], arr[pivot] = arr[pivot], arr[second_index+1]
#     return second_index+1

# def quickSort(arr, left, right):
#     if left<right:
#         pi = partition(arr, left, right)
#         quickSort(arr, left, pi-1)
#         quickSort(arr, pi+1, right)
#     return arr

# print(quickSort([3, 1, 5, 4, 2], 0, 4))


import Rough
# class QuickSortAlgo():
#     def __init__(self) -> None:
#         pass

#     def partition(self, arr, left, right):
#         pivot = right
#         second_index = left-1
#         for i in range(left, right):
#             if arr[i] < arr[pivot]:
#                 second_index +=1
#                 arr[i], arr[second_index] = arr[second_index], arr[i]
#         arr[second_index+1], arr[pivot] = arr[pivot], arr[second_index+1]
#         return second_index +1

#     def quickSort(self, arr, left, right):
#         if left < right:
#             partition_index = self.partition(arr, left, right)
#             self.quickSort(arr, left, partition_index-1)
#             self.quickSort(arr, partition_index+1, right)
#         return arr

# sort = QuickSortAlgo()

# def partition(arr, left, right):
#     pivot = right
#     second_index = left-1
#     for i in range(left, right):
#         if arr[i] < arr[pivot]:
#             second_index += 1
#             arr[second_index], arr[i] = arr[i], arr[second_index]
#     arr[second_index+1], arr[pivot] = arr[pivot], arr[second_index+1]
#     return second_index+1

# def quickSort(arr, left, right):
#     if left < right:
#         pi = partition(arr, left, right)
#         quickSort(arr, left, pi-1)
#         quickSort(arr, pi+1, right)
#     return arr

# print(quickSort(rawArr, 0, len(rawArr)-1))

def partition(arr, left, right):
    pivot = right
    second_index = left - 1

    for i in range(left, right):
        if arr[i] <= arr[pivot]:
            second_index +=1
            arr[second_index], arr[i]  = arr[i], arr[second_index]
    arr[second_index+1], arr[pivot] = arr[pivot], arr[second_index+1]
    return second_index+1

def quickSort(arr, left, right):
    if left < right:
        pi = partition(arr, left, right)
        quickSort(arr, left, pi-1)
        quickSort(arr, pi+1, right)

    return arr

print(quickSort(Rough.theGreatArray, 0, len(Rough.theGreatArray)-1))
