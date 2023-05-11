import unittest

import merge_sort
# import array 
# print(array.nums)

class TestMain(unittest.TestCase):
    def mergeSort1(self):
        arr = [5, 4, 7, 6, 3, 9, 2, 1, 8]
        result = merge_sort.mergeSort(arr)
        self.assertEqual(result, [1,2,3,4,5,6,7,8,9])

    def mergeSort2(self):
        arr = [5,1,9,11,2,4,8,10,13,3,6,7,15,14,12,16]
        result = merge_sort.mergeSort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    # def test_quickSort2(self):
    #     arr = [19, -2, 10, 4, -4, -11, 0, -1.4, -2.002]
    #     result = quickSort.quickSort(arr, 0, len(arr)-1)
    #     self.assertEqual(result, [-11, -4, -2.002, -2, -1.4, 0, 4, 10, 19])

unittest.main()