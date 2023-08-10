class SearchAlgo():
    def __init__(self) -> None:
        pass

    def binarySearch(self, array, target):
        low = 0
        high = len(array)-1
        i = 0
        while i < len(array) // 2:
            mid = (low + high) //2
            if array[mid] == target:
                return True
            elif target < array[mid]:
                high = mid-1
            else:
                low = mid +1
            i+=1
        return False

    def binarySearchRecur(self, array, target, low, high):
        if low > high:
            return False
        else:
            mid = (low + high) // 2
            if target == array[mid]:
                return True
            elif target < array[mid]:
                return self.binarySearchRecur(array, target, low, mid-1)
            else:
                return self.binarySearchRecur(array, target, mid+1, high)



search = SearchAlgo()

#################
##################################3
########################################
# BINARY SEARCH

# print(search.binarySearch([2, 4, 6, 8, 10, 12, 14], 14))

#################
##################################3
########################################
# BINARY SEARCH RECURSIVELY

print(search.binarySearchRecur([2, 4, 6, 8, 10, 12, 14], 14, 0, 6))