def insertionSort(array):
    size = len(array)
    for i in range(1, size):
        j = i-1
        key = array[i]

        while array[j] > key and j >= 0:
            array[j+1] = array[j]
            j-=1
        
        array[j+1] = key
    return array

list1 = [6, 3, 8, 3 , 9, 2, 0]

print(list1)
print(insertionSort(list1))