rawArray = [5, 3, 7, 1, 0, 19, -1]


def selectionSort(arr):
    
    for i in range(len(arr)):
        print(rawArray)
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr

# selectionSort(rawArray)