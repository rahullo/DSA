def partition(array, low, high):
    pivot = high
    i = low -1
    for j in range(low, high):
        if array[j] < array[pivot]:
            i+=1
            array[j], array[i] = array[i], array[j]
    array[i+1], array[pivot] = array[pivot], array[i+1]
    return i+1

def quickSort(array, low, high):
    if low < high:
        partition_Index = partition(array, low, high)
        quickSort(array, low, partition_Index-1)
        quickSort(array, partition_Index+1, high)
    return array

list1 = [6, 3, 8, 3 , 9, 2, 0]

print(list1)
print(quickSort(list1, 0, 6))