class Hash_table():
    def __init__(self, size):
        self.size = size
        self.data = [None]*self.size

    def __str__(self):
        return str(self.__dict__)

    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash+ord(key[i]) * i) % self.size
        return hash

    def set(self, key, value): 
        hash = self._hash(key)
        if not self.data[hash]: 
            self.data[hash] = [key,value]
        else: 
            self.data[hash].append([key, value])

    def get(self, key):
        hash = self._hash(key)
        if self.data[hash]:
            for i in range(2, len(self.data[hash])):
                if self.data[hash][i][0] == key:
                     return self.data[hash][i]
        return None

    def printData(self, data):
        for i in range(len(data)):
            print(data[i])

    def returnVal(self, table):
        val = []
        for item in table:
            if len(item) > 1:
                val.append(item[1])
                for i in range(2, len(item)):
                    val.append(item[i][1])
            else:
                val.append(item[1])

        return val

    def returnkeys(self, table):
        val = []
        for item in table:
            if len(item) > 1:
                val.append(item[0])
                for i in range(2, len(item)):
                    val.append(item[i][0])
            else:
                val.append(item[0])

        return val
        

    

new_hash = Hash_table(10)
print(new_hash.data)
new_hash.set('one', 1)
new_hash.set('two', 2)
new_hash.set('three', 3)
new_hash.set('four', 4)
new_hash.set('five', 5)
new_hash.set('six', 6)
new_hash.set('seven', 7)
new_hash.set('eight', 8)
new_hash.set('nine', 9)
new_hash.set('ten', 10)
new_hash.set('eleven', 11)
new_hash.set('twelve', 12)
new_hash.set('thirteen', 13)
new_hash.set('fourteen', 14)
new_hash.set('fifteen', 15)
new_hash.set('sixteen', 16)
new_hash.set('seventeen', 17)
new_hash.set('eighteen', 18)
new_hash.set('nineteen', 19)
new_hash.set('twenty', 20)
new_hash.set('twety one', 21)



new_hash.printData(new_hash.data)

print(new_hash.get('sixteen'))
print(new_hash.returnVal(new_hash.data))
print(new_hash.returnkeys(new_hash.data))


