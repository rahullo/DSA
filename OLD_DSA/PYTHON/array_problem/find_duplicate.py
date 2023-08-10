def duplicate(array):
    for i in range(len(array)-1):
        for j in range(len(array)):
            if(array[i] == array[j]):
                return True

    return False

# print(duplicate([1,2,3,4,4]))

def betterDuplicate(array):
    array.sort()
    for i in range(1, len(array)):
        if array[i-1] == array[i]:
            return True

    return False


# print(betterDuplicate([1, 2, 3, 4]))


def smart_duplicate(array):
    dictionary = dict()
    if len(array) < 2:
        return False

    else:
        for i in range(len(array)):
            if array[i] in dictionary:
                return True

            else:
                dictionary[array[i]] = True

        return False

print(smart_duplicate([1, 2, 3, 4, 1]))