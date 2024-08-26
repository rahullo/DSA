def merge(left, right):
    l = len(left)
    r = len(right)
    i =  j = 0
    ans = []

    while i < l and j < r:
        if left[i] < right[j]:
            ans.append(left[i])
            i+=1
        else:
            ans.append(right[j])
            j+=1
    return ans+left[i:]+right[j:]



def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left_arr = arr[:mid]
    right_arr = arr[mid:]

    return merge(merge_sort(left_arr), merge_sort(right_arr))



print(merge_sort([4, 3, 5, 2, 6, 1, 7, 9, 0]))