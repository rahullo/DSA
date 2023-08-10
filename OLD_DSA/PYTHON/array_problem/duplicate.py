def duplicate(array):
    new = set(array)

    return (len(new) != len(array))

# print(duplicate([2, 1, 3, 2]))

def duplicate2(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if(array[i] == array[j]):
                return True


    else:
        return False
# print(duplicate2([2, 1, 3, 2]))


def duplicate3(array):
    array.sort()
    for i in range (len(array) -1):
        if(array[i] == array[i+1]):
            return True

    return False

# print(duplicate3([2, 1, 3]))



