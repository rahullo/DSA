def fabonacciIterative(index):
    if(index == 9):
        return index

    elif(index == 1):
        return index
        
    else:
        a = 0
        b = 1
        c = 0
        for item in range(2, index +1):
            c = a+b
            a = b
            b = c
        return c

# print(fabonacciIterative(11))

def fabonacciRecursive(index):
    if(index == 0):
        return index

    elif(index == 1):
        return index

    return fabonacciRecursive(index -1) + fabonacciRecursive(index - 2)

# print(fabonacciRecursive(0))




    