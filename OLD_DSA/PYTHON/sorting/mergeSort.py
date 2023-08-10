# def mergeSort(array):
#     if(len(array) ==1):
#         return array
    
#     else:
#         mid = len(array)//2
#         left = array[ :mid]
#         right = array[mid: ]
#         return merge(mergeSort(left), mergeSort(right))


# def merge(left, right):
#     l = len(left)
#     r = len(right)
#     sorted_array = []
#     left_index = 0
#     right_index = 0
#     while left_index < l and right_index < r:
#         if(left[left_index] < right[right_index]):
#             sorted_array.append(left[left_index])
#             left_index+=1

#         else:
#             sorted_array.append(right[right_index])
#             right_index+= 1

#     return sorted_array + left[left_index:] + right[right_index:]


# print(mergeSort([4, 3, 9, 0, 1, -1]))

def mergeSort(array):
    if(len(array) < 2):
        return array

    mid = len(array)//2
    left = array[:mid]
    right = array[mid:]

    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    left_index = 0
    right_index = 0
    sortedarray = []
    l = len(left)
    r = len(right)

    while left_index < l and right_index < r:
        if(left[left_index] < right[right_index]):
            sortedarray.append(left[left_index])
            left_index+=1
        else:
            sortedarray.append(right[right_index])
            right_index+=1

    return sortedarray + left[left_index: ] + right[right_index: ]


# array = [4, 3, 5, 3, -1, 0]
# print(array)
# print(mergeSort(array))