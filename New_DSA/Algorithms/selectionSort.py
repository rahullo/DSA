def selectionSort(array):
    array_size = len(array)
    for i in range(array_size):
        min = i
        for j in range(i+1, array_size):
            if array[min] > array[j]:
                min = j
        if min != i:
            array[min], array[i] = array[i], array[min]
    return array

list1 = [6, 3, 8, 3 , 9, 2, 0]

print(list1)
print(selectionSort(list1))