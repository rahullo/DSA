class MyArray:
    array = []
    i = -1

    def __init__(self, size) -> None:
        self.array = [x*0 for x in range(size)]

    # Method to insert the element at end of the list/array.
    def push(self, val):
        self.i+=1
        self.array[self.i] = val

    # Method to remove a element from end of the list/array
    def pop(self):
        item = self.array[self.i]
        self.array[self.i] = 0
        self.i -= 1
        return item
    
    # Method to insert a element at given position by user
    def insert(self, val, pos):
        if pos > self.i:  # If the position is too ahead of length of list
            self.array[pos] = val
        else:
            j = self.i+1
            while j > pos: # Shift elements one position ahead
                self.array[j] = self.array[j-1]
                j-=1
            self.array[j] = val

    # Method to delete first occuring element in array given by user
    def delete(self, val):
        j = 0
        while j < len(self.array):
            if self.array[j] == val:
                x = j+1
                while x < len(self.array):
                    self.array[x-1] = self.array[x]
                    x+=1
            j+=1

    def printArray(self):
        print(self.array)
    
arr1 = MyArray(9)

# arr1.printArray()
arr1.push(2)
arr1.push(4)
arr1.push(6)
arr1.push(8)
# arr1.printArray()
# print(arr1.pop())
arr1.insert(5, 7)
arr1.printArray()
# arr1.delete(5)
arr1.delete(4)
arr1.printArray()

