def bubbleSort(array):
    array_size = len(array)
    for i in range(array_size-1):
        for j in range(i+1, array_size):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

    return array


list1 = [6, 3, 8, 3 , 9, 2, 0]

print(list1)
print(bubbleSort(list1))