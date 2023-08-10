###################################################
###########################################
#Selection sorting

# array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

# def selectionSort(array):
#     for i in range(len(array)):
#         mini = i
#         temp = array[i]
#         for j in range(i+1, len(array)):
#             if(array[j] < array[mini]):
#                 mini = j

#         array[i] = array[mini]
#         array[mini] = temp

#     return array

# selectionSort(array)
# print(array)

##############################################
##############################################
#   Bubble sorting



# array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

# def bubbleSort(array):
#     length = len(array)
#     for i in range(length):
#         for j in range(length-1):
#             if(array[j] > array[j+1]):
#                 temp = array[j]
#                 array[j] = array[j+1]
#                 array[j+1] = temp

#             j+=1
#         i+=1

#     return array

# bubbleSort(array)
# print(array)

######################################
#################################################
#       Merge sorting

# from operator import length_hint


array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 10];

def mergeSort(array):
    length = len(array)
    mid=0
    if(length == 1):
        return array

    if(length % 2 == 0):
        mid = length//2 - 1
    else:
        mid = round(length//2)-1

    def newArray(array, i, j):
        answer = []
        for item in range(i, j+1):
            answer.append(array[item])

        return answer

    # print(mid)

    firstSection = newArray(array, 0, mid)
    secondSection = newArray(array, mid+1, length-1)
    print(array)
    print("left", firstSection)
    print('right', secondSection)


    def merge(left, right):
        result = []
        leftIndex = 0
        rightIndex =0 
        while(leftIndex < len(left) and rightIndex < len(right)):
            if(left[leftIndex] < right[rightIndex]):
                result.append(left[leftIndex])
                leftIndex+=1

            else:
                result.append(right[rightIndex])
                rightIndex+=1
        return result+(newArray(left, leftIndex, len(left)-1) + newArray(right, rightIndex, len(right)-1))

    return merge(mergeSort(firstSection), mergeSort(secondSection))

# print(mergeSort(array))



# bigArray = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 10]
# array = [3, 2, 5, 1]

# def swapping(array, first, second):
#     temp = array[first];
#     array[first]  = array[second]
#     array[second] = temp
#     return array


# def selectionSort(array):
#     length = len(array)

#     for i in range(length):
#         mini = i
#         temp = array[i]
#         for j in range(i+1, length):
#             if(array[mini] > array[j]):
#                 mini = j
#         swapping(array, i, mini)
#     # (temp, array[mini]) = (array[mini] , temp)
#         # array[i] = array[mini]
#         # array[mini] = temp

#     return array


# selectionSort(array)
# print(array)


# ###############################################
###############################################################
# BUBBLE SORT

# def bubblesort(array):
#     for i in range(len(array)):
#         for j in range(len(array)-1):
#             if(array[j] > array[j+1]):
#                 temp = array[j]
#                 array[j] = array[j+1]
#                 array[j+1] = temp
#     return array

# # print(bubblesort(array))


# ################################
# #############################################
# #INSERTION SORT  [3, 2, 5, 1] 

# def insertionSort(array):
#     for i in range(1, len(array)):
#         key = array[i]
#         j = i -1
#         print(array)
#         while (j >=0 and key < array[j]):
#             print(array, j)
#             array[j+1] = array[j]
#             j = j-1

#         array[j+1] = key
        

#     return array

# print(insertionSort(array))

from math import floor
from tarfile import LENGTH_NAME

from numpy import left_shift


bigArray = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 10]
array = [3, 2, 5, 1]

################################################
#############################################################
##BUBBLE SORTING ALGORITHM

# def bubbleSort(array):
#     for i in range(len(array)):
#         for j in range(len(array) - 1):
#             if(array[j] > array[j+1]):
#                 temp = array[j]
#                 array[j] = array[j+1]
#                 array[j+1] = temp

#     return array

# print(bubbleSort(bigArray))


#############################################
#########################################################
##SELECTION SORTING ALGORITHM
# def selectionSort(array):
#     for i in range(len(array)):
#         minIndex = i
#         for j in range(i+1, len(array)):
#             if(array[minIndex] > array[j]):
#                 minIndex = j

#         temp = array[i]
#         array[i] = array[minIndex]
#         array[minIndex] = temp

    
#     return array

# print(selectionSort(bigArray))

#######################################################3
#############################################################
##MERGE SORTING ALGORITHM
# def mergeSort(array):
#     length = len(array)
#     if(length <= 1):
#         return array

#     if(length%2 == 1):
#         mid = floor(length//2) -1

#     else:
#         mid = floor(length//2) - 1

#     def newArray(array, i, j):
#         answer = []
#         for item in range(i, j+1):
#             answer.append(array[item])

#         return answer

#     firstHalf = array[ : mid+1]
#     secondHalf = array[mid+1: ]

#     def merge(left, right):
#         result = []
#         leftIndex = 0
#         rightIndex = 0
#         while (leftIndex<len(left) and rightIndex<len(right)):
#             if(left[leftIndex] < right[rightIndex]):
#                 result.append(left[leftIndex])
#                 leftIndex+=1

#             else:
#                 result.append(right[rightIndex])
#                 rightIndex+=1

#         return result+(newArray(left, leftIndex, len(left)-1) + newArray(right, rightIndex, len(right)-1))
#     return merge(mergeSort(firstHalf), mergeSort(secondHalf))

# print(mergeSort(bigArray))



    
