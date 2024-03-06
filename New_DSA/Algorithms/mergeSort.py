def mergeSort(array):
    if len(array) <=1:
        return array
    
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    l = len(left)
    r = len(right)
    i = j = 0

    ans = []

    while i < l and j < r:
        if left[i] < right[j]:
            ans.append(left[i])
            i+=1
        elif right[j] < left[i]:
            ans.append(right[j])
            j+=1
    
    return ans+left[i:]+right[j:]


list1 = [5, 4, 9, 3, 0, 2, 6, 8, 7, 1]

print(list1)
print(mergeSort(list1))