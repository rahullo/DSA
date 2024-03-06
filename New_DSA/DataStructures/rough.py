list1 = [1, 2, 3, 4]

string = 'rahul'

# print(string[0:1] == string[0])
# print(type(string[0:1]))
# print(type(string[0]))

nested = [[2, [37]], 4, ["hello"]]

print(nested[0][1][0])

def randomFunc(arr, index, value):
    if index >= 0 and index < len(arr):
        arr[index] = value
        return True
    else:
        value = value+1
        return False
    
arr = [ 1, 3, 5, 6]
value = 7
print(arr)

print(randomFunc(arr, 3, value))

print(arr, value)
