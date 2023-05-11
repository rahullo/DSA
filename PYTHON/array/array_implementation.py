class Array:
    def __init__(self):
        self.length = 0
        self.data = {}

    def push(self, item):
        self.data[self.length] = item
        self.length+=1

    def pop(self):
        data =  self.data[self.length-1]
        del self.data[self.length-1]
        self.length-=1
        return data

    def insert(self, index, item):
        self.length +=1
        for i in range(self.length-1, index, -1):
            self.data[i] = self.data[i-1]

        self.data[index] = item


    def get(self, index):
        if(len(self.data) < 1):
            return "first enter some data!!!"
        return self.data[index]

    def delete(self, index):
        print(self.length)
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]

        del self.data[self.length-1]
        self.length-=1


arr1 = Array()
arr1.push(1)
arr1.push(3)
arr1.push(5)
arr1.push(0)
arr1.push(10)
print(arr1.get(0))
print(arr1.data)
arr1.insert(2, 19)
print(arr1.data)
arr1.delete(2)
print(arr1.data)