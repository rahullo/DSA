class MyArray:
    def __init__(self):
        self.data = {}
        self.length = 0


    def push(self, number):
        self.data[self.length] = number
        self.length += 1

    def get(self, index):
        if(index < self.length):
            ele = self.data[index]
            return ele
        else:
            return 'Out of range!!!'

    def pop(self):
        self.length -=1
        return self.data.pop(self.length)


    def insert(self, index, item):
        self.length+=1
        for i in range(self.length-1, index, -1):
            self.data[i] = self.data[i-1]
        self.data[index] = item

    def delete(self, index):
        ele = self.data[index]
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]

        self.pop()
        return ele
        
        

arr1 = MyArray()
arr1.push(1)
arr1.push(2)
arr1.push(3)
# print(arr1.get(2))
# print(arr1.pop())
arr1.insert(0, 0)
print(arr1.delete(1))
arr1.push(5)
arr1.push(6)
print(arr1.data)


