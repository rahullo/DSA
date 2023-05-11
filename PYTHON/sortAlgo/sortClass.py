class SortAlgo():
    def __init__(self) -> None:
        pass

    def merge(self, left, right):
        ans = []
        l = len(left)
        r = len(right)
        i = 0
        j = 0
        while i < l and j < r:
            if left[i] < right[j]:
                ans.append(left[i])
                i+=1
            else:
                ans.append(right[j])
                j+=1
        return ans + left[i: ] + right[j: ]

    def mergeSort(self, array):
        if len(array) <= 1:
            return array
        
        mid = len(array) // 2

        left = array[:mid]
        right = array[mid:]

        return self.merge(self.mergeSort(left), self.mergeSort(right))

    def partition(self, array, left, right):
        pivot = right
        second_index = left - 1
        for i in range(left, right):
            if array[i] < array[pivot]:
                second_index += 1
                array[i], array[second_index] = array[second_index], array[i]
        array[second_index+1], array[pivot] = array[pivot], array[second_index+1]
        return second_index+1

    def quickSort(self, array, left, right):
        if left < right:
            partition_index = self.partition(array, left, right)
            self.quickSort(array,left, partition_index-1)
            self.quickSort(array, partition_index+1, right)
        return array



sort = SortAlgo()
# ###########################################
#########################################
# MERGE SORT ALGO

# print(sort.mergeSort([4, 6, 2, 3, 1, 5]))
# print(sort.mergeSort([41, -6, 21, 13, 11, 5]))
# print(sort.mergeSort([14, -26, 2, 322, 100, .5]))

# ###########################################
#########################################
# QUICK SORT ALGO

# print(sort.quickSort([4, 6, 2, 3, 1, 5], 0, 5))
# print(sort.quickSort([41, -6, 21, 13, 11, 5], 0, 5))
# print(sort.quickSort([14, -26, 2, 322, 100, .5], 0, 5))