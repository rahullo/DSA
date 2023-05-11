rawArray = [5, 3, 7, 1, 0, 19, -1]



# def mergeSort(array):
#     if len(array) > 1:

#         r = len(array)//2
#         L = array[:r]
#         M = array[r:]
#         # print(r, array)
        
#         mergeSort(L)
#         mergeSort(M)
#         print(L, M)

#         i = j = k = 0
#         while i < len(L) and j < len(M):
#             if L[i] < M[j]:
#                 array[k] = L[i]
#                 i += 1
#             else:
#                 array[k] = M[j]
#                 j += 1
#             k += 1
#         while i < len(L):
#             array[k] = L[i]
#             i += 1
#             k += 1

#         while j < len(M):
#             array[k] = M[j]
#             j += 1
#             k += 1
#     return rawArray

# def merge(left, right):
#     l = len(left)
#     r = len(right)
#     arr = []

#     i, j = 0, 0
#     while i < l and j < r:
#         if left[i] < right[j]:
#             arr.append(left[i])
#             i+=1
#         else:
#             arr.append(right[j])
#             j+=1
#     return arr + left[i:] + right[j:]

# def mergeSort(array):
#     if len(array) <= 1:
#         return array
#     mid = len(array)//2
#     left = array[ :mid]
#     right = array[mid: ]

#     return merge(mergeSort(left), mergeSort(right))

# def merge(left, right):
#     l = len(left)
#     r = len(right)
#     i = 0
#     j = 0
#     ans = []
#     while i < l and j < r:
#         if left[i] < right[j]:
#             ans.append(left[i])
#             i+=1
#         else:
#             ans.append(right[j])
#             j+=1
#     return ans+left[i:]+right[j:]

# def mergeSort(array):
#     if len(array) <= 1:
#         return array

#     mid = len(array)//2

#     left = array[:mid]
#     right = array[mid:]
#     return merge(mergeSort(left), mergeSort(right))


# print(mergeSort(rawArray))


# class SortingAlgo():
#     def __init__(self) -> None:
#         pass

#     def merge(self, left, right):
#         ans = []
#         l = len(left)
#         r = len(right)
#         i = 0
#         j = 0

#         while i < l and j < r:
#             if left[i] < right[j]:
#                 ans.append(left[i])
#                 i+=1
#             else:
#                 ans.append(right[j])
#                 j+=1
#         return ans + left[i:] + right[j:]

#     def mergeSort(self, arrays):
#         if len(arrays) <= 1:
#             return arrays

#         mid = len(arrays)//2

#         left = arrays[:mid]
#         right = arrays[mid:]

#         return self.merge(self.mergeSort(left), self.mergeSort(right))


# sort = SortingAlgo()
# print(sort.mergeSort(rawArray))

import Rough

class Solution():
    def __init__(self):
        pass

    def merge(self, left, right):
        l = len(left)
        r = len(right)
        i = 0
        j = 0
        ans = []
        while i < l and j < r:
            if left[i] <= right[j]:
                ans.append(left[i])
                i+=1
            else:
                ans.append(right[j])
                j+=1
        return ans + left[i:] + right[j:]


    def mergeSort(self, array):
        if len(array) <= 1:
            return array

        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        return self.merge(self.mergeSort(left), self.mergeSort(right))

s1 = Solution()
# print(s1.mergeSort(Rough.theGreatArray))