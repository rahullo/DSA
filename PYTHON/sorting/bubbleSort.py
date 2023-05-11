def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if(array[j] > array[j+1]):
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

    return array



# print(bubbleSort([13, 50, 4, 21, 17 , 1, 0]))


