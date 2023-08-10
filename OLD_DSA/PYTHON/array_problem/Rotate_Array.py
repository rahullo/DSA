from distutils.command.build import build
from numpy import newaxis


array = [1,2,3,4,5,6,7]
k = 3

# def naive_rotation(array, K):
#     new_array = []
#     for i in range(len(array)-k, len(array)):
#         new_array.append(array[i])

#     for i in range(len(array)-k):
#         new_array.append(array[i])

#     return new_array


# print(naive_rotation(array, k))

def brute_rotation(array, k):
    for i in range(k):
        temp = array[-1]
        for j in range(len(array)-1, 0, -1):
            array[j] = array[j-1]

        array[0] = temp

    return array

print(brute_rotation(array, k))