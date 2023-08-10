def linearSearch(arr, num):
    for item in arr:
        if item == num:
            return True
    return False

print(linearSearch([3, 2, 5, 1, 8, 9], 1))