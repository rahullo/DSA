def getOneBits(n):
    # Write your code here
    arr = [0]
    binary = bin(n)[2:]
    print(binary)
    for n in range(len(binary)):
        if binary[n] == '1':
            arr.append(n+1)
    print(arr)
    arr[0] = len(arr)-1
    return arr

print(getOneBits(161))