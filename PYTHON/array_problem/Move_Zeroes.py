array = [0,0,0,0,1,0,3,0,0,0,12,9,7]


# def naive_zero_mover(array):
#     l = len(array)
#     for i in range(l):
#         if array[i] == 0:
#             array.append(0)

#     j = 0
#     c = 0

#     while c < l:
#         if array[j] != 0:
#             j+=1

#         else:
#             array.pop(j)

#         c+=1
#     return array

# print(naive_zero_mover(array))
print(array)

def swap_move(array):
    z = 0
    for i in range(len(array)):
        if array[i] != 0:
            array[i], array[z] = array[z], array[i]
            z+=1

    return array

print(swap_move(array))