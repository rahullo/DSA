# def partition(array, left, right):
#     smaller_index = left - 1
#     pivot = array[right]
#     for i in range(left, right):
#         if array[i] < pivot:
#             smaller_index += 1
#             print(array[i], pivot, smaller_index)
#             array[smaller_index], array[i] = array[i], array[smaller_index]
#             print( array)

#     array[smaller_index+1], array[right] = array[right], array[smaller_index+1]
#     # print(array)
#     return (smaller_index+1)

# def quick_sort(array, left, right):
#     if left < right:
#         partitioning_index = partition(array, left, right)
#         print(partitioning_index)
#         quick_sort(array,left,partitioning_index-1)
#         quick_sort(array,partitioning_index+1,right)



# def quickSort2(array, left, right):
#     if(len(array) < 2):
#         return array
#     pivot = array[right]
#     smaller_index = left-1
#     index = 0
#     for i in range(left, right+1):
#         if(array[i] <= pivot):
#             smaller_index += 1
#             array[i], array[smaller_index] = array[smaller_index], array[i]
#             index = i
#             print(array)

#     firstArray = array[left: index-1]
#     secondArray = array[index-1: right+1]
#     print(firstArray, secondArray)
#     quickSort2(firstArray, left, index)
#     quickSort2(secondArray, index, right)

#     return array

# array = [5, 3, 8, 2, 0, 1, 4]
# print(quickSort2(array, 0, (len(array)-1)))



def partition(array, left, right):
    smaller_index = left-1
    pivot = array[right]
    for i in range(left, right):
        if array[i]<pivot:
            smaller_index+=1
            array[smaller_index], array[i] = array[i], array[smaller_index]
        
    array[smaller_index+1], array[right] = array[right], array[smaller_index+1]
    return smaller_index+1

def quicksort(array, start, end):
    if start>end:
        return array

    partitionIndex = partition(array, start, end)
    quicksort(array, start, partitionIndex-1)
    quicksort(array, partitionIndex+1, end)
    


array = [3, 2, 4, 1, 6, 9, 8, 7]
print(array)
quicksort(array, 0, len(array)-1)
print(array)


