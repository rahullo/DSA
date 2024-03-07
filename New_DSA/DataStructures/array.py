class MyArray:
    array = []
    i = -1

    def __init__(self, size) -> None:
        self.array = [x*0 for x in range(size)]

    def push(self, val):
        self.i+=1
        self.array[self.i] = val

    def pop(self):
        item = self.array[self.i]
        self.array[self.i] = 0
        self.i -= 1
        return item

    def printArray(self):
        print(self.array)
    
arr1 = MyArray(9)

arr1.printArray()
arr1.push(2)
arr1.push(4)
arr1.push(6)
arr1.push(8)
arr1.printArray()
print(arr1.pop())
arr1.printArray()
