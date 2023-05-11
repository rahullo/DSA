def insertionSort(array):
    key = 0
    for i in range(1, len(array)):
        while array[i-1] > array[i] and i > 0:
            array[i], array[i-1] = array[i-1], array[i]
            i -= 1
    return array


# print(insertionSort([4, 3, 9, 0, 1, -1]))


