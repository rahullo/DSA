array = [5, 2, 9, 0, 1]
    
def selectionSort(array):
    # current_Minimum = array[key]
    for i in range(len(array)):
        key = i
        for j in range(i+1, len(array)):
            if(array[key]>array[j]):
                key = j

        temp = array[i]
        array[i] = array[key]
        array[key] = temp
    return array

# print(selectionSort([4, 3, 9, 0, 1, -1]))

def selectionSort2(array):
    for i in range(len(array)):
        key = i
        for j in range(i, len(array)):
            if(array[key] > array[j]):
                key = j
        array[i], array[key] = array[key], array[i]

    return array

print(selectionSort([4, 3, 5, 13, 0, 11, 2, 7, 8, 9, 6, 1]))